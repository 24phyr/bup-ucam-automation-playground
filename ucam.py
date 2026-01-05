from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
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


viewdetail_elem = browser.find_element(By.NAME, 'ctl00$MainContainer$gvExamMarkSummary$ctl02$btnViewDetails')
viewdetail_elem.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblMarks"]')))

class Course_1:
    def __init__(self, code, title, CT1, CT2, CT3, CT4, mid, assignment, attendance):
        self.code = code
        self.title = title
        self.CT1 = CT1
        self.CT2 = CT2
        self.CT3 = CT3
        self.CT4 = CT4
        self.mid = mid
        self.assignment = assignment
        self.attendance = attendance

c1 = Course_1(browser.find_element(By.ID, 'ctl00_MainContainer_gvExamMarkSummary_ctl02_lblFormalCode').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvExamMarkSummary_ctl02_lblTitle').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblMarks').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl03_lblMarks').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl04_lblMarks').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl05_lblMarks').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl06_lblMarks').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl07_lblMarks').text, browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl08_lblMarks').text)