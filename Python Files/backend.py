# All the imports we need
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import tokens

driver = webdriver.Chrome(tokens.PATH)  # Setting up the webdriver

# Getting the login info
emailForLogIn = tokens.email
passwordForLogIn = tokens.password

# Test variables for debugging
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

number_street = 1
block_address = 2
entrance_address = 3
floor_address = 4
apartment_address = 5

companyName = "Кон"
translatedCompanyName = "Kon"
sAddress = "Бургас"
seatAddressPostCode = "8000"
seatAddressHousingEstate = "Въздраждане"
seatAddressStreet = "Гладстон"

contact_phone = "0894448698"
eMail = "informationtechtest123@gmail.com"
page = "codingburgas.bg"

correspondenceAddress = "Бургас"
correspondencePostCode = "8000"
correspondenceHousingEstate = "Славейков"
correspondenceAddressStreet = "Гладстон"
correspondence_number_street = 1
correspondence_block_address = 2
correspondence_entrance_address = 3
correspondence_floor_address = 4
correspondence_apartment_address = 5




def logIn(email, password):  # First function to Log in
    driver.get(
        "https://login.registryagency.bg/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_mode"
        "%3Dform_post%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fportal.registryagency.bg%252Flogin"
        "%26client_id%3Depzeu.ui.client%26nonce%3Db8e326aa4724a3019dedce167e854726%26state"
        "%3D671b6e62ceb9f322da7d3fc31ccf58e4%26scope%3Dopenid%2520profile%2520epzeu.api%2520offline_access")

    emailLog = driver.find_element_by_id("Username")  # Search for the Username input
    passwordLog = driver.find_element_by_id("Password")  # Search for the Password input

    # Send the login information
    emailLog.send_keys(email)
    passwordLog.send_keys(password)
    # Press enter for the login to be done
    passwordLog.send_keys(Keys.ENTER)

    # Function to fill all the information in the first page


def registerCompanyPage1(Name, EGN, birthPlace, cityOfBirth, countryOfLife, cityOfLife, nbHoodOfLife,streetOfLife, postCode, numberOfStreet, addressBlock, addressEntrance, addressFloor, addressApartment   ):

    driver.get("https://portal.registryagency.bg/CR/applications/ApplicationProcesses/A4")  # Go to the web page
    time.sleep(5)  # Wait for the page to load

    cookieButton = driver.find_element_by_xpath("/html/body/aside/div/div/div[2]/button")
    cookieButton.click()

    driver.maximize_window()

    driver.execute_script("window.scrollTo(0, 500)")

    # Search for the
    nameForm = driver.find_element_by_id("application_applicants.applicantsList.[0].person.name")
    nameForm.clear()
    nameForm.send_keys(Name)

    EGNForm = driver.find_element_by_id("application_applicants.applicantsList.[0].person.indent")
    EGNForm.clear()
    EGNForm.send_keys(EGN)

    birthPlaceForm = driver.find_element_by_id("application_applicants.applicantsList.[0].birthPlace.country")
    birthPlaceForm.clear()
    birthPlaceForm.send_keys(birthPlace)

    cityOfBirthForm = driver.find_element_by_id("application_applicants.applicantsList.[0].birthPlace.place")
    cityOfBirthForm.clear()
    cityOfBirthForm.send_keys(cityOfBirth)

    countryOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.country")
    countryOfLifeForm.click()
    countryOfLifeForm.clear()
    countryOfLifeForm.send_keys(countryOfLife)
    countryOfLifeForm.click()

    Form = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[4]/div[2]/div/span/ul/li")))
    Form.click()

    cityOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.settlement")
    cityOfLifeForm.click()
    cityOfLifeForm.send_keys(cityOfLife)

    FormTemp = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[4]/div[3]/div[1]/span/ul/li")))
    FormTemp.click()

    postCodeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.postCode")
    postCodeForm.clear()
    postCodeForm.send_keys(postCode)

    nbHoodOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.housingEstate")
    nbHoodOfLifeForm.clear()
    nbHoodOfLifeForm.send_keys(nbHoodOfLife)

    streetOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.street")
    streetOfLifeForm.clear()
    streetOfLifeForm.send_keys(streetOfLife)

    numberAddressForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.streetNumber")
    numberAddressForm.clear()
    numberAddressForm.send_keys(numberOfStreet)

    addressBlockForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.block")
    addressBlockForm.clear()
    addressBlockForm.send_keys(addressBlock)

    addressEntranceForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.entrance")
    addressEntranceForm.clear()
    addressEntranceForm.send_keys(addressEntrance)

    addressFloorForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.floor")
    addressFloorForm.clear()
    addressFloorForm.send_keys(addressFloor)

    addressApartmentForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.apartment")
    addressApartmentForm.clear()
    addressApartmentForm.send_keys(addressApartment)

    driver.execute_script("window.scrollTo(0, 1000)")

    inputButton = driver.find_element_by_xpath("//html/body/div[1]/div[2]/div[2]/div[3]/div/div[3]/div[2]/div/div[1]/label")
    inputButton.click()


