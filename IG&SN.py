import pyttsx3
import requests
import os
import sys
import nmap3
from colorama import Fore
# clear page
from os import system , name
import socket
try :
	def clear():
		if name == "nt" :
			_ = system('cls')
		else :
			_ = system('clear')
	clear()
	# end clear functrion
	engine = pyttsx3.init()
	def speak(audio):
	    engine.say(audio)
	    engine.runAndWait()
	    rate = engine.getProperty('rate')
	    engine.setProperty('rate', rate - 8)
	speak("Hello , Welcome Back Hacker")
	print(Fore.GREEN + """
██╗░██████╗░░██████╗███╗░░██╗
██║██╔════╝░██╔════╝████╗░██║
██║██║░░██╗░╚█████╗░██╔██╗██║
██║██║░░╚██╗░╚═══██╗██║╚████║
██║╚██████╔╝██████╔╝██║░╚███║
╚═╝░╚═════╝░╚═════╝░╚═╝░░╚══╝
		""")
	print(Fore.RED + """
	1.Information Gathering
	2.Scanning
		""")
	speak("""
	1.Information Gathering
	2.Scanning
		""")
	select = int(input(Fore.GREEN + "[+] " + Fore.BLUE + "[HACKER] | [SELECT NUMBER] : "))
	if select == 1 :
		clear()
		print(Fore.GREEN + """
	██╗░██████╗░
	██║██╔════╝░
	██║██║░░██╗░
	██║██║░░╚██╗
	██║╚██████╔╝
	╚═╝░╚═════╝░
	Welcome To Information Gathering Menue
			""")
		speak("Welcome To Information Gathering Menue")
		print(Fore.YELLOW + """
	1.WhoIs
	2.Email Gathering
	3.Sub Domain Gathering
	4.Directory Brute Force
			""")
		speak("""
	1.WhoIs
	2.Email Gathering
	3.Sub Domain Gathering
	4.Directory Brute Force
			""")
		ig = int(input(Fore.GREEN + "[+] " + Fore.BLUE + "[HACKER] + [IG] : "))
		if ig == 1 :
			print("")
			speak("Give Me A Domain")
			domain = input(Fore.RED + "Domain : ").lower()
			domain = domain.replace("http://","")
			domain = domain.replace("https://","")
			domain = domain.replace("www.","")
			if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
			    whois_server = "whois.internic.net"
			else:
			    whois_server =  "whois.iana.org"
			s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
			s.connect((whois_server,43))
			s.send((domain+"\r\n").encode())
			msg = s.recv(10000)
			print("")
			print(Fore.GREEN + msg.decode())
			speak(msg.decode())
		elif ig == 2 :
			print("")
			print(Fore.GREEN + "For Information Gathring About Email : https://github.com/laramies/theHarvester")
			print(Fore.GREEN + "You Can Go To This Link & Install This Tool & Enjoy :)")
			print(Fore.GREEN + "Tip : I Have this tool In Here So Please See Tool Folder")
			speak("""
	For Information Gathring About Email : https://github.com/laramies/theHarvester
	You Can Go To This Link & Install This Tool & Enjoy
	Tip : I Have this tool In Here So Please See Tool Folder
				""")
		elif ig == 3 :
			print("")
			speak("Give Me A Domain")
			domain = input(Fore.RED + "Domain : ").lower()
			domain = domain.replace("http://","")
			domain = domain.replace("https://","")
			domain = domain.replace("www.","")
			file = open("subdomains.txt")
			content = file.read()
			subdomains = content.splitlines()
			discovered_subdomains = []
			for subdomain in subdomains:
				url = f"http://{subdomain}.{domain}"
				try:
					requests.get(url)
				except requests.ConnectionError:
					pass
				else:
					print(Fore.GREEN + "[+] Discovered subdomain:", url)
					speak("Discovered subdomain " + str(url))
					discovered_subdomains.append(url)
			with open("discovered_subdomains.txt", "w") as f:
				for subdomain in discovered_subdomains:
					print(subdomain, file=f)
		elif ig == 4 :
			print("")
			speak("Please Give Me A Domain With HTTP Or HTTPS")
			print(Fore.GREEN + "Please Give Me A Domain With HTTP Or HTTPS")
			dirsite = input(Fore.YELLOW + "Domain : ")
			os.system("pip install dirsearch")
			os.system("dirsearch -u " + str(dirsite))
	elif select == 2 :
		clear()
		print(Fore.GREEN + """
	░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗██╗███╗░░██╗░██████╗░
	██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██║████╗░██║██╔════╝░
	╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║██║██╔██╗██║██║░░██╗░
	░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██║██║╚████║██║░░╚██╗
	██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║██║██║░╚███║╚██████╔╝
	╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░
	Welcome To Scanning Menue
			""")
		speak("Welcome To Scanning Menue")
		speak("Warning In Scanning Module You Need To Run This Script By Root Privilage")
		print(Fore.YELLOW + "Warning : " + Fore.RED + "In Scanning Module You Need To Run This Script By Root Privilage")
		print(Fore.CYAN + """
	1.Port Scanning
	2.DNS Brute
	3.OS Scanning
	4.Version Detection
	5.Sub Net Scan
	6.FIN Scan
	7.IDLE Scan
	8.PING Scan
	9.SYN Scan
	10.TCP Scan
	11.UDP Scan
	12.ARP Discovery
	13.Site Down Or Up?
			""")
		speak("""
	1.Port Scanning
	2.DNS Brute
	3.OS Scanning
	4.Version Detection
	5.Sub Net Scan
	6.FIN Scan
	7.IDLE Scan
	8.PING Scan
	9.SYN Scan
	10.TCP Scan
	11.UDP Scan
	12.ARP Discovery
	13.Site Down Or Up?
			""")
		scanmen = int(input(Fore.GREEN + "[+] " + Fore.BLUE + "[HACKER] | [SCANNING] : "))
		if scanmen == 1 :
			print("")
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.Nmap()
			res = nmap.scan_top_ports(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		elif scanmen == 2 :
			print("")
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.Nmap()
			res = nmap.nmap_dns_brute_script(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 3 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.Nmap()
			res = nmap.nmap_os_detection(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 4 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.Nmap()
			res = nmap.nmap_version_detection(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 5 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.Nmap()
			res = nmap.nmap_subnet_scan(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 6 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.NmapScanTechniques()
			res = nmap.nmap_fin_scan(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 7 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.NmapScanTechniques()
			res = nmap.nmap_idle_scan(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 8 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.NmapScanTechniques()
			res = nmap.nmap_ping_scan(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 9 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.NmapScanTechniques()
			res = nmap.nmap_syn_scan(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 10 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.NmapScanTechniques()
			res = nmap.nmap_tcp_scan(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 11 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.NmapScanTechniques()
			res = nmap.nmap_udp_scan(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 12 :
			tar = input(Fore.CYAN + "TARGET : ")
			nmap = nmap3.NmapHostDiscovery()
			res = nmap.nmap_arp_discovery(tar)
			if res == [] :
				print("")
				print(Fore.RED + "I Don't Have Response :|")
				print(Fore.YELLOW + "Please Run this script By Root Privilage & Try Again")
			else :
				print("")
				print(Fore.GREEN + str(res))
		if scanmen == 13 :
			print("")
			print(Fore.YELLOW + "Warning : " + Fore.RED + "Give Me A Domain With HTTP Or HTTPS")
			print("")
			domain = input(Fore.CYAN + "TARGET : ")
			checkurldownorup = requests.get(domain)
			if checkurldownorup.status_code == 200 :
				print(Fore.GREEN + "TARGET IS UP")
			elif checkurldownorup.status_code == 302 :
				print(fore.YELLOW + "TARGET MOVED")
			elif checkurldownorup.status_code == 404 :
				print(Fore.YELLOW + "TARGET NOT FOUND")
			elif checkurldownorup.status_code == 400 :
				print(Fore.YELLOW + "TARGET IS BAD REQUESTS")
			elif checkurldownorup.status_code == 500 :
				print(Fore.YELLOW + "TARGET INTERNAL SERVER ERROR")
			else :
				print(Fore.RED + "TARGET IS DOWN")
except :
	speak("I Hope You enjoy My Script")
	speak("Bye")