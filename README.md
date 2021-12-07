# WebScanner-and-Screenshoter
```text
* Works only if you have chrome installed.
* This is the first draft and will continue to evolve and get better (as I keep learning) with time.
```

This repository consists of a web scanner python file and a python file to take screenshots.
* The idea is to supply the scanner with a list of urls which then perform some common port scans, fetch website title and headers and save the result in output.txt file.
* If ports are open the scanner will generate a results.txt file which will be used by the other python file to generate screenshots.


## If you face issues with chromedriver download the latest version from the site below.
> https://chromedriver.chromium.org/

https://user-images.githubusercontent.com/60841283/144974041-1aae4fcd-2077-45d5-9982-08974e697184.mp4

## Steps to install 
```bash
git clone https://github.com/0xLegendKiller/WebScanner_and_Screenshoter_v0.1.git
cd WebScanner_and_Screenshoter_v0.1
Put the list of URLs in urls.txt
python3 screener.py
python3 projector.py
```

Thanks for visitng !
