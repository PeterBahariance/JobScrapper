from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv



jobTitle = []
jobLocation = []
jobCompanyName = []
salary = []



def simulate_typing(input_box, text, delay_range=(0.1, 0.3)):
    for char in text:
        input_box.send_keys(char)
        time.sleep(random.uniform(*delay_range))  # Random delay between characters

def next_page_exists():
    try:
        # Try to find the 'Next Page' button (this might need to be adjusted depending on your site's structure)
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]'))
        )
        return True  # There is a next page
    except:
        return False  # No next page


def perform_page_actions():

    

    time.sleep(5)

    ul_elements = driver.find_element(By.CSS_SELECTOR, ".css-1faftfv.eu4oa1w0")



    print()
    print()

    job_elements = ul_elements.find_elements(By.CSS_SELECTOR, ".css-1ac2h1w.eu4oa1w0")

    cashAmount = ""
    for job in job_elements:
        try:
            span_element = job.find_element(By.TAG_NAME, "span")

            span_title = span_element.get_attribute("title")  # If title is an attribute
            

            print(f"Title found: {span_title}")
            
            jobTitle.append(span_title)

            job_info_elements = job.find_element(By.CSS_SELECTOR, ".heading6.tapItem-gutter.metadataContainer.css-keyg3o.eu4oa1w0")

            li_elements_job_info = job_info_elements.find_elements(By.TAG_NAME, "li")
            
            if(len(li_elements_job_info) == 0):
                print("NO job specifications")

            try:
                companyName = job.find_element(By.CSS_SELECTOR, ".css-1h7lukg.eu4oa1w0")

                companyLocation = job.find_element(By.CSS_SELECTOR, ".css-1restlb.eu4oa1w0")    
                locationText = companyLocation.text

                if "\n" in locationText:
                    locationText = locationText.replace("\n", "").strip()


                print(f"Testing debug of location: {locationText}")



                print(f"This is the location: {locationText}")
                print(f"This is the name: {companyName.text}")
                
                jobCompanyName.append(companyName.text)
                jobLocation.append(locationText)            

            except:
                print("Company info (location or name) not listed!")
            # more-items css-kfr17i eu4oa1w0
            # more-items css-kfr17i eu4oa1w0
            
            for li in li_elements_job_info: 
                valid_info = li.find_element(By.CSS_SELECTOR, ".css-18z4q2i.eu4oa1w0")

                valid_info_text = valid_info.text

                # Check if any elements with the specified class exist
                try:
                                                                    #more-items css-kfr17i eu4oa1w0
                #                                             class="more-items css-kfr17i eu4oa1w0"
                    removeText = li.find_element(By.CSS_SELECTOR, ".more-items.css-kfr17i.eu4oa1w0")
                    #print("The element with the additional class we want to remove exists!")
                    #print(removeText.text)
                    valid_info_text = valid_info.text.replace(removeText.text, "").strip()
                    # print("Prior to printing the specification")
                    #print(valid_info_text)

                except:
                    print("The element with the additional class does not exist.")


                print(f"printing specification: {valid_info_text}")
                
                if '$' in valid_info_text:
                    cashAmount = valid_info_text

            
        
            print(f"This is the current amount of salarys listed: {len(salary)}")

            print()
            print()


            if cashAmount == "":
                cashAmount = "NA"

            print(f"This is the cash amount: {cashAmount} ")

            salary.append(cashAmount)        

            
        except:

            if len(salary) != len(jobTitle):
                salary.append("NA")


            print("We hit a crash statement")
            print()
            print()


    


    print(f"This is how many li elements there are: {len(job_elements)}")

    print()




AUTH = 'brd-customer-hl_93fc9cec-zone-scraping_browser1:ygly5ztsma26'
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

print('Connecting to Scraping Browser...')
sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
with Remote(sbr_connection, options=ChromeOptions()) as driver:
    print('Connected! Navigating...')
    driver.get('https://indeed.com')
    print('Taking page screenshot to file page.png')
    driver.get_screenshot_as_file('./page.png')
    print('Navigated! Scraping page content...')
    html = driver.page_source
    print(html)

    time.sleep(15)

    # West Covina, CA

    WebDriverWait(driver, 5).until(

        # <div class="css-1buvxxw e37uo190">

        EC.presence_of_element_located((By.CSS_SELECTOR, ".css-4pnak9.e1jgz0i3"))

    )

    searchButton = driver.find_element(By.CSS_SELECTOR, ".css-4pnak9.e1jgz0i3")

    locationButton = driver.find_element(By.CSS_SELECTOR, ".css-tphyky.e1jgz0i3")
    
    # Click to focus on the location input box
    locationButton.click()

    time.sleep(2)

    # Clear any existing text
    driver.execute_script("arguments[0].value = '';", locationButton)

    time.sleep(5)
    # Enter new location
    locationButton.send_keys("West Covina, CA")

    time.sleep(3)

    searchButton.click()


    inputBox = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".css-4pnak9.e1jgz0i3"))
    )

    # Simulate typing the search term with a delay
    inputBox.send_keys("Software Engineering Internships")
    inputBox.submit()


    # if after 5 seconds, the element doesn't exist, the program will automatically crash
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".css-1faftfv.eu4oa1w0"))
    )


    while True:
    # Step 1: Perform actions you need on the current page (scraping, etc.)
        perform_page_actions()
        
        # Step 2: Check if there's a next page
        if next_page_exists():
            # Step 3: Click the next page button
            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]'))
            )
            
            next_button.click()

            # Wait for the page to load (you can adjust the wait time as necessary)
            time.sleep(5)  # or use WebDriverWait to wait for a specific element

        else:
            # Step 4: Exit the loop if there's no next page
            print("No more pages to go through.")
            break
        

    print(f"This is the length of jobTitle {len(jobTitle)}")
    print(f"This is the length of jobLocation {len(jobLocation)}")
    print(f"This is the length of jobCompanyName {len(jobCompanyName)}")
    print(f"This is the length of salary {len(salary)}")


    # Save data to a CSV file
   # Save data to a text file

   # Specify the directory path and filename
    output_directory = "./"
    output_file = output_directory + "job_data.txt"

    with open(output_file, "w") as file:
        # make table NBA fields fname, lname, age, position, team
        #insert into NBA values Stephen, Curry, 33, Guard, \"Golden State Warriors\"

        file.write(f"make table existingJobs fields \"Job Title\", Location, \"Company Name\", Salary\n")
        for title, location, company, salary_value in zip(jobTitle, jobLocation, jobCompanyName, salary):
            file.write(f"insert into existingJobs values \"{title}\", \"{location}\", \"{company}\", \"{salary_value}\"\n")


    time.sleep(1000)


    driver.quit()



# jobTitle = []
# jobLocation = []
# jobCompanyName = []
# salary = []

# Things I want for data:
# Company name (definitely)
# Job title (definitely)
# location (definitely)
# if its  remote or in person
# salary 