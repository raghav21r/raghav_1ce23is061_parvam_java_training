from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "shreeskanda2715@gmail.com"
PASSWORD = "Skanda@2706"

def build_driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def login(driver):
    driver.get("https://scholar.parvam.in/student/login")

    wait = WebDriverWait(driver, 20)

    try:
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]")))
        login_btn.click()
    except:
        print("Login button not found")

    try:
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    except:
        print("Login fields not found")
        return

    email_input.clear()
    email_input.send_keys(EMAIL)

    password_input.clear()
    password_input.send_keys(PASSWORD)

    try:
        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        submit_btn.click()
    except:
        password_input.send_keys(Keys.RETURN)

    print("Login attempted")

def main():
    driver = build_driver()
    login(driver)

    print("Browser will stay open (session active)")
    input("Press ENTER to close browser...")

    driver.quit()

if __name__ == "__main__":
    main()