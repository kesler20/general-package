from flask.globals import session
import selenium
from selenium import webdriver as wb
import os
from os import path as ps
import time
import subprocess
import time
import schedule

list_of_chilled_music = ['''Guns N' Roses - Sweet Child O' Mine (Official Music Video)''',
'''VACATIONS - YOUNG (SLOWED+REVERB+SATURATION) ''',
'''K CAMP - Switch (Official Video)''',
'''vas - jagger finn (1 hour)''',
'''Rental''','''Current joys A Different Age''']

common_exceptions = { 'no_element':'selenium.common.exceptions.NoSuchElementException',
'not_interact':'selenium.common.exceptions.ElementNotInteractableException'}

TargetJobs = 'https://targetjobs.co.uk/internships'
Muse_url = 'https://www.sheffield.ac.uk/'
Gradcracker = 'https://www.gradcracker.com/search/all-disciplines/engineering-jobs'
drive_cpe260 = 'https://drive.google.com/drive/u/1/folders/0ADQwLtxBAjhwUk9PVA'
drive_cpe270 = 'https://drive.google.com/drive/u/1/folders/0ACNSaKFc0HonUk9PVA'
jm_board = 'https://jamboard.google.com/d/1SqHIdqVxT_se4BaCzIXfmmAqj0j6mEfxB31kEBx-xLI/viewer?f=2'
emg_drive = 'https://drive.google.com/drive/u/1/folders/0AL6GBsvh_FEMUk9PVA'
documents_python = 'https://docs.python.org/3/library/functions.html#func-list'
subject_code = 0
exceptiontime = 120
session_lenght = 120
email_read_time = 10

def workflow_automation(e_mail, email_read_time):
    x = ps.abspath('msedgedriver.exe')
    driver = wb.Edge(x)
    
    #open email and log in
    if e_mail == True:
        driver.get('https://mail.google.com/mail/u/1/#inbox')
        search_box = driver.find_element_by_id('identifierId')
        search_box.send_keys('kuisoko1@sheffield.ac.uk')
        next_buttom = driver.find_element_by_id("identifierNext")
        try:
            next_buttom.click()
        except selenium.common.exceptions.ElementClickInterceptedException as err:
            print(err)
            time.sleep(20)
        time.sleep(10)
        username_search_box = driver.find_element_by_id('username')
        username_search_box.send_keys('fca19kui')
        password_searchbox = driver.find_element_by_id('password')
        password_searchbox.send_keys('keslerisoko20')
        login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
        login_button.click()
        time.sleep(60*email_read_time)
    else:
        pass
    
    #blackboard 
    driver.get('https://vle.shef.ac.uk/?new_loc=%2Fultra%2Fcourse')
    cookiebox = driver.find_element_by_id('agree_button')
    cookiebox.click()
    userBox = driver.find_element_by_id("user_id")
    userBox.send_keys('fca19kui')
    passwordBox = driver.find_element_by_id('password')
    passwordBox.send_keys('keslerisoko20')
    driver.find_element_by_id('entry-login').click()
    time.sleep(60*session_lenght)

def get_driver(url):
    #setup the driver
    x = ps.abspath('msedgedriver.exe')
    driver = wb.Edge(x)

    driver.get(url)
    return driver
    
def get_music(index_list):
    x = ps.abspath('msedgedriver.exe')
    driver = wb.Edge(x)

    driver.get('https://www.youtube.com/')
    time.sleep(20)
    '''
    sign_in_button_xpath = '//*[@id="text"]'
    
    sign_in = driver.find_element_by_xpath(sign_in_button_xpath)
    sign_in.click()
    search_box = driver.find_element_by_id('identifierId')
    search_box.send_keys('kuisoko1@sheffield.ac.uk')
    next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    next_button.click()
    time.sleep(10)
    '''

    username_search_box = driver.find_element_by_id('username')
    username_search_box.send_keys('fca19kui')
    password_searchbox = driver.find_element_by_id('password')
    password_searchbox.send_keys('keslerisoko20')
    login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
    login_button.click()
    time.sleep(10)

    search_box_youtube = driver.find_element_by_id('search')
    search_box_youtube.send_keys(list_of_chilled_music[index_list])
    driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon').click()

    while True:
        time.sleep(60)

