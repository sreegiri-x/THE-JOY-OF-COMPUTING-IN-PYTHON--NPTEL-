

# The Joy of Computing using Python - Unit 14 - Week 11

## Automating Message Dispatch on WhatsApp Web Using Selenium

### Background
Web automation tools are often used to reduce repetitive manual tasks. One common example is interacting with web-based messaging platforms to send reminders, notifications, or test message workflows. WhatsApp Web, being a browser-based interface, can be automated using Selenium to simulate real user actions such as clicking, typing, and pressing keys.

This case study examines a Python-based Selenium script that automates sending multiple messages to a specific contact on WhatsApp Web.

### Objective
The goal of the script is to:
* Open WhatsApp Web in a browser
* Allow the user to authenticate manually via QR code
* Search for a specific contact by name
* Open the chat window of that contact
* Send the same message multiple times at fixed intervals
* Close the browser session after completion

### Tools and Technologies Used
* Selenium WebDriver
* Google Chrome Browser
* ChromeDriver
* WhatsApp Web

---

## Workflow Explanation

1.  **Browser Initialization**
    The script begins by initializing the Chrome WebDriver. This enables Python to control the Chrome browser programmatically.
    * **Key idea:** The WebDriver acts as a bridge between Python commands and browser actions.

2.  **Loading WhatsApp Web**
    The browser navigates to the WhatsApp Web URL. Since WhatsApp requires authentication, the script pauses implicitly while the user scans the QR code using their mobile WhatsApp application.
    * **Important observation:** Automation does not bypass authentication. Human intervention is required at this step.

3.  **Identifying the Target Chat**
    The script defines:
    * A contact name
    * A message string
    It then constructs an XPath expression that locates a chat whose title attribute contains the contact's name. `WebDriverWait` is used to ensure the element is loaded before interaction.
    * **Concepts involved:** XPath-based element selection and Explicit waits to handle dynamic content.

4.  **Opening the Chat**
    Once the contact element is located, a click action opens the chat window. This simulates a real user selecting a chat from the chat list.

5.  **Locating the Message Input Box**
    The script finds the message input field using its class name. This element is where text messages are typed. This step relies on understanding the DOM structure of WhatsApp Web.

6.  **Sending Messages in a Loop**
    A loop sends the same message multiple times:
    * The message text is typed
    * The Enter key is pressed to send
    * A delay is added between messages
    * **Why the delay matters:** Prevents rapid-fire actions, reduces the risk of detection or UI failure, and mimics human behavior.

7.  **Closing the Session**
    After sending all messages, the browser is closed gracefully using the quit method. This ensures system resources are released properly.

---

## Python Code Snippet

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("path_to_chromedriver.exe")
driver.get("https://web.whatsapp.com/")

recipient_name = "Ravi Kiran"
message_text = "Message sent using Python"

# Wait for the contact to appear and click
xpath = "//span[contains(@title, '" + recipient_name + "')]"
target = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath)))
target.click()

# Locate the input box
input_box = driver.find_element(By.CLASS_NAME, "_1Pipp")

# Send messages in a loop
for i in range(50):
    input_box.send_keys(message_text)
    input_box.send_keys(Keys.RETURN)
    time.sleep(1)

