#importing Required modules from library
import os                                              # for printer hard copies 
import mysql.connector as mysql                        # for connecting python with sql
import stdiomask as mask                               # for hiding password
import datetime                                        # for date and time
from prettytable import PrettyTable                    # for tables
import matplotlib.pyplot as plt                        # for graphs 
from random import randint as rint                     # for id generation
from datetime import timedelta                         # helps with selecting range of dates



#connecting python and sql using mysql.connector
try :
     print('''
*************************************************************************************
                 WELCOME TO PETROLEUM PUMP DATA SERVER
*************************************************************************************
''')
     mydb = mysql.connect(host='localhost',
     password=mask.getpass(prompt='Enter the Database Password: ',mask='*'),
     user='root',
     database="ppdms")
except mysql.Error:                                  #error message if program registration not done
     print(

'''
*************************************************************************************
            WELCOME TO PETROLEUM PUMP DATA SERVER
                         Error
*************************************************************************************
     Error:  Registration Not Done, Register before you use….
     (Open reg_ppdms.py to Register)
     Exiting….
'''
)
     input('\t Press Any Key To Exit…')
     exit()






#User defined funtion goes here

def _credits():                                                  #Developers
     print('''
***************************************************************************************
                         Alagar Public School
---------------------------------------------------------------------------------------

     Name: DHAKSHIN A.V.   (Mail: avdhakshin1354@gmail.com)
     Name: Paul Samuel D
     Name: Viswa M
'''
           )
     input('Enter any Key to move back to menu...')
     return
     



def _admins():                                                   # Admin contacts for workers
     sql='Select Name,ph,mail from emp where acctyp=\'Owner\' or acctyp=\'Admin\''
     cursor=mydb.cursor()
     cursor.execute(sql)
     data=cursor.fetchall()
     print(
'''
*************************************************************************************

               WELCOME TO PETROLEUM PUMP DATA SERVER
                         Contact Admin
*************************************************************************************

'''
)
     table=PrettyTable (['Name','Phone','Mail'])
     for i in data:
          table.add_row([str(i[0]),str(i[1]),str(i[2])])
     print(table)
     input('Enter any key to be back to menu...')
     return
     

     

def accid(uid):                                                  #acc_id getting
     sql='select iD from uid where username=%s'
     cursor=mydb.cursor()
     cursor.execute(sql,(uid,))
     data=cursor.fetchall()
     acc_id=data[0][0]
     return acc_id


def choicenum(ch):                                               #Avoid error in selecting choice....
     if ch.isdigit():
          ch=int(ch)
          return ch,False
     else:
          print('Enter a valid Choice...')
          return ch,True




def Admlogverify(uid,pas):                                       # verify the login
          sql='Select password from uid where username= %s and (acctyp=\'Owner\' or acctyp=\'Admin\') and status=\'ACTIVE\''
          cursor=mydb.cursor()
          cursor.execute(sql,(uid,))
          data=cursor.fetchall()
          if data==[]:
               print('Invalid Username or Username not found')
               return False
          elif data[0][0]==pas:
               return True
          else:
               print('Invalid Password')
               return False


def Adminlog():                                                    #admin login
     print('''
*********************************************************************************
                WELCOME TO PETROLEUM PUMP DATA SERVER
                            Admin Login
*********************************************************************************
'''
           )
     i=4
     while i>0:
          admuserid=input('Enter the Username:')
          admpass=mask.getpass(prompt='Enter the Password:',mask='*')
          print('Verifying…. \n Please Wait....')
          if Admlogverify(admuserid,admpass):
               print('```````````````````````````````')
               print('Verified... (loading Admin Home)')
               global acc_id
               acc_id=accid(admuserid)
               Admhome()
          else:
                print()
                i-=1
                print('Chance left:', i)
     print('Chances Exhasted... try Later...')
     Home()
     
     
