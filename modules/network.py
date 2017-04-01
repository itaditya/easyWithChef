from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Network():

    def __init__(self):
        self.baseUrl = "https://www.codechef.com"
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(710, 602)
        self.quesList = []

    def fetchQuesList(self,type):
        url = self.baseUrl + "/problems/" + type + "/?sort_by=Accuracy&sorting_order=desc"
        # url = "http://localhost:8000/home.html"
        self.driver.get(url)       
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "problemrow"))
        )
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".dataTable .problemrow:nth-child(-n+10)")
        # elements = self.driver.find_elements(
        #     By.CSS_SELECTOR, ".dataTable .problemrow")
        for element in elements:
            ques = element.find_element(
                By.CSS_SELECTOR, "td .problemname a")
            quesObj = {}
            quesObj["quesLink"] = ques.get_attribute("href")
            quesObj["quesName"] = ques.find_element(
                By.CSS_SELECTOR, "b").text
            quesObj["quesCode"] = element.find_element(
                By.CSS_SELECTOR, "td:nth-child(2) a").text
            self.quesList.append(quesObj)
                    
        print("==================")

    def fetchQues(self,quesLink):
        self.driver.get(quesLink)    
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".problem-statement"))
        )
        # element = self.driver.find_element(
        # By.CSS_SELECTOR, ".problem-statement")    
        # print(element.text)
        # return(element.text.encode('utf-8').strip())
        return ""

    def switchTab(self,switchTo):
        window_after = self.driver.window_handles[switchTo]
        self.driver.switch_to_window(window_after)

    def newTab(self):
        self.driver.execute_script("window.open()")

    def runAns(self,quesCode,ansText):
        self.newTab()
        self.switchTab(1)
        self.driver.get(self.baseUrl + "/ide")
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )
        print("ns-heading")
        return ""


def main():
    app = Network()
    app.runAns("abc","efg")

if __name__ == '__main__':
    main()



