import requests

print('Checking for captive portal...')
page = requests.get('http://captive.apple.com/hotspot-detect.html')
if "Success" not in page.text:
    print('Authenticating')
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://psu-guest.psu.edu',
        'Pragma': 'no-cache',
        'Referer': 'https://psu-guest.psu.edu/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    data = {
        'user': 'psu-guest',
        'password': '123456',
        'url': 'https://www.psu.edu',
        'cmd': 'authenticate',
        'Login': 'Log In',
    }

    response = requests.post('https://captiveportal-login.wlm.psu.edu/cgi-bin/login', headers=headers, data=data)
else:
    print('Already Authenticated')