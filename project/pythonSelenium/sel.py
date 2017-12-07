import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyautogui


def main():

    chromeOptions = Options()
    chromeOptions.add_argument('--start-fullscreen')
    browser = webdriver.Chrome(chrome_options=chromeOptions)

    file = open('urls.txt', 'r')
    urls_list = file.read()
    urls = urls_list.split('\n')

    count = 0
    for url in urls:
        browser.get('http://' + url)
        time.sleep(2)
        im = pyautogui.screenshot('url_screenshot' + str(count) + '.png')
        count = count + 1
        count = takeScreenshot(browser, count)


    browser.quit()
    file.close()


def takeScreenshot(driver, count):
    href_link = driver.find_element_by_tag_name('a')
    new_link = href_link.get_attribute('href')
    #print(new_link, type(new_link))

    try:
        driver.get(new_link)
        time.sleep(2)
        im = pyautogui.screenshot('url_screenshot' + str(count) + '.png')
        count = count + 1
    except Exception as e:
        return count

    return count


main()