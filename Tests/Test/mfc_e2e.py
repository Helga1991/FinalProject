from selene.support.shared import browser
from time import sleep
from selene.support.shared.jquery_style import s, ss
from Tests.mfc_testing.Model import port

def test_mfce2e():
    port.open()
    port.search('сироватка')
    port.open_item_page()
    port.button_add_to_cart_click()
    port.cart_click()

    sleep(3)


# #додати до кошика
# browser.element('[href="/item?variant_id=225"]').click()
# browser.element('').click()
#
# sleep (3)











#browser.element('/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/div[2]/a[3]/span[2]').click()
