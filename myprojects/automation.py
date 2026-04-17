from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import sys

# ============================================
# LOGIN CREDENTIALS - UPDATE THESE
# ============================================
EMAIL = "raghav.rajpurohit1759@gmail.com"  # Update with your email
PASSWORD = "Raghav@2005"        # Update with your password
URL = "https://scholar.parvam.in/student/login"

# ============================================
# CHROMEDRIVER PATH - Update if needed
# ============================================
# If chromedriver is in PATH, you can leave this as None
CHROMEDRIVER_PATH = None  # Set to your chromedriver path if not in PATH

# ============================================
# CONFIGURE CHROME OPTIONS
# ============================================
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Uncomment to run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized')

try:
    # ============================================
    # INITIALIZE WEBDRIVER
    # ============================================
    if CHROMEDRIVER_PATH:
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)
    
    print("✓ Chrome browser initialized successfully")
    
    # ============================================
    # NAVIGATE TO LOGIN PAGE
    # ============================================
    print(f"→ Navigating to {URL}...")
    driver.get(URL)
    print("✓ Page loaded")
    
    # Wait for page to load completely
    time.sleep(2)
    
    # ============================================
    # LOCATE AND FILL EMAIL FIELD
    # ============================================
    print("→ Locating email field...")
    try:
        # Try multiple selectors for email field
        email_field = None
        selectors = [
            (By.NAME, "email"),
            (By.ID, "email"),
            (By.CSS_SELECTOR, "input[type='email']"),
            (By.XPATH, "//input[@type='email']"),
            (By.NAME, "username"),
            (By.ID, "username")
        ]
        
        for by, selector in selectors:
            try:
                email_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((by, selector))
                )
                print(f"✓ Email field found using selector: {selector}")
                break
            except:
                continue
        
        if email_field is None:
            print("⚠ Email field not found with standard selectors")
            print("Available form elements:")
            inputs = driver.find_elements(By.TAG_NAME, "input")
            for i, inp in enumerate(inputs):
                print(f"  Input {i}: name='{inp.get_attribute('name')}', id='{inp.get_attribute('id')}', type='{inp.get_attribute('type')}'")
            raise Exception("Could not locate email field")
        
        email_field.clear()
        email_field.send_keys(EMAIL)
        print(f"✓ Email entered: {EMAIL}")
        
    except Exception as e:
        print(f"✗ Error entering email: {e}")
        raise
    
    # ============================================
    # LOCATE AND FILL PASSWORD FIELD
    # ============================================
    print("→ Locating password field...")
    try:
        # Try multiple selectors for password field
        password_field = None
        selectors = [
            (By.NAME, "password"),
            (By.ID, "password"),
            (By.CSS_SELECTOR, "input[type='password']"),
            (By.XPATH, "//input[@type='password']")
        ]
        
        for by, selector in selectors:
            try:
                password_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((by, selector))
                )
                print(f"✓ Password field found using selector: {selector}")
                break
            except:
                continue
        
        if password_field is None:
            raise Exception("Could not locate password field")
        
        password_field.clear()
        password_field.send_keys(PASSWORD)
        print(f"✓ Password entered")
        
    except Exception as e:
        print(f"✗ Error entering password: {e}")
        raise
    
    # ============================================
    # FIND AND CLICK LOGIN BUTTON
    # ============================================
    print("→ Locating login button...")
    try:
        # Try multiple selectors for login button
        login_button = None
        selectors = [
            (By.XPATH, "//button[contains(text(), 'Login')]"),
            (By.XPATH, "//button[contains(text(), 'Sign In')]"),
            (By.XPATH, "//button[contains(text(), 'Submit')]"),
            (By.ID, "login-button"),
            (By.NAME, "submit"),
            (By.CSS_SELECTOR, "button[type='submit']"),
            (By.XPATH, "//input[@type='submit']")
        ]
        
        for by, selector in selectors:
            try:
                login_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((by, selector))
                )
                print(f"✓ Login button found using selector: {selector}")
                break
            except:
                continue
        
        if login_button is None:
            print("⚠ Login button not found with standard selectors")
            print("Available buttons:")
            buttons = driver.find_elements(By.TAG_NAME, "button")
            for i, btn in enumerate(buttons):
                print(f"  Button {i}: {btn.text}")
            raise Exception("Could not locate login button")
        
        print("→ Clicking login button...")
        login_button.click()
        print("✓ Login button clicked")
        
    except Exception as e:
        print(f"✗ Error clicking login button: {e}")
        raise
    
    # ============================================
    # WAIT FOR LOGIN TO COMPLETE
    # ============================================
    print("→ Waiting for login to complete...")
    time.sleep(3)
    
    current_url = driver.current_url
    print(f"✓ Current URL: {current_url}")
    print("✓ Login automation completed successfully!")
    print("\n" + "="*50)
    print("SCHOLAR DASHBOARD - LOGGED IN")
    print("="*50)
    print(f"Email: {EMAIL}")
    print(f"Logged in at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nSession is active. Close the browser window to end the session.")
    print("="*50 + "\n")
    
    # ============================================
    # KEEP SESSION ACTIVE UNTIL USER CLOSES
    # ============================================
    try:
        print("Keeping browser session open. Press Ctrl+C to close...")
        while True:
            time.sleep(1)
            # Check if browser is still open
            try:
                driver.current_url
            except:
                print("\n✓ Browser window closed by user")
                break
    except KeyboardInterrupt:
        print("\n→ Closing browser session...")
    
except Exception as e:
    print(f"\n✗ Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")
    sys.exit(1)

finally:
    # ============================================
    # CLEANUP
    # ============================================
    try:
        if 'driver' in locals():
            driver.quit()
            print("✓ Browser session closed cleanly")
    except:
        pass
