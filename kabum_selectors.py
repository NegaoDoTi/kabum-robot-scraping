from selenium.webdriver.common.by import By


class KabumSelectors:
    
    product_div = {"css_selector" : "div.productCard"}
    span_name = (By.CSS_SELECTOR, "span.nameCard")
    span_price = (By.CSS_SELECTOR, "span.priceCard")
    b_price = {"css_selector" : 'div[id="listingCount"] b'}
    ul_pages = {"css_selector" : 'ul.pagination li'}