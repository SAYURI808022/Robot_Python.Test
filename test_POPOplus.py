# coding=UTF-8
from cgitb import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import allure
import time

@allure.story('登入測試')
def test_login():
    driver=openbrowser()
    login(driver)
    closeBrowser(driver)

@allure.story('修改個資測試')  
def test_presonal_information(): 
    driver=openbrowser()
    login(driver)
    personal_information(driver)
    check(driver)
    change_nickname(driver) 
    rest_nickname(driver)
    closeBrowser(driver)

@allure.story('查詢店家活動')
def test_store():
    driver=openbrowser()
    login(driver)
    search_store(driver)
    verify_store(driver)
    closeBrowser(driver)

@allure.story('查詢卡片')
def test_verify_card():
    driver=openbrowser()
    search_button(driver)
    search_name(driver)
    next_page(driver)
    search_picture(driver)
    closeBrowser(driver)

@allure.story('查詢相關規範')
def test_verify_rule():
    driver=openbrowser()
    new_web_page_button(driver)
    check_regulations(driver)
    closeBrowser(driver)

@allure.step('打開網頁')
def openbrowser():
    path="./geckodriver"
    service = Service(path)
    driver=webdriver.Firefox(service=service)
    driver.get('https://asia.pokemon-card.com/tw/')
    return driver

@allure.step("closeBrowser")
def closeBrowser(driver):
    driver.quit()

@allure.step('選擇登入按鈕')
def login(driver): 
    driver.find_element(By.XPATH,'/html/body/header/nav[2]/ul/li[2]/a/span').click() 
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/main/article/section/section[1]')
            ))    
    email=driver.find_element(By.XPATH,'//*[@id="mail"]')
    password=driver.find_element(By.XPATH,'//*[@id="password"]')
    email.send_keys('sunshinecrazy113229@gmail.com')
    password.send_keys('jesse123') 
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    # WebDriverWait(driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (By.XPATH,'/html/body/main/article/section/section[1]/form/div[3]/button')
    #         ))
    time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/main/article/section/section[1]/form/div[3]/button').click()
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/main/div/div/div/section/ul[1]')
            ))       
    nickname=driver.find_elements(By.XPATH,'/html/body/main/div/div/div/section/ul[1]/li[2]')
    for title in nickname:
        assert(title.text=='SAYURI*808022')

@allure.step('點選用戶情報')   
def personal_information(driver): 
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)        
    driver.find_element(By.XPATH,'/html/body/main/div/div/div/section/ul[2]/li/ul/li[4]').click()

@allure.step('檢查個人資料是否錯誤和更改')
def check(driver): # verify_personal_infomation_modify
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/main/div/div/article')
            ))
    time.sleep(1)        
    titles=driver.find_elements(By.XPATH,'/html/body/main/div/div/article/section/table/tbody/tr[3]/td')
    for title in titles:
        assert(title.text=='楊育昌')
    WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH,'/html/body/main/div/div/article/section/div[1]/a')
            ))
    driver.find_element(By.XPATH,'/html/body/main/div/div/article/section/div[1]/a').click()
    driver.find_element(By.XPATH,'//*[@id="emailConfirmation"]').send_keys('sunshinecrazy113229@gmail.com')
    driver.find_element(By.XPATH,'//*[@id="nickname"]').clear()
    driver.find_element(By.XPATH,'//*[@id="nickname"]').send_keys('SAYURI*808033')
    driver.find_element(By.XPATH,'/html/body/main/div/header/h1').click()
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/main/div/div/article/section/form/div/button[2]').click()
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/main/div/header/h1')
            ))
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/main/div/div/article/section/form/div/button[2]').click()

@allure.step('檢查更改是否正確') 
def change_nickname(driver): 
    check_name=driver.find_elements(By.XPATH,'/html/body/main/div/div/div/section/ul[1]/li[2]')
    for chang_name in check_name:
        assert(chang_name.text == 'SAYURI*808033')

@allure.step('改回名字')
def rest_nickname(driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5) 
    driver.find_element(By.XPATH,'/html/body/main/div/div/div/section/ul[2]/li/ul/li[4]').click()
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN) 
    time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/main/div/div/article/section/div[1]/a').click()
    driver.find_element(By.XPATH,'//*[@id="emailConfirmation"]').send_keys('sunshinecrazy113229@gmail.com')
    driver.find_element(By.XPATH,'//*[@id="nickname"]').clear()
    driver.find_element(By.XPATH,'//*[@id="nickname"]').send_keys('SAYURI*808022')
    driver.find_element(By.XPATH,'/html/body/main/div/header/h1').click()
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/main/div/div/article/section/form/div/button[2]').click()
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/main/div/header/h1')
            ))
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/main/div/div/article/section/form/div/button[2]').click()

