from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
import webbrowser
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
global len_dis
global len_stn


countD = 2
countS = 1


def addCounterDis():
    global countD
    countD = countD + 1
    return countD

def addCounter():
    global countS
    countS = countS + 1
    return countS

def pdf():
    # //Print column values
    before_XPath = "/html/body/center/div/div[4]/div[2]/table/tbody" #xpath till table id
    # Below are xpath extentions post table id for specific row and columns
    aftertd_XPath_1 = "/td[1]/center"
    aftertd_XPath_2 = "/td[2]/center"
    aftertd_XPath_3 = "/td[3]/center"
    aftertd_XPath_4 = "/td[4]/center"
    aftertd_XPath_5 = "/td[5]/center"
    aftertd_XPath_6 = "/td[6]/center"
    # aftertr_XPath = "]"
    elements = driver.find_elements_by_xpath('/html/body/center/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/center/a')
    print('elements:', elements)
    text_list = [element.text for element in elements]  # list of strings
    print('text_list:', text_list)
    # time.sleep(3s0)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "tb")))
    rows = len(driver.find_elements_by_xpath("/html/body/center/div/div[4]/div[2]/table/tbody/tr"))
    print('rows:', rows)
    columns = len(driver.find_elements_by_xpath("/html/body/center/div/div[4]/div[2]/table/tbody/tr[1]/td"))
    print('columns:', columns)
    for t_row in range(1, (rows + 1)):
        # print('t_row:', t_row)
        tr_row = "/tr[" + str(t_row) + "]"
        FinalXPath = before_XPath + tr_row + aftertd_XPath_4
        cell_text = driver.find_element_by_xpath(FinalXPath).text
        output = cell_text.find("294-IPC")
        # print('cell_text', cell_text)
        if (output != -1):
            # print('t_row:', t_row)
            FinalXPath = before_XPath + tr_row + aftertd_XPath_6 + "/a"
            # print('FinalXPath:', FinalXPath)
            download = []
            download = driver.find_element_by_xpath(FinalXPath).get_attribute('href')
            time.sleep(2)
            webbrowser.open(download, new=2)
            time.sleep(15)
            pyautogui.press('enter')
            print("downloaded:", download)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://search.cgpolice.gov.in/CCTNS_Citizen_Portal/Citizen_Portal.jsp")
driver.maximize_window()
driver.refresh()
time.sleep(3)

Police_station = driver.find_elements_by_xpath('/html/body/center/div/div[3]/div/div/form/div[1]/div/div[5]/select/option')
global len_stn
len_stn = len(Police_station)
time.sleep(2)
district = driver.find_elements_by_xpath('/html/body/center/div/div[3]/div/div/form/div[1]/div/div[2]/select/option')
global len_dis
len_dis = len(district)

# xpath for options in district storing data from xpath in District variable
def district_selection():
    global countD
    print('countD:', countD)
    district = driver.find_elements_by_xpath('/html/body/center/div/div[3]/div/div/form/div[1]/div/div[2]/select/option')
    global len_dis
    len_dis = len(district)
    print('len_dis:', len_dis)
    dist = Select(driver.find_element_by_xpath('//*[@id="dist"]'))#Selecting a district name from the dropdown
    for d in range(countD):  #//1
        dist.select_by_visible_text(district[d].text)
        print(district[d].text)

def police_stn():
    addCounter()
    global countS
    print('countS:', countS)
    Police_station = driver.find_elements_by_xpath('/html/body/center/div/div[3]/div/div/form/div[1]/div/div[5]/select/option')
    global len_stn
    len_stn = len(Police_station)
    print('len_stn:', len_stn)
    station = Select(driver.find_element_by_xpath('//*[@id="station"]'))
    for s in range(countS):
        station.select_by_visible_text(Police_station[s].text)
        print(Police_station[s].text)



for i in range(len_dis):
    district_selection()
    time.sleep(0.5)
    for j in range(len_stn):
        police_stn()
        time.sleep(2)
        # To select from date
        driver.execute_script("document.getElementById('fromDt').value='11-10-2021'")
        time.sleep(2)
        # to select To Date
        driver.execute_script("document.getElementById('toDt').value='12-10-2021'")
        time.sleep(2)
        # Detect Seach Button
        search_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/center/div/div[3]/div/div/form/div[3]/button[1]"))
        )
        search_btn.click()  # To click on Search button
        # time laps / delay
        time.sleep(3)
        '''
        driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(3)
        pdf()
        '''
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://search.cgpolice.gov.in/CCTNS_Citizen_Portal/Citizen_Portal.jsp")
        driver.maximize_window()
        time.sleep(1)
        driver.refresh()
        time.sleep(3)
        district_selection()
        '''
        if (countS == len_stn):
            addCounterDis()
            district_selection()
        else:
        '''




'''
time.sleep(2)
#xpath for station and stations for specific district are stired in Police_station variable
Police_station = driver.find_elements_by_xpath('/html/body/center/div/div[3]/div/div/form/div[1]/div/div[5]/select/option')
len_stn = len(Police_station)
print(len_stn)
station = Select(driver.find_element_by_xpath('//*[@id="station"]'))
for s in range(2):
    station.select_by_visible_text(Police_station[s].text)
    print(Police_station[s].text)

time.sleep(2)
#To select from date
driver.execute_script("document.getElementById('fromDt').value='11-10-2021'")
time.sleep(2)
#to select To Date
driver.execute_script("document.getElementById('toDt').value='12-10-2021'")
time.sleep(2)


time.sleep(2)

#Detect Seach Button
search_btn = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/center/div/div[3]/div/div/form/div[3]/button[1]"))
)
search_btn.click()  # To click on Search button

# time laps / delay
time.sleep(3)
driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
time.sleep(10)
s +=1
'''