def Checkemp():                                                       # if no employee created..
          sql='Select iD from uid where acctyp=\'Worker\' and status=\'ACTIVE\''
          cursor=mydb.cursor()
          cursor.execute(sql)
          data=cursor.fetchall()
          if data!=[]:
               return

          else:
               print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              Employee Login
*************************************************************************************
At least add one Worker to Login… (Redirecting to Home…)
'''
                )
               Home()



          
def Emplogverify(empuserid,emppass):                                  # verify the login
          sql='Select password from uid where username=%s and status=\'ACTIVE\''
          cursor=mydb.cursor()
          cursor.execute(sql,(empuserid,))
          data=cursor.fetchall()
          if data==[]:
               print('Invalid Username or Username not found')
               return False
          elif data[0][0]==emppass:
               return True
          else:
               print('Invalid Password')
               return False




def Emplogin():                                                       #worker Login
     Checkemp()
     print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                               Employee Login
*************************************************************************************
'''
           )
     i=4
     while i>0:
          empuserid=input('Enter the Username:')
          emppass=mask.getpass(prompt='Enter the Password:',mask='*')
          print('Verifying…. \n Please Wait....')
          if Emplogverify(empuserid,emppass):
               print('```````````````````````````````')
               print('Verified... (loading Worker Home)')
               global acc_id
               acc_id=accid(empuserid)
               Emphome()
          else:
                print()
                i-=1
                print('Chance left:', i)
     print('Chances Exhasted... try Later...')
     Home()


def checkiD(iD):                                            #avoid repetation
          sql='select iD from emp where iD= %s'
          cursor=mydb.cursor()
          cursor.execute(sql,(iD,))
          data=cursor.fetchall()
          if data==[]:
               return False
          else:
               return True
     

def iDgen(n):                                               #generate iD
     true=True
     while true:
          num1=rint(1,4)
          num2=rint(250,999)
          num=str(num1*num2)
          iD=n[0]+num
          print(iD)
          true=checkiD(iD)
     return iD
     

def upemprecords(uid,name):                                  # Add noob records to database
     cursor=mydb.cursor()
     sql='insert into uid values(%s,%s,%s,%s,%s)'
     cursor.execute(sql,uid)
     mydb.commit()
     cursor=mydb.cursor()
     sql='insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s)'
     cursor.execute(sql,name)
     mydb.commit()


def Noobs():                                                            # New Registration
     
     print(
'''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                             Employee Registration
*************************************************************************************

'''
           )
     #gendral details
     while True:
          name=input(' Name:')
          iD=iDgen(name)
          age=input(' Age:')
          sex=input(' Gender:')
          dob=input(' Date of Birth(yyyy-mm-dd) :')
          phone=input(' Phone no:')
          mail=input(' Mail id:')
          acctype=input('(Admin/Worker) ? :')
          print('Please check the entered details... Make sure the details are correct')
          name=(iD,name,age,sex,dob,phone,mail,acctype)
          print('Name:',name,'\n Age:',age,'\n Gender',sex,'\n DoB(yyyy-mm-dd):',dob,'\n Ph:',phone,'\n mail:',mail,'\n',acctype,'\n')
          ch=input('Are You Sure To Contiue? (Y/N)')
          if ch.isalpha():
               if ch.upper() in ['Y','YES']:
                    print(' Record accepted....')
                    print('Processing')
                    break
               else:
                    print('Enter the values again.....')

     #login details
     while True:
          userid=input( 'Username:')
          while True:
               password=mask.getpass(prompt=' Password:',mask='*')
               repassword=mask.getpass(prompt=' Re-Password:',mask='*')
               if password==repassword:
                    break
               else:
                    pass
          uid=iD,userid,password,acctype,'INACTIVE'
          ch=input('Are You Sure To Contiue? (Y/N)')
          if ch.isalpha():
               if ch.upper() in ['Y','Yes']:
                    print(' Record accepted....')
                    print('Processing')
                    break
               else:
                    print('Enter the values again.....')
     print()
     print('Wait please Uploading records')
     upemprecords(uid,name)
     print()
     print('Reacord added')
     print('''
Success… 
Wait Until You Get Approval from Admin…
Press any key to continue… 
''')
     input()
     print('(Redirecting to home…)')
     Home()


