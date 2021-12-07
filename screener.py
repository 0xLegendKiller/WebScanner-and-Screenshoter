import uuid
from selenium import webdriver
from time import sleep
import pyfiglet

ascii_banner = pyfiglet.figlet_format("LegendKiller")
print(ascii_banner)
print("Usage :- python3 screener.py \n Sit back and let me capture the screenshots.")


def screenShooter(webpages):
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(executable_path=r"chromedriver.exe", options=option)
        browser.get(webpages)
        sleep(1)
        browser.get_screenshot_as_file('{}.png'.format(str(uuid.uuid4().hex)))
        browser.quit()
    except Exception as e:
        print(e)


with open('output.txt', 'r') as h:
    web = [lines.strip() for lines in (h.read()).split("\n") if lines]

for webs in web:
    screenShooter(webpages=webs)

print("Done")
