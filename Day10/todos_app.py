from pymongo import MongoClient #pymongo
from urllib.parse import quote_plus #urllib3
username=quote_plus('gmaheswaranmca')
password=quote_plus('@2019$Guido')
server='cluster0.slxn7ab.mongodb.net'
url = f'mongodb+srv://{username}:{password}@{server}/'
print(url)
client = MongoClient(url)
db = client['todos_app_db']
todos_collection = db['todos']

def read_all():
    return todos_collection.find()
#Driver code 
def main():
    todos = read_all()
    for todo in todos: 
        print(todo)
main()