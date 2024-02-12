import requests
import json
from bs4 import BeautifulSoup

headers = {
        'authorization': 'Mjk3MTk0ODk4MzY3NDQ3MDQw.GpKk6H.I1L_DwkbCBPGElyjUPGcgKG5tr2njnIvauGfq8'
    }

def retreive_messages(channel_id, headers):
    headers = {
        'authorization': 'Mjk3MTk0ODk4MzY3NDQ3MDQw.GpKk6H.I1L_DwkbCBPGElyjUPGcgKG5tr2njnIvauGfq8'
    }
    req = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers = headers)
    jsonn = json.loads(req.text)
    return jsonn[0]['content']
    


def fill(code, headers):
    payload = {
    'content': code
}
    req = requests.post('https://discord.com/api/v9/channels/1141155655076544514/messages', data=payload, headers=headers)

def fill_top(code):
    payload = {
    'student_id': code
    }
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjcwNDMxOTksImV4cCI6MTY5MjE0Nzg5NSwiaWF0IjoxNjkyMTQ2MDk1LCJyZWZyZXNoX3Rva2VuX2xpZmVzcGFuIjo2NDMzMjgsImRhdGFfbmFtZXNwYWNlIjoicHJvZHVjdGlvbjp1cyIsInJvbGVfYXV0aG9yaXphdGlvbiI6eyJ2ZXJzaW9uIjowLjEsInJvbGVfd2l0aG91dF9jb250ZXh0IjoiU1RVREVOVCIsInJvbGVzIjp7IlNUVURFTlQiOnsiQ09VUlNFIjpbIjMyNzAwMSIsIjcyOTUzNCIsIjc3OTg5NCJdfX19LCJ1c2VyX2RhdGEiOnsiY3JlYXRlZF90aW1lc3RhbXBfbXMiOjE2NjI1NjM0MTMwMDAsImhhc190b3BoYXRfZW1haWwiOmZhbHNlLCJvcmdfaWQiOjQ3fX0.xQLraJYHItogxeaVKBS2ne6dEtMST8sjwBe9M7mhA2kne_ggU46HrsTsq1N4XQaC2e3rh-mYFSQViKs6opfKyQ'
    }
    req = requests.patch('https://app.tophat.com/api/v2/user//7043199/', data=payload, headers = headers)

print(retreive_messages(1141155655076544514, headers))
fill_top(retreive_messages(1141155655076544514, headers))

  
cookies = {
    '__dcfduid': 'd52c6c2007d911ee9499c359bf7e47ba',
    '__sdcfduid': 'd52c6c2107d911ee9499c359bf7e47ba599deb39832c7227e6fba8c0c2c52bff5350c7e2219f92b7f764aa27e65d2e31',
    '__cfruid': 'de5fb23ec5b035953e2c1c094e172eea0a120aa0-1691674572',
    'cf_clearance': 'DZOMN9MftOZtaCiAJ6sc03HFpss_jNt321GiuiKlxBw-1691891535-0-1-6fd28b84.f1b45ab9.d08353b3-0.2.1691891535',
    'locale': 'en-US',
    '_gcl_au': '1.1.1278758775.1692057277',
    '_ga_Q149DFWHT7': 'GS1.1.1692057277.1.0.1692057277.0.0.0',
    '_ga': 'GA1.2.401575672.1687288820',
    '_gid': 'GA1.2.1995019595.1692057441',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+Aug+14+2023+19%3A57%3A20+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
}

headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '__dcfduid=d52c6c2007d911ee9499c359bf7e47ba; __sdcfduid=d52c6c2107d911ee9499c359bf7e47ba599deb39832c7227e6fba8c0c2c52bff5350c7e2219f92b7f764aa27e65d2e31; __cfruid=de5fb23ec5b035953e2c1c094e172eea0a120aa0-1691674572; cf_clearance=DZOMN9MftOZtaCiAJ6sc03HFpss_jNt321GiuiKlxBw-1691891535-0-1-6fd28b84.f1b45ab9.d08353b3-0.2.1691891535; locale=en-US; _gcl_au=1.1.1278758775.1692057277; _ga_Q149DFWHT7=GS1.1.1692057277.1.0.1692057277.0.0.0; _ga=GA1.2.401575672.1687288820; _gid=GA1.2.1995019595.1692057441; OptanonConsent=isIABGlobal=false&datestamp=Mon+Aug+14+2023+19%3A57%3A20+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
    'dnt': '1',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/login?redirect_to=%2Fchannels%2F%40me',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'America/New_York',
    'x-fingerprint': '1140796294273704068.VYqaEnt44shwE7rEnHTCN5Jp0ms',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjE5ODM5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
}

json_data = {
    'login': 'vmodalla@gmail.com',
    'password': 'replace with your password',
    'undelete': False,
    'login_source': None,
    'gift_code_sku_id': None,
}

toPost = requests.post('https://discord.com/api/v9/auth/login', cookies=cookies, headers=headers, json=json_data)
print(toPost.status_code)


response = requests.get('https://discord.com/channels/1120436978350039052/1120443668688547980')

soup = BeautifulSoup(response.content,'html.parser')




