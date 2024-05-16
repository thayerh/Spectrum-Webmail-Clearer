from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


from time import sleep

URL = "https://webmail.spectrum.net/mail"

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

driver = webdriver.Chrome()
driver.get(URL)

# Wait until user indicates that they've signed in
page = int(input("Type the largest page number you see at the bottom and press Enter: "))


xs = driver.find_elements(By.LINK_TEXT, str(page))
print(xs)
x = xs[0]
x.click()

input("Press Enter after the page is loaded")

fail = 0

while True:
    try:
        x = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/table/thead/tr/th[2]/div/input")
        x.click()
    except:
        print("Failed")
        fail += 1
        if fail > 5:
            break
        sleep(5)
        continue

    sleep(.5)
    # input("Press Enter after you've selected the checkbox")

    x = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/ul/li[13]")
    x.click()

    sleep(.5)
    # input("Press Enter after you've selected the delete button")

    x = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/button[2]")
    x.click()

    # page -= 1;
    # Wait until the new page number a element is visible
    # WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.LINK_TEXT, str(page-5))))
    # print("Found " + str(page-5))
    sleep(150)
    # input("Press Enter after you've confirmed the deletion")


print("success")
driver.close()