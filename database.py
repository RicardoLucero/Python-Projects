
import sqlite3
# We will connect to the tuples.db if it does not exist then it will be created
conn = sqlite3.connect('tuples.db')

with conn:
    cur = conn.cursor()# We are creating the table if it does not exist tbl_documents
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT\
        )")
    conn.commit()# conn.commit commits what we are submitting to the db

con = sqlite3.connect('tuples.db')# connecting back to the db
#the tuple list of documents to scan through for .txt files
fileList = ('information.docx','Hello.txt','myImage.png', \
              'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# loop through each object in the tuple to find the files that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_documents (col_file) VALUES (?)", (x,))
            print(x)
conn.close()
