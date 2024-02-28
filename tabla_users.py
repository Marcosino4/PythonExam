import pandas as pd
import json
from openpyxl import Workbook

def loadUserData(file_path):
    with open(file_path) as userJson:
        userData = json.load(userJson)
    return userData
def saveDataframeToExcel(df, excelName):
    with pd.ExcelWriter(excelName, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

if __name__ == "__main__":
    userData = loadUserData("secure-users.json")
    df = pd.DataFrame(userData)
    excelName = f"usuarios.xlsx"
    saveDataframeToExcel(df, excelName)