def allprod():
          sql='select * from stock'
          cursor=mydb.cursor()
          cursor.execute(sql)
          data=cursor.fetchall()
          print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              All stock Records
***********************************************************************************
''')
          table=PrettyTable (['Product_code','Prduct_name','Qty_Avail(Ltr/bottles)','Price_per_unit'])
          for i in data:
               table.add_row([i[0],i[1],i[2],i[3]])
          print(table)
          input('Enter any key to back to menu...')
          return
               
     

     
def Qtyedit():
          print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              Update stock Records
***********************************************************************************
''')
          iD=input('Enter the product code:')
          print('Note: use -ve sign if you remove some qty of stock')
          Qty=int(input('Enter the new stock:'))
          sql='select qty from stock where iD= %s'
          cursor=mydb.cursor()
          cursor.execute(sql,(iD,))
          data=cursor.fetchall()
          qty=data[0][0]
          Qty+=qty
          sql='update stock set qty= %s where iD= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(Qty,iD))
          mydb.commit()
          print('Edited successfully...')
          input('Enter any key to back to menu...')
          return
               


def stockdb(L):
    i=0
    while i<len(L):
       cursor=mydb.cursor()
       sql='insert into stock values(%s,%s,%s,%s)'
       cursor.execute(sql,L[i])
       mydb.commit()
       i+=1


def newprod():
     print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              New stock Records
***********************************************************************************
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
     input('Enter any key to back to menu...')
     return


def dropprod():
     print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              Drop stock Records
***********************************************************************************
''')
     iD=input('Enter the Product iD:')
     print('Are you sure to Delete the Product :',iD,end='')
     ch=input('? (Y/N):')
     if ch.upper() in ['Y','YES']:
          sql='delete from stock where iD= %s'
          cur=mydb.cursor()
          cur.execute(sql,(iD,))
          mydb.commit()
          print('Successfully deleted...')
          input('Enter any key to back to menu...')
          return
     else:
          ch=input('Do you to be back to menu ? (Y/N):')
          if ch.upper() in ['Y','YES']:
               input('Enter any key to back to menu...')
               return
          else:
               dropprod()




def newrate():
          print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              Update stock Records
***********************************************************************************
''')
          iD=input('Enter the product code:')
          p=float(input('Enter the new Price:'))
          sql='update stock set price= %s where iD= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(p,iD))
          mydb.commit()
          print('Edited successfully...')
          input('Enter any key to back to menu...')
          return
     





def Stock():
     print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                                Manage Stocks
*************************************************************************************
     1.	Show the all Product
     2. Update new Price
     3.	Edit Qty of  Product 
     4.	Add  a  new  Product
     5.	Remove  a    Product
     6.	Back To Menu
''')  
     true=True
     while true:                                                           #choice selection
          choice=input('Enter your choice (1-6):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>6 or choice<1):
                    print('Enter the choice between (1-6)')
                    true=True
               else:
                    true=False
     #Choice execution
     if choice==1:
          allprod()
          Admhome()
     elif choice==2:
          newrate()
          Admhome()
     elif choice==3:
          Qtyedit()
          Admhome()
     elif choice==4:
          newprod()
          Admhome()
     elif choice==5:
          dropprod()
     elif choice==6:
          Admhome()


def alltax():
          sql='select * from tax'
          cursor=mydb.cursor()
          cursor.execute(sql)
          data=cursor.fetchall()
          print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              All TAX Records
***********************************************************************************
''')
          table=PrettyTable (['Tax_code','Percentage%'])
          for i in data:
               table.add_row([i[0],i[1]])
          print(table)
          input('Enter any key to back to menu...')
          return
     

def taxedit():
          print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              Update Tax Records
