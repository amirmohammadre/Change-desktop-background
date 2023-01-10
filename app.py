import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options = options)


driver.get("https://www.bing.com/")
driver.maximize_window()


time.sleep(5)


download_btn = driver.find_element("xpath", "//a[@class='downloadLink ']")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(download_btn).click(download_btn).perform()


time.sleep(3)
driver.quit()


subprocess.run('mv /home/amir/Downloads/BingWallpaper.jpg /tmp', shell = True)
subprocess.run("gsettings set org.gnome.desktop.background picture-uri-dark 'file:///tmp/BingWallpaper.jpg'", shell = True)




