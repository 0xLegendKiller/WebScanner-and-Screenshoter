# -*- coding: utf-8 -*-
import socket
import requests
from bs4 import BeautifulSoup
import pyfiglet

ascii_banner = pyfiglet.figlet_format("LegendKiller")
print(ascii_banner)
print("Starting all the scan. \n Output is saved in result.txt and list of urls for screenshots is saved in "
      "output.txt. \n Once the scans are complete run python3 screener.py")
writeTo = open('result.txt', 'a')
screenS = open('output.txt', 'a')


def port_scanner(url):
    writeTo.writelines(("-------------------------------Target Changed--------------------------------\n" * 2))
    print("\nStarting scan for {}".format(url))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        target = socket.gethostbyname(url)
        def_ports = [80, 8000, 8080]
        for port in def_ports:
            conn = s.connect_ex((target, port))
            # print("Running")
            if conn == 0:
                writeTo.writelines("Open port {} at target {}\n".format(port, url))
                print("\nOpen port {} at target {}".format(port, url))
                wk_url = "http://{}:{}".format(url, port)
                r = requests.get(wk_url)
                print(r.headers)
                screenS.writelines(wk_url)
                screenS.writelines("\n")
                writeTo.writelines("Url is {}\n".format(r.url))
                writeTo.writelines("Status Code at target {} is {}\n".format(wk_url, r.status_code))
                writeTo.writelines("Cookies at target {} are {}\n".format(wk_url, r.cookies))
                writeTo.writelines("Header at target {} are {}\n".format(wk_url, r.headers))
                writeTo.writelines("Request headers at {} are {}\n".format(wk_url, r.request.headers))
                soup = BeautifulSoup(r.text, 'html.parser')
                for title in soup.find_all('title'):
                    print("Website title for target {} is {}\n".format(wk_url, title.get_text()))
                    writeTo.writelines("Website title for target {} is {}\n".format(wk_url, title.get_text()))
            else:
                continue
    except KeyboardInterrupt:
        print("Stopped by user")
    except socket.gaierror:
        print("Could not find host")
    except socket.error:
        print("Server not responding")


with open('urls.txt', 'r') as h:
    urls = [lines.strip() for lines in (h.read()).split("\n") if lines]

for u in urls:
    port_scanner(u)
writeTo.close()
screenS.close()