def registerCompanyPage2(companyName, translatedName, sAddress, sAPostCode, sAddressHE, sAddressStreat, contactPhone,email, webPage):
    nameOfCompanyForm = driver.find_element_by_id("application_fields.company.text")
    nameOfCompanyForm.clear()
    nameOfCompanyForm.send_keys(companyName)

    translatedCompanyNameForm = driver.find_element_by_id("application_fields.transliteration.text")
    translatedCompanyNameForm.clear()
    translatedCompanyNameForm.send_keys(translatedName)

    seatAddressForm = driver.find_element_by_id("application_fields.seat.address.settlement")
    seatAddressForm.click()
    seatAddressForm.clear()
    seatAddressForm.send_keys(sAddress)
    seatAddressForm.click()

    Form = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div[4]/div[2]/div[1]/div[2]/div[1]/span/ul/li")))
    Form.click()

    seatPostCodeForm = driver.find_element_by_id("application_fields.seat.address.postCode")
    seatPostCodeForm.clear()
    seatPostCodeForm.send_keys(sAPostCode)

    seatAddressHousingEstateForm = driver.find_element_by_id("application_fields.seat.address.housingEstate")
    seatAddressHousingEstateForm.clear()
    seatAddressHousingEstateForm.send_keys(sAddressHE)

    seatAddressStreatForm = driver.find_element_by_id("application_fields.seat.address.street")
    seatAddressStreatForm.clear()
    seatAddressStreatForm.send_keys(sAddressStreat)

    contactPhoneForm = driver.find_element_by_id("application_fields.seat.contacts.phone")
    contactPhoneForm.clear()
    contactPhoneForm.send_keys(contactPhone)

    emailForCompanyForm = driver.find_element_by_id("application_fields.seat.contacts.eMail")
    emailForCompanyForm.clear()
    emailForCompanyForm.send_keys(email)

    webPageForm = driver.find_element_by_id("application_fields.seat.contacts.url")
    webPageForm.clear()
    webPageForm.send_keys(webPage)



def registerCompanyPage3(correspondence_address, correspondence_post_code, correspondence_housing_estate, correspondence_address_street, correspondence_number_Street, correspondence_block_Address, correspondence_entrance_Address, correspondence_floor_Address, correspondence_apartment_Address):





# TODO Do the rest of the Automation
logIn(emailForLogIn, passwordForLogIn)

registerCompanyPage1(Name, EGN, placeOfBirth, cityOfBirth, country_live, city_live, neighborhood_live, street_live, postCode, number_street, block_address, entrance_address, floor_address, apartment_address)

buttonForNextPageForm = driver.find_element_by_xpath("//button[text()='Продължи']").click()

time.sleep(5)

registerCompanyPage2(companyName, translatedCompanyName, sAddress, seatAddressPostCode, seatAddressHousingEstate, seatAddressStreet, contact_phone, eMail, page)

registerCompanyPage3(correspondenceAddress, correspondencePostCode, correspondenceHousingEstate, correspondenceAddressStreet, correspondence_number_street, correspondence_block_address, correspondence_entrance_address, correspondence_floor_address, correspondence_apartment_address)

