import config

import os
import pathlib
from selenium import webdriver
from time import sleep

config.clean_download_dir()

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
# windows 7 だと効かない
fp.set_preference("browser.download.dir", config.download_dir())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", config.MIMETYPE)

driver = webdriver.Firefox(
    firefox_profile=fp,
    executable_path=config.geckodriver_path(),
    service_log_path=config.LOG_PATH
)
driver.implicitly_wait(2)

driver.get(config.URL)
driver.find_element_by_name("sei_login").send_keys(config.SSO_ID)
driver.find_element_by_name("sei_passwd").send_keys(config.SSO_PASSWORD)
driver.find_element_by_name("login").submit()

driver.switch_to.frame("fr_menu")
driver.find_element_by_css_selector(
    "body > table:nth-child(8) > tbody > tr:nth-child(2) > td > a").click()

driver.switch_to.parent_frame()
driver.switch_to.frame("fr_main")

sleep(1)

driver.find_element_by_name("kensyu_nm").send_keys(config.SEARCH)
driver.find_element_by_name("btn_submit").submit()

driver.find_element_by_id("pms_SeiResult2_link_vd_semdate_fne01_0").click()

driver.find_element_by_css_selector(
    "#pms_dtl2_pms_SeiResult2_link_vd_detailview_fne01_0").click()

default_window = driver.current_window_handle
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if driver.title == config.WINDOW:
        break

sleep(2)

driver.find_element_by_link_text(config.LINK).click()

driver.switch_to.window(default_window)
sleep(3)
driver.close()
driver.quit()

# os.remove("geckodriver.log")
