from concurrent.futures import ThreadPoolExecutor
from httpx_socks import SyncProxyTransport
from random import choice
from string import ascii_letters
from httpx import Client
from hfuck import bypass
from time import sleep, time
import json
import random
import requests

out_file = "proxies.txt"

with open("config.json") as data:
    config = json.load(data)
with open("bypassproxies.txt") as fp:
    bypassproxies = fp.read().splitlines()
_0, __0, _______0, _____0, ________0 = 0, open(out_file, encoding='utf-8').readlines(), 5, ThreadPoolExecutor(max_workers=int(1000000000)), 500 
___0 = config['invite'] # Invite Code 
____0 = 1000000 # Thread Amount
_________0 = config['name']
__________0 = 6 #Random Text

def _O():
    global _0, __0
    try:
        _ = __0[_0]
        _0 += 1
    except:
        _, _0 = __0[0], 0
    return _.replace('\n','')

def __O(_0):
  return ''.join(choice(ascii_letters)for _ in range(__________0))

def ___O(X, OO_):
    global __X0, __X1
    X_ = bypass('f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34', 'discord.com', f"{random.choice(bypassproxies)}", 's') # magic happens
    print("[hCapt] - Done")
    while True:
        if OO_ <= int(time()):
            break
        sleep(1)
    while True:
        try:
            ptype = config['type']
            hook = config['webhook']
            with Client(transport=SyncProxyTransport.from_url(f'{ptype}://{_O()}')) as _00:
                _ = _00.post("https://discord.com/api/v9/auth/register", headers={"Host":"discord.com", "Connection":"keep-alive", "sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "X-Fingerprint": "", "Accept-Language":"en-US", "sec-ch-ua-mobile":"?0", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47", "Content-Type":"application/json", "Authorization":"undefined", "Accept":"*/*", "Origin":"https://discord.com", "Sec-Fetch-Site":"same-origin", "Sec-Fetch-Mode":"cors", "Sec-Fetch-Dest":"empty", "Referer":"https://discord.com/register", "X-Debug-Options":"bugReporterEnabled", "Accept-Encoding":"gzip, deflate, br", "Cookie": "OptanonConsent=version=6.17.0; locale=th"}, json={"fingerprint": "", "username":f'{__O(8)} | {_________0}', "invite": X , "consent": True, "gift_code_sku_id":"", "captcha_key": X_}).json()
            ______0 = open("tokens.txt", "a")
            ______0.write(f'{_["token"]}\n')
            ______0.close()
            requests.post(hook, json={
                "username": "DcServicesV2",
                "content": f'{_["token"]}',
            }, headers={"content-type": "application/json"})
            return _["token"]
        except: pass

#print when a token is generated
def ____O(OO_):
    print('[GOOD] ' + ___O(___0, OO_))

___OO = int(time()+int(_______0))
print(f"bypassing, starts in: {_______0} secs")
for _ in range (____0):
    _____0.submit(____O, ___OO)
    if _ == ________0:
        sleep(10);________0 += 500