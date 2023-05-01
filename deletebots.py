import time
import undetected_chromedriver as wb
from undetected_chromedriver import By

options = wb.ChromeOptions()
driver = wb.Chrome(use_subprocess=True, options=options)

user='USER'
password='PASS'

wikilang='en'

driver.get("https://"+wikilang+".touhouwiki.net/index.php?title=Special:Login")
nameField=driver.find_element(By.ID,"wpName1")
passwordField=driver.find_element(By.ID,"wpPassword1")
loginField=driver.find_element(By.ID,"wpLoginAttempt")

nameField.send_keys(user)
passwordField.send_keys(password)
loginField.click()

time.sleep(1)

def method1():
    finish = False
    while (finish != True):
        try:
            driver.get("https://"+wikilang+".touhouwiki.net/wiki/Special:ConfirmAccounts/authors")
            reviewButton = driver.find_element(By.CLASS_NAME,"mw-confirmaccount-type-0  a")
            reviewButton.click()
            form=driver.find_element(By.NAME,"accountconfirm")
            spam=driver.find_element(By.ID,"submitSpam")
            spam.click()
            form.submit()
        except OSError:
            finish = True
    
        time.sleep(1)
def method2():
    initialId = 10527
    finalId= 10531
    for i in range(initialId,finalId+1):
        driver.get("https://"+wikilang+".touhouwiki.net/index.php?title=Special:ConfirmAccounts/authors&acrid="+str(i))
    
        form=driver.find_element(By.NAME,"accountconfirm")
        spam=driver.find_element(By.ID,"submitSpam")
    
        spam.click()
        form.submit()
        time.sleep(1)

method = 1
match method:
    case 1:
        print("Using method 1")
        method1()
    case 2:
        print("Using method 2")
        method2()

time.sleep(20)