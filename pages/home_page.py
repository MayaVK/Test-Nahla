from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def login(self, username, password):
        
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_polje.clear()
        username_polje.click()
        username_polje.send_keys(username)
        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_polje.clear()
        password_polje.click()
        password_polje.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
    
    def get_products_page(self):
        products_page = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return products_page.text

    def add_to_cart(self):
        first_product = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        first_product.click()
        second_product = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        second_product.click()
        shopping_cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart.click()
    
    def your_cart_page(self):
        your_cart = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return your_cart.text

    def first_product(self):
        backpack = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
        return backpack.text

    def second_product(self):   
        shirt = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']")
        return shirt.text

    def checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

    def checkout_page(self):
        checkout_your_information = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return checkout_your_information.text

    def checkout_info(self, first_name, last_name, postal_code):
        first_name_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name_polje.clear()
        first_name_polje.click()
        first_name_polje.send_keys(first_name)
        last_name_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        last_name_polje.clear()
        last_name_polje.click()
        last_name_polje.send_keys(last_name)
        postal_code_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        postal_code_polje.clear()
        postal_code_polje.click()
        postal_code_polje.send_keys(postal_code)
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def checkout_overview_page(self):
        checkout_overview = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return checkout_overview.text
    
    def finish(self):
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

    def checkout_complete_page(self):
        checkout_complete = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return checkout_complete.text
    
    def ikona_izbornika(self):
        ikona_izbornika_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        ikona_izbornika_button.click()
        logout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_button.click()
    
    def login_page(self):
        login_page_url = self.driver.current_url
        return login_page_url