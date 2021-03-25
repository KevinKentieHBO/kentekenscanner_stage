import keyboard
import Kenteken_Uitlezen
import Database_Connection
import Rest_Service

#while True:
 #   if keyboard.is_pressed('k'):
Rest_Service.getjSON()
Database_Connection.select("/Users/kevinkentie/Documents/Programmeren/SQLite Databases/Innovatieve_Parkeergarage.db")
Kenteken_Uitlezen.activering()