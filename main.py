import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

def doScrape():
    #Setup - get HTML data from dynamic website.
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    rowData = [] 
    for i, row in enumerate(soup.find_all('tr')):
        if i > 0:
            rowData.append([e.text.strip() for e in row.find_all('td')])
    rowData = [sublist for sublist in rowData if sublist]
    rowData = rowData[:5]

    # To extract data after clicking
    rowCount = 0
    btn = driver.find_element('link text', str(rowData[0][1]))
    res = []
    while(rowCount != 5):
        tempData = []
        tempAns = []
        btn.click()
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        tables = soup.find_all('table' , class_ = 'posting-table')
        for table in tables:
            innerData = table.find_all('td')
            for i in innerData:
                if(i.text.strip() != ""):
                    tempData.append(i.text.strip())
        tempAns.append(dataFinder(tempData, 'Closing Date:'))
        tempAns.append(dataFinder(tempData, 'Est. Value Notes:'))
        tempAns.append(dataFinder(tempData, 'Description:'))
        res.append(tempAns)

        # increment counter & click the 'next' button.
        rowCount += 1
        btn = driver.find_element("id",'id_prevnext_next')

    # Write to a CSV file
    csv_file_path = 'output.csv'
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Closing Date', 'Est. Value Notes', 'Description'])
        csv_writer.writerows(res)

# Function to find the value of required data (closing date, est. value notes, etc.)
def dataFinder(data, key):
    for i, item in enumerate(data):
        if item == key:
            if i + 1 < len(data):
                return data[i + 1]
            else:
                return None

doScrape()