import time
import threading
import sys

def other_function():
    print("Other function called")
    #run function with scannedData

def background():
    while True:
       print("Waiting...")
       time.sleep(5)
       #running other functions not related to input()

threading1 = threading.Thread(target=background)
threading1.daemon = True
threading1.start()

while True:
    scannedData = input()
    if scannedData == 'INPUTX':
        other_function()
        
    else:
        print ('invalid input')
