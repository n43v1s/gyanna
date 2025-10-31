from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

TARGET_HOUR = 12
TARGET_MINUTE = 59
TARGET_SECOND = 57

print(f"Waiting until {TARGET_HOUR:02d}:{TARGET_MINUTE:02d}:{TARGET_SECOND:02d}...")
while True:
    now = datetime.now()
    if (
            now.hour == TARGET_HOUR and
            now.minute == TARGET_MINUTE and
            now.second == TARGET_SECOND
    ):
        break
    time.sleep(0.5)
print(f"It's {TARGET_HOUR:02d}:{TARGET_MINUTE:02d}, running automation...")


start_time = time.time()
# xpaths
childs_name_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
pdob_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
age_field_xpath = '//*[@id="i17"]/div[2]'
gender1_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
# gender2_field_xpath = '//*[@id="i37"]/div[2]'
religion_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
parents_name_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'
department_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
phone_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'
address_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input'
allergies_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input'
booking_date1_field_xpath = '//*[@id="i71"]/div[2]'
booking_date2_field_xpath = '//*[@id="i74"]/div[2]'
booking_date3_field_xpath = '//*[@id="i77"]/div[2]'
booking_date4_field_xpath = '//*[@id="i80"]/div[2]'
booking_date5_field_xpath = '//*[@id="i83"]/div[2]'
submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'

# texts
childs_name = "Gyanna"
pdob = "Jakarta, 6 November"
gender  = "Perempuan"
religion = "Protestan"
parents_name = "Astria Martina Silaban" 
department = "KSA"
phone = "6282161175790"
address = "Depok"
allergies = "None"

driver = webdriver.Chrome()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdWVUCFpICwmeqUKVPNhtc_w9HryyeZ_iGcUeGZEoivdiJilQ/viewform")

time.sleep(1)

childs_name_field = driver.find_element(By.XPATH, childs_name_field_xpath)
childs_name_field.send_keys(childs_name)
# time.sleep(1.2)

pdob_field = driver.find_element(By.XPATH, pdob_field_xpath)
pdob_field.send_keys(pdob)
# time.sleep(1.2)

age_field = driver.find_element(By.XPATH, age_field_xpath)
age_field.click()
# time.sleep(1.2)

# pdob_field = driver.find_element(By.XPATH, gender1_field_xpath)
# pdob_field.send_keys(gender)
# # time.sleep(1.2)

# gender_field = driver.find_element(By.XPATH, gender2_field_xpath)
# gender_field.click()
# # time.sleep(1.2)

religion_field = driver.find_element(By.XPATH, religion_field_xpath)
religion_field.send_keys(religion)
# time.sleep(1.2)

parents_name_field = driver.find_element(By.XPATH, parents_name_field_xpath)
parents_name_field.send_keys(parents_name)
# time.sleep(1.2)

department_field = driver.find_element(By.XPATH, department_field_xpath)
department_field.send_keys(department)
# time.sleep(1.2)

phone_field = driver.find_element(By.XPATH, phone_field_xpath)
phone_field.send_keys(phone)
# time.sleep(1.2)

address_field = driver.find_element(By.XPATH, address_field_xpath)
address_field.send_keys(address)
# time.sleep(1.2)

allergies_field = driver.find_element(By.XPATH, allergies_field_xpath)
allergies_field.send_keys(allergies)
# time.sleep(1.2)


booking_date1_field = driver.find_element(By.XPATH, booking_date1_field_xpath)
booking_date2_field = driver.find_element(By.XPATH, booking_date2_field_xpath)
booking_date3_field = driver.find_element(By.XPATH, booking_date3_field_xpath)
booking_date4_field = driver.find_element(By.XPATH, booking_date4_field_xpath)
booking_date5_field = driver.find_element(By.XPATH, booking_date5_field_xpath)

booking_date1_field.click()
# time.sleep(1.2)

booking_date2_field.click()
# time.sleep(1.2)

booking_date3_field.click()
# time.sleep(1.2)

booking_date4_field.click()
# time.sleep(1.2)

booking_date5_field.click()
# time.sleep(1.2)

submit_button = driver.find_element(By.XPATH, submit_button_xpath)
# submit_button.click()
end_time = time.time()

# time.sleep(1.2)

# screenshot = pyautogui.screenshot()
# filename = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")
# screenshot.save(filename)

 # record when the program ends
elapsed_time = end_time - start_time  # seconds taken

print(f"Total time taken: {elapsed_time:.2f} seconds")
print("Form Submmited on " + datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))

time.sleep(3600)
# driver.quit()