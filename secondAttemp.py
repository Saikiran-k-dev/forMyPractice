import xlrd as xlrd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
url = 'https://smartamcu.smartmoo.com/#/login'
target_url = 'https://smartamcu.smartmoo.com/#/home/erp/erpconfig'
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver,100)
wait.until(EC.element_to_be_clickable((By.NAME,"name"))).send_keys("srinidhi_ntp")
wait.until(EC.element_to_be_clickable((By.NAME,"password"))).send_keys("Stellapps@123")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-primary']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle']")))
driver.get(target_url)
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Push Farmers"))).click()
time.sleep(2)
workbook = xlrd.open_workbook('/home/stellapps/Downloads/seleniumtest.xls')
sheet = workbook.sheet_by_name('Sheet1')
for row_index in range(sheet.nrows):
    Organization = str(sheet.cell_value(row_index, 0))
    Chillingcenter = str(sheet.cell_value(row_index, 1))
    Collectioncenter = str(sheet.cell_value(row_index, 2))
    print(Organization, Chillingcenter, Collectioncenter)

    dropdown = wait.until(EC.visibility_of_element_located((By.NAME, "organization")))
    select = Select(dropdown)

    if Organization == "Organization":
        continue
    time.sleep(2)
    select.select_by_visible_text(Organization)
    time.sleep(2)
    finalChillingCenter=Chillingcenter.split(".")[0]
    finalCollectionCenter=Collectioncenter.split(".")[0]
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='button multiSelectButton ng-binding']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{finalChillingCenter}')]"))).click()
    wait.until(EC.presence_of_all_elements_located((By.XPATH,"//button[@class='button multiSelectButton ng-binding']")))[1].click()
    time.sleep(5)
    wait = WebDriverWait(driver,10000)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '105')]"))).click()

