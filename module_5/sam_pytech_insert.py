""" 
    Title: pytech_insert.py
    Author: Professor Sampson
    Date: 5/26/2021
    Description: Test program for inserting new documents 
                 into the students collection 
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.jjk8u.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Ripley
ripley = {
    "student_id": "123687",
    "first_name": "Ellen",
    "last_name": "Ripley",
    "crew": "Warrant Officer"
}

# Dallas
dallas = {
    "student_id": "123688",
    "first_name": "John",
    "last_name": "Dallas",
    "crew": "Captain"
}

# Parker
parker = {
    "student_id": "123689",
    "first_name": "Ed",
    "last_name": "Parker",
    "crew": "Chief Engineer"
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
ripley_student_id = students.insert_one(ripley).inserted_id
print("  Inserted student record Ripley into the students collection with document_id " + str(ripley_student_id))

dallas_student_id = students.insert_one(dallas).inserted_id
print("  Inserted student record Dallas into the students collection with document_id " + str(dallas_student_id))

parker_student_id = students.insert_one(parker).inserted_id
print("  Inserted student record Parker into the students collection with document_id " + str(parker_student_id))

input("\n\n  End of program, press any key to exit... ")