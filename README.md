# Juggernaut
A Python program for putting a timer on Bitcoin transactions. Designed for use cases where individuals may wish to avoid '$5 wrench attacks' at checkpoints or borders.

Uses the block.io API – use the guide <a href=https://github.com/BlockIo/block_io-python>here</a> to install it using pip. Alternatively, the _JuggernautNoded.py_ file allows you to interact directly with your own node (so as to mitigate counterparty risk) – just install Garzik's <a href=https://github.com/jgarzik/python-bitcoinrpc>python-bitcoinrpc</a> to do so.

Users are further able to set up a <a href=https://www.twilio.com>Twilio</a> account, in order to be notified by SMS when the countdown reaches its halfway point – this message can be customised (in the existing code, it's set to look like a message from a friend/family member – save the contact accordingly). Without a paid plan, however, this is prefixed with an announcement that the message is coming from Twilio, so may raise suspicion under duress.

Set up an account, and grab the Account SID and Authentication Token from the dashboard. You'll need to add these into the file later on.

Use pip to install the Twilio API:

`pip install twilio`

To make use of the Twilio function, uncomment the necessary lines.


Copy the contents of the _Juggernaut.py_ or _JuggernautNoded.py_ file into your text editor, and save it with a _.py_ extension. Replace the text in square brackets with the necessary information from your block.io and Twilio accounts.

Run the code in your terminal with:

`sudo python Juggernaut.py`

Transactions cannot execute without the device being kept powered on for the duration of the countdown (The Raspberry Pi Zero W works well to these ends – I'll update the wiki as there are a couple of tweaks to make to some of its packages).



My coding ability is fairly limited, so please feel free to build on this. 
