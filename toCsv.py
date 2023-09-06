from selenium import webdriver
from get_chrome_driver import GetChromeDriver
import csv
get_driver = GetChromeDriver()
get_driver.install()


def get_product_links(url):

    driver = webdriver.Chrome();
    driver.get(url);
    product_links = [];
    elements = driver.find_elements_by_css_selector("a.js-product-url");
    for element in elements:
        product_links.append(element.get_attribute("href"));

    driver.quit();

    return product_links;



def extract_comments(url):

    driver = webdriver.Chrome();
    driver.get(url);
    comments = [];
    elements = driver.find_elements_by_css_selector("div.c-comments__content");
    for element in elements:
        comment_text = element.find_element_by_css_selector("p").text;
        rate = element.find_element_by_css_selector("span.c-rating__value").text;
        comments.append([comment_text, rate]);

    driver.quit();

    return comments;


url = "https://www.digikala.com/search/category-mobile-phone/product-list/";
product_links = get_product_links(url);

allComments = [];
for url in product_links:
    allComments.append(extract_comments(url));

with open("comments.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file);
    writer.writerow(["Comment", "Rate"]);
    writer.writerows(allComments);