driver.quit()
```

---

## Quiz: Week 11 Assignment 11

**1) Why is WebDriverWait preferred over using a fixed time.sleep() before locating the chat element?**
* It waits only until the required element becomes available, making the script more reliable
* It reduces CPU usage of the Python program
* It prevents WhatsApp from detecting automation
* It speeds up QR code scanning
**Answer:** It waits only until the required element becomes available, making the script more reliable

**2) What is the main limitation of using the contact's name in the XPath selector?**
* It works only for group chats
* It may fail if multiple contacts share similar names
* It cannot locate encrypted chats
* It increases page load time
**Answer:** It may fail if multiple contacts share similar names

**3) Why does the script require manual QR code scanning instead of automating login?**
* Selenium does not support camera access
* WhatsApp Web blocks JavaScript execution
* Authentication is tied to a real user session for security
* ChromeDriver cannot load HTTPS websites
**Answer:** Authentication is tied to a real user session for security

**4) What would most likely happen if the delay between messages (time.sleep(1)) were removed?**
* Messages would not be sent at all
* The browser would crash immediately
* Selenium would raise a syntax error
* The script could trigger UI failures or platform restrictions
**Answer:** The script could trigger UI failures or platform restrictions

**5) Which Selenium feature is primarily responsible for simulating a real user pressing Enter?**
* Keys.RETURN
* By.CLASS_NAME
* driver.get()
* WebDriverWait
**Answer:** Keys.RETURN

**6) Why is automation of messaging platforms considered ethically sensitive?**
* It consumes more internet bandwidth
* It can lead to misuse such as spamming or harassment
* It requires paid browser drivers
* It increases system memory usage
**Answer:** It can lead to misuse such as spamming or harassment

**7) Which design choice makes this script platform-dependent?**
* Use of Python language
* Reliance on internet connectivity
* Dependence on WhatsApp Web's DOM structure
* Use of loops for repetition
**Answer:** Dependence on WhatsApp Web's DOM structure

**8) Why is driver.quit() preferred over simply closing the browser window manually?**
* It saves execution time
* It sends logout signals to WhatsApp
* It keeps the session active for reuse
* It properly terminates the WebDriver and releases system resources
**Answer:** It properly terminates the WebDriver and releases system resources

---

## Case Study: Automated Academic Schedule Analyzer

### Background
A university administration system needs to analyze academic schedules for a semester. The system should be able to:
* Track important academic dates (semester start, exams, holidays)
* Determine weekdays for given dates
* Identify leap years (important for February schedules)
* Generate monthly calendars for planning purposes
* Compute gaps between important academic events

### Part 1: Working with Dates and Time (datetime Module)
The system begins by capturing the current date and time when the administrator logs in.

```python
import datetime
login_time = datetime.datetime.now()
print(login_time)
```

**Creating Fixed Academic Dates**
The semester officially starts on August 5, 2025, and the mid-semester exam is scheduled for October 12, 2025.

```python
semester_start = datetime.date(2025, 8, 5)
mid_exam = datetime.date(2025, 10, 12)
```

**Calculating Duration Between Events**
The system calculates how many days students have between the semester start and the mid-semester exam.

```python
gap = mid_exam - semester_start
print(gap.days)
```

**Extracting Date Components**
```python
year = semester_start.year
month = semester_start.month
day = semester_start.day
```

**Formatting Dates for Reports**
```python
formatted_date = semester_start.strftime("%A, %d %B %Y")
print(formatted_date)
```

### Part 2: Academic Calendar Analysis (calendar Module)
To assist with planning lectures and exams, the system generates a monthly calendar.

```python
import calendar
print(calendar.month(2025, 8))
```

**Checking Leap Year Constraints**
```python
calendar.isleap(2024)
```

**Identifying Weekdays for Exams**
```python
exam_day = calendar.weekday(2025, 10, 12)
print(calendar.day_name[exam_day])
```

**Counting Days in a Month**
```python
days_in_august = calendar.monthrange(2025, 8)[1]
print(days_in_august)
```

---

## Questions 9 - 15

**9) What does gap.days logically represent?**
* The number of calendar days between the two academic events
* The number of weekdays between the two dates
* The number of lecture days excluding holidays
* The number of months between the two dates
**Answer:** The number of calendar days between the two academic events

**10) Which of the following attributes is NOT directly available from a datetime.date object?**
* semester_start.year
* semester_start.hour
* semester_start.month
* semester_start.day
**Answer:** semester_start.hour

**11) Which part of the output is produced specifically by %A in strftime?**
* Numeric day of the month
* Full name of the month
* Full name of the weekday
* Four-digit year
**Answer:** Full name of the weekday

**12) Why does the system check calendar.isleap(2024)?**
* To determine whether weekends change in 2024
* To confirm February has 29 days in that year
* To find how many weekdays exist in 2024
* To calculate the total number of academic days
**Answer:** To confirm February has 29 days in that year

**13) Why is identifying the exam weekday a two-step process?**
* calendar.weekday() returns a string index
* calendar.weekday() returns a month name
* calendar.weekday() returns an integer mapped to a weekday
* calendar.day_name only works for leap years
**Answer:** calendar.weekday() returns an integer mapped to a weekday

**14) In the code `calendar.monthrange(2025, 8)[1]`, what does the index [1] specifically retrieve?**
* The weekday of the first day of August
* The number of Sundays in August
* The total number of days in August
* The number of weekdays in August
**Answer:** The total number of days in August

**15) Why is datetime.datetime.now() used instead of datetime.date.today() for login tracking?**
* date.today() is slower
* Login tracking requires both date and time
* datetime.date cannot be stored in logs
* datetime.now() works only on servers
**Answer:** Login tracking requires both date and time

