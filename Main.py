# By: Zoidiano0


#imports

import json
import base64
import requests


# Functions Definitions

def Authentication():       #Token gathering
    response = requests.post(APIAUTHOST, data={'grant_type':'client_credentials','client_id':CLIENT_ID, 'client_secret' : SECRET})
    return response


def queue(autor):                #Query template
    payload = {'q':autor, 'type': 'artist'}
    rawdata = requests.get( APIHOST, headers={'Authorization': 'Bearer '+API_Token}, params=payload )
    return rawdata


def getgenres(datain):      # Get All Genres of an Artists
    var = ''
    x = (len(datain['genres']))
    if x != 0:
        for n in range(x):
            var = var + datain['genres'][n]
            if x > 3:
                break
        return var
    else:
        return 'Not Available'

def CheckInput(Disp_Text): # Input Validation
    while True:
        inText = input('\n'+ Disp_Text+ '\t')
        if inText != None and len(inText)>=3:
            break
    return inText

#      Global Variables Declaration

author = ''
x =0

API_Token = ''
artistid = ''
# API HOST LINKS
APIAUTHOST = "https://accounts.spotify.com/api/token"
APIHOST = "https://api.spotify.com/v1/search"



# Presentation

print("\n\n\n\n")
print("=================================================================")
print("================== Emerging Technologies ========================")
print("=================================================================")
print("=================== By:Santiago Estévez =========================")
print("=================================================================")
print("\n")
print(" Assignment 1: API Integration Challenge ")
print(" API Integration: Spotify ")
print("\n\n")

print('Authentication Model used - Client Credentials Flow') #   Prints and Request Pospotify Login Method.
CLIENT_ID = CheckInput('Enter Your Spotify USER ID')
SECRET = CheckInput('Enter Your Secret for the provided ID')
print('Authenticating with Spotify using Provided ID/Secret')
print('Awaiting Response...')

while True:
    attempt = Authentication()          # request Authentication with provided Data

    if attempt.status_code == 200:
        print('Authentication Aproved !')
        print('Token Generated: '+ (str((attempt.json()['access_token']))))
        API_Token = str((attempt.json()['access_token']))                       # saves provided token
        print('Setting up Query Engine ')
        
        while True:
            
            author = CheckInput("Please type the name of the artist to Seach:")
            # Data Setup from Query 
            jsonData = queue(author).json()
            print('\n')
            print('[' + str('         Artist Name').ljust(40)+']   ' + '[' +str('           Genres Involved').ljust(45)+']   ' + '[' +str('popularity')+ ']')
            print('\n')
            for data in (jsonData['artists']['items']): # Printing the information
                print('[' + str(data['name']).ljust(40)+']   ' + '[' +str(getgenres(data)).ljust(45)+']   ' + '[' +str(data['popularity'])+ ']')            
            

    else:
        print('Retrying Connection with Spotify API Services.')  # if authtentication fails too many times exit's the Program. 
        x = x+1
        if x==4:
            print('Exiting.. too many Attempts')
            break
    


    


