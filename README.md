# Blackhost-demo
Selenium bot auto complete

<h3>What you might need and how to run the script</h3>
<ul>
  <li> You must have <ahref="https://pypi.org/project/selenium/>Selenium</a> installed </li>
  <li> Firefox </li>
</ul>

## **Installation**

- Install Requirements
```elm
pip3 install -r requirements.txt
```
- Install Selenium with pip (In case requirement.txt oudated)
```elm
pip install selenium
```
- Download Web Driver
```elm
wget 'https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz' -O driver.tar.gz
```
- Install Web Driver

```elm
chmod +x driver.tar.gz
```
```elm
tar -zxvf driver.tar.gz 
```
```elm
sudo cp geckodriver /usr/local/bin
```
## **Running🚀**
```elm
python3 Bot.py
```
<h3>Read more about <a href="https://www.selenium.dev/documentation/webdriver/getting_started/">Selenium</a></h3>
