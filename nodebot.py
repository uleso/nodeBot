

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

import EachRow
import loadXl
import datetime
currentDaytime = datetime.datetime.today()
Today = currentDaytime.date()
xl = loadXl.loadXl(r"Nodes.xlsx")
Nodes = xl.loadData(1,1,2,30,True)
Handlers = []
#result 0 = running
#result 1 = No node
#result 2 = Error Page
#result 3 = finished
class Handler:
    def __init__(self,window,node,result=0):
        self.window = window
        self.node = node
        self.result = result
    
# eCon1=EC.visibility_of_element_located((By.XPATH,"//*[@id='outer']//h2"))
# eCon2=
if Nodes is not None:
    options = Options()
    options.page_load_strategy ="none"

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=options)


adhocUrl = r"http://oss-cluster1.mgmt.net.cable.rogers.com/node_qualification.html"
dir_path=r"C:\Users\YPN-1135\Desktop\NodeBot\Screenshots" #herkesin desktop yolunu ekle

def screenshotCount():
    fileList=[]    
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path,path)):
            fileList.append(path)
    return len(fileList)



def nodeBas(node):

    try:
        nodeBox = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"NODE_NUMBER")))

    except exceptions.TimeoutError:
        print("EXCEPTION TIMEOUT")
    finally:
        driver.find_element(By.NAME,"NODE_NUMBER").send_keys(str(node) + Keys.ENTER)

def wHandler(Handler):
    driver.switch_to.window(Handler.window)
    try: 
        WebDriverWait(driver,1200).until(EC.visibility_of_element_located((By.ID,"data-heading1")))
           
    except exceptions.TimeoutException:
        try:
            driver.find_element(By.ID,"L_64_2")
            
            
        except exceptions.NoSuchElementException:
            driver.set_window_size(300,660)
            driver.find_element(By.ID,"data-heading1").location_once_scrolled_into_view
            driver.save_screenshot(f"Screenshots//{Handler.node}_{str(Today)}.png")
        
    driver.set_window_size(868,660)
    driver.find_element(By.ID,"data-heading1").location_once_scrolled_into_view
    driver.save_screenshot(f"Screenshots//{Handler.node}_{str(Today)}.png")
    # else:
        
    #     marker = driver.find_element(By.ID,"data-heading1").location_once_scrolled_into_view
    #     if marker == None:
    #         marker = driver.find_element(By.ID,"data-heading1").location_once_scrolled_into_view
    #     else:
    #         driver.save_screenshot(f"Screenshots//{Handler.node}_{str(Today)}.png")



            
Rows=[]
sNodes = []
if Nodes is not None:
    for cell in Nodes:
        Rows.append(EachRow.EachRow(str(cell)))

    for  EachRow.EachRow in Rows:

        if (type(EachRow.EachRow.splittedNodes) is not tuple):
            sNodes.append(EachRow.EachRow.nodes)
            driver.switch_to.new_window("tab")
            driver.get(adhocUrl)
            nodeBas(EachRow.EachRow.nodes)

        elif(type(EachRow.EachRow.splittedNodes) is tuple):
            for nodes in EachRow.EachRow.splittedNodes:
                sNodes.append(nodes)
                driver.switch_to.new_window("tab")
                driver.get(adhocUrl)
                nodeBas(nodes)

driver.switch_to.window(driver.window_handles[0])
driver.close()
ALL_W = driver.window_handles
nodesW = tuple(zip(ALL_W,sNodes))

for window in nodesW:
    Handlers.append(Handler(window[0],window[1]))

for Handler in Handlers:
    wHandler(Handler)   
