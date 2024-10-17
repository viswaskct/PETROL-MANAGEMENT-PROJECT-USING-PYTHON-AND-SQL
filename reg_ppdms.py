#One tiime registration purpose.....
#Creating the database adding tables
#Adding  ownership details, etc

#importing Required modules from library
import mysql.connector as mysql                   # for connecting python with sql
import stdiomask as mask                          # for hiding password


#intro
print(
'''
*************************************************************************************

               WELCOME TO PETROLEUM PUMP DATA SERVER
                                             
*************************************************************************************

'''
)

#Sql  connect
mydb = mysql.connect(host='localhost',
password=mask.getpass(prompt='Enter the Database Password: ',mask='*'),
user='root')
if(mydb):
        print("connection successfull")

# to avoid error of mixing a old database deleting the old to crate a new one
try:
        #creating the database
        cursor=mydb.cursor()
        cursor.execute('CREATE DATABASE ppdms;')
        mydb.commit()
except mysql.errors.DatabaseError:
        cursor=mydb.cursor()
        cursor.execute('drop database ppdms;')
        mydb.commit()
        #creating the database
        cursor=mydb.cursor()
        cursor.execute('CREATE DATABASE ppdms;')
        mydb.commit()

#opening the database
cursor=mydb.cursor()
cursor.execute('USE PPDMS;')
mydb.commit()

#creating table for employee details
print('creating table for employee details')
cursor=mydb.cursor()
cursor.execute('''CREATE TABLE emp
               ( iD char(6) UNIQUE NOT NULL,
                  NAME VARCHAR(50) NOT NULL,
                  Age integer(2) not null,
                  GEN CHAR(6) not null,
                  DOB DATE not null,
                  PH varChar (20) UNIQUE not null,
                  MAIL VARCHAR(50) UNIQUE not null,
                  acctyp varchar(10) not null);''')
mydb.commit()
print('Success...')
print()



#creating table for passwords
cursor=mydb.cursor()
cursor.execute('''create table uid
(iD char(6) UNIQUE NOT NULL,
username varchar(25) unique not null,
password varchar(25) not null,
acctyp varchar(10) not null,
Status varchar(20) not null)''')
mydb.commit()


#creating tables for stocks
print('Adding tables for stocks')
cursor=mydb.cursor()
cursor.execute('''create table stock
(iD char(6) UNIQUE NOT NULL,
name varchar(35) not null,
qty integer(10) not null,
price decimal(8,2) not null)        ''')
mydb.commit()
print('Success...')
print()


#creating tabes for bills
print('Adding tables for bills')
cursor=mydb.cursor()
cursor.execute('''CREATE TABLE bills
               ( bill_no int(20) UNIQUE NOT NULL,
                  Atnd_id CHAR(5) NOT NULL,
                  vehi_no Char(10),
                  DATE date not null,
                  Time Time not null,
                  product_code varchar(200) not null,
                  products varchar(500) not null,
                  price_unit  varchar(200) not null,
                  qty  varchar(200) not null,
                  amount varchar(200) not null,
                  net_pay decimal(10,2) not null);''')
mydb.commit()


print('Success...')
print()

#creating table for tax
print('Adding tables for Taxes')
cursor=mydb.cursor()
cursor.execute('''CREATE TABLE tax
               ( tax_typ char(15) UNIQUE NOT NULL,
                  perctage integer(2) not null );''')
mydb.commit()
print('Success...')



#userdefined function for updating reords
def adddetails(uid,name):
     cursor=mydb.cursor()
     sql='insert into uid values(%s,%s,%s,%s,%s)'
     cursor.execute(sql,uid)
     mydb.commit()
     cursor=mydb.cursor()
     sql='insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s)'
     cursor.execute(sql,name)
     mydb.commit()

def stockdb(L):
        i=0
        while i<len(L):
                sql='insert into stock values(%s,%s,%s,%s)'
                cursor=mydb.cursor()
                cursor.execute(sql,L[i])
                mydb.commit()
                i+=1
def taxdb(L):
        i=0
        while i<len(L):
                cursor=mydb.cursor()
                sql='insert into tax values(%s,%s)'
                cursor.execute(sql,L[i])
                mydb.commit()
                i+=1

 

#registration goes on....
print(
'''
*****************************************************************************
                  WELCOME TO PETROLEUM PUMP DATA SERVER
                                Registration
*****************************************************************************
Owner Details:-
~~~~~~~~~~~~~
'''
)
#gendral details
while True:
     name=input(' Name :')
     age=input(' Age :')
     sex=input(' Gender :')
     dob=input(' Date of Birth(yyyy-mm-dd) :')
     phone=input(' Phone no :')
     mail=input(' Mail id :')
     iD=name[0]+'8055'
     print('Please check the entered details... Make sure the details are correct...')
     Val2=iD,name,age,sex,dob,phone,mail,'Owner'
     print('Name:',name,'\n Age:',age,'\n Gender',sex,'\n DoB(yyyy-mm-dd):',dob,'\n Ph:',phone,'\n mail:',mail,'\n')
     ch=input('Are You Sure To Contiue? (Y/N) :')
     if ch.isalpha():
          if ch.upper() in ['Y','YES']:
               print(' Record accepted....')
               print('Processing...')
               break
          else:
               print('Enter the values again.....')

#login details
while True:
     userid=input( 'Username :')
     while True:
          password=mask.getpass(prompt=' Password :',mask='*')
          repassword=mask.getpass(prompt=' Re-Password :',mask='*')
          if password==repassword:
               break
          else:
               print('Password did not match... try again')
               pass
     Val1=iD,userid,password,'Owner','ACTIVE'
     ch=input('Are You Sure To Contiue? (Y/N) :')
     if ch.isalpha():
          if ch.upper() in ['Y','YES']:
               print(' Record accepted....')
               print('Processing...')
               break
          else:
               print('Enter the values again.....')

#updating record
adddetails(Val1,Val2)
print('Record added')
print()


#done with owner details
#Create sql table for stock management
print('creating stocks...')
print('''
******************************************************************************
                WELCOME TO PETROLEUM PUMP DATA SERVER
                                Stock
******************************************************************************
''')
list=[]
while True:
        itm_code=input('Ener the Product code:')
        itm_name=input('Product Name:')
        base_qty=int(input('Qty (ltr/bottles) :'))
        price=float(input('Enter the Price per Qty :'))
        t=(itm_code,itm_name,base_qty,price)
        list.append(t)
        ch=input('Do you want to add more ? (Y/N) :')
        if ch.upper() in ['N','NO']:
                break
#adding the records to database
stockdb(list)
print('Record added Successfully!..')
print()
print('Please wait...')



#Adding tax
print('''
******************************************************************************
                WELCOME TO PETROLEUM PUMP DATA SERVER
                                Taxes
******************************************************************************
''')
list=[]
while True:
        tax_typ=input('Ener the Tax code:')
        tax_per=int(input('Tax percentage(%) :'))
        t=(tax_typ,tax_per)
        list.append(t)
        ch=input('Do you want to add more ? (Y/N) :')
        if ch.upper() in ['N','NO']:
                break
taxdb(list)
print('Record added')
print()


#success
print('''
******************************************************************************
                WELCOME TO PETROLEUM PUMP DATA SERVER
                
                                Success
******************************************************************************

Success…

Registration Completed…

Press any key to exit….
'''
      )
input()


#closing sql
cursor.close()
mydb.close()

