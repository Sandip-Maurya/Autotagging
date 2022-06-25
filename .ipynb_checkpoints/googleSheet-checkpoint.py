
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("Questions IDs record")  #open sheet
q_id_record_tab = sheet.worksheet('q_id_record_tab')


# Data must be 2d. Number of rows in the data should be atleast one and number of columns should be 4

def append_record(data):
    if len(data) >= 1 and len(data[0])==4:
        q_id_record_tab.append_rows(data)
        return 'Question data updated in the google sheet successfully'
    else:
        return 'Please check the data format. Data should be a list of 2 dimensions with column size as 4'


def get_all_values_from_google_sheet():
    all_values = q_id_record_tab.get_all_values()
    return all_values