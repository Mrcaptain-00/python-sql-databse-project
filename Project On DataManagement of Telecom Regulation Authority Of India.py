#Python Sql connection Project(I.P)
#Project on TRAI
#By Mridul Singh
#12th 
import os
import platform as pltf
import mysql.connector as sqltor
import matplotlib.pyplot as plt
import pandas as pd

mycon1= sqltor.connect(host='localhost',user='root',passwd='mridul',database='trai')

mycursor=mycon1.cursor()
print("[-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]") 
print("[------------------------------------------------------[Welcom TO TRAI(Telecom Regulatory Authority Of India)]------------------------------------------------------------------]")
print("[-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]")
def subdetailInsert():
    print("Choose Option")
    print("1 - Add subscriber")
    print("2 - Update Subscriber Detail")
    def subinsert():
        A=[]
        ID=input("Enter Assigned ID:")
        A.append(ID)
        Name=input("Enter Name:")
        A.append(Name)
        Ph_No=int(input("Enter Ph_no:"))
        A.append(Ph_No)
        Com=input("Enter Network Provider Name:")
        A.append(Com)
        NetTy=input("Enter Network Type:")
        A.append(NetTy)
        Sql = "insert into subscribers_detail values(%s,%s,%s,%s,%s)"
        mycursor.execute(Sql,A)
        mycon1.commit()
        print("Successfully Added")
    def subdetailupdate():
        C=[]
        Name=input("Enter New Name No:")
        C.append(Name)
        Netpr=input("Enter New Network Provider No:")
        C.append(Netpr)
        Nety=input('Enter New Network Type:')
        C.append(Nety)           
        ID=input("Enter ID on which you have to update :")
        C.append(ID)
        Sql="update subscribers_detail set Registered_Name=%s,Service_Provider=%s,Network_Type=%s where Subs_ID=%s "
        mycursor.execute(Sql,C)
        mycon1.commit()
        print("Successfully Updated")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
       subinsert()
    elif ch==2:
       subdetailupdate()
    else : print("invalid input")    
       
def toviewdetails():
    print("Choose Option")
    print("1 - To View Basic Details of Subscribers")
    print("2 - To View IDentity Details of Subscribers")
    def viewdetails():
        print("Choose Search Criteria:")
        print("1-ID")
        print("2-Name")
        print("3-Ph_No")
        ch=int(input("Enter your choice:"))
        if (ch == 1):
            a=input("Enter Subs_ID:")
            L=[a]
            Sql="select*from subscribers_detail where Subs_Id=%s"
            mycursor.execute(Sql,L)
        elif (ch == 2):
            a=input("Enter name:")
            L=[a]
            Sql="Select*from subscribers_detail where Registered_Name=%s"
            mycursor.execute(Sql,L)
        elif (ch == 3):
            a=int(input("Enter Ph_No:"))
            L=[a]
            Sql="select*from subscribers_detail where Ph_No=%s"
            mycursor.execute(Sql,L)    
        res=mycursor.fetchall()
        print("The Subscriber Detail are as follows")
        A=[]
        for i in res:
            A.append(i)
        df=pd.DataFrame(A,columns=['Subs_Id','Registered_Name','Ph_No','Service_Provider','Network_Type'])
        print(df)
    def toviewidentitydetail():
        print("Choose Search Criteria:")
        print("1-ID")
        print("2-MCC")
        ch=int(input("Enter Your Choice:"))
        if (ch == 1):
            a=input("Enter Subs_ID:")
            L=[a]
            Sql="Select*From Subscriber_Identity_Details where Subs_ID = %s"
        
            mycursor.execute(Sql,L)
        elif (ch == 2):
            a=int(input("Enter MCC Code :"))
            L=[a]
            Sql="Select*from subscriber_identity_details where MCC = %s"
            mycursor.execute(Sql,L)
        res=mycursor.fetchall()
        print("Subscriber Identity Detials are as follows:")
        A=[]
        for i in res:
            A.append(i)
        df=pd.DataFrame(A,columns=["IMSI_No","MCC","MSIN_No","ICCID","Subs_ID"])
        print(df)
    ch=int(input("Enter your Choice:"))

    if ch==1 :
        viewdetails()
    elif ch==2:
        toviewidentitydetail()
    else : print("invalid input")    
        
        


