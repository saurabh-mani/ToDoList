import mysql.connector

#Connection to MySQL
mydb = mysql.connector.connect(host='localhost',user='username',passwd='password',database='ToDoList')

#cursor
mycursor = mydb.cursor()


print("1. List all records")
print("2. List pending")
print("3. Mark done")
print("4. Add entry")
operation = input("Choose an operation:")

if operation=='1':
	qry = "Select * from todolist;"
elif operation=='2':
	qry = "Select * from todolist where Flag = 1"
elif operation=='3':
	 entryid = int(input("Enter Entry Id: "))
	 qry = ("update todolist set Flag = 0 where EntryId = "+str(entryid)+";") 
	 mycursor.execute(qry)
	 mydb.commit()
elif operation=='4':
	title = input("Title: ")
	desc = input("Description: ")
	mycursor.execute(qry)
	mydb.commit()


if(operation=='1' or operation=='2'):
	mycursor.execute(qry)
	print("--------------------------------------------------------")
	print("Entry Id|Title\t\t|Description")
	print("--------+---------------+--------------------------------")
	for i in mycursor:
		print(str(i[0])+"\t|"+i[1]+"\t|"+i[2])
	print("--------------------------------------------------------")
	