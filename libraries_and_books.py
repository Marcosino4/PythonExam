import json
import pandas as pd
import json
from datetime import date
from openpyxl import Workbook
def loadUserData(filePath):
    with open(filePath) as userJson:
        userData = json.load(userJson)
    return userData

def saveDataframeToExcel(df, excelName):
    with pd.ExcelWriter(excelName, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

users = open("users.json")
usersData = json.load(users)
userBooks = []

for i in usersData['books']:
    userBooks.append(i["bookId"])

diccionario = []

Library = {
        "IDBiblioteca": "",
        "IDLibro": "",
        "Titulo": "",
        "Editorial": "",
        "AñoPublicacion": "",
        "IDUsuario": "",
        "NombreCompleto": "",
    }

if __name__ == "__main__":
    userData = loadUserData("users.json")
    df = pd.DataFrame(userData)
    hoy = date.today()
    fecha = f"{hoy.day}-{hoy.month}-{hoy.year}"
    excelName = f"{fecha}-libros-prestados.xlsx"
    saveDataframeToExcel(df, excelName)