def removesubscriber():
    a=input("Enter the ID of Subscriber to be deleted:")
    L=[a]
    Sql="Delete from subscriber_identity_details where Subs_ID =%s"
    mycursor.execute(Sql,L)
    Sql="Delete from subscribers_detail where Subs_ID=%s"
    mycursor.execute(Sql,L)
    mycon1.commit()
    print("Successfully Deleted")

def insertpdateidentitydetails():
    print("Chosse Option")
    print("1 - Add Identity Details")
    print("2 - Update Identity Details")
    def insert():
        print("Please Enter Valid Subs_ID")
        B=[]
        IMSI=int(input("Enter IMSI No:"))
        B.append(IMSI)
        MCCode=int(input("Enter MCC code:"))
        B.append(MCCode)
        MSIN=int(input("Enter MSIN No:"))
        B.append(MSIN)
        ICCI=input("Enter ICCID:")
        B.append(ICCI)
        ID=input("Enter Subs_ID (already exixt) :")
        B.append(ID)
        Sql="insert into subscriber_identity_details values(%s,%s,%s,%s,%s)"
        mycursor.execute(Sql,B)
        mycon1.commit()
        print("Successfully Added")
    def updatesubidentitydetail():
        B=[]
        IMSI=int(input("Enter New IMSI No:"))
        B.append(IMSI)
        MCCode=int(input("Enter New MCC code:"))
        B.append(MCCode)
        MSIN=int(input("Enter New MSIN No:"))
        B.append(MSIN)
        ICCI=input("Enter New ICCID:")
        B.append(ICCI)
        ID=input("Enter ID on which you have to update :")
        B.append(ID)
        Sql="update subscriber_identity_details set IMSI_No=%s,MCC=%s,MSIN_No=%s,ICCID=%s where Subs_ID=%s "
        mycursor.execute(Sql,B)
        mycon1.commit()
        print("Successfully Updated")
    ch=int(input("Enter Your Choice:"))
    if ch==1 :
        insert()
    elif ch==2:
        updatesubidentitydetail()
    else : print("Invalid input")    
        
        
def sortbasicDetails():
    print("Enter Your choice:")
    print("1 : By Name")
    print("2 : By Id")
    print("3 : By Networ Type")
    ch = int(input("Enter Your Choice:"))
    if ch==1 :
        Sql="select*from Subscribers_detail order by Registered_Name"
        mycursor.execute(Sql)
    elif ch==2:
        Sql="Select*from subscribers_detail order by Subs_ID"
        mycursor.execute(Sql)
    elif ch==3 :
        Sql="Select*from Subscribers_detail order by Network_Type"
        mycursor.execute(Sql)
    res=mycursor.fetchall()
    A=[]
    for i in res :
        A.append(i)
    df=pd.DataFrame(A,columns=['Subs_ID','Registered_name', 'Ph_No' , 'Service_Provider' , 'Network_Type'])
    print(df)
    
def sortidentityDetails():
    Sql="select*from subscriber_identity_details order by  Subs_ID"
    mycursor.execute(Sql)
    res=mycursor.fetchall()
    A=[]
    for i in res :
        A.append(i)
    df=pd.DataFrame(A,columns=['IMSI_No','MCC','MSIN_No','ICCID','Subs_ID'])    
    print(df)    
    
def frstletterofname():
    L=[]
    A=input("Enter First letter of name:")
    L.append
    Sql="select * from subscribers_detail where registered_name like '%s%%' ;" %(A,)
    mycursor.execute(Sql,L)
    res=mycursor.fetchall()
    print("")
    B=[]
    for i in res:
        B.append(i)
    df=pd.DataFrame(B,columns=['Subs_ID','Registered_name'  , 'Ph_No', 'Service_Provider' , 'Network_Type'])
    print(df)
        
