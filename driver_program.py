import sys
import random
import datetime

def new_menu():
    print('''
1.Print the list of books
2.Update the list of books
3.Search a BOOK
4.Delete a book
0.Exit''')
    n=int(input("Enter CODE accordingly:"))
    if(n==1):
        Open()
    elif(n==2):
        update()
    elif(n==3):
        search()
    elif(n==4):
        deletion()
    elif(n==0):
        main()
    else:
        print("\nEnter VALID CODE!!!!\n")
        new_menu()

def deletion():
    name=input("Enter name of the book: ")
    with open("book.txt")as f:
        text=f.read()
        l1=text.split("\n")
        for detail in l1:
            word=detail.split("\t")
            if(len(word)>1):
                if(name==word[1]):
                    l1.remove(detail)
        text="\n".join(l1)
        print(text)
        a=text
    with open("book.txt","w")as f:
        f.write(text)
    print("\nSUCCESSFULLY DELETED")
    i=int(input("\nEnter 0 to exit: "))
    if(i!=0):
        print("\nINVALID input\nRedirecting to previous MENU.")
    new_menu()
        

def search():
    print("\n")
    name=input("Enter the name of the book: ")
    text=-1
    with open("book.txt")as f:
        text=-1
        count=0
        while(text!=""):
            text=f.readline()
            word=text.split("\t")
            if(len(word)==3):
                if(name==word[1]):
                    print('''
NOTE!!!!
The details of the books are in the form:
["ID","BOOK","AUTHOR"]
''')
                    print(word)
                    count+=1
                    break
    if(count==0):
         print("\nBOOK IS NOT IN LIST!!!\n(HINT:The spelling of the book might be wrong..) ")
    i=int(input("\nEnter 0 to exit: "))
    if(i!=0):
        print("\nINVALID input\nRedirecting to previous MENU.")
    new_menu()
    
def Open():
    print("\nFormat is : \nID\tBOOK\tAUTHOR\n")
    with open("book.txt")as f:
        text=-1
        while(text!=""):
            text=f.readline()
            print(text)

    i=int(input("\nEnter 0 to exit: "))
    if(i!=0):
        print("\nINVALID input\nRedirecting to previous MENU.")
    new_menu()    

def update():
    
    print("\nWould you like to continue UPDATING??")
    i=int(input("\n1.YES\n0.NO:"))
    if(i==1):
        id_new=random.randint(10000,100000)
        book_new=input("Enter the name of the BOOK: ")
        author_new=input("Enter the name of the AUTHOR: ")
        with open("book.txt","a")as f:
            f.write(f"{id_new}\t")
            f.write(f"{book_new}\t")
            f.write(f'''{author_new}
''')
    elif(i==0):
        new_menu()
    else:
        print("\nEnter VALID input: ")
    update()

def entry():
    ID=int(input("Enter Student ID no.: "))
    if(ID>9999 and ID<100000):
        std_id=str(ID)
        std_name=input("Enter student name: ")
        std_branch=input("Enter BRANCH: ")
        with open("student.txt","a")as f:
            f.write("\n")
            f.write(f"{std_id}\t")
            f.write(f"{std_name}\t")
            f.write(f"{std_branch}\t")
        print("\nDONE!!!\n")
        std_menu()
    else:
        print("Enter 5-digit ID!!!!")
    entry()

def print_list():
    print("Format is : \nID\tSTUDENT NAME\tBRANCH")
    with open("student.txt")as f:
        text=-1
        while(text!=""):
            text=f.readline()
            print(text)

    i=int(input("\nEnter 0 to exit: "))
    if(i!=0):
        print("\nINVALID input\nRedirecting to previous MENU.")
    std_menu()  

def find():
    ID=int(input("Enter Student ID: "))
    count=0
    with open("student.txt")as f:
        text=-1
        while(text!=""):
            text=f.readline()
            word=text.split("\t")
            if(len(word)==4):
                index=int(word[0])
                if(index==ID):
                    print('''
NOTE!!!!
The details of the students are in the form:
["ID","NAME","BRANCH"]
''')
                    print(word)
                    print("\n1.Assign a book\n2.Check Submission status\n0.EXIT\n")
                    i=int(input("Enter responce: "))
                    if(i==1):
                        assign(text)
                    elif(i==2):
                        Return(text)
                    elif(i!=0):
                        printf("INVALID response!!\nRedirecing to previous menu!!\n")
                    std_menu()
                    break
    if(count==0):
        print("\nSTUDENT is not in list!!!\n(Check the id and try again later)\n")
        std_menu()
        

