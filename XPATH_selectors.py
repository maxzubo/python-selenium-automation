from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


service = Service("C:\\Users\1tnya\python-selenium-automation\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# 1
driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')
expected_result1 = 'Sign in'
actual_result1 = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text
assert expected_result1 == actual_result1, f'Error! Expected {expected_result1}, but got {actual_result1}' 
# 2
driver.find_element(By.XPATH, '//*[@class="a-form-label"]')
expected_result2 = 'Email or mobile phone number'
actual_result2 = driver.find_element(By.XPATH, '//*[@class="a-form-label"]').text
assert expected_result2 == actual_result2, f'Error! Expected {expected_result2}, but got {actual_result2}'
# 3
driver.find_element(By.XPATH, '//*[@type="email"] ')
expected_result3 = driver.find_element(By.XPATH, '//*[@type="email"] ')
actual_result3 = driver.find_element(By.XPATH, '//*[@type="email"] ')
assert expected_result3 == actual_result3, f'Error! Expected {expected_result3}, but got {actual_result3}'
# 4
driver.find_element(By.XPATH, '//*[@id="continue"]')
expected_result4 = 'Continue'
actual_result4 = driver.find_element(By.XPATH, '//*[@id="continue"]').text
assert expected_result4 == actual_result4, f'Error! Expected {expected_result4}, but got {actual_result4}'
# 5
driver.find_element(By.XPATH, '//*[text()="Conditions of Use"]')
expected_result5 = 'Conditions of Use'
actual_result5 = driver.find_element(By.XPATH, '//*[text()="Conditions of Use"]').text
assert expected_result5 == actual_result5, f'Error! Expected {expected_result5}, but got {actual_result5}'
# 6
driver.find_element(By.XPATH, '//*[text()="Privacy Notice"]')
expected_result6 = 'Privacy Notice'
actual_result6 = driver.find_element(By.XPATH, '//*[text()="Privacy Notice"]').text
assert expected_result6 == actual_result6, f'Error! Expected {expected_result6}, but got {actual_result6}'
# 7
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]')
expected_result7 = 'Need help?'
actual_result7 = driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]').text
assert expected_result7 == actual_result7, f'Error! Expected {expected_result7}, but got {actual_result7}'
# 8
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]').click()
driver.find_element(By.XPATH, '//a[@id="auth-fpp-link-bottom"]')
expected_result8 = 'Forgot your password?'
actual_result8 = driver.find_element(By.XPATH, '//a[@id="auth-fpp-link-bottom"]').text
assert expected_result8 == actual_result8, f'Error! Expected {expected_result8}, but got {actual_result8}'
# 9
driver.find_element(By.XPATH, '//a[@id="ap-other-signin-issues-link"]')
expected_result9 = 'Other issues with Sign-In'
actual_result9 = driver.find_element(By.XPATH, '//a[@id="ap-other-signin-issues-link"]').text
assert expected_result9 == actual_result9, f'Error! Expected {expected_result9}, but got {actual_result9}'
print ('test case passed')
driver.quit()