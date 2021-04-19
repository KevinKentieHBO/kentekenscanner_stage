from Logica import Kenteken_Uitlezen, Betaling_Berekenen
from Services import Rest_Service

def checkReservering(kenteken):
    try:
        #id = Rest_Service.getKentekenId(Kenteken_Uitlezen.activering())['response']['AutoId']
        id2 = Rest_Service.getKentekenId(kenteken)['response']['AutoId']

        try:
            if Rest_Service.getReservering(id2,1)['response']:
                resid = Rest_Service.getReservering(id2, 1)['response']['reservering_Id']
                try:
                    if Rest_Service.getInrijdtijd(resid):
                        try:
                            if Rest_Service.getAbonnement(id2,1):
                                try:
                                    Rest_Service.updateUitrijtijd(resid)
                                    Rest_Service.createTransactie(0.00,Rest_Service.getAccount(id2)['response']['Account_Id'])
                                    return "Deze auto staat bij de exit. Deze auto heeft wel een abonnement, saldo wordt niet afgeschreven"
                                except:
                                    return "Betaling bij abonnement kan niet aangemaakt worden"
                            else:
                                try:
                                    Rest_Service.updateUitrijtijd(resid)
                                    Rest_Service.updateAccount(Rest_Service.getAccount(id2)['response']['Account_Id'],Betaling_Berekenen.berekenBedrag(Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Inrijtijd'],Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Uitrijtijd']))
                                    Rest_Service.createTransactie(Betaling_Berekenen.berekenBedrag(Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Inrijtijd'],Rest_Service.getInUitrijtijd(resid)['response']['Reservering_Uitrijtijd']),Rest_Service.getAccount(id2)['response']['Account_Id'])
                                    return "Deze auto staat bij de exit. Deze auto heeft geen abonnement, saldo wordt afgeschreven"
                                except:
                                    return "Betaling zonder abonnement kan niet aangemaakt worden"
                        except:
                            return "fout bij abonnement opzoeken"
                    else:
                        try:
                            Rest_Service.updateInrijtijd(resid)
                            return "Deze auto staat bij de entree, de poort gaat open en er wordt een rijtijd genoteerd"
                        except:
                            return "fout bij updaten inrijtijd"
                except:
                    return "fout bij auto binnen check"
        except:
            return "Deze auto heeft geen reserveringen"
    except:
        return "Deze auto bestaad niet"


