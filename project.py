# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as  np
import pandas as pd
a = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\PLACES.xlsx')
b = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\Tourist_cities.xlsx')
c = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\TRANSPORT.xlsx')
d = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\Uttarakhand.xlsx')
e = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\Rajasthan.xlsx')
f = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\Himachal.xlsx')
g = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\Punjab.xlsx')
h = pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\Sikkim.xlsx')
i= pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\Kerala.xlsx')
j=pd.read_excel(r'C:\Users\HP\Desktop\IP\IP Project\payment.xlsx')

df1=(a.set_index([pd.Index([1,2,3,4,5,6])]))
df2=(b.set_index([pd.Index([1,2,3])]))
df3=(c.set_index([pd.Index([1,2,3])]))
df4=(d.set_index([pd.Index([1,2,3])]))
df5=(e.set_index([pd.Index([1,2,3])]))
df6=(f.set_index([pd.Index([1,2,3])]))
df7=(g.set_index([pd.Index([1,2,3])]))
df8=(h.set_index([pd.Index([1,2,3])]))
df9=(i.set_index([pd.Index([1,2,3])]))
df10=(j.set_index([pd.Index([1,2,3,4])]))

print("BEYOND BORDERS")
Name=input("Enter your name:")
No=int(input("Enter your number:"))
print(df1)
print("Enter Serial number")
n=int(input("Choose your destination:"))
if n==1:
    s=(df1.iloc[0])
    print(s)
    t=pd.DataFrame(s) 
    p1=(t.iloc[1])
    print("Places to visit in Himachal Pradesh")
    print(df2.loc[:,['Himachal Pradesh']])
    print("Hotels to stay")
    print(df6)
    x=int(input("Choose hotel name:"))
    if x==1:
        l=(df6.iloc[0])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==2:
        l=(df6.iloc[1])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==3:
        l=(df6.iloc[2])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    else:
        print("Not Available")     
    print("To cofirm your bookings please verify the following details")
elif n==2:
    s=(df1.iloc[1])
    print(s)
    t=pd.DataFrame(s) 
    p1=(t.iloc[1]) 
    print("Places to visit in Kerala")
    print(df2.loc[:,['Kerala']])
    print("Hotels to stay")
    print(df9)
    x=int(input("Choose hotel name:"))
    if x==1:
        l=(df9.iloc[0])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==2:
        l=(df9.iloc[1])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==3:
        l=(df9.iloc[2])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    else:
        print("Not Available")     
    print("To cofirm your bookings please verify the following details")
elif n==3:
    s=(df1.iloc[2])
    print(s)
    t=pd.DataFrame(s) 
    p1=(t.iloc[1])
    print("Places to visit in Punjab ")
    print(df2.loc[:,['Punjab']])
    print("Hotels to stay")
    print(df7)
    x=int(input("Choose hotel name:"))
    if x==1:
        l=(df7.iloc[0])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==2:
        l=(df7.iloc[1])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==3:
        l=(df7.iloc[2])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    else:
        print("Not Available")    
    print("To cofirm your bookings please verify the following details")
elif n==4:
    s=(df1.iloc[3])
    print(s)
    t=pd.DataFrame(s) 
    p1=(t.iloc[1])
    print("Places to visit in Rajasthan")
    print(df2.loc[:,['Rajasthan']])
    print("Hotels to stay")
    print(df5)
    x=int(input("Choose hotel name:"))
    if x==1:
        l=(df5.iloc[0])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==2:
        l=(df5.iloc[1])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==3:
        l=(df5.iloc[2])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    else:
        print("Not Available")       
    print("To cofirm your bookings please verify the following details")
elif n==5:
    s=(df1.iloc[4])
    print(s)
    t=pd.DataFrame(s) 
    p1=(t.iloc[1])
    print("Places to visit in Sikkim")
    print(df2.loc[:,['Sikkim']])
    print("Hotels to stay")
    print(df8)
    x=int(input("Choose hotel name:"))
    if x==1:
        l=(df8.iloc[0])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==2:
        l=(df8.iloc[1])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==3:
        l=(df8.iloc[2]) 
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    else:
        print("Not Available")       
    print("To cofirm your bookings please verify the following details")
elif n==6:
    s=(df1.iloc[5])
    print(s)
    t=pd.DataFrame(s) 
    p1=(t.iloc[1])
    print("Places to visit in Uttrakhand")
    print(df2.loc[:,['Uttrakhand']])
    print("Hotels to stay")
    print(df4)
    x=int(input("Choose hotel name:"))
    if x==1:
        l=(df4.iloc[0])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==2:
        l=(df4.iloc[1])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    elif x==3:
        l=(df4.iloc[2])
        print(l)
        w=pd.DataFrame(l) 
        p2=(w.iloc[1])
    else:
        print("Not Available")      
    print("To cofirm your bookings please verify the following details")
else:
    print("Not Available")   
while(n<=6): 
    print("Name:",Name)    
    print("No:",No)
    p=int(input("No of adults:"))
    s=int(input("No of children under 5(half price):"))
    d=int(input("Enter Aadhar No:"))
    g=(input("Enter boarding place:"))
    print("Different mode of transport")    
    print(df3)
    m=int(input("Choose mode of transport:"))
    if m==1:
        z=(df3.iloc[0])
        print(z)
        r=pd.DataFrame(z) 
        p3=(r.iloc[1])
    elif m==2:
        z=(df3.iloc[1])
        print(z)
        r=pd.DataFrame(z) 
        p3=(r.iloc[1])
    elif m==3:
        z=(df3.iloc[2])
        print(z)
        r=pd.DataFrame(z) 
        p3=(r.iloc[1])
    else:
        print("Not Available") 
    pt1=([p1,p2,p3])
    pt2=pd.concat(pt1)
    pt=(pt2.sum())
    at=(pt*p)
    ct=((pt*s)/2)
    am=(at+ct)
    print("Total amount:",am)
    print(df10)
    pay=int(input("Choose payment method:"))
    if pay==1:
        print(df10.iloc[0])
        in1=int(input("Enter Debit card no.:"))
    elif pay==2:
        print(df10.iloc[1])
        in1=int(input("Enter Credit card no.:"))
    elif pay==3:
        print(df10.iloc[2])
        in1=int(input("Enter account no.:"))
    elif pay==4:
        print(df10.iloc[3])
        int1=int(input("Enter account no.:"))
    else:
        print("Not Available")
    print("Thankyou for planning your memorable moments with us!")
    print("HAPPY JOURNEY!!!:)")
    break
   
    

    





 
             