import http.client
conn = http.client.HTTPSConnection("apigw1.bot.or.th")

headers = {
    'x-ibm-client-id': "5a7c9544-9b4b-4089-a2e9-895864d7c185",
    'accept': "application/json"
    }

conn.request("GET", "/bot/public/Stat-ReferenceRate/v2/MONTHLY_REF_RATE/?start_period=2017-01&end_period=2020-09", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

import pandas as pd
j=pd.io.json.loads(data)
df=pd.DataFrame(j['result']['data']['data_detail'])
#แปลงให้เป็น Type DateTime
df.period= pd.to_datetime(df.period)
#แปลงให้เป็น Type Numeric
df.rate= pd.to_numeric(df.rate)
print(df)

import matplotlib.pyplot as plt #plot graph เส้น และกาหนดขนาดของเส้น
plt.plot(df.period,df.rate, linewidth=1) #กำหนด Description แต่ละเส้นพร้อมบอกตาแหน่งที่แสดง
plt.legend(["Line 1"], loc="upper right")
plt.show()