***********************************************************************************
''')
          iD=input('Enter the tax_code:')
          Qty=input('Enter the tax_percentage:')
          sql='update tax set perctage= %s where tax_typ= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(Qty,iD))
          mydb.commit()
          print('Edited successfully...')
          input('Enter any key to back to menu...')
          return


def taxdb(L):
        i=0
        while i<len(L):
                cursor=mydb.cursor()
                sql='insert into tax values(%s,%s)'
                cursor.execute(sql,L[i])
                mydb.commit()
                i+=1



def newtax():
          print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              New Tax Records
***********************************************************************************
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
          input('Enter any key to back to menu...')
          return



def droptax():
     iD=input('Enter the Tax iD:')
     print('Are you sure to Delete the Tax :',iD,end='')
     ch=input('? (Y/N):')
     if ch.upper() in ['Y','YES']:
          sql='delete from tax where tax_typ=%s'
          cur=mydb.cursor()
          cur.execute(sql,(iD,))
          mydb.commit()
          print('Successfully deleted...')
          input('Enter any key to back to menu...')
          return
     else:
          ch=input('Do you to be back to menu ? (Y/N):')
          if ch.upper() in ['Y','YES']:
               input('Enter any key to back to menu...')
               return
          else:
               droptax()
 


def Taxes():
     print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                                Manage Taxes
*************************************************************************************
     1.	Show the Tax 
     2.	Edit Tax (%)
     3.	Add  new Tax
     4.	Remove a Tax
     5.	Back To Main Menu
'''  ) 
     true=True
     while true:                                                                #choice selection
          choice=input('Enter your choice (1-5):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>5 or choice<1):
                    print('Enter the choice between (1-5)')
                    true=True
               else:
                    true=False
     #Choice execution
     if choice==1:
          alltax()
          Admhome()
     elif choice==2:
          taxedit()
          Admhome()
     elif choice==3:
          newtax()
          Admhome()
     elif choice==4:
          droptax()
          Admhome()
     elif choice==5:
          Admhome()



def allemp():
          sql='select * from emp'
          cursor=mydb.cursor()
          cursor.execute(sql)
          data=cursor.fetchall()
          print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                            All Employee Records
***********************************************************************************
''')
          table=PrettyTable (['iD','Name','Age','Gen','DOB','Phone','Mail','acctype'])
          for i in data:
               table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
          print(table)
          input('Enter any key to back to menu...')
          return
               


def Age_1():
          iD=input('Enter the iD:')
          sql='select Age from emp where iD= %s'
          cursor=mydb.cursor()
          cursor.execute(sql,(iD,))
          data=cursor.fetchall()
          age=data[0][0]
          age+=1
          sql='update emp set Age= %s where iD= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(age,iD))
          mydb.commit()
          print('Edited successfully...')
          input('Enter any key to back to menu...')
          return


def Phone():
          iD=input('Enter the iD:')
          Ph=int(input('Enter The New Phone No.:'))
          sql='update emp set PH= %s where iD= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(Ph,iD))
          mydb.commit()
          print('Edited successfully...')
          input('Enter any key to back to menu...')
          return

def Mail():
          iD=input('Enter the iD:')
          mail=input('Enter The New Mail iD.:')
          sql='update emp set MAIL=%s where iD= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(mail,iD))
          mydb.commit()
          print('Edited successfully...')
          input('Enter any key to back to menu...')
          return


def empedit():
     print('''
***********************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                           Update Employee Records
***********************************************************************************
     1. Age (+1)
     2. Phone
     3. Mail iD
     4. Back to menu
     
''')
     true=True
     while true:                                                                 #choice selection
          choice=input('Enter your choice (1-4):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>4 or choice<1):
                    print('Enter the choice between (1-4)')
                    true=True
               else:
                    true=False

     #Choice execution
     if choice==1:
          Age_1()
          empedit()
     elif choice==2:
          Phone()
          empedit()
     elif choice==3:
          Mail()
          empedit()
     elif choice==4:
          return

     

def approveemp():
          iD=input('Enter the iD to approve:')
          sql='update uid set Status= \'ACTIVE\' where iD= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(iD,))
          mydb.commit()
          print('Edited successfully...')
          input('Enter any key to back to menu...')
          return



def ownerverify2(uid,pas):                                              # verify the login
          sql='Select password from uid where username= %s and acctyp=\'Owner\''
          cursor=mydb.cursor()
          cursor.execute(sql,(uid,))
          data=cursor.fetchall()
          if data==[]:
               print('Invalid Username or Username not found')
               return False
          elif data[0][0]==pas:
               return True
          else:
               print('Invalid Password')
               return False


def ownerverify1():
     i=4
     while i>0:
          admuserid=input('Enter your Username:')
          admpass=mask.getpass(prompt='Enter your Password:',mask='*')
          print('Verifying…. \n Please Wait....')
          if ownerverify2(admuserid,admpass):
               print('```````````````````````````````')
               print('Verified...')
               return True
          else:
                print()
                i-=1
                print('Chance left:', i)
     print('Chances Exhasted...')
     return False


def owner(iD):
          sql='Select acctyp from emp where iD= %s;'
          cursor=mydb.cursor()
          cursor.execute(sql,(iD,))
          data=cursor.fetchall()
          if data[0][0]=='Owner':
               print('You cannot delete owner')
               return True
          else:
               return False
          

def fireemp():
          print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                                Fire Employee
*************************************************************************************
''')
          iD=input('Enter the iD to be Deleted:')
          sql='select iD from emp where iD=%s'
          cursor=mydb.cursor()
          cursor.execute(sql,(iD,))
          data=cursor.fetchall()
          if data==[]:
               print('iD Not Found...')
               input('Enter any key to be back to menu...')
               return
          if owner(iD):
               return
          ch=input('Are you sure to Delete:(Y/N):')
          if ch.upper() in ['N','NO']:
               return

          print('verify you Before Deleting')
          true=ownerverify1()
          if true:
               sql='delete from emp where iD=%s '
               cursor=mydb.cursor()
               cursor.execute(sql,(iD,))
               mydb.commit()
               sql='delete from uid where iD=%s '
               cursor=mydb.cursor()
               cursor.execute(sql,(iD,))
               mydb.commit()
               print('Deleted successfully...')
               input('Enter any key to back to menu...')
               return
          else:
               print('To many wrong attemps...')
               print('Record Not Deleted')
               input('Enter any key to back to menu...')
               return




