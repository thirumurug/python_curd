import mysql.connector

#connecting mysql with python .....
con = mysql.connector.connect(host="localhost", user="root", password="Thiru#2001", database="zogx")
print("Mysql and Python Connected Succussfully...!!!")

#calling .....
def calling():
    print("Select your choice what you want to do : \n")
    print("1.Insert Record")
    print("2.Update Record")
    print("3.Select Record")
    print("4.Delete Record")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        insert()
    elif choice == 2:
        update()
    elif choice == 3:
        select()
    elif choice == 4:
        delete()
    elif choice == 5:
        exit() #quit()
    else :
        print("Invalid Input  Please Select valid option")
        
#insert function ....        
def insert():
    print("Your are choosing the insert option : ")
    name = input("Enter Name : ")
    Age = int(input("Enter Age : "))
    address = input("Enter Address : ")
    phone = int(input("Enter Contact : "))
    email = input("Enter Mail : ")
    
    db1 = con.cursor()                                                          
    s='insert  into data (name,Age,address,phone,email) values(%s,%s,%s,%s,%s)'
    t=(name,Age,address,phone,email)
    db1.execute(s,t)
    con.commit()
    print("\nRecord Insert Successfully...!!!")

#update function ....  
def update():
    print("Your are choosing the update option : \n")
    print("1.Name")
    print("2.Age")
    print("3.Address")
    print("4.Contact")
    print("5.Email")
    option = int(input("\nWhich field you want to update :"))
    if option == 1:
        id = int(input("Enter Your ID:"))
        name = input("Enter Your Name:")
        db1 = con.cursor()
        sql = "UPDATE data set name=%s where id=%s"
        db1.execute(sql, (name, id))
        con.commit()
        print("Successfully name was updated...!!!")
    elif option == 2:
        id = int(input("Enter Your ID:"))
        age = input("Enter Your Age:")
        db1 = con.cursor()
        sql = "UPDATE data set age=%s where id=%s"
        db1.execute(sql, (age, id))
        con.commit()
        print("Successfully age was updated...!!!")    
    elif option == 3:
        id = int(input("Enter Your ID:"))
        address = input("Enter Your Address:")
        db1 = con.cursor()
        sql = "UPDATE data set address=%s where id=%s"
        db1.execute(sql, (address, id))
        con.commit()
        print("Successfully address was updated...!!!")
    elif option == 4:
        id = int(input("Enter Your ID:"))
        contact = input("Enter Your Contact:")
        cur = con.cursor()
        sql = "UPDATE data set contact=%s where id=%s"
        db1.execute(sql, (contact, id))
        con.commit()
        print("Successfully content was updated...!!!")
    elif option == 5:
        id = int(input("Enter Your ID:"))
        email = input("Enter Your Email:")
        db1 = con.cursor()
        sql = "UPDATE data set email=%s where id=%s"
        db1.execute(sql, (email, id))
        con.commit()
        print("Successfully email was updated...!!!")
    else:
        print("Sorry Invalid Input")

#delete function ....  
def delete():
    print("Your are choosing the Delete option : \n")
    id = input("Enter Your ID:")
    db1 = con.cursor()
    sql = "delete from data where id=%s"
    db1.execute(sql,(id))
    con.commit()
    print("Record was Deleted Successfully...!!!")

#select function ....  
def select():   
    print("Do you want fetch the full record or particular person record ?")
    print("To fetch all record use F/f as keyword\nTo fetch particular record use P/p as keyword")
    n=input("Enter the keyWord : ")
    if n == 'F' or n == 'f':
        db1 = con.cursor()
        db1.execute("select * from data")
        result=db1.fetchall()
        print("Record in the table ..........\n")
        for i in result:
            id=i[0]
            name = i[1]
            Age = i[2]
            address = i[3]
            phone = i[4]
            email = i[5]
            print(id,name,Age,address,phone,email)
            con.commit()
        print("\n")
    elif n== 'P' or n == 'p':
        id = input("Enter Your ID:")
        db1 = con.cursor()
        sql = "select * from data where id=%s"
        db1.execute(sql,(id,))
        result=db1.fetchall()
        print("Record matched for the given ID ..........\n")
        for i in result:
            id=i[0]
            name = i[1]
            Age = i[2]
            address = i[3]
            phone = i[4]
            email = i[5]
            print(id,name,Age,address,phone,email)
            con.commit()
        print("\n")
    else :
        print("Invalid Input  Please Select valid option")

#exit function .....
def exit():
    print("Are you sure Do you want to exit...")
    print("Wishes : Y/N")
    s=input("Enter you wish : ")
    if s=='Y' or s=='y':
        print("Bye")
        quit()
    elif s == 'N' or s=='n':
       calling()
    else :
        print("Invalid Input Please Select valid option")
       
while True:
    calling()