@allure.step('活動搜尋')
def search_store(driver):
    driver.find_element(By.XPATH,'/html/body/main/div/div/article/section/div[2]/a/button').click()
    driver.find_element(By.XPATH,'//*[@id="keyword"]').send_keys('鬥樂一中店')
    driver.find_element(By.XPATH,'//*[@id="endDate"]').send_keys('07-20-2022')
    driver.find_element(By.XPATH,'/html/body/main/div/div/div[1]/form/div[1]/div[4]/div/div[2]').click()
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'//*[@id="addSearchConditionModal"]/div/div/div[3]/h5[1]')
            ))
    driver.find_element(By.XPATH,'//*[@id="addSearchConditionModal"]/div/div/div[3]/div[1]/div[1]').click()
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'//*[@id="addSearchConditionModal"]/div/div/div[3]/h5[2]')
            ))
    driver.find_element(By.XPATH,'//*[@id="addSearchConditionModal"]/div/div/div[3]/div[1]/div[2]/div[4]/label').click()
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'//*[@id="addSearchConditionModal"]/div/div')
            ))
    driver.find_element(By.XPATH,'//*[@id="addSearchConditionModal"]/div/div/div[3]/div[5]/button[2]').click()
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'//*[@id="addSearchConditionModal"]/div/div/div[4]')
            ))
    driver.find_element(By.XPATH,'/html/body/main/div/div/div[1]/form/div[1]/div[6]/button[2]').click()
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/main/div/div/div[2]/div/div')
            ))

@allure.step('確認店家')
def verify_store(driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    search_name=driver.find_elements(By.XPATH,'/html/body/main/div/div/div[2]/ul/a[1]/li/div[2]/p[3]')
    for title in search_name:
        assert(title.text=='鬥樂一中店')
        driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/ul/a[1]/li/div[2]/p[2]').click()

@allure.step('點選搜尋標籤')
def search_button(driver):
    driver.find_element(By.XPATH,'/html/body/header/nav[2]/ul/li[1]/button/span').click()

@allure.step('搜尋名字')
def search_name(driver):
    driver.find_element(By.XPATH,'//*[@id="keyword"]').send_keys('皮卡丘')#搜尋選項
    WebDriverWait(driver, 20).until(#延遲時間
        EC.presence_of_element_located((By.XPATH,'/html/body/footer/div')) 
        )       
    driver.find_element(By.XPATH,'//*[@id="tabContentCard"]/form/div/div[1]/button').click()

@allure.step('換下一頁')
def next_page(driver):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/main/div/header/h1')) 
        )
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    WebDriverWait(driver, 20).until(#延遲時間
        EC.element_to_be_clickable((By.XPATH,'/html/body/main/div/form/div/div[2]/div[2]/ul/li[20]/a/div/img')) 
        )
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[2]/div[2]/section/nav/ol/li[4]/a').click()

@allure.step('搜尋圖片')
def search_picture(driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    WebDriverWait(driver,20).until(#延遲時間
        EC.element_to_be_clickable((By.XPATH,'/html/body/main/div/form/div/div[2]/div[2]/ul/li[14]/a/div/img')) 
        )
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[2]/div[2]/ul/li[14]/a/div/img').click()
    verify_pitcure=driver.find_element(By.XPATH,'/html/body/main/div/div/section[1]/div/img')
    assert(verify_pitcure.get_attribute("src") == "https://asia.pokemon-card.com/tw/card-img/tw00002805.png")
    # picture_link = etree.xpath('/html/body/main/div/div/section[1]/div/img')
    # for list in picture_link:
    #     html = '<img src="https://asia.pokemon-card.com/tw/card-img/tw00002805.png">' + list.xpath('/html/body/main/div/div/section[1]/div/img')[0]
    #     name = list.xpath("./a/img/@alt")[0] + ".png"
    #     assert(list.text=='<img src="https://asia.pokemon-card.com/tw/card-img/tw00002805.png">')

@allure.step('點選新網頁')
def new_web_page_button(driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    # WebDriverWait(driver,20).until(#延遲時間
    #     EC.element_to_be_clickable((By.XPATH,'/html/body/footer/div/section[1]/a/button')) 
    #     )
    time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/footer/div/nav[1]/ul/li[2]').click()
    time.sleep(0.5)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    
@allure.step('檢查法規')  
def check_regulations(driver):
    regulations=driver.find_element(By.XPATH,'/html/body/main/article/h3[7]')
    assert(regulations.text=='第7條 智慧財產權')
    # regulations_branch=driver.find_element(By.XPATH,'/html/body/main/article/p[6]')
    # assert(regulations_branch.text=='本服務所刊載的設計、照片、影像、文章、音樂、聲音等所有內容資料（下稱「資料」）之著作權或使用授權之權利，歸屬本公司所有。關於本服務上之任何內容，帳號持有人不取得智慧財產權、請求權或其他任何權利，嚴格禁止從本服務中拷貝、複製、變更、出版、揭露、電信傳送、或散布資料。且不得於本服務外使用此等資料。')
