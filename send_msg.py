# 1. Import required libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random

# Download the ChromeDriver from https://googlechromelabs.github.io/chrome-for-testing/
# Check your Chrome version -> chrome://settings/help
# Put the ChromeDriver.exe in the same folder as this script (Done)
# Remember to explain how the .Keys works (https://www.selenium.dev/documentation/webdriver/actions_api/keyboard/)
# Also remember that you can always ctrl + l_click the Keys library to check the code


# 1. Create a list of WhatsApp contacts
contacts = ["Juler", "Micali"]

# 2. Create a list of random messages
# Add the contact value in the first message to make it more personal
messages_template = [
    "Hola {name}!",
    "Recuerda que el día de hoy tenemos sesión del Círculo de IA a las (no se tdv)",
    "Nos vemos!"
]

# 3. Open Google and WhatsApp Web
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://www.google.com/")
driver.implicitly_wait(5)
driver.get("https://web.whatsapp.com/")
time.sleep(100)  # Wait for QR code scanning and session to load

# 4. Define a function to send messages
def send_messages():
    for contact in contacts:
        # Find the search box and enter the contact name
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @data-tab="3" and @role="textbox" and @title="Cuadro de texto para ingresar la búsqueda"]')
        search_box.clear()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.ENTER)  # Simulate pressing Enter to open the chat
        time.sleep(2)  # Allow time for the chat to open

        # Send each message, format the first message to include the contact name
        for message in messages_template:
            formatted_message = message.format(name=contact) if '{name}' in message else message
            message_box = driver.switch_to.active_element  # Ensure focus is on the active message input
            message_box.send_keys(formatted_message)
            message_box.send_keys(Keys.ENTER)  # Simulate pressing Enter to send the message
            print(f"Message sent to {contact}: {formatted_message}")

# 5. Send messages
send_messages()

# Close the browser after sending messages
driver.quit()


# The code below is suposed to extract the WhatsApp content and save it in a txt file but Wpp is encrypted and
# it is not possible (for me) to extract the content. The code below is just a test and it is not working. xdd

# Print all the WhatsApp Content and Save it in a txt file called "whatsapp_content.txt"
#with open("whatsapp_content.txt", "w") as f:
#    f.write(driver.page_source)
#    print("WhatsApp Content Saved")
#time.sleep(160)
