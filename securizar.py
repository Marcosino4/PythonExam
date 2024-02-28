import hashlib
import json

def getIndex(user_id):
    return userId.index(user_id)

def hashing(str):
    encrypted = hashlib.sha256(str.encode()).hexdigest()
    return encrypted

writeable = open("secure-users.json", "w")
users = open("users.json")
usersData = json.load(users)
userId = []
diccionario = []

user = {
        "nombreId": "",
        "pass": "",
    }
for i in usersData:
    userId.append(i["userId"])

for i in userId:
    passwd = str(usersData[getIndex(i)]["password"])
    passwd = hashing(passwd)
    user = {
        "nombreId": i,
        "pass": passwd
    }
    diccionario.append(user)

writeable.write(json.dumps(diccionario, indent=2))
users.close()
