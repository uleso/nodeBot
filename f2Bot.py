
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions  as EC

import loadXl
import datetime
xl = loadXl.loadXl(r"Nodes.xlsx")
f2Nodes = xl.loadData(1,1,2,50,True)
service = Service(executable_path = ChromeDriverManager().install())
f2options = webdriver.ChromeOptions()
f2options.page_load_strategy = "normal"
docsisDriver = webdriver.Chrome(service=service,options=f2options)


docsisUrl= r"http://snmp-prod-dyas.osn.wireless.rogers.com/graph/Rogers_Tools_files/search.html"


docsisDriver.implicitly_wait(100)
currentDaytime = datetime.datetime.today()
Today = currentDaytime.date()
windowNumber=0
def f2nodeBas(node):
   
    
    docsisDriver.switch_to.new_window("window") 
    docsisDriver.get(docsisUrl)
    nodeTextBox = docsisDriver.find_element(By.NAME,"node")
    nodeTextBox.clear()
    nodeTextBox.send_keys(node)
    docsisDriver.find_element(By.XPATH,r"//body/center/table/tbody/tr/td[3]/form/input[2]").click()
    windowlist.append(docsisDriver.current_window_handle)
    
    
    
    
    
def canvasCheck(nodesW):
   
    for window in nodesW:
        docsisDriver.switch_to.window(window[0])
        docsisDriver.set_window_size(1060,690)
        try:
            element = WebDriverWait(docsisDriver,600).until(EC.presence_of_element_located((By.ID,"fchart1")))
        finally:
            docsisDriver.save_screenshot(f"Screenshots//{window[1]}_{str(Today)}.png")

windowlist = []
for node in f2Nodes:
    f2nodeBas(str(node))
    

ALL_W = docsisDriver.window_handles
docsisDriver.switch_to.window(ALL_W[0])
docsisDriver.close()

for window in windowlist:
    docsisDriver.switch_to.window(window)
    docsisDriver.close()

ALL_W2=docsisDriver.window_handles
nodesW=tuple(zip(ALL_W2,f2Nodes))
print(nodesW)
canvasCheck(nodesW)
