from block_io import BlockIo
import json
import urllib
import time
#Twilio API. Uncomment to use
#from twilio.rest import Client

from os import remove
from sys import argv

block_io = BlockIo
block_io = BlockIo('[API KEY GOES HERE]', '[ACCOUNT PIN GOES HERE]', 2)

#Twilio API. Uncomment to use
#client = Client("[ACCOUNT SID FROM TWILIO]", "[AUTHENTICATION TOKEN FROM TWILIO]")


getbalanceurl = "https://block.io/api/v2/get_balance/?api_key=[API KEY GOES HERE]"
getbalancedecode = urllib.urlopen(getbalanceurl)
getbalancestring = json.loads(getbalancedecode.read())
your_balance = getbalancestring[u'data'][u'available_balance']

killer = False

print('            _                                                        _   ')
print('           | | _   _   __ _   __ _   ___  _ __  _ __    __ _  _   _ | |_ ')
print("        _  | || | | | / _` | / _` | / _ \| '__|| '_ \  / _` || | | || __|")
print('       | |_| || |_| || (_| || (_| ||  __/| |   | | | || (_| || |_| || |_ ')
print('        \___/  \__,_| \__, | \__, | \___||_|   |_| |_| \__,_| \__,_| \__|')
print('                      |___/  |___/                                       ')
print('----------------------')
print('Welcome to Juggernaut!')
print('----------------------')
while True:
 print('------------------------------------------------------------')
 hours = raw_input('How many hours would you like to delay your transaction for?\n------------------------------------------------------------\n')
 try: 
   float(hours)
   break
 except ValueError:
   print('-------------------------------')
   print('Please input a numerical value.')
   print('-------------------------------')

while True: 
 print('-------------------------------------------------------------')
 addy = raw_input('Please enter the address to which you wish to send your BTC:\n-------------------------------------------------------------\n')
 if len(addy) <= 26 or len(addy) >= 36:
  print("That doesn't look right.")
 else:
  print('----------------------------------------------------------------------------------------------')
  confaddy = raw_input('Confirm that the address you wish to send funds to is ' + addy + "? [y/n]\n----------------------------------------------------------------------------------------------\n")
  if confaddy == 'y':
   break

while True:
 print('----------------------------------------------------------------------')
 send_amt = raw_input('Your current balance is: ' + your_balance + ' BTC. How much do you want to send?\n----------------------------------------------------------------------\n')
 try:
  int(send_amt)
 except ValueError:
  try:
   float(send_amt)
  except ValueError:
   print('Please enter a valid amount.\n')
 if float(send_amt) >= (float(your_balance) - 0.005):
  print('-------------------')
  print('Insufficient funds!')
  print('-------------------')
 else:
  while True:
   #Twilio API. Uncomment to use
   #while True:
    #print('------------------')
    #updates = raw_input('Send updates?[y/n]\n------------------\n')
    #if updates == 'y':
     #print('---------------')
     #print('Updates enabled')
     #print('---------------')
     #sendupdates = 'to="[PHONE NUMBER TO TEXT WITH UPDATE]", from_="[TWILIO-GENERATED PHONE NUMBER]", body="I\'m halfway there, see you soon!"')
     #break
    #else:
     #print('----------------')
     #print('Updates disabled')
     #print('----------------')
     #break
   print('--------------------------------------------------------------------------------------')
   confset = raw_input('Confirm sending of ' + send_amt + 'BTC to address "' + addy + '" in ' + hours + ' hours?[y/n]\n--------------------------------------------------------------------------------------\n')
   if confset == 'y':
     print('----------------------------------------------------------------------------')
     killswitch = raw_input('Activate the kill switch? This will delete the program upon completion.[y/n]\n----------------------------------------------------------------------------\n')
     if killswitch == 'y':
      killer = True
     print('-----------------------------------------------------------------------------------')
     print('Transaction queued! Please keep this device switched on until funds have been sent.\nIf you wish to cancel it, simply exit the program.')
     print('-----------------------------------------------------------------------------------')
     break
  break

time.sleep(float(hours)*3600/2)
try:
 client.messages.create(sendupdates)
except:
 pass
time.sleep(float(hours)*3600/2)

block_io.withdraw(amounts=send_amt, to_addresses=addy, pin='[ACCOUNT PIN GOES HERE]')
print('Sent!')
if killer:
 remove(argv[0])
