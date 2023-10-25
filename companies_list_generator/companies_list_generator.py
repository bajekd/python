from bs4 import BeautifulSoup
import requests
import pprint

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def company_spliter(company):
    company = (
        company.split("Sp.")[0]
        .split("SP ")[0]
        .split("SP. ")[0]
        .split("sp. ")[0]
        .split("Sp z")[0]
        .split("Sp. z")[0]
        .split("S.A")[0]
        .strip()
    )
    return company


def get_jobs_from_bulldogjob():
    companies_list = set()

    full_url = "https://bulldogjob.pl/companies/jobs/s/remote,true/skills,Python"
    bulldog_job = requests.get(full_url).text

    soup = BeautifulSoup(bulldog_job, "lxml")
    for ad in soup.find_all("a", class_="search-list-item"):
        company = ad.find("div", class_="company").text
        company = company_spliter(company)
        companies_list.add(company)

    return companies_list


def get_jobs_from_nofluffjobs():
    full_url = "https://nofluffjobs.com/pl/praca-it/praca-zdalna/python?page=1"
    options = webdriver.ChromeOptions()
    options.add_argument(" - incognito")

    browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
    browser.get(full_url)
    timeout = 30

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@class='page-item ng-star-inserted']"))
        )
    except TimeoutException:
        print(f"{timeout} sec has passed -> Timeout!")
        browser.quit()

    companies_list = set()
    last_page_str = browser.find_elements(By.XPATH, "//a[@class='page-link']")[-2].text  # penultimate elem in list
    last_page = int(last_page_str)

    companies = browser.find_elements(By.CSS_SELECTOR, "span.ml-1.posting-title__company")
    for company in companies:
        # <NAZWA STANOWSKA>< W NAZWA_FIRMY> - usunięcie " w " <NAZWA FIRMY>
        company = company.text[2:].strip()
        # usunięcie dopisku SP. <cośtam cośtam> oraz zbędnych spacji
        company = company_spliter(company)
        companies_list.add(company)

    for i in range(2, (last_page + 1)):
        try:
            browser.get(f"https://nofluffjobs.com/pl/praca-it/praca-zdalna/python?page={i}")
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//li[@class='page-item ng-star-inserted']"))
            )
        except TimeoutException:
            print(f"{timeout} sec has passed -> Timeout!")
            browser.quit()

        for company in browser.find_elements(By.CSS_SELECTOR, "span.ml-1.posting-title__company"):
            company = company.text[2:].strip()
            company = company_spliter(company)
            companies_list.add(company)

    return companies_list


def add_to_already_seen_and_print_results(companies_list):
    already_seen = set()
    with open("already_seen.txt") as file:
        companies = file.readlines()
        for company in companies:
            company = company.replace("\n", "")
            company = company.split("-->")[1].strip()
            already_seen.add(company)

    companies_great_list = companies_list - already_seen

    with open("already_seen.txt", "a") as f:
        # i.e in companies are 133 elements, new element to file should start from 134
        i = len(companies) + 1
        for company in companies_great_list:
            f.write(f"{i} --> {company}\n")
            i += 1

    pprint.pprint(companies_great_list)

companies_list = get_jobs_from_nofluffjobs() | get_jobs_from_bulldogjob()
add_to_already_seen_and_print_results(companies_list)
