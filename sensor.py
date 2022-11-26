"""
This program simulates a fall sensor used by a person. There is no real sensor so you should manually enter 1 in the terminal to simulate a fall being detected. After that, sensor.py sends a HTTP PUT request to server.py, changing fall to True. If you enter 2 in the menu the program ends.
"""

"""
Python time module lets you stop the program execution for a number of seconds.
Python requests is a library that lets you send HTTP requests.
"""
import time
from requests import put

"""
menu is a control variable to determine if the menu should be shown to the user.
"""
menu = True
print("### FALL SENSOR ###")

"""
Shows the menu and wait for user input.
"""
while(menu):
    print("Did the person fall?")
    print("1 - YES")
    print("2 - EXIT")
    answer = input()

    if(answer == "1"):
        # Sends HTTP PUT to server.py, changing fall to True.
        put('http://localhost:5000/', data={'data': True}).json()
        print("\nFall detected!\n")
        # Stops sensor.py for 5 seconds.
        time.sleep(5)
        # Sends HTTP PUT to server.py, changing fall to False.
        put('http://localhost:5000/', data={'data': False}).json()
        # The "sensor" is reset, checking again if a fall is detected.
        print("Sensor reset\n")

    elif(answer == '2'):
        quit()