from selenium import webdriver;
# from get_chrome_driver import GetChromeDriver;
import csv;
# get_driver = GetChromeDriver();
# get_driver.install();
from selenium.webdriver.common.by import By;
from selenium.webdriver.chrome.service import Service;
service = Service(executable_path='./chromedriver114');
import time;

def get_product_links(url):

    driver = webdriver.Chrome(service=service);
    driver.get(url);
    time.sleep(10);
    product_links = [];
    for i in range(0,0):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)");
        time.sleep(5);

    elements = driver.find_elements(By.CLASS_NAME, "product-list_ProductList__item__LiiNI");

    for element in elements:
        link = (element.find_element(By.TAG_NAME, 'a').get_attribute("href"));
        print(link+'\n');
        product_links.append(link);

    driver.quit();

    return product_links;



def extract_comments(url):

    driver = webdriver.Chrome(service=service);
    driver.get(url);
    time.sleep(5);
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)");
    time.sleep(2);
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)");
    # time.sleep(2);
    button= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[10]/div[1]/div[1]/div/section/div[2]/div[1]/div");
    driver.execute_script("arguments[0].click();", button);
    time.sleep(3);
    
    elements = driver.find_element(By.ID, "modal-root").find_element(By.CLASS_NAME, "fixed").find_element(By.CLASS_NAME, "bg-000").find_element(By.CLASS_NAME, "grow-1").find_element(By.CLASS_NAME, "h-100").find_element(By.CLASS_NAME, "grow-1").find_element(By.CLASS_NAME, "d-flex").find_element(By.ID, "14").find_element(By.CLASS_NAME, "d-flex").find_elements(By.CLASS_NAME, "border-b-200")

    comments = [];
    for element in elements:
        rate = element.find_element(By.CLASS_NAME, "mb-1").find_element(By.CLASS_NAME, "py-3").find_element(By.CLASS_NAME, "ml-2").find_element(By.CLASS_NAME, "p-1").text
        comment_text = element.find_element(By.CLASS_NAME, "mb-1").find_element(By.CLASS_NAME, "py-3").find_element(By.CLASS_NAME, "w-full").find_element(By.CLASS_NAME, "w-full").find_element(By.CLASS_NAME, "d-flex").find_element(By.CLASS_NAME, "grow-1").find_element(By.CLASS_NAME, "text-body-1").text
        comments.append([comment_text, rate]);
        print(comment_text,rate)

    driver.quit();

    return comments;


url = "https://www.digikala.com/search/category-book/";
product_links = get_product_links(url);

allComments = [];
for product_link in product_links:
    product_comments= extract_comments(product_link);
    # print(product_comments)
    allComments.append(product_comments);
# with open("comments.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file);
#     writer.writerow(["Comment", "Rate"]);
#     writer.writerows(allComments);