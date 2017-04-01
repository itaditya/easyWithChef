from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Network():

    def __init__(self):
        self.baseUrl = "https://www.codechef.com"
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(710, 602)
        self.quesList = []

    def fetchQues(self,type):
        url = self.baseUrl + "/problems/" + type + "/?sort_by=Accuracy&sorting_order=desc"
        url = "http://localhost:8000/home.html"
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.CLASS_NAME, "problemrow"))
            )
            elements = self.driver.find_elements(
                By.CSS_SELECTOR, ".dataTable .problemrow:nth-child(-n+10)")
            for element in elements:
                ques = element.find_element(
                    By.CSS_SELECTOR, "td .problemname a")
                quesObj = {}
                quesObj["quesLink"] = self.baseUrl + ques.get_attribute("href")
                quesObj["quesName"] = ques.find_element(
                    By.CSS_SELECTOR, "b").text
                quesObj["quesCode"] = element.find_element(
                    By.CSS_SELECTOR, "td:nth-child(2) a").text
                print(quesObj["quesCode"])
                self.quesList.append(quesObj)
                    
        finally:
            self.driver.quit()
        print("==================")

def main():
    app = Menu()


if __name__ == '__main__':
    main()



