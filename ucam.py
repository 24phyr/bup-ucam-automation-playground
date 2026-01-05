from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from dotenv import load_dotenv
load_dotenv()

print("BUP UCAM Automation")

browser = webdriver.Firefox()
browser.get('https://ucam.bup.edu.bd/')

print("Logging In...")

user_elem = browser.find_element(By.ID, 'UserId')
user_elem.send_keys(os.environ["USERID"])

password_elem = browser.find_element(By.ID, 'Password')
password_elem.send_keys(os.environ["PASSWORD"])
password_elem.submit()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'ctl00_lblLogout')))
student_name = browser.find_element(By.ID, 'ctl00_lblAvatarName').text

print("Login Successful")
print("Welcome, " + student_name)

examMark_elem = browser.find_element(By.LINK_TEXT, 'Current Exam Mark')
examMark_elem.click()

# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[3]/div/div/div/div[1]/label')))

select_element = browser.find_element(By.NAME, 'ctl00$MainContainer$ddlSession')
select = Select(select_element)
select.select_by_value('1066')

#WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'ctl00_MainContainer_gvExamMarkSummary')))
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContainer_gvExamMarkSummary_ctl02_btnViewDetails"]')))


viewdetail_elem1 = browser.find_element(By.NAME, 'ctl00$MainContainer$gvExamMarkSummary$ctl02$btnViewDetails')
viewdetail_elem1.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblMarks"]')))

class Course:
    def __init__(self, serial, code, title):
        self.serial = serial
        self.code = code
        self.title = title
        self.CT1 = browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblMarks').text
        self.CT2 = browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl03_lblMarks').text
        self.CT3 = browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl04_lblMarks').text
        self.CT4 = browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl05_lblMarks').text
        self.mid = browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl06_lblMarks').text
        self.assignment = browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl07_lblMarks').text
        self.attendance = browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl08_lblMarks').text
        
c1 = Course(browser.find_element(By.XPATH, "(//b[contains(text(),'1')])[1]").text, browser.find_element(By.ID, 'ctl00_MainContainer_gvExamMarkSummary_ctl02_lblFormalCode').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvExamMarkSummary_ctl02_lblTitle').text)

viewdetail_elem3 = browser.find_element(By.NAME, 'ctl00$MainContainer$gvExamMarkSummary$ctl04$btnViewDetails')
viewdetail_elem3.click()

time.sleep(3) # Had to implement time.sleep() because i cant find any new to presence_of_element_located() . Otherwise it takes the previous course values because Table loads fast with same elements and IDs.

c3 = Course(browser.find_element(By.XPATH, "(//b[contains(text(),'3')])[1]").text, browser.find_element(By.ID, 'ctl00_MainContainer_gvExamMarkSummary_ctl04_lblFormalCode').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvExamMarkSummary_ctl04_lblTitle').text)

print(c1.serial)
print(c1.code)
print(c1.title)
print(c1.CT1)
print(c1.CT2)
print(c1.CT3)
print(c1.CT4)
print(c1.mid)
print(c1.assignment)
print(c1.attendance)
print("==================")
print(c3.serial)
print(c3.code)
print(c3.title)
print(c3.CT1)
print(c3.CT2)
print(c3.CT3)
print(c3.CT4)
print(c3.mid)
print(c3.assignment)
print(c3.attendance)