def Empmanage():
     print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              Manage Employee
*************************************************************************************
     
     1.	Show Employee Details
     2.	Edit Employee Details
     3.	Approve New Employee
     4.	Remove Employee(Requires owner Authorization)
     5.	Back To Main Menu
''')
     true=True
     while true:                                                                #choice selection
          choice=input('Enter your choice (1-5):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>5 or choice<1):
                    print('Enter the choice between (1-5)')
                    true=True
               else:
                    true=False
     #Choice execution
     if choice==1:
          allemp()
          Admhome()
     elif choice==2:
          empedit()
          Admhome()
     elif choice==3:
          approveemp()
          Admhome()
     elif choice==4:
          fireemp()
          Admhome()
     elif choice==5:
          Admhome()


#bills

def Printbill(P1,t,P3,tax,Print4):
     location=os.path.dirname(__file__)
     location+=r"\Printer.txt"
     with open(location,'w')as P :
          for i in P1:
               P.write(str(i))
          P.write(str(t))
          for i in P3:
               P.write(str(i))
          for i in tax:
               P.write(str(i))
          for i in Print4:
               P.write(str(i))
     os.startfile(location, "print")
     input('Enter any key to be back to menu...')
     return



def showbill(billno):
          sql='select * from bills where bill_no=%s'
          cursor=mydb.cursor()
          cursor.execute(sql,(billno,))
          data=cursor.fetchall()
          if data==[]:
               print('Bill Not Found...')
               input('Enter any key to be back to menu...')
               return
          sql='select * from tax'
          cursor=mydb.cursor()
          cursor.execute(sql)
          data2=cursor.fetchall()
          Print1=('''
