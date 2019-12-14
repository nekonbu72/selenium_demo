from pathlib import Path
from time import sleep

from config import Config
from secret import Secret
from selenium import webdriver

# firefox, geckodriver, selenium のバージョン対応は下記をチェック
# https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html

fp = webdriver.FirefoxProfile(profile_directory=Config.PROFILE)
for key, value in Config.PREFERENCE.items():
    fp.set_preference(key, value)

# firefox が立ちあがる前に削除しないといけない
FOLDERINNERTEMP = "webdriver-py-profilecopy"
for name in ["mimeTypes.rdf", "handlers.json"]:
    p = Path(fp.tempfolder).joinpath(FOLDERINNERTEMP, name)
    if p.is_file():
        p.unlink()

with webdriver.Firefox(
    firefox_profile=fp,
    firefox_binary=Config.FIREFOX,
    executable_path=Config.GECKODRIVER,
    log_path=Config.LOG
) as driver:

    driver.implicitly_wait(2)

    driver.get(Secret.URL)
    driver.find_element_by_name("sei_login").send_keys(Secret.SSO_ID)
    driver.find_element_by_name("sei_passwd").send_keys(Secret.SSO_PASSWORD)
    driver.find_element_by_name("login").submit()

    sleep(2)

    driver.switch_to.frame("fr_menu")
    driver.find_element_by_css_selector(
        "body > table:nth-child(8) > tbody > tr:nth-child(2) > td > a").click()

    driver.switch_to.parent_frame()
    driver.switch_to.frame("fr_main")

    sleep(1)

    driver.find_element_by_name("kensyu_nm").send_keys(Secret.SEARCH)
    driver.find_element_by_name("btn_submit").submit()

    sleep(2)

    driver.find_element_by_id("pms_SeiResult2_link_vd_semdate_fne01_0").click()

    driver.find_element_by_css_selector(
        "#pms_dtl2_pms_SeiResult2_link_vd_detailview_fne01_0").click()

    default_window = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if driver.title == Secret.WINDOW:
            break

    sleep(2)

    driver.find_element_by_link_text(Secret.LINK).click()

    driver.switch_to.window(default_window)
    sleep(10)
