from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://chykalophia.com/")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.maximize_window()

#1.Verify footer (each social media icon is working and redirects to the correct page)

#LinkedIn
driver.find_element(By.XPATH, "//a/i").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "LinkedIn")
LinkedIn_url = driver.current_url
print(LinkedIn_url)
if LinkedIn_url == "https://chykalophia.com/":
    print("LinkedIn URL is OK")
else:
     print("Wrong URL")

#Facebook
driver.find_element(By.XPATH, "//span[2]/a/i").click()
driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.facebook.com/')]")

facebook_url = driver.current_url
print(facebook_url)

if facebook_url == "https://chykalophia.com/":
    print("facebook URL is OK")
else:
    print("Wrong URL")

#Twitter
driver.find_element(By.XPATH, "//span[3]/a/i").click()
driver.find_element(By.XPATH, "//a[contains(@href, /Chykalophia)]")
Twitter_url = driver.current_url
print(Twitter_url)

if Twitter_url == "https://chykalophia.com/":
    print("Twitter URL is OK")
else:
    print("Wrong URL")

#Instagram
# driver.find_element(By.XPATH, "//span[4]/a/i").click()
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.instagram.com/chykalophia/')]")
# Instagram_url = driver.current_url
# print(Instagram_url)
#
# if Instagram_url == "https://chykalophia.com/":
#     print("Instagram URL is OK")
# else:
#     print("Wrong URL")

#YouTube
driver.find_element(By.XPATH, "//span[5]/a/i").click()
driver.find_element(By.XPATH, "//a[contains(@href, /Chykalophia)]")
Youtube_Meta_url = driver.current_url
print(Youtube_Meta_url)

if Youtube_Meta_url == "https://chykalophia.com/":
    print("Youtube_Meta URL is OK")
else:
    print("Wrong URL")
#GitHub
driver.find_element(By.XPATH, "//span[6]/a/i").click()
driver.find_element(By.XPATH, "//a[contains(@href, /Chykalophia)]")
GitHub_url = driver.current_url
print(GitHub_url)

if GitHub_url == "https://chykalophia.com/":
    print("GitHub URL is OK")
else:
    print("Wrong URL")

#Behance
driver.find_element(By.XPATH, "//span[7]/a/i").click()
driver.find_element(By.XPATH, "//a[contains(@href, /Chykalophia)]")
Behance_url = driver.current_url
print(Behance_url)

if Behance_url == "https://chykalophia.com/":
    print("Behance URL is OK")
else:
    print("Wrong URL")
#driver.close()

#2.Verify footer (Privacy Policy/Cookie Policy)
driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Policy')]").click()
driver.find_element(By.XPATH, "//h1[contains(.,'Privacy Policy of Chykalophia Group, LLC')]").get_attribute("title")
assert "Privacy Policy of Chykalophia Group, LLC" in driver.title
print(driver.title)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
driver.get("https://chykalophia.com/")

driver.find_element(By.XPATH, "//a[contains(text(),'Cookie Policy')]").click()
driver.find_element(By.XPATH, "//h2[contains(.,'Cookie Policy of Chykalophia Group, LLC')]").get_attribute("title")
assert "Cookie Policy of Chykalophia Group, LLC" in driver.title
print(driver.title)

