from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
load_dotenv()

print('BUP UCAM Automation')

browser = webdriver.Firefox()
browser.get('https://ucam.bup.edu.bd/')

print('Logging In...')

user_elem = browser.find_element(By.ID, 'UserId')
user_elem.send_keys(os.environ["USERID"])

password_elem = browser.find_element(By.ID, 'Password')
password_elem.send_keys(os.environ["PASSWORD"])
password_elem.submit()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'ctl00_lblLogout')))
student_name = browser.find_element(By.ID, 'ctl00_lblAvatarName').text

print('Login Successful')
print("Welcome, " + student_name)

examMark_elem = browser.find_element(By.LINK_TEXT, 'Current Exam Mark')
examMark_elem.click()

# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[3]/div/div/div/div[1]/label')))

select_element = browser.find_element(By.NAME, 'ctl00$MainContainer$ddlSession')
select = Select(select_element)
select.select_by_value('1066')

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'ctl00_MainContainer_gvExamMarkSummary')))
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContainer_gvExamMarkSummary_ctl02_btnViewDetails"]')))

viewdetail_elem = browser.find_element(By.NAME, "ctl00$MainContainer$gvExamMarkSummary$ctl02$btnViewDetails") #This is the first course
viewdetail_elem.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblMarks"]')))

if browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblMarks').text == '--':
    ct1_value = 0
else:
    ct1_mark = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblExamTemplateBasicItemMark').text)
    ct1_obtained = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl02_lblMarks').text)
    ct1_value = (ct1_obtained/ct1_mark) * 10

if browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl03_lblMarks').text == '--':
    ct2_value = 0
else:
    ct2_mark = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl03_lblExamTemplateBasicItemMark').text)
    ct2_obtained = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl03_lblMarks').text)
    ct2_value = (ct2_obtained/ct2_mark) * 10

if browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl04_lblMarks').text == '--':
    ct3_value = 0
else:
    ct3_mark = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl04_lblExamTemplateBasicItemMark').text)
    ct3_obtained = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl04_lblMarks').text)
    ct3_value = (ct3_obtained/ct3_mark) * 10

if browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl05_lblMarks').text == '--':
    ct4_value = 0
else:
    ct4_mark = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl05_lblExamTemplateBasicItemMark').text)
    ct4_obtained = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl05_lblMarks').text)
    ct4_value = (ct4_obtained/ct4_mark) * 10

if browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl06_lblMarks').text == '--':
    mid_value = 0
else:
    mid_mark = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl06_lblExamTemplateBasicItemMark').text)
    mid_obtained = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl06_lblMarks').text)
    mid_value = (mid_obtained/mid_mark) * 20

if browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl07_lblMarks').text == '--':
    ass_value = 0
else:
    ass_mark = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl07_lblExamTemplateBasicItemMark').text)
    ass_obtained = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl07_lblMarks').text)
    ass_value = (ass_obtained/ass_mark) * 10

if browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl08_lblMarks').text == '--':
    attendance = 0
else:
    attendance_mark = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl08_lblExamTemplateBasicItemMark').text)
    attendance_obtained = float(browser.find_element(By.ID, 'ctl00_MainContainer_gvgvExamMarkSummaryDetails_ctl08_lblMarks').text)
    attendance_value = (attendance_obtained/attendance_mark) * 10

all_quiz = [ct1_value, ct2_value, ct3_value, ct4_value]
lowest = min(all_quiz)
all_quiz.remove(lowest)
best_of_three = all_quiz
quiz_avg = sum(best_of_three) / len(best_of_three)

incourse_total = quiz_avg + mid_value + ass_value + attendance_value

print("Quiz Marks: " + str(quiz_avg))
print("Mid Marks: " + str(mid_value))
print("Assignment Marks: " + str(ass_value))
print("Attendance Marks: " + str(attendance_value))


print("Total Incourse: " + str(incourse_total))