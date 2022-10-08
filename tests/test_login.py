from pages.home_page import HomePage

def test_login(driver):
    home_page = HomePage(driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_products_page() == "PRODUCTS"
    home_page.add_to_cart()
    assert home_page.your_cart_page() == "YOUR CART"
    assert home_page.first_product() == "Sauce Labs Backpack"
    assert home_page.second_product() == "Sauce Labs Bolt T-Shirt"
    home_page.checkout()
    assert home_page.checkout_page() == "CHECKOUT: YOUR INFORMATION"
    home_page.checkout_info("maja", "vk", "71000")
    assert home_page.checkout_overview_page() == "CHECKOUT: OVERVIEW"
    assert home_page.first_product() == "Sauce Labs Backpack"
    assert home_page.second_product() == "Sauce Labs Bolt T-Shirt"
    home_page.finish()
    assert home_page.checkout_complete_page() == "CHECKOUT: COMPLETE!"
    home_page.ikona_izbornika()
    assert home_page.login_page() == "https://www.saucedemo.com/"