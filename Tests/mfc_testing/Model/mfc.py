from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss




class Mfc:
    def __init__(self):
        self.base_url = 'https://mariefreshcosmetics.com/'

    def open(self):
        browser.open('https://mariefreshcosmetics.com/')
        browser.driver.maximize_window()
        return self

    def search(self, port: str):
        browser.element('[placeholder="Пошук"]').type(port).press_enter()
        return self

    def open_item_page(self):
        browser.element('[href="/products/serum"]').click()
        return self

    def button_add_to_cart_click(self):
        browser.element('[href="/item?variant_id=225"]').click()
        return self

    def cart_click(self):
        s('/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/div[2]/a[1]/span[2]').click()
        return self

    def cart_add_item_click(self):
        