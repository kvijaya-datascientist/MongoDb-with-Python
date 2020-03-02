# MongoDB with Python - Querying JSON Documents

#Connecting to MongoDB & inserting documents(records) to MongoDB
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/') # mongodb - protocol ,
mydb = client['Employee'] # checks whether Employee database is already exists or not. if not it will create database - we can check this in mongoDb compass
information = mydb.employeeinformation  #
record ={
    'fname':'vijaya',
    'lname': 'kaja',
    'dept':'analytics'
}
information.insert_one(record)  # inserting one record

records = [ {
'fname':'vijaya',
    'lname': 'kaja',
    'dept':'analytics'},
{
'fname':'kanth',
    'lname': 'polana',
    'dept':'cs'},
{
'fname':'prasad',
    'lname': 'kaja',
    'dept':'Hotel Mgmt'}

]
information.insert_many(records)


# Simaple way of query
print(information.find_one())
#like Select * from information
for info in information.find():
  print(info)

# Query json documents based on conditions
 for record in information.find({'fname':'vijaya'}):
    print(record)

# Query documents using query operators($in,$ln,$gt)
for record in information.find({'dept':{'$in':['analytics']}}):
   print(record)

# and operator
 for record in information.find({'dept':'hotel','fname':'prasad'}):
    print(record)

# OR operator
""" for record in information.find({'$or':[{'fname':'vijaya'},{'dept':'cs'}]}):
    print(record)  """

inventory = mydb.inventory
inventory.insert_many([
    { 'item': "journal", 'qty': 25, 'size': { 'h': 14, 'w': 21,'uom': "cm" }, 'status': "A" },
   { 'item': "notebook", 'qty': 50,'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "A" },
   { 'item': "paper", 'qty': 100, 'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "D" },
   { 'item': "planner", 'qty': 75, 'size': { 'h': 22.85,'w': 30,'uom': "cm" },'status': "D" },
   { 'item': "postcard", 'qty': 45, 'size': { 'h': 10, 'w': 15.25,'uom': "cm" },'status': "A" }
])

for records in inventory.find({'size':{ 'h': 14, 'w': 21,'uom': "cm" }}):
    print(records)