def Toviewtop_bottom():
    print( "Choice:")
    print("1 : from Top ")
    print("2 : from botom")
    ch=int(input("Enter your choice:" ))
    
    if ch==1:
        A=int(input("Enter No. of Rows to Display:"))
        Sql=" select*from subscribers_detail,subscriber_identity_details"
        mycursor.execute(Sql)
        res=mycursor.fetchall()
        B=[]
        for i in res:
            B.append(i)
        df=pd.DataFrame(B,columns=['Subs_ID','Registered_name', 'Ph_No' , 'Service_Provider' , 'Network_Type','IMSI_No','MCC','MSIN_No','ICCID','Subs_ID'])
        print(df.head(A))
        
    elif ch==2:
        A=int(input("Enter No. of Rows to Display:"))
        Sql="select*from subscribers_detail,subscriber_identity_details  "
        mycursor.execute(Sql)
        res=mycursor.fetchall()
        B=[]
        for i in res :
            B.append(i)
        df=pd.DataFrame(B,columns=['Subs_ID','Registered_name', 'Ph_No' , 'Service_Provider' , 'Network_Type','IMSI_No','MCC','MSIN_No','ICCID','Subs_ID'])    
        print(df.tail(A))

        
def Alldetail():
    sql="Select*from subscribers_detail"
    mycursor.execute(sql)
    a=mycursor.fetchall()
    A=[]
    for i in a:
        A.append(i)
    df=pd.DataFrame(A,columns=['Subs_Id','Registerd_Name','Ph_No','Service_Provider','Network_Type'])
    print(df)

    
def Allidentitydetail():
    sql="Select*from subscriber_identity_details"
    mycursor.execute(sql)
    a=mycursor.fetchall()
    A=[]
    for i in a:
        A.append(i)
    df=pd.DataFrame(A,columns=['IMSI_No','MCC','MSIN_No','ICCID','Subs_ID'])
    print(df)
                 

def MainMenu():
    print("All Subscribers")
    Alldetail()
    print("-------------------------------------------------------------------------")
    print("Identiy Details")
    Allidentitydetail()
    print("---------------------------------End------------------------------------")
    print("------------------------------------------------------------------------")
    print("---------------------------------------")
    print("---------------MAIN MENU---------------")
    print("---------------------------------------")
    print("Enter 1 - To Add/Update Subscriber")
    print("Enter 2 - To Add/Update Identiy Details")
    print("Enter 3 - To View Details(Basic and Identity)")
    print("Enter 4 - To Remove Subscribers")
    print("Enter 5 - To Sort Basic Details")
    print("Enter 6 - To Sort Identity Details")
    print("Enter 7 - To View Details By First letter of Name")
    print("Enter 8 - To View Details(Top and Bottom)")
        
    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("Thats not valid input type")
    else:
        if userInput==1 :
            subdetailInsert()
        elif userInput==2:
            insertpdateidentitydetails()
        elif userInput==3:
            toviewdetails()
        elif userInput==4:
            removesubscriber()
        elif userInput==5:
            sortbasicDetails()
        elif userInput==6 :
            sortidentityDetails()
        elif userInput==7:
            frstletterofname()
        
        elif userInput==8:
            Toviewtop_bottom()
            
        else:
            print("Invalid Input")
        
def runagain():
    A=input("You want to continue Y/N :")
    while(A.lower()=='y'):
        if(pltf.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MainMenu()
        A=input("You want to continue Y/N :")
        
def passwd():
    A='mridul'
    b=100
    a=input("Enter Username:")
    
    if A==a:
        B=int(input("Enter Password:"))
        if B==b:
            MainMenu()
            while(True):
                runagain()    
        else: print("Invalid Password")    
    else : print("Invalid Username")   
                
                
        
passwd()            




        

    
    
    