def get_calendar(calendar):
    x = ps.abspath('msedgedriver.exe')
    driver = wb.Edge(x)

    driver.get('https://vle.shef.ac.uk/?new_loc=%2Fultra%2Fcourse')
    cookiebox = driver.find_element_by_id('agree_button')
    cookiebox.click()
    userBox = driver.find_element_by_id("user_id")
    userBox.send_keys('fca19kui')
    passwordBox = driver.find_element_by_id('password')
    passwordBox.send_keys('keslerisoko20')
    driver.find_element_by_id('entry-login').click()
    time.sleep(10)
    
    cpe260 = driver.find_element_by_xpath('//*[@id="course-link-_90148_1"]/h4')
    cpe260.click()
    time.sleep(10)
    driver.back()
    driver.find_element_by_xpath('//*[@id="course-link-_90149_1"]/h4').click()
    time.sleep(5)
    cpe_260_270_checklist = driver.find_element_by_xpath('//*[@id="paletteItem:_1451727_1"]/a/span')
    cpe_260_270_checklist.click()
    time.sleep(10)    
    if calendar == True:
        driver.back()
        driver.find_element_by_xpath('//*[@id="anonymous_element_11"]/a/span').click()
    
    while True:
        time.sleep(10)

def textbooks_opener(subject):
    if subject == 260:
        url = 'https://www.vlebooks.com/Vleweb/Product/Index/1144266?page=0'

        x = ps.abspath('msedgedriver.exe')
        driver = wb.Edge(x)  
        driver.get(url)     
        shyboleah = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div[2]/a[1]')
        shyboleah.click()
        time.sleep(3)
        search_uni = driver.find_element_by_id('typeahead')
        search_uni.send_keys('university of sheffield')
        time.sleep(5)
        click_sheffield = driver.find_element_by_xpath('//*[@id="results-table"]/table/tbody/tr[1]/td[2]/div/span')
        click_sheffield.click()
        username_search_box = driver.find_element_by_id('username')
        username_search_box.send_keys('fca19kui')
        password_searchbox = driver.find_element_by_id('password')
        password_searchbox.send_keys('keslerisoko20')
        login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
        login_button.click()
        time.sleep(60*session_lenght)
    else:
        url = 'https://ebookcentral.proquest.com/lib/sheffield/detail.action?docID=4625968'
        x = ps.abspath('msedgedriver.exe')
        driver = wb.Edge(x)

        driver.get(url)
        username_search_box = driver.find_element_by_id('username')
        username_search_box.send_keys('fca19kui')
        password_searchbox = driver.find_element_by_id('password')
        password_searchbox.send_keys('keslerisoko20')
        login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
        login_button.click()
        time.sleep(60*session_lenght)               

def design_project_drive(check_time=70):
    process_safety_group_drive = r'https://drive.google.com/drive/u/1/folders/0AF2F0Qdd4zDvUk9PVA'
    driver = get_driver(process_safety_group_drive)
    search_box = driver.find_element_by_id('identifierId')
    search_box.send_keys('kuisoko1@sheffield.ac.uk')
    next_buttom = driver.find_element_by_id("identifierNext")
    try:
        next_buttom.click()
    except selenium.common.exceptions.ElementClickInterceptedException as err:
        print(err)
        time.sleep(20)
    time.sleep(10)
    username_search_box = driver.find_element_by_id('username')
    username_search_box.send_keys('fca19kui')
    password_searchbox = driver.find_element_by_id('password')
    password_searchbox.send_keys('keslerisoko20')
    login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
    login_button.click()


def initialize_workflow():
    os.system('start https://d.docs.live.net/d6e96d5e52a0d29c/Documents/Routines/Gymnasium.xlsx')
    os.system('start https://d.docs.live.net/d6e96d5e52a0d29c/Documents/Routines')
    os.system('start https://d.docs.live.net/d6e96d5e52a0d29c/Documents')

    get_timetable()
    design_project_drive()

    try:
        workflow_automation(True, 5)
    except selenium.common.exceptions.NoSuchElementException:
        while True:
            time.sleep(60*exceptiontime)
        
