from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime, timedelta

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfAroUfYkZqG7MuHRSG2-ly81tfK4qbw0frwnjhZP-hmgJQqQ/viewform"
IS_TIME_TARGETED = False
TARGET_HOUR = 13
TARGET_MINUTE = 0

# Time Targeted Function
def wait_until_target(hour: int, minute: int):
    now = datetime.now()
    target = now.replace(hour = hour, minute = minute, second = 0, microsecond = 0)
    if target <= now:
        target = target + timedelta(days = 1)
        print(f"Waiting until {target.strftime('%H:%M')} WIB......")
        while True:
            now = datetime.now()
            if now >= target:
                break
            time.sleep(0.5)
        print(f"It's {target.strftime('%H:%M')}, running automation.....")


def wait_for_form_loaded(driver, timeout=20):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']"))
    )
    
def find_question_block(driver, label_text):
    xpaths = [
        f"//div[@role='listitem'][.//*[normalize-space(text())='{label_text}']]",
        f"//div[@role='listitem'][.//*[contains(normalize-space(text()), '{label_text}')]]",
    ]

    for xpath in xpaths:
        try:
            return driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            continue
    return None


def fill_text_by_label(driver, label_text, value, timeout=10):
    xpaths = [
        f"//input[@aria-label='{label_text}']",
        f"//textarea[@aria-label='{label_text}']",
    ]
    for xpath in xpaths:
        try:
            el = WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
            el.clear()
            el.send_keys(value)
            return True
        except TimeoutException:
            pass

    block = find_question_block(driver, label_text)
    if block:
        for inner in [".//input", ".//textarea"]:
            try:
                el = block.find_element(By.XPATH, inner)
                tag = el.tag_name.lower()
                if tag == "input" or tag == "textarea":
                    el.clear()
                    el.send_keys(value)
                    return True
            except NoSuchElementException:
                continue
        try:
            editable = block.find_element(By.XPATH, ".//*[@contenteditable='true']")
            editable.click()
            editable.send_keys(value)
            return True
        except NoSuchElementException:
            pass
    return False

def click_radio_by_label(driver, label_text, option_text, timeout=10):
    block = find_question_block(driver, label_text)
    if block:
        xpaths = [
            f".//*[@role='radio' and @aria-label='{option_text}']",
            f".//*[normalize-space(text())='{option_text}']/ancestor::*[@role='radio' or self::label or self::div][1]",
        ]

        for xpath in xpaths: 
            try:
                el = WebDriverWait(block, timeout).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                el.click()
                return True
            except TimeoutException:
                continue
    return False

def select_dropdown_by_label(driver, label_text, option_text, timeout=10):
    block = find_question_block(driver, label_text)
    if not block:
        return False
    try:
        open_btn = WebDriverWait(block, timeout).until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@role='button' and @aria-haspopup='listbox']"))
        )
        open_btn.click()
        opt = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option' and .//*[normalize-space(text())='{option_text}']]"))
        )
        opt.click()
        return True
    except TimeoutException:
        return False
    
def click_submit(driver, timeout=10):
    for xp in [
        "//span[normalize-space(text())='Kirim']/ancestor::div[@role='button']",
        "//span[normalize-space(text())='Submit']/ancestor::div[@role='button']",
    ]:
        try:
            btn = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xp))
            )
            btn.click()
            return True
        except TimeoutException:
            continue
    return False

answers = {
    "Nama Anak": "Gyanna",
    "Tempat Tanggal Lahir": "Jakarta, 06 November 2024",
    "Usia Anak": "16 s/d 72 Bulan",   # radio
    "Jenis Kelamin": "Perempuan",     # radio
    "Agama": "Islam",
    "Nama Orangtua": "Bapak/Ibu Contoh",
    "Satker": "Biro X",
    "NO Telepon": "08123456789",
    "Alamat": "Jl. Contoh No. 123",
    "Alergi": "-",                    # optional? still safe to fill
    "Tanggal Booking": "Senin, 1 September 2025"
}

def run():
    if IS_TIME_TARGETED:
        wait_until_target(TARGET_HOUR, TARGET_MINUTE)
    

    driver = webdriver.Chrome()
    driver.get(FORM_URL)
    try:
        wait_for_form_loaded(driver)

        # Text
        text_labels = [
            "Nama Anak",
            "Tempat Tanggal Lahir",
            "Agama",
            "Nama Orangtua",
            "Satker",
            "NO Telepon",
            "Alamat",
            "Alergi",
        ]
        for lbl in text_labels:
            if lbl in answers:
                ok = fill_text_by_label(driver, lbl, answers[lbl])
                if not ok:
                    print(f"[WARN] Could not fill text for: {lbl}")

        # Radios
        radio_pairs = [
            ("Usia Anak", answers.get("Usia Anak")),
            ("Jenis Kelamin", answers.get("Jenis Kelamin")),
            ("Tanggal Booking", answers.get("Tanggal Booking")),
        ]
        for q, val in radio_pairs:
            if val:
                ok = click_radio_by_label(driver, q, val)
                if not ok:
                    print(f"[WARN] Could not click radio {q} -> {val}")

        # Submit
        ok = click_submit(driver)
        if not ok:
            print("[WARN] Submit button not found or not clickable.")
        else:
            print("Form submitted.")

    finally:
        time.sleep(60)
        driver.quit()

if __name__ == "__main__":
    run()