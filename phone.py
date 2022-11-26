"""
This program simulates a phone that constantly checks server.py for a fall status. If a fall is detected an alert is shown to the user.
For phone.py to work you must run phone.py, server.py and sensor.py at the same time.
"""

"""
Python time module lets you stop the program execution for a number of seconds.
Python requests is a library that lets you send HTTP requests.
"""
import time
from requests import get

print("### PHONE APP ###")
print("STATUS: OK")

# sensor.py sends HTTP GET requests indefinitely, until terminated.
while(True):
    # Sends HTTP GET to server.py, checking if a fall was reported.
    status = get('http://localhost:5000/').json()

    if(status["fall"] == "True"):
        print("STATUS: FALL DETECTED!")
        # Stops phone.py for 5 seconds.
        time.sleep(5)
        # Reset the "phone" status.
        print("STATUS: OK")
    # Stops phone.py for 1 second.
    time.sleep(1)