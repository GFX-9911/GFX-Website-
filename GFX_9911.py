print ("Welcome to the GFX O_9911 website ")
name = input ("Enter your name: ")
print ("hello",name)
print ("Let me explain the site to you. The site is a site to let you know what vulnerabilities exist and other things.....")
What_do_you_want =int (input ("What do you want? Type 1 to see the most important loopholes. Type 2 to see all the loopholes "))
if What_do_you_want == 1:
	print ("sql injection, xss, csrf, file upload vurnerabilities")
elif What_do_you_want == 2:
	print("""1- SQL Injection
2- Cross-Site Scripting (XSS)
3- Remote Code Execution (RCE)
4- Directory Traversal
5- Cross-Site Request Forgery (CSRF)
6- Local File Inclusion (LFI)
7- Remote File Inclusion (RFI)
8- Server-Side Request Forgery (SSRF)
9- Broken Authentication
10- XML External Entities (XXE)
11- Insecure Deserialization
12- Command Injection
13- Buffer Overflow
14- Privilege Escalation
15- Clickjacking
16- DNS Spoofing
17- ARP Spoofing
18- Session Fixation""")