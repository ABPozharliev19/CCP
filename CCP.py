from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import tokens

driver = webdriver.Chrome(tokens.PATH)

emailForLogIn = tokens.email
passwordForLogIn = tokens.password


Name = "Георги Стоянов Димитров"
EGN = "0348011188"

placeOfBirth = "България"
cityOfBirth = "Бургас"

postCode = "8000"
country_live = "България"
city_live = "Бургас"
region_live = "Бургас"
neighborhood_live = "Славейков"
street_live = "Гладстон"

companyName = "Кон"
translatedCompanyName = "Kon"
sAddress = "Бургас"
seatAddressPostCode = "8000"
seatAddressHousingEstate = "Въздраждане"
seatAddressStreat = "Гладстон"




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
    
    #inputButton = driver.find_elements_by_xpath("//*[@type=radio] and [@value=type").click()
    
    time.sleep(2)
    
    
def registerCompanyPage2(companyName,translatedName,sAddress,sAPostCode,sAddressHE,sAddressStreat ):
    nameOfCompanyForm = driver.find_element_by_id("application_fields.company.text")
    nameOfCompanyForm.send_keys(companyName)
    
    translatedCompanyNameForm = driver.find_element_by_id("application_fields.transliteration.text")
    translatedCompanyNameForm.send_keys(translatedName)
    
    seatAddress = driver.find_element_by_id("application_fields.seat.address.settlement")
    seatAddress.send_keys(sAddress)
    
    time.sleep(5)

    #try:
     #   Form = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=dab15b44-7611-4fe3-9bfc-0f133af26ff6]/div[1]/div[2]/div[1]/div")))

    
    #//*[@id="dab15b44-7611-4fe3-9bfc-0f133af26ff6"]/div[1]/div[2]/div[1]/div

    seatPostCodeForm = driver.find_element_by_id("application_fields.seat.address.postCode")
    seatPostCodeForm.send_keys(sAPostCode)

    seatAddressHousingEstateForm = driver.find_element_by_id("application_fields.seat.address.housingEstate")
    seatAddressHousingEstateForm.send_keys(sAddressHE)

    seatAddressStreatForm =  driver.find_element_by_id("application_fields.seat.address.street")
    seatAddressStreatForm.send_keys(seatAddressStreat)

    #application_fields.seat.contacts.phone



    

logIn(emailForLogIn,passwordForLogIn)

registerCompanyPage1(Name,EGN,placeOfBirth,cityOfBirth,country_live,city_live,region_live,neighborhood_live,street_live,postCode)

buttonForNextPageForm = driver.find_element_by_xpath("//button[text()='Продължи']").click()

time.sleep(5)

registerCompanyPage2(companyName, translatedCompanyName, sAddress,seatAddressPostCode,seatAddressHousingEstate,seatAddressStreat)


    