***************************************************
                PETROLEUM PUMP
***************************************************
''','Date:',data[0][3],'\t'*3,'Time:',data[0][4],'\n',
'Bill No.:',data[0][0],'\t'*3,'Atend_iD:',data[0][1],'\n',
'Vehic No:',data[0][2],'\n',
'---------------------------------------------------\n')
          Print3=('''
---------------------------------------------------
Items:''','\t',len(list(data[0][5].replace("[","").replace("]","").split(","))),'\t','included Taxs:','\n','\t'*4,)
          Print4=('\n','NET_PAY::',data[0][10],'''
--------------------------------------------------
               Thank You!
              Visit Again!
''')
          table=[]
          table=PrettyTable (['Itm_code','Item','Qty','Price/unit','Amount'])
          t=[]
          t.append(data[0][5].replace("[","").replace("]","").split(","))
          t.append(data[0][6].replace("[","").replace("]","").split(","))
          t.append(data[0][8].replace("[","").replace("]","").split(","))
          t.append(data[0][7].replace("[","").replace("]","").split(","))
          t.append(data[0][9].replace("[","").replace("]","").split(","))
          for i in range(len(t[0])):
               add=[]
               for j in range(len(t)):
                    add.append(t[j][i])
               table.add_row(add)
          Print=''
          for i in Print1:
               print(i,end='')
          print(table)
          for i in Print3:
               print(i,end='')
          tax=''
          for i in data2:
               tax+=i[0]+':'
               tax+=str(i[1])+'%'+'\n'
          print(tax)
          for i in Print4:
               print(i,end='')
          print('\n Do you what to print this? (Y/N):',end='')
          ch=input()
          if ch.upper() in ['N','NO']:
               input('Enter any key to be back to menu...')
               return
          else:
               print('Preparing to print please wait....')
               Printbill(Print1,table,Print3,tax,Print4)
          
     


def Searchbill():
     print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                                Search Bill
*************************************************************************************
''')
     billno=input('Enter the Billno. to Search:')
     showbill(billno)
     return





def recordbill(tup):
     sql='insert into bills values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
     cursor=mydb.cursor()
     cursor.execute(sql,tup)
     mydb.commit()
     print('Record Recored')

def updateqty(iD,qty):
     i=0
     while i<len(iD):
          sql='select qty from stock where iD= %s'
          cursor=mydb.cursor()
          cursor.execute(sql,(iD[i],))
          data=cursor.fetchall()
          QTY=int(data[0][0])
          QTY=QTY-int(qty[i])
          sql='update stock set qty= %s where iD= %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(QTY,iD[i]))
          mydb.commit()
          i+=1

def checkqty(qty,iD):
     sql='select qty from stock where iD= %s'
     cursor=mydb.cursor()
     cursor.execute(sql,(iD,))
     data=cursor.fetchall()
     QTY=int(data[0][0])
     QTY=QTY-int(qty)
     if QTY>0:
          print('Stock available')
          return True
     else:
          print('Stock not available ...')
          print('Enter again...')
          return False
          


def itmname(itm_code):
     sql='select name,price from stock where iD= %s'
     cursor=mydb.cursor()
     cursor.execute(sql,(itm_code,))
     data=cursor.fetchall()
     return data[0][0],float(data[0][1])
     

def billno():
     sql='select max(bill_no) from bills'
     cursor=mydb.cursor()
     cursor.execute(sql)
     data=cursor.fetchall()
     if data[0][0]==None:
          return 1
     else:
          data=int(data[0][0])
          data=data+1
          return data

