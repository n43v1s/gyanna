from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

TARGET_HOUR = 13
TARGET_MINUTE = 00

print(f"Waiting until {TARGET_HOUR:02d}:{TARGET_MINUTE:02d}...")
while True:
    now = datetime.now()
    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        break
    time.sleep(1)
print(f"It's {TARGET_HOUR:02d}:{TARGET_MINUTE:02d}, running automation...")



# xpaths
childs_name_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
pdob_field_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
age_field_xpath = '//*[@id="i17"]/div[2]'
gender_field_xpath = '//*[@id="i32"]/div[2]'
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
submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'

# texts
childs_name = "Gyanna"
pdob = "Jakarta, 6 November"
religion = "Protestan"
parents_name = "Astria Martina Silaban" 
department = "KSA"
phone = "6282161175790"
address = "Depok"
allergies = "None"

driver = webdriver.Chrome()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScxnNF6jb31-sSWVh5x3M-2GywkJ3LmqorfNhzNuhBAoPAdxQ/viewform?usp=header")

time.sleep(1)

childs_name_field = driver.find_element(By.XPATH, childs_name_field_xpath)
childs_name_field.send_keys(childs_name)

pdob_field = driver.find_element(By.XPATH, pdob_field_xpath)
pdob_field.send_keys(pdob)

age_field = driver.find_element(By.XPATH, age_field_xpath)
age_field.click()

gender_field = driver.find_element(By.XPATH, gender_field_xpath)
gender_field.click()

religion_field = driver.find_element(By.XPATH, religion_field_xpath)
religion_field.send_keys(religion)

parents_name_field = driver.find_element(By.XPATH, parents_name_field_xpath)
parents_name_field.send_keys(parents_name)

department_field = driver.find_element(By.XPATH, department_field_xpath)
department_field.send_keys(department)

phone_field = driver.find_element(By.XPATH, phone_field_xpath)
phone_field.send_keys(phone)

address_field = driver.find_element(By.XPATH, address_field_xpath)
address_field.send_keys(address)

allergies_field = driver.find_element(By.XPATH, allergies_field_xpath)
allergies_field.send_keys(allergies)


booking_date1_field = driver.find_element(By.XPATH, booking_date1_field_xpath)
booking_date2_field = driver.find_element(By.XPATH, booking_date2_field_xpath)
booking_date3_field = driver.find_element(By.XPATH, booking_date3_field_xpath)
booking_date4_field = driver.find_element(By.XPATH, booking_date4_field_xpath)
booking_date5_field = driver.find_element(By.XPATH, booking_date5_field_xpath)

booking_date1_field.click()
booking_date2_field.click()
booking_date3_field.click()
booking_date4_field.click()
booking_date5_field.click()



submit_button = driver.find_element(By.XPATH, submit_button_xpath)
submit_button.click()

print("Form Submmited")


time.sleep(5)
# driver.quit()