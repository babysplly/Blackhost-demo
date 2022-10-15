from importlib import import_module
from lib2to3.pgen2.driver import Driver
from lib2to3.pgen2.token import NAME
from re import A, search
import itertools
import threading
from unicodedata import name
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os,time,sys


# ip =input ("your ip *cek on https://ipleak.net/ :")

#style
banner = """\u001b[1;31;31m 
██████  ███████ ██████   ██████  ██   ██  ██ ██████  ██████  
██   ██ ██      ██   ██ ██  ████  ██ ██  ███ ██   ██      ██ 
██████  █████   ██████  ██ ██ ██   ███    ██ ██   ██  █████  
██      ██      ██   ██ ████  ██  ██ ██   ██ ██   ██      ██ 
██      ███████ ██   ██  ██████  ██   ██  ██ ██████  ██████
\u001b[0m \u001b[32m
            -Author by: Splly
            -Contact:Y2F0Y2htZWlmeW91Y2FuX2FsQHByb3Rvbi5tZQo=
 \u001b[1;31;31m """
print(banner)

#animation


done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here


#start

driver = webdriver.Firefox()
driver.get("https://www.blackhost.xyz/")
#delet to maximize# driver.maximize_window()
#play a game
hack = driver.find_element(By.XPATH,"//*[@id='nav']/ul/li[5]/a")
hack.click()
#start 
play = driver.find_element(By.XPATH, "//*[@id='main']/p[4]/a")
play.click()

#level 1
lvl_1 = driver.find_element(By.NAME, "pass")
lvl_1.send_keys("k5=vm[69:s_b}]}0")
btn_lvl_1 = driver.find_element(By.XPATH,"//*[@id='main']/form/p/input[2]")
btn_lvl_1.click()

#level 2
lvl_2 = driver.find_element(By.NAME, "pass")
lvl_2.send_keys("=h7003n*z^cu(6q.")
btn_lvl_2= driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_2.click()

#level 3
lvl_3 = driver.find_element(By.NAME,"pass")
lvl_3.send_keys("Tk.on/ce!2rHSEgj")
btn_lvl_3 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_3.click()

#level 4
lvl_4 = driver.find_element(By.NAME,"pass")
lvl_4.send_keys("43{nm'-p78rem[t}")
btn_lvl_4 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_4.click()

#level 5
lvl_5 = driver.find_element(By.NAME,"pass")
lvl_5.send_keys("null")
btn_lvl_5 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_5.click()

#level 6
lvl_6 = driver.find_element(By.NAME,"pass")
lvl_6.send_keys("text/javascript")
btn_lvl_6 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_6.click()

#level 7
lvl_7 = driver.find_element(By.NAME,"pass")
lvl_7.send_keys("^(%b36rbf9gsu0qf")
btn_lvl_7 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_7.click()

#level 8
lvl_8 = driver.find_element(By.NAME,"pass")
lvl_8.send_keys("adhmpty26^)%,;è°")
btn_lvl_8 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_8.click()

#level 9
lvl_9 = driver.find_element(By.NAME,"pass")
lvl_9.send_keys("{6cK!h^z%402*)H3sA")
btn_lvl_9 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_9.click()

#level 10
lvl_10 = driver.find_element(By.NAME,"pass")
lvl_10.send_keys("cdt=vlu1qncl4:,:")
btn_lvl_10 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_10.click()

#level 11
lvl_11 = driver.find_element(By.NAME,"pass")
lvl_11.send_keys(".b%+z'tbj-)^tf*u")
btn_lvl_11 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_11.click()

#level 12
pw = ('!y%}_"v*"fk%6?gd')
lvl_12 = driver.find_element(By.NAME,"pass")
lvl_12.send_keys(pw)
btn_lvl_12 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_12.click()

#level 13
lvl_13 = driver.find_element(By.NAME,"pass")
lvl_13.send_keys("tv=.2-3+*d0w+$:7")
btn_lvl_13 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_13.click()

#level 14
lvl_14 = driver.find_element(By.NAME,"pass")
lvl_14.send_keys("6?w1l+.|*x1%_y!0")
btn_lvl_14 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_14.click()

#level 15
lvl_15 = driver.find_element(By.NAME,"pass")
lvl_15.send_keys("({|;i_d6:e6yj(+]")
btn_lvl_15 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_15.click()

#level 16
lvl_16 = driver.find_element(By.NAME,"pass")
lvl_16.send_keys("4POSO0U7XNVS7E1K")
btn_lvl_16 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_16.click()

#level 17
lvl_17 = driver.find_element(By.NAME,"pass")
lvl_17.send_keys("password")
btn_lvl_17 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
btn_lvl_17.click()

#level 18
lvl_18= driver.find_element(By.NAME,"pass")
lvl_18.send_keys('5*8,"f48)_dvzj8L')
btn_lvl_18 = driver.find_element(By.XPATH, "//*[@id='main']/form/p/input[2]")
# btn_lvl_18.click()  
# ganti= driver.SetAttribute('method="post"')
# ganti.getAttribute("get").replace("post")

# driver.execute_script('arguments[0].setAttribute("style", "%s")' % new_style, div_elem)
done = True
