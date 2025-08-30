from numpy.f2py.auxfuncs import throw_error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime, timedelta

FORM_URL = "https://forms.gle/aq52XaqC9sduLyvy5"
IS_TIME_TARGETED = False
TARGET_HOUR = 13
TARGET_MINUTE = 0

TEXT_INPUT_XPATHS = {}
TEXTAREA_INPUT_XPATHS = {}
RADIO_INPUT_XPATHS = {}
CHECKBOX_INPUT_XPATHS = {}

TEXT_INPUT_TAKEOUT_ITEMS = []
TEXTAREA_INPUT_TAKEOUT_ITEMS = []

CHECKBOX_TAKEOUT_ITEMS = [
    "Usia Anak",
    "16 s/d 72 Bulan",
    "tanggal booking"
]

RADIO_TAKEOUT_ITEMS = [
    # "Jenis Kelamin"
]

TEXT_INPUT_ANSWERS = {
    "Nama Anak": "John Doe",
    "Tempat Tanggal Lahir": "Jakarta, 1 January 2000",
    "Agama": "Catholic",
    "Nama Orangtua": "Jane Doe",
    "Satker": "Finance",
    "NO Telepon": "6281234567890",
    "Alamat": "Jakarta",
    "Alergi": "-"

}

def time_validation(hour: int, minute: int):
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

def form_items_load_validation(driver, timeout=5):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']"))
    )

def collect_radio_options_in_block(block, block_index):
    options = {}
    radios = block.find_elements(By.CSS_SELECTOR, "div[role='radio']")
    for i, r in enumerate(radios, start=1):
        label = (r.get_attribute("aria-label")
                 or r.get_attribute("data-value")
                 or r.text
                 or f"Option_{i}")
        label = label.strip()
        if r.get_attribute("aria-label"):
            xp = f"(//div[@role='listitem'])[{block_index}]//div[@role='radio' and @aria-label='{label}']"
        elif r.get_attribute("data-value"):
            xp = f"(//div[@role='listitem'])[{block_index}]//div[@role='radio' and @data-value='{label}']"
        else:
            xp = f"(//div[@role='listitem'])[{block_index}]//div[@role='radio'][{i}]"
        options[label] = xp
    return options

def load_form_items(driver):
    blocks = driver.find_elements(By.XPATH, "//div[@role='listitem']")

    for idx, block in enumerate(blocks, start=1):
        try:
            label_el = block.find_element(By.XPATH, ".//*[self::span or self::div][normalize-space(text())!='']")
            label = label_el.text.strip()
        except:
            label = f"Unnamed_{idx}"

        try:
            # text
            if block.find_elements(By.XPATH, ".//input[@type='text']"):
                TEXT_INPUT_XPATHS[label] = f"(//div[@role='listitem'])[{idx}]//input[@type='text']"
                continue

            # textarea
            if block.find_elements(By.XPATH,".//textarea"):
                TEXT_INPUT_XPATHS[label] = f"(//div[@role='listitem'])[{idx}]//input[@type='textarea']"
                continue

            # radio
            if block.find_elements(By.CSS_SELECTOR, "div[role='radio']"):
                RADIO_INPUT_XPATHS[label] = collect_radio_options_in_block(block, idx)
                continue

            # checkbox
            if block.find_elements(By.XPATH, ".//*[@role='checkbox']"):
                CHECKBOX_INPUT_XPATHS[label] = f"(//div[@role='listitem'])[{idx}]"
                continue
        except Exception as e:
            print(f"Error inspecting block {idx}: {e}")

def fill_form(driver):
    answers = "examples"
    for text_field in TEXT_INPUT_XPATHS:
        if text_field in TEXT_INPUT_ANSWERS:
            driver.find_element(By.XPATH, f"{TEXT_INPUT_XPATHS[text_field]}").send_keys(TEXT_INPUT_ANSWERS[text_field])
            continue
        else:
            throw_error(driver)

    for checkbox_field in CHECKBOX_INPUT_XPATHS:
        if checkbox_field in CHECKBOX_TAKEOUT_ITEMS:
            continue
        driver.find_element(By.XPATH, f"{CHECKBOX_INPUT_XPATHS[checkbox_field]}//*[@role='checkbox']").click()

    for radio_field in RADIO_INPUT_XPATHS:
        if radio_field in RADIO_TAKEOUT_ITEMS:
            continue
        driver.find_element(By.XPATH, f"{RADIO_INPUT_XPATHS[radio_field]}//*[@role='radio']").click()

def xpaths_validation():
    for key in list(CHECKBOX_INPUT_XPATHS.keys()):
        if key in CHECKBOX_TAKEOUT_ITEMS:
            CHECKBOX_INPUT_XPATHS.pop(key)
            print(f"{key} Already removed from checkbox xpath list")
            continue

    for key in list(RADIO_INPUT_XPATHS.keys()):
        if key in RADIO_TAKEOUT_ITEMS:
            RADIO_INPUT_XPATHS.pop(key)
            print(f"{key} Already removed from radio xpath list")
            continue

def run():
    if IS_TIME_TARGETED:
        time_validation(TARGET_HOUR, TARGET_MINUTE)
    
    driver = webdriver.Chrome()
    driver.get(FORM_URL)

    try:
        form_items_load_validation(driver)
        load_form_items(driver)

        xpaths_validation()
        fill_form(driver)

        print("TEXT_INPUT_XPATHS =", TEXT_INPUT_XPATHS)
        print("TEXTAREA_INPUT_XPATHS =", TEXTAREA_INPUT_XPATHS)
        print("RADIO_INPUT_XPATHS =", RADIO_INPUT_XPATHS)
        print("CHECKBOX_INPUT_XPATHS =", CHECKBOX_INPUT_XPATHS)
    finally:
        print("Automation finished.....")
        time.sleep(60)
        driver.quit()

if __name__ == "__main__":
    run()