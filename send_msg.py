from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# pip install selenium -U
# https://www.selenium.dev/documentation/webdriver/browsers/chrome/
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/browsers/test_chrome.py#L9-L10


driver = webdriver.Chrome(r'C:\Users\Ignacio\Desktop\Wpp_Messages\chromedriver\chromedriver-win64\chromedriver.exe')

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Please make sure you're logged into WhatsApp Web and your devices are linked.")
time.sleep(10)  # Wait for the user to scan the QR code if needed and WhatsApp to load.

contacts = ["Loco Juler", "Loco Javi Javi Olazabal"]  # List of contacts you want to message.

message = "A"

for contact in contacts:
    try:
        # Use the search box to find the contact
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Search input textbox"]'))
        )
        search_box.clear()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.RETURN)

        # Wait for the message box to be clickable, then send the message
        message_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@title="Type a message"]'))
        )
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        print(f"Message sent to {contact}")
    except Exception as e:
        print(f"Failed to send message to {contact}: {str(e)}")

    time.sleep(2)  # Brief pause between messages

# Close the driver after sending all messages
driver.quit()
