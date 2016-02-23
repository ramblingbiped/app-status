from selenium import webdriver
import time

driver = webdriver.PhantomJS()

driver.get("http://www.google.com/appsstatus#hl=en&v=status")
time.sleep(1)

app_services = {
    'Gmail' : 2,
    'Calendar' : 3,
    'Messenger' : 4,
    'Drive' : 5,
    'Docs' : 6,
    'Sheets' : 7,
    'Slides' : 8,
    'Drawings' : 9,
    'Sites' : 10,
    'Groups' : 11,
    'Admin console' : 12,
    'Postini' : 13,
    'Hangouts' : 14,
    'Vault' : 15
}

for key, value in app_services.items():

    service_name = driver.find_element_by_xpath('//table/tbody/tr[%d]/td[2]' % value).text
    service_status = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr[%d]/td[1]/span' % value).get_attribute('class')

    if service_status != 'aad-green-circle':
        #Replace print statements with email and/or sms based notifications, Add in global variables to define recipient(s) and sender address.
        notice = 'There is currently a problem with %s!\nCheck http://www.google.com/appsstatus for further information.\n' % service_name

        print(notice)

driver.close()