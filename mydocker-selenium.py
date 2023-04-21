from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import datetime
import glob
import os
import time


def refresh():
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Firefox(options=options)

    driver.get("https://mydocker.centralesupelec.fr/shell")

    # click on the login button
    driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/div/div/button/span[1]").click()

    # find username and password fields
    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')

    # enter username and password
    username.send_keys("ilyes.hamdi@student-cs.fr")
    password.send_keys("halawalaIMO99@")

    # click on the login button
    driver.find_element(By.XPATH, "/html/body/div[3]/main/div/div/section/div/div[2]/form/div/button").click()

    # click on the header GPU
    driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div/app-course-list/mat-tab-group/div/mat-tab-body[2]/div/mat-accordion/div[3]/mat-expansion-panel/div/div/app-course-detail/app-shell-access/div[2]/div/button').click()

    # click on the refresh button
    driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div/app-course-list/mat-tab-group/div/mat-tab-body[2]/div/mat-accordion/div[3]/mat-expansion-panel/div/div/app-course-detail/app-shell-access/div[2]/div/button/span[1]').click()

if __name__ == "__main__":
    refresh()