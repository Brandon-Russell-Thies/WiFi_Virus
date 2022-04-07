import socket, os, subprocess, time
import sqlite3 as sq
############################


#This bug disconnects from any router if the specified router in the database
#is not in range of the computer
def WiFi_bug():
    #The following lines of code gets the name of the router
    #that must be in range for the internet not to get disconnected
    conn = sq.connect("system_info.db")
    c = conn.cursor()
    c.execute("SELECT * FROM ROUTER")
    router_name = c.fetchone()
    
    while True:
        time.sleep(5)
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)
        if IPAddr == "127.0.0.1":#Every computer will have this IP
            pass                 #if not connected to the internet
        else:
            print(router_name[0])
            devices = str(subprocess.check_output("netsh wlan show interfaces"))#gets all the router names in range
            print(devices)
            if router_name[0] in devices:#checks to see if the name of the router in the database is in the list of routers in range
                pass
            else:
                os.system("netsh wlan disconnect")
#end of function
        
        
WiFi_bug()
