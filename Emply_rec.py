import mysql.connector
l=mysql.connector.connect(
     host="localhost",
     user="root",
     password="anus123",
     database="demo"
)     
#c=l.cursor()
#c.execute("create table emplyrec(name varchar(50) primary key not null,age int,salary int)")#
#l.commit()
#c.close()
def list_emp():
    l = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anus123",
        database="demo"
)   
c = l.cursor()
c.execute("select * from emplyrec")
rows=c.fetchall()
print("Name         Age     Salary")
for rows in rows:
    for col in rows:
        print(col,end='       ')
    print()
c.close()
def add_emp(nm,ag,sal):
    l = mysql.connector.connect(
      host="localhost",
        user="root",
        password="anus123",
        database="demo"
)  
    c=l.cursor()
    s="insert into emplyrec(name,age,salary)values (%s,%s,%s)"
    val=[(nm,ag,sal)] 
    c.executemany(s,val)
    l.commit()
    l.close()
def edit_emp(n,n_n,n_a,n_s):
    l = mysql.connector.connect(
      host="localhost",
        user="root",
        password="anus123",
        database="demo"
)  
    c=l.cursor()
    s=("update emplyrec set name=%s,age=%s,salary=%s where name=%s")
    val=[(n_n,n_a,n_s,n)]
    c.executemany(s,val)
    l.commit()
    l.close()
def del_emp(n):
    l = mysql.connector.connect(
      host="localhost",
        user="root",
        password="anus123",
        database="demo"
)  
    c=l.cursor()
    s=("delete from emplyrec where name=%s")
    val=[(n,)]
    c.executemany(s,val)
    l.commit()
    l.close()
ch=1
while(ch<5):
 print("\n1.List\n2.Add\n3.Edit\n4.Delete\n5.Exit\n")
 ch=int(input("Please select your input:  "))
 if ch==1:
    print("\nThe list of Employees")
 elif ch==2:
    nm=input("Enter the name:")
    ag=int(input("Enter the age:"))
    sal=int(input("Enter the salary:")) 
    add_emp(nm,ag,sal)
    print("\nEmployee Details Added Sucessfully.....!")
 elif ch==3:
     n= input("Enter the name of the Employee to be edited:")
     n_n=input("Enter the new name:")
     n_a=input("Enter the age:  ")
     n_s=input("Enter the new salary:  ") 
     edit_emp(n,n_n,n_a,n_s)
     print("\nEmployee Details Editted sucessfully....!") 
 elif ch==4:
   n = input("Enter the name of the employee to be deleted: ")
   del_emp(n) 
   print("\nEmployee Details Deleted Sucessfully....!")
 else:
    if ch==5:
         continue
    print("\nInvalid")        