def get_timetable():
    url = 'https://cmisgonow.sheffield.ac.uk/CMISGo/Web/Timetable'
    x = ps.abspath('msedgedriver.exe')
    driver = wb.Edge(x)
    driver.get(url)    
    time.sleep(10)
    username_search_box = driver.find_element_by_id('username')
    username_search_box.send_keys('fca19kui')
    password_searchbox = driver.find_element_by_id('password')
    password_searchbox.send_keys('keslerisoko20')
    login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
    login_button.click()
    time.sleep(60)

def get_SURE_calendar(calendar_check_time=70):
    Skills301 = 'https://301skills.shef.ac.uk/events/calendar'
    Skills301 = 'https://301skills.shef.ac.uk/events/categories/academic_skills_workshop_core'
    Skills301 = 'https://301skills.shef.ac.uk/events/calendar'
    driver = get_driver(r'https://calendar.google.com/calendar/u/1/r/week/2021/6/26?cid=Y19uNGM1MmVhdWU5ZDRwNDcxY2gzN3FoaDJna0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t&pli=1')
    search_box = driver.find_element_by_id('identifierId')
    search_box.send_keys('kuisoko1@sheffield.ac.uk')
    next_buttom = driver.find_element_by_id("identifierNext")
    try:
        next_buttom.click()
    except selenium.common.exceptions.ElementClickInterceptedException as err:
        print(err)
        time.sleep(20)
    time.sleep(10)
    username_search_box = driver.find_element_by_id('username')
    username_search_box.send_keys('fca19kui')
    password_searchbox = driver.find_element_by_id('password')
    password_searchbox.send_keys('keslerisoko20')
    login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
    login_button.click()
    time.sleep(calendar_check_time)

def Process_Safety_Drive(check_time=70):
    process_safety_group_drive = r'https://drive.google.com/drive/u/1/folders/1-mCn__Vcor3SlNmAbqGZ5MmEaDfUXWzO'
    driver = get_driver(process_safety_group_drive)
    search_box = driver.find_element_by_id('identifierId')
    search_box.send_keys('kuisoko1@sheffield.ac.uk')
    next_buttom = driver.find_element_by_id("identifierNext")
    try:
        next_buttom.click()
    except selenium.common.exceptions.ElementClickInterceptedException as err:
        print(err)
        time.sleep(20)
    time.sleep(10)
    username_search_box = driver.find_element_by_id('username')
    username_search_box.send_keys('fca19kui')
    password_searchbox = driver.find_element_by_id('password')
    password_searchbox.send_keys('keslerisoko20')
    login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
    login_button.click()
    time.sleep(6)
    push_button = driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button')
    push_button.click()
    time.sleep(check_time)

def get_website(url, uni_website=False, check_time=120):
    if uni_website:
        driver = get_driver(url)
        search_box = driver.find_element_by_id('identifierId')
        search_box.send_keys('kuisoko1@sheffield.ac.uk')
        next_buttom = driver.find_element_by_id("identifierNext")
        try:
            next_buttom.click()
        except selenium.common.exceptions.ElementClickInterceptedException as err:
            print(err)
            time.sleep(20)
        time.sleep(10)
        username_search_box = driver.find_element_by_id('username')
        username_search_box.send_keys('fca19kui')
        password_searchbox = driver.find_element_by_id('password')
        password_searchbox.send_keys('keslerisoko20')
        login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
        login_button.click()
        time.sleep(6)
        push_button = driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button')
        push_button.click()
        time.sleep(check_time)
    else:
        driver = get_driver(url)
        #search_box = driver.find_element_by_id('identifierId')
        #search_box.send_keys('uchekesla@gmail.com')
        #next_buttom = driver.find_element_by_id("identifierNext")
        #try:
        #    next_buttom.click()
        #except selenium.common.exceptions.ElementClickInterceptedException as err:
        #    print(err)
        #    time.sleep(20)
        time.sleep(check_time)

def start_gym():
    os.system('start C:/Users/Uchek/Desktop/ngrok-stable-windows-amd64/ngrok.exe http 5500')

