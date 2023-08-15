import requests
import json
import readchar
print('pls intere your age:')
age=str(readchar.readkey())+(str(readchar.readkey()))
age = int(age)
def person(want_age):
    want_age=int(want_age)
    while True:
        response=requests.get('https://randomuser.me/api/')
        personal_info=response.json()
        age=personal_info['results'][0]['dob']['age']
        if age < want_age:
            accepted_age='Hey, now I have found a %s years old person maybe you want to chat with \nif you want more detail push "y".' % age
            # print('Hey, now I have found a %s years old person maybe you want to chat with.' % age) just for test
            break
    return accepted_age , personal_info
x=person(age)
print(x[0])
if readchar.readkey()=='y':
    print (x[1])
# sms_info=requests.get('https://api.kavenegar.com/v1/0/utils/getdate.json') for test api server and accebility
# print(sms_info.json())
# sms=requests.post('https://api.kavenegar.com/v1/7065344F526B327A6359512B5A4E314A347332364355616A646D495A61364D39755047592B4E76343463773D/sms/send.json?receptor=09104346645&sender=10008663&message=%s' % x)
# sms=sms.json()
# print(sms)