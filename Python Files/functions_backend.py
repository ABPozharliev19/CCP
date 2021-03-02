
def search_by_id(browser, name_of_form, id, sent_text):
    name_of_form = browser.find_element_by_id(id)
    name_of_form.clear()
    name_of_form.send_keys(sent_text)