def assign(text1):
    flag=0
    print("\nWould you like to continue ASSIGNING??")
    i=int(input("\n1.YES\n0.NO:"))
    if(i==1):
        word1=text1.split("\t")
        with open("history.txt","a")as f:
            f.write(f"{word1[0]}\t{word1[1]}\t")
        book_ass=input("Enter book to be assigned: ")
        with open("book.txt")as f:
            text2=-1
            count=0
            while(text2!=""):
                text2=f.readline()
                word2=text2.split("\t")
                if(len(word2)==3):
                    if(book_ass==word2[1]):
                        with open("history.txt","a")as f:
                            f.write(f"{word2[1]}\t{word2[0]}\t")
                        count+=1
                        break
        if(count==0):
            print("\nBOOK not found!!!\nSEARCH AGAIN!!!")
            flag+=1
            assign(text1)
        date1=datetime.datetime.today()
        ass_date=date1.strftime("%Y-%m-%d")
        date2=date1+datetime.timedelta(days=15)
        ret_date=date2.strftime("%Y-%m-%d")
        with open("history.txt","a")as f:
            f.write(f"{ass_date}\t{ret_date}\n")
        if(count!=0):
            print("\nBook assigned SUCCESSFULLY\n")
    elif(flag==0):
        find()
    

def Return(text1):
    print("\n")
    word1=text1.split("\t")
    today_date=datetime.date.today()
    print(today_date)
    with open("history.txt")as f:
        while True:
            text2 = f.readline()
            if not text2:
                break
            #print(text2)
            word2=text2.strip().split("\t")
            #print(word2)
            if(len(word2)>5):
                a=word2[5]
                try:
                    exp_date = datetime.datetime.strptime(a, "%Y-%m-%d").date()
                except ValueError:
                    print(f"Invalid date format for {a}")
                    continue
                #print(exp_date)
                dif=(today_date)-(exp_date)
                #print(dif)
                dif_day=dif.days
                #print(dif_day)
                due=float(dif_day)
                #print(due)
                #print(word1[0]==word2[0])
                #print(word1[0])
                #print(word2[0])
                if(word1[0]==word2[0]):
                    if(due>=0.0):
                        print(f"\n{word2[1]} has {word2[2]} book due for {due} days.\n")
                        penalty=due*0.5
                        print(f"The Penalty of late Return for this book is Rs.{penalty}")
                    elif(due>-3.0 and due<0.0):
                        print(f"\nThe tenure for book {word2[2]} are about to expire in {-1*due}days.\n")
    i=input("Press 0 to return to previous menu:")
    if(i!=0):
        print("\nINVALID INPUT!!!\nRedirecting to Previous menu.")
    std_menu()
            
def overall_pend():
    print('''
NOTE!!!!
The details of the students are in the form:

STD_ID  STD_NAME    BOOK_NAME   BOOK_ID    ASSIGNED_DATE    SUBMISSION_DATE
''')
    today_date=datetime.date.today()
    with open("history.txt")as f:
        line=-1
        while(line!=""):
            line=f.readline()
            word=line.strip().split("\t")
            if(len(word)>5):
                a=word[5]
                exp_date=datetime.datetime.strptime(a,"%Y-%m-%d")
                exp_date=exp_date.date()
                dif=(today_date)-(exp_date)
                dif_day=dif.days
                due=float(dif_day)
                if(due>0):
                    print(line)
    print("\nNO OTHER PENDING submission!!\n")
    main()

def history():
    print("\nFormat is : \nSTD_ID  STD_NAME\tBOOK_NAME\tBOOK_ID\tASSIGNED_DATE\tSUBMISSION_DATE\n")
    with open("history.txt")as f:
        text=-1
        while(text!=""):
            text=f.readline()
            print(text)

    i=int(input("\nEnter 0 to exit: "))
    if(i!=0):
        print("\nINVALID input\nRedirecting to previous MENU.")
    main()

def std_menu():    
    print('''
1.Add new student
2.Print Student List
3.Search particular student
0.Exit''')
    n=int(input("Enter CODE accordingly:"))
    if(n==1):
        entry()
    elif(n==2):
        print_list()
    elif(n==3):
        find()
    elif(n==0):
        main()
    else:
        print("\nEnter VALID CODE!!!!\n")
        std_menu()

def main():
    print('''
1.Books in Library
2.Students 
3.Overall Pending Submissions
4.Print History
0.Exit''')
    n=int(input("Enter CODE accordingly: "))      
    if (n==1):
        new_menu()
    elif(n==2):
        std_menu()
    elif(n==3):
        overall_pend()
    elif(n==4):
        history()
    elif (n==0):
        print("\nTHANK YOU!!!")
        sys.exit()
    else:
        print("\nEnter Valid INPUT!!!")
        main()

print('''
GREETINGS ADMIN...
START WITH YOUR LIBRARY MANAGEMENT SYSTEM...
''')
main()
