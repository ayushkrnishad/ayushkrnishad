import time
import requests
import random
from lxml.html import fromstring
import pyfiglet




def banner():
    ascii_banner = pyfiglet.figlet_format("W H I T E R O S E")
    print(ascii_banner)

def change_ip_address():
    with open("ip_address.txt", "r") as file:
        allText = file.read()
        ip = list(map(str, allText.split()))
        change_ip = random.choice(ip)

    def get_proxies():
        # response = requests.get(change_ip)
        parser = fromstring(change_ip)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)

            return proxies

        proxies = get_proxies()
        print(proxies)

        clock()

    # this will change the ip address every five seconds
def clock():
    for i in range(5, 0, -1):
        print(i)
        seconds = i
        time.sleep(1)
        if seconds == 1:
            change_ip_address()

    if __name__ == '__main__':
        banner()
        change_ip_address()
        clock()

# this is for calling the functions
