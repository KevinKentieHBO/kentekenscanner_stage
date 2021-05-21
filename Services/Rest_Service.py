from datetime import date, datetime

import requests
from Security_Dir import AES128
import json


def getKentekenId(kenteken):
    cryptor = AES128.AESCipher()
    encodedKenteken = AES128.AESCipher.encrypt(cryptor, kenteken).decode("utf-8")
    encodedKenteken = encodedKenteken.replace("/", "%2F")
    encodedKenteken = encodedKenteken.replace("+", "%2B")
    responseEnc = requests.get("http://localhost:8080/auto/get/"+encodedKenteken+"/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        return to_python
    except:
        return "Deze auto bestaat niet"

def getReservering(auto_Id, parkeergarage_id):
    datum = date.today().strftime("%d-%m-%Y")

    cryptor = AES128.AESCipher()
    encodedAuto_Id = AES128.AESCipher.encrypt(cryptor, str(auto_Id)).decode("utf-8")
    encodedAuto_Id = encodedAuto_Id.replace("/", "%2F")
    encodedAuto_Id = encodedAuto_Id.replace("+", "%2B")

    encodedDatum = AES128.AESCipher.encrypt(cryptor, str(datum)).decode("utf-8")
    encodedDatum = encodedDatum.replace("/", "%2F")
    encodedDatum = encodedDatum.replace("+", "%2B")

    encodedParkeergarageId = AES128.AESCipher.encrypt(cryptor, str(parkeergarage_id)).decode("utf-8")
    encodedParkeergarageId = encodedParkeergarageId.replace("/", "%2F")
    encodedParkeergarageId = encodedParkeergarageId.replace("+", "%2B")
    responseEnc = requests.get(
        "http://localhost:8080/reserveringen/get/" + encodedAuto_Id + "/"+encodedDatum+"/"+encodedParkeergarageId+"/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        return to_python

    except:
        return "Deze auto heeft geen reserveringen"

def getAbonnement(auto_Id, garage_Id):
    cryptor = AES128.AESCipher()
    encodedAuto_Id = AES128.AESCipher.encrypt(cryptor, str(auto_Id)).decode("utf-8")
    encodedAuto_Id = encodedAuto_Id.replace("/", "%2F")
    encodedAuto_Id = encodedAuto_Id.replace("+", "%2B")

    encodedGarage_Id = AES128.AESCipher.encrypt(cryptor, str(garage_Id)).decode("utf-8")
    encodedGarage_Id = encodedGarage_Id.replace("/", "%2F")
    encodedGarage_Id = encodedGarage_Id.replace("+", "%2B")

    responseEnc = requests.get(
        "http://localhost:8080/abonnement/" + encodedAuto_Id + "/"+encodedGarage_Id+"/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        if not to_python['response']:
            return False
        else:
            return True

    except:
        return "Deze auto heeft geen abonnement"

def getAccount(auto_Id):
    cryptor = AES128.AESCipher()
    encodedAuto_Id = AES128.AESCipher.encrypt(cryptor, str(auto_Id)).decode("utf-8")
    encodedAuto_Id = encodedAuto_Id.replace("/", "%2F")
    encodedAuto_Id = encodedAuto_Id.replace("+", "%2B")

    responseEnc = requests.get(
        "http://localhost:8080/accountauto/" + encodedAuto_Id + "/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        return to_python
    except:
        return "Deze auto heeft geen account"

def updateAccount(account_id, saldo):
    cryptor = AES128.AESCipher()
    encodedAccount_Id = AES128.AESCipher.encrypt(cryptor, str(account_id)).decode("utf-8")
    encodedAccount_Id = encodedAccount_Id.replace("/", "%2F")
    encodedAccount_Id = encodedAccount_Id.replace("+", "%2B")

    encodedSaldo = AES128.AESCipher.encrypt(cryptor, str(saldo)).decode("utf-8")
    encodedSaldo = encodedSaldo.replace("/", "%2F")
    encodedSaldo = encodedSaldo.replace("+", "%2B")

    responseEnc = requests.get(
        "http://localhost:8080/account/updatemin/" + encodedAccount_Id + "/" +encodedSaldo+"/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        if not to_python['response']:
            return False
        else:
            return True
    except:
        return "Deze saldo is niet afgetrokken"

def createTransactie(kosten,account_id):
    cryptor = AES128.AESCipher()

    datum = date.today().strftime("%d-%m-%Y")
    tijd = datetime.now().strftime("%H:%M")


    kostenMin = "-"+str(kosten)
    encodedKosten = AES128.AESCipher.encrypt(cryptor, str(kostenMin)).decode("utf-8")
    encodedKosten = encodedKosten.replace("/", "%2F")
    encodedKosten = encodedKosten.replace("+", "%2B")

    encodedDatum = AES128.AESCipher.encrypt(cryptor, str(datum)).decode("utf-8")
    encodedDatum = encodedDatum.replace("/", "%2F")
    encodedDatum = encodedDatum.replace("+", "%2B")

    encodedTijd = AES128.AESCipher.encrypt(cryptor, str(tijd)).decode("utf-8")
    encodedTijd = encodedTijd.replace("/", "%2F")
    encodedTijd = encodedTijd.replace("+", "%2B")

    encodedAccountid = AES128.AESCipher.encrypt(cryptor, str(account_id)).decode("utf-8")
    encodedAccountid = encodedAccountid.replace("/", "%2F")
    encodedAccountid = encodedAccountid.replace("+", "%2B")

    responseEnc = requests.get(
        "http://localhost:8080/betaling/create/" + encodedKosten + "/" +encodedDatum+"/" +encodedTijd+"/"+encodedAccountid+"/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        if not to_python['response']:
            return False
        else:
            return True
    except:
        return "Er is geen betaling aangemaakt."

def updateInrijtijd(reserveringid):
    cryptor = AES128.AESCipher()

    tijd = datetime.now().strftime("%H:%M")

    encodedTijd = AES128.AESCipher.encrypt(cryptor, str(tijd)).decode("utf-8")
    encodedTijd = encodedTijd.replace("/", "%2F")
    encodedTijd = encodedTijd.replace("+", "%2B")

    encodedReserveringId = AES128.AESCipher.encrypt(cryptor, str(reserveringid)).decode("utf-8")
    encodedReserveringId = encodedReserveringId.replace("/", "%2F")
    encodedReserveringId = encodedReserveringId.replace("+", "%2B")

    responseEnc = requests.get(
        "http://localhost:8080/reservering/inrijtijd/" + encodedTijd +"/"+encodedReserveringId+"/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        if not to_python['response']:
            return False
        else:
            return True
    except:
        return "Er is geen inrijtijd gezet"

def updateUitrijtijd(reserveringid):
    cryptor = AES128.AESCipher()

    tijd = datetime.now().strftime("%H:%M")

    encodedTijd = AES128.AESCipher.encrypt(cryptor, str(tijd)).decode("utf-8")
    encodedTijd = encodedTijd.replace("/", "%2F")
    encodedTijd = encodedTijd.replace("+", "%2B")

    encodedReserveringId = AES128.AESCipher.encrypt(cryptor, str(reserveringid)).decode("utf-8")
    encodedReserveringId = encodedReserveringId.replace("/", "%2F")
    encodedReserveringId = encodedReserveringId.replace("+", "%2B")

    responseEnc = requests.get(
        "http://localhost:8080/reservering/uitrijtijd/" + encodedTijd +"/"+encodedReserveringId+"/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        if not to_python['response']:
            return False
        else:
            return True
    except:
        return "Er is geen inrijtijd gezet"


def getTarieven(parkeergarage_id):
    cryptor = AES128.AESCipher()
    encodedParkeergarageId = AES128.AESCipher.encrypt(cryptor, str(parkeergarage_id)).decode("utf-8")
    encodedParkeergarageId = encodedParkeergarageId.replace("/", "%2F")
    encodedParkeergarageId = encodedParkeergarageId.replace("+", "%2B")
    responseEnc = requests.get(
        "http://localhost:8080/betaaltarief/" + encodedParkeergarageId + "/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        return to_python
    except:
        return "Er zijn geen tarieven voor deze parkeergarage"


def getInUitrijtijd(resId):
    cryptor = AES128.AESCipher()
    encodedresId = AES128.AESCipher.encrypt(cryptor, str(resId)).decode("utf-8")
    encodedresId = encodedresId.replace("/", "%2F")
    encodedresId = encodedresId.replace("+", "%2B")
    responseEnc = requests.get(
        "http://localhost:8080/reservering/tijden/" + encodedresId + "/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        return to_python
    except:
        return "Deze auto heeft geen in of uitrijtijden"


def getInrijdtijd(resId):
    cryptor = AES128.AESCipher()
    encodedresId = AES128.AESCipher.encrypt(cryptor, str(resId)).decode("utf-8")
    encodedresId = encodedresId.replace("/", "%2F")
    encodedresId = encodedresId.replace("+", "%2B")

    responseEnc = requests.get(
        "http://localhost:8080/reserveringen/inrijtijd/get/" + encodedresId + "/4PlSfJj3PXz%2FLR%2Bqahuc7A==/nLdiqyrWM%2BkxxasxXscPF0Qt3sovUmjJ9S83NFcaU6LltU7mS4jaRXd0oRooDuSM")
    try:
        response = AES128.AESCipher.decrypt(cryptor, responseEnc.text)
        string = '{"response": ' + response.strip(" ") + '}'
        to_python = json.loads(string)
        if not to_python['response']:
            return False
        else:
            return True

    except:
        return "Er gaat iets fout met de inrijtijd"