from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = "chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)


def login_to_github(username, password, url):
    driver.get(url)

    driver.find_element(By.NAME, "login").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()

    print("successfully login")


def search_target(targetUsername):
    driver.get(f"https://github.com/{targetUsername}")

    repositories_tab = driver.find_element(By.ID, "repositories-tab")
    repo_count = repositories_tab.find_element(By.CLASS_NAME, "Counter").text

    print(f"{targetUsername}'s repo count is {repo_count}")
    print("COMMAND LINE ENDS HERE")


# FILL THE USERNAME AND PASSWORD
url = "https://github.com/login"


login_to_github(username, password, url)
search_target("developerAromal")
