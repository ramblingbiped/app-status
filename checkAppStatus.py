import smtplib
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

    #Check the status of services, if not "green" send notification email.
    if service_status != 'aad-green-circle':

        content = 'There is currently a problem with %s!\n\nCheck http://www.google.com/appsstatus for further information directly relevant to the outage.\n' % service_name
        subject = '%s Service Interruption' % service_name
        message = 'Subject: %s\n\n%s' % (subject, content)

        #Credentials of the account authenticating with Google's SMTP server
        email = 'app-user@gmail.com'
        password = 'app-password'

        #Person to be notified of service outage/downtime
        sender_address = 'apps.status@gmail.com'
        recipient_address = 'example.user@domain.com'

        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(sender_address, recipient_address, message)
        mail.close()

driver.close()