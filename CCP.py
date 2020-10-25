from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH=r"C:\Users\nnask\AppData\Local\Programs\Python\Python38\Stuff\chromedriver.exe"
driver=webdriver.Chrome(PATH)

emailforLogIn="informationtechtest123@gmail.com"
passwordForLogIn="passwordxd123"

Name="Георги Стоянов Димитров"
EGN="0348011188"

placeOfBirth="България"
cityOfBirth="Бургас"

postCode="8000"
country_live="България"
city_live="Бургас"
region_live="Бургас"
neighborhood_live="Славейков"
street_live="Гладстон"

companyName = "Кон"
translatedCompanyName = "Kon"
sAdress = "Бургас"




def logIn(email,password):
    driver.get("https://login.registryagency.bg/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_mode%3Dform_post%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fportal.registryagency.bg%252Flogin%26client_id%3Depzeu.ui.client%26nonce%3Db8e326aa4724a3019dedce167e854726%26state%3D671b6e62ceb9f322da7d3fc31ccf58e4%26scope%3Dopenid%2520profile%2520epzeu.api%2520offline_access")
    
    emailLog = driver.find_element_by_id("Username")
    passwordLog = driver.find_element_by_id("Password")
    
    emailLog.send_keys(email)
    passwordLog.send_keys(password)
    passwordLog.send_keys(Keys.ENTER)

def registerCompanyPage1(Name,EGN,birthPlace,cityOfBirth,countryOfLife,cityOfLife,regionOfLife,nbHoodOfLife,streetOfLife,postCode):
    driver.get("https://portal.registryagency.bg/CR/applications/ApplicationProcesses/A4")
    time.sleep(5)
    
    nameForm = driver.find_element_by_id("application_applicants.applicantsList.[0].person.name")
    nameForm.send_keys(Name)
    
    EGNForm=driver.find_element_by_id("application_applicants.applicantsList.[0].person.indent")
    EGNForm.send_keys(EGN)
    
    birthPlaceForm = driver.find_element_by_id("application_applicants.applicantsList.[0].birthPlace.country")
    birthPlaceForm.send_keys(birthPlace)
    
    cityOfBirthForm = driver.find_element_by_id("application_applicants.applicantsList.[0].birthPlace.place")
    cityOfBirthForm.send_keys(cityOfBirth)
    
    countryOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.country")
    countryOfLifeForm.send_keys(countryOfLife)

    try:
     Form= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "application_applicants.applicantsList.[0].address.postCode")))
     
    except:
        driver.quit()
        print("We couldn't find that country!/nTry again")
        
    cityOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.settlement")
    cityOfLifeForm.send_keys(cityOfLife)
    
    try:
            Form=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,"form-text")))

    except:
        driver.quit()
        print("We couldn't find that country ")
        
    postCodeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.postCode")
    postCodeForm.send_keys(postCode)
    
    nbHoodOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.housingEstate")
    nbHoodOfLifeForm.send_keys(nbHoodOfLife)
    
    streetOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.street")
    streetOfLifeForm.send_keys(streetOfLife)
    
    '''inputButton = driver.find_elements_by_xpath("//*[@type=radio] and [@value=type").click()'''
    
    time.sleep(2)
    
    
def registerCompanyPage2(companyName,translatedName,sAdress):
    nameOfCompanyForm = driver.find_element_by_id("application_fields.company.text")
    nameOfCompanyForm.send_keys(companyName)
    
    translatedCompanyNameForm = driver.find_element_by_id("application_fields.transliteration.text")
    translatedCompanyNameForm.send_keys(translatedName)
    
    seatAdress = driver.find_element_by_id("application_fields.seat.address.settlement")
    seatAdress.send_keys(sAdress)
    
    
    
    

logIn(emailforLogIn,passwordForLogIn)

registerCompanyPage1(Name,EGN,placeOfBirth,cityOfBirth,country_live,city_live,region_live,neighborhood_live,street_live,postCode)

buttonForNextPageForm=driver.find_element_by_xpath("//button[text()='Продължи']").click()

registerCompanyPage2(companyName,translatedCompanyName,sAdress)


    




