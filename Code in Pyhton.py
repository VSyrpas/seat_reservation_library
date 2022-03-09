I can not reveale the university.


# Step 1 :


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())



# I select the seat that I like most in the Library 

url="the link of the library"
driver.get(url)


# Step 2 : I write my userame and my passowrd 


search_input_box = driver.find_element_by_name("username")
search_input_box.send_keys("u******")
search_input_box = driver.find_element_by_name("password")
search_input_box.send_keys("*********")
driver.find_element_by_css_selector('button').click()


# Step 3 : I book 7 days in advance


i=1
for i in range(1,8):
    driver.find_element_by_css_selector('.fc-next-button.btn.btn-default.btn-sm').click()
    i=i+1


# Step 4 :scroll down the page


driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


# Step 5 : I book 4 time slots, from 8am to 4pm


i=1
import time
for i in range(1,5):
    driver.find_element_by_css_selector('.fc-timeline-event.fc-h-event.fc-event.fc-event-start.fc-event-end.fc-event-future.s-lc-eq-avail').click()
    i=i+1
    time.sleep(0.5)


# Step 6 : I delete the first 3 time slots


for i in range(1,4):
    driver.find_element_by_css_selector('.fa.fa-trash-o').click()
    i=i+1
    time.sleep(0.5)


# Step 7


from selenium.webdriver.support.ui import Select
time.sleep(1)



ddelement= Select(driver.find_element_by_css_selector('.form-control.input-sm.b-end-date'))


# Step 8: I book from 4 am to 10:30 pm


ddelement.select_by_index(30);
time.sleep(0.5)


# Step 9 :I press the button for booking

driver.find_element_by_css_selector('.btn.btn-primary').click()


# Step 10 : Scroll down


time.sleep(0.5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


# Step 11 : I write my student number


search_input_box = driver.find_element_by_name("q1045")
search_input_box.send_keys("*****")


# Step 12 : I book the seat


search_input_box = driver.find_element_by_name("q1041[]").click()
driver.find_element_by_css_selector('.btn.btn-primary').click()