def Newbill():
     product_code=[]
     products=[]
     price_unit=[]
     qty=[]
     price=[]
     net_pay=0
     bill_no=str(billno())
     Atnd_id=acc_id
     Date=datetime.date.today()
     dt= datetime.datetime.now()
     Time= dt.strftime("%H:%M:%S")
     Vehi_no=input('Vehicle Reg. No.:' )
     if Vehi_no=='':
          Vehi_no='Not Entered'
     while True:
          itm_code=input('Enter the product code:')
          itm_name,ppu=itmname(itm_code)
          print('Enter Qty / Price ')
          while True:
               Qty=input('Enter the Qty:')
               Price=input('Enter the Price:')
               if (Qty=='' and Price=='') :
                    print('Enter Any one')
                    continue
               elif (Qty!='' and Price==''):
                    print('processing price')
                    Price=int(Qty)*ppu
                    Price=round(Price,2)
               else:
                    print('If you entered both Quantity ignored')
                    print('Processing Qty...')
                    Qty=int(Price)/ppu
                    Qty=round(Qty,2)
               if checkqty(Qty,itm_code):
                    break
          product_code.append(itm_code)
          products.append(itm_name)
          price_unit.append(ppu)
          qty.append(Qty)
          price.append(Price)
          net_pay+=int(Price)
          ch=input('Do You want To Add more? (Y/N)')
          if ch.isalpha():
               if ch.upper() in ['N','NO']:
                    print(' Record accepted....')
                    print('Processing')
                    break
               else:
                    print('Record acceptd')
     tup=bill_no,Atnd_id,Vehi_no,Date,Time,str(product_code),str(products),str(price_unit),str(qty),str(price),net_pay
     updateqty(product_code,qty)
     print('Stock Updated...')
     recordbill(tup)
     print('Bill Uploded....')
     showbill(bill_no)
     return
     
     


def Showallbills():
          sql='select * from bills'
          cursor=mydb.cursor()
          cursor.execute(sql)
          data=cursor.fetchall()
          print('''
**********************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                              All Bill Records
**********************************************************************************************
''')
          table=PrettyTable (['Bill_No','Atnd_id','vehi_no','Date','Time','Product_code','Net_Pay'])
          for i in data:
               table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[10]])
          print(table)
          input('Enter any key to be back to menu...')
          return
               


def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])




def AddMonths(d,x):
    newmonth = ((( d.month - 1) + x ) % 12 ) + 1
    newyear  = int(d.year + ((( d.month - 1) + x ) / 12 ))
    return datetime.date( newyear, newmonth, d.day)



def earngraph():
     f1 = {'family':'Comic Sans MS','color':'Blue','size':16}
     f2 = {'family':'Comic Sans MS','color':'black','size':12}
     x=[]
     y=[]
     print('End date(autometic) (+ a year of start date)')
     print('default day = 1')
     day=1
     month=int(input('Month:'))
     year=int(input('Year:'))
     sd=datetime.date(year,month,day)
     sd1=datetime.date(year,month,day)
     for i in range(12):
          x.append(sd.strftime("%b"))
          sd1=AddMonths(sd,1)
          sql='select sum(net_pay) from bills where DATE BETWEEN %s AND %s '
          cursor=mydb.cursor()
          cursor.execute(sql,(sd,sd1))
          data=cursor.fetchone()
          y.append(data)
          sd=AddMonths(sd,1)
     net=0
     i=[]
     for j in y:
          j=list(j)
          if j[0]==None:
               j[0]=0
          i.append(j[0])
     net=sum(i)
     net=str(net)
     net='Net_Earn = '+ net
     plt.title(net,fontdict = f1)
     plt.xlabel("Month",fontdict = f2)
     plt.ylabel("Earnings",fontdict = f2)
     plt.bar(x,i,width = 0.5)
     addlabels(x, i)
     print('Close the graph to be back to menu...')
     plt.show()




