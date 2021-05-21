from Logica import Kenteken_Uitlezen, Betaling_Berekenen
from Services import Rest_Service
import time

def checkReservering(auto):
    start = time.time()
    try:
        id = Rest_Service.getKentekenId(Kenteken_Uitlezen.activering(auto))['response']['AutoId']
        print(id)
        try:
            if Rest_Service.getReservering(id, 1) == "Deze auto heeft geen reserveringen":
                return "Deze auto heeft geen reserveringen"
            if Rest_Service.getReservering(id, 1)['response']['reservering_resultaat'] == '1':
                resid = Rest_Service.getReservering(id, 1)['response']['reservering_Id']
                try:
                    if Rest_Service.getInrijdtijd(resid):
                        try:
                            if Rest_Service.getAbonnement(id,1):
                                try:
                                    Rest_Service.updateUitrijtijd(resid)
                                    Rest_Service.createTransactie(0.00,Rest_Service.getAccount(id)['response']['Account_Id'])
                                    print(time.time() - start)
                                    return "Deze auto staat bij de exit. Deze auto heeft wel een abonnement, saldo wordt niet afgeschreven"
                                except:
                                    print(time.time() - start)
                                    return "U mag uitrijden, er is geen saldo afgerekend"
                            else:
                                try:
                                    Rest_Service.updateUitrijtijd(resid)
                                    Rest_Service.updateAccount(Rest_Service.getAccount(id)['response']['Account_Id'],Betaling_Berekenen.berekenBedrag(Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Inrijtijd'],Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Uitrijtijd']))
                                    Rest_Service.createTransactie(Betaling_Berekenen.berekenBedrag(Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Inrijtijd'],Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Uitrijtijd']),Rest_Service.getAccount(id)['response']['Account_Id'])
                                    print(time.time() - start)
                                    return "Deze auto staat bij de exit. Deze auto heeft geen abonnement, saldo wordt afgeschreven"
                                except:
                                    print(time.time() - start)
                                    return "U mag uitrijden, het saldo is afgerekend"
                        except:
                            print(time.time() - start)
                            return "fout bij abonnement opzoeken"
                    else:
                        try:
                            Rest_Service.updateInrijtijd(resid)
                            print(time.time() - start)
                            return "U mag inrijden"
                        except:
                            print(time.time() - start)
                            return "fout bij updaten inrij-tijd"
                except:
                    print(time.time() - start)
                    return "fout bij auto binnen check"
            elif Rest_Service.getReservering(id, 1)['response']['reservering_resultaat'] == '2':
                return "U kunt inrijden tot uiterlijk 15 minuten voor uw eindtijd"
            elif Rest_Service.getReservering(id, 1)['response']['reservering_resultaat'] == '3':
                return "U kunt pas inrijden een half uur voor aanvang van uw reservering"
            else:
                return "Deze auto heeft geen reserveringen"
        except:
            print(time.time() - start)
            if Rest_Service.getReservering(id, 1)['response']['reservering_resultaat'] == '2':
                return "u kunt inrijden tot uiterlijk 15 minuten voor uw eindtijd"
            elif Rest_Service.getReservering(id, 1)['response']['reservering_resultaat'] == '3':
                return "u kunt pas inrijden een half uur voor aanvang van uw reservering"
            else:
                return "Deze auto heeft geen reserveringen"
    except:
        print(time.time() - start)
        return "Deze auto bestaat niet"


