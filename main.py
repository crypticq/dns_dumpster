from bs4 import BeautifulSoup
import requests
import re
import json
import time
import pyfiglet
import sys
import argparse

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'




banner = pyfiglet.figlet_format("Dns enumeration...")
print(banner)
print(style.BLUE +'[*] Dns enumeration [*] ')
print(style.RED + 'Coded By Eng Yazeed ')
print(style.CYAN + " [*] instagram COMMPLICATED [*] ")





class sub_domains:


	def __init__(self , target ,  out):

		self.target = target
		self.out = out


	def dns_dumpster(self):



		headers = {
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		    'Accept-Encoding': 'gzip, deflate, br',
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'Origin': 'https://dnsdumpster.com',
		    'Connection': 'keep-alive',
		    'Referer': 'https://dnsdumpster.com/',
		    'Upgrade-Insecure-Requests': '1',
		    'Sec-Fetch-Dest': 'document',
		    'Sec-Fetch-Mode': 'navigate',
		    'Sec-Fetch-Site': 'same-origin',
		    'Sec-Fetch-User': '?1',
		}


		s = requests.session()
		s.get('https://dnsdumpster.com/', headers=headers)
		cookies_dictionary = s.cookies.get_dict()
		data = {
	    'csrfmiddlewaretoken': s.cookies['csrftoken'],
	    'targetip': self.target ,
	    'user': 'free'
		}

		response = requests.post('https://dnsdumpster.com/', headers=headers,data=data , cookies=cookies_dictionary)
		soup = BeautifulSoup(response.content , 'lxml')

		for x in soup.find_all('td' , class_='col-md-4'):
			c = x.text.split()
			for line in c:
				if self.target not in line:
					pass
				else:
					with open(self.out , 'a') as infile:
						infile.write("\n")
						infile.write(line)
						print(style.CYAN+"******************************************" + "\n")

						print(f"{style.GREEN} Found a sub  {line}" + "\n")
						
						print(style.CYAN+"******************************************" + "\n")
		print(f' [*] Result saved in {self.out} [*]')



def get_args():
	parser = argparse.ArgumentParser(description='Dns enumeration')
	parser.add_argument('-t', '--target', dest="target", required=True, action='store', help='Target to get enumerate Dns . ')
	parser.add_argument('-f', '--file', dest="file", required=True, action='store', help='fie name to save output.')
	args = parser.parse_args()
	return args

args = get_args()
target = args.target
fileo = args.file


if __name__ == '__main__':

	d = sub_domains(target , fileo)
	d.dns_dumpster()