def populargraph():
     f1 = {'family':'Comic Sans MS','color':'black','size':14}
     x=[]
     y=[]
     print('End Value of date is Max of one month(30 days)(autometic)')
     print('Enter as integer value...')
     day=int(input('Day:'))
     month=int(input('Month:'))
     year=int(input('Year:'))
     sd=datetime.date(year,month,day)
     for i in range(30):
          x.append(sd)
          sql='select * from bills where DATE=%s'
          cursor=mydb.cursor()
          cursor.execute(sql,(sd,))
          sd+=timedelta(days=1)
          d=cursor.fetchall()
          data=len(d)
          y.append(data)
     plt.plot(x,y,marker = 'o')
     plt.xlabel("Day",fontdict = f1)
     plt.ylabel("No.of custmers",fontdict = f1)
     print('Close the graph to be back to menu...')
     plt.show()
     return




     
def Bill():
     print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                                Manage Bills
*************************************************************************************
     
     1.	Show all Bill Records 
     2.	Search For Bill Record
     3.	Find the Net. Earning per month (for year)
     4. Coust. per day as Bill Records (for month)
     5.	Back To the Main Menu
''')
     true=True
     while true:                                                                #choice selection
          choice=input('Enter your choice (1-5):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>5 or choice<1):
                    print('Enter the choice between (1-5)')
                    true=True
               else:
                    true=False
     #Choice execution
     if choice==1:
          Showallbills()
          Admhome()
     elif choice==2:
          Searchbill()
          Admhome()
     elif choice==3:
          earngraph()
          Admhome()
     elif choice==4:
          populargraph()
          Admhome()
     elif choice==5:
          Admhome()
     


def Admhome():                                                        # Admin Home
     print('''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                                Admin Home
*************************************************************************************
Logined as:''',accid ,'''
     1.	New Bill
     2.	Manage Stock 
     3.	Manage Taxes
     4.	Manage Employee
     5.	Manage Bill Register
     6.	Contact Developer
     7.	Home

'''
           )
     true=True
     while true:                                                                #choice selection
          choice=input('Enter your choice (1-7):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>7 or choice<1):
                    print('Enter the choice between (1-7)')
                    true=True
               else:
                    true=False
     #Choice execution
     if choice==1:
          Newbill()
          Admhome()
     elif choice==2:
          Stock()
          Admhome()
     elif choice==3:
          Taxes()
          Admhome()
     elif choice==4:
          Empmanage()
          Admhome()
     elif choice==5:
          Bill()
          Admhome()
     elif choice==6:
          _credits()
          Admhome()
     elif choice==7:
          Home()
          Admhome()


           
def Emphome():                                                             #Employee Home
     print(
'''
*************************************************************************************
                    WELCOME TO PETROLEUM PUMP DATA SERVER
                               Employee Home
*************************************************************************************
Logined as:''',accid ,'''
     1.	New Bill 
     2.	Show the Product list 
     3.	Show all Bill Records
     4.	Search For Bill Record
     5.	Contact Admin
     6.	Home


''')
     true=True
     while true:                                                                #choice selection
          choice=input('Enter your choice (1-6):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>6 or choice<1):
                    print('Enter the choice between (1-6)')
                    true=True
               else:
                    true=False
     #Choice execution
     if choice==1:
          Newbill()
          Emphome()
     elif choice==2:
          allprod()
          Emphome()
     elif choice==3:
          Showallbills()
          Emphome()
     elif choice==4:
          Searchbill()
          Emphome()
     elif choice==5:
          _admins()
          Emphome()
     elif choice==6:
          Home()
               


def Home():
     #A drop down list!!!
     print('''
*************************************************************************************
               WELCOME TO PETROLEUM PUMP DATA SERVER
                            Home
*************************************************************************************

     1. Login as Admin
     2.Login as Worker
     3.Employee Register 
     4.Exit
'''
           )
     true=True
     while true:                                                                 #choice selection
          choice=input('Enter your choice (1-4):')
          choice,true=choicenum(choice)
          if true==False:
               if (choice>4 or choice<1):
                    print('Enter the choice between (1-4)')
                    true=True
               else:
                    true=False

     #Choice execution
     if choice==1:
          Adminlog()
     elif choice==2:
          Emplogin()
     elif choice==3:
          Noobs()
     elif choice==4:
          exit()

#main funtion call Statement
Home()
