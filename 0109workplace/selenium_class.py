from selenium.webdriver import Chrome
driver = Chrome("./chromedriver")
import time
from password import password
from pytube import Playlist
import os


# 打開網址
driver.get("https://www.youtube.com/view_all_playlists")
# find_element = find
# find_elements = find_all
# 傳入帳號
driver.find_element_by_id("identifierId").send_keys(password.username)
# 選取繼續
driver.find_element_by_id("identifierNext").click()
# 不能太快速 睡一秒
time.sleep(1)
# 傳入密碼
driver.find_element_by_class_name("whsOnd").send_keys(password.password)
# 選取繼續
driver.find_element_by_id("passwordNext").click()
time.sleep(5)

for p in driver.find_elements_by_class_name("vm-video-title-text"):
    url = p.get_attribute("href")

    print(p.text, url)
    pl = Playlist(url,suppress_exception=True)
    dirname = './youtube/' + p.text
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    pl.download_all(dirname)


time.sleep(3)
driver.close()





