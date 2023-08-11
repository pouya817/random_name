import requests
import json
def match_ege():
    while True:
        response=requests.get('https://randomuser.me/api/')
        t=response.json()
        age=t['results'][0]['dob']['age']
        if age < 30:
            X='Hey, now I have found a %s years old person maybe you want to chat with.' % age
            print('Hey, now I have found a %s years old person maybe you want to chat with.' % age)
            break
    return X
x=match_ege()
sms_info=requests.get('https://api.kavenegar.com/v1/0/utils/getdate.json')
print(sms_info.json())
sms=requests.post('https://api.kavenegar.com/v1/7065344F526B327A6359512B5A4E314A347332364355616A646D495A61364D39755047592B4E76343463773D/sms/send.json?receptor=09104346645&sender=10008663&message=%s' % x)
sms=sms.json()
print(sms)