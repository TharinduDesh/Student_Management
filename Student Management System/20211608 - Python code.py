import os
import sys
import mysql.connector

# Define variables
option=0



#Menu For The Student Management System

def menu():
	
# Open database connetion
    conDict={'host':"localhost",
         'database':'student',
         'user':"root",
         'password':""}
    global db
    db=mysql.connector.connect(**conDict)
# Print Menu for the user

    print("|======== Welcome To Student Management System ========|")
    print("\nOption 1 : To View Student's List \nOption 2 : To view Attendance List \nOption 3 : To Add New Student detail  \nOption 4 : To Delete student detail \nOption 5 : To Update student detail \nOption 6 : To mark attendance\nOption 7 : To view selected student attendance")
    userInput=int(input("\nPlease Select An Above Option: "))
    while userInput<1 or userInput>7:
        print("\n Incorrect option number") #Error Message
        userInput = int(input("Please Select An Above Option: "))


    # ---------- Option 01 ---------- #

    if userInput==1:
        print("\nList of students : ")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM student")
        data=cursor.fetchall()
        for item in data:
            print(item)
        db.close()

        again=input("\nYou want to go back to menu? (Y/N) : ")
        if again=="Y" or "y":
            menu()
        else:
            exit()

    # ---------- Option 02 ---------- #
    if userInput==2:
        print("\nList of attend students : ")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM student_attend")
        data=cursor.fetchall()
        for item in data:
            print(item)
        db.close()

        again=input("\nYou want to go back to menu? (Y/N) : ")
        if again=="Y" or "y":
            menu()
        else:
            exit()


    # ---------- Option 03 ---------- #

    # Open database connetion
    if userInput==3:
            print("\nPlease enter following details")
            cursor=db.cursor()
            # Read user input
            stNo = int(input("\nType student Number: "))
            fName = input("Type first name : " )
            lName = input("type last name : ")
            dob = input("type date of birth : ")
            telephoneNo = int(input("Type telephone number: " ))

            # Execute SQL Query using execute() method
            mySQLText= "INSERT INTO student(stNo,fName,lName,dob,telephoneNo) VALUES (%s,%s,%s,%s,%s)"
            myValues=(stNo,fName,lName,dob,telephoneNo)
            cursor.execute(mySQLText, myValues)
            # Commit the change
            db.commit()
            print("\nStudent information Added")
            db.close()
            again=input("\nYou want to go back to menu? (Y/N) : ")
            if again=="Y" or "y":
                menu()
            else:
                exit()
            
    # ---------- Option 04 ---------- #
    # Open database connetion
    if userInput==4:
            print("\nPlease enter following details")
            cursor=db.cursor()
            stNo=input("\nEnter the student number to be removed :")
            # Execute SQL Query using execute() method
            cursor.execute("DELETE FROM student WHERE stNo="+ stNo +"")
            # Commit the change
            db.commit()
            print(cursor.rowcount,"Student information Deleted")        
            db.close()
            again=input("\nYou want to go back to menu? (Y/N) : ")
            if again=="Y" or "y":
                menu()
            else:
                exit()

    # ---------- Option 05 ---------- #
    # Open database connetion
    if userInput==5:
            global option
            option=input("\nWhich part you want to update? (stNo,fName,lName,dob,telephoneNo) : ")
    if option=="stNo":
            cursor=db.cursor()
            stNo=input("Type student number: ")
            newstNo=input("Enter new student number: ")
            updTxt="UPDATE student SET stNo='" + newstNo + "'WHERE stNo=" + stNo
            cursor.execute(updTxt)
            db.commit()
            print(cursor.rowcount,"Student number Updated")
            db.close()
    elif option=="fName":
            cursor=db.cursor()
            stNo=input("Type student number: ")
            fName=input("Enter student first name: ")
            updTxt="UPDATE student SET fName='" + fName + "'WHERE stNo=" + stNo
            cursor.execute(updTxt)
            db.commit()
            print(cursor.rowcount,"Student first name Updated")
            db.close()
           

    elif option=="lName":
            cursor=db.cursor()
            stNo=input("Type student number: ")
            lName=input("Enter student last name: ")
            updTxt="UPDATE student SET lName='" + lName + "'WHERE stNo=" + stNo
            cursor.execute(updTxt)
            db.commit()
            print(cursor.rowcount,"Student last name Updated")
            db.close()
    elif option=="dob":
            cursor=db.cursor()
            stNo=input("Type student number: ")
            dob=input("Enter student date of birth (Year/month/Day): ")
            updTxt="UPDATE student SET dob='" + dob + "'WHERE stNo=" + stNo
            cursor.execute(updTxt)
            db.commit()
            print(cursor.rowcount,"Student Date of birth Updated")
    elif option=="telephoneNo":
            cursor=db.cursor()
            stNo=input("Type student number: ")
            telephoneNo=input("Enter student telephone no: ")
            updTxt="UPDATE student SET telephoneNo='" + telephoneNo + "'WHERE stNo=" + stNo
            cursor.execute(updTxt)
            db.commit()
            print(cursor.rowcount,"Student telephone number Updated")
            again=input("\nYou want to go back to menu? (Y/N) : ")
            if again=="Y" or "y":
                menu()
            else:
                exit()
            

    # ---------- Option 06 ---------- #
    # Open database connetion

    if userInput==6:
            cursor=db.cursor()
            cursor.execute("SELECT * FROM student")
            data=cursor.fetchall()
            for item in data:
                    print(item)
                    stNo=input("Type student number: ")
                    attendDate=input("Enter date : ")
                    attendance=input("Is this student attend? (Yes/No) :")
                    # Execute SQL Query using execute() method
                    mySQLText="INSERT INTO student_attend(stNo,attendDate,attendance) VALUES (%s,%s,%s)"
                    myValues=(stNo,attendDate,attendance)
                    cursor.execute(mySQLText, myValues)
                    # Commit the change
            db.commit()
            db.close()
            again=input("\nYou want to go back to menu? (Y/N) : ")
            if again=="Y" or "y":
                menu()
            else:
                exit()

    # ---------- Option 07 ---------- #
    
    if userInput==7:
            cursor=db.cursor()
            stNo=input("Enter the student number to find his/her attendance :")
            # Execute SQL Query using execute() method
            cursor.execute("SELECT * FROM student_attend WHERE stNo="+ stNo +"")
            data=cursor.fetchall()
            print("\nStudent attend detail(stNo,Attend Date,Attendance) :")
            for item in data:
                    print(item)
            # Commit the change
            db.commit()
            db.close()

            again=input("\nYou want to go back to menu? (Y/N) : ")
            if again=="Y" or "y":
                menu()
            else:
                exit()

menu()
        
        
        
        

        
                
                



