# Juggernaut
A Python program for putting a timer on Bitcoin transactions. Designed for use cases where individuals may wish to avoid '$5 wrench attacks' at checkpoints or borders.

Uses the block.io API – use the guide <a href=https://github.com/BlockIo/block_io-python>here</a> to install it using pip.

Copy the contents of the _Juggernaut.py_ file into your text editor, and save it with a _.py_ extension. Replace the text in square brackets with the necessary information from your block.io account.

Run the code in your terminal with:

`sudo python Juggernaut.py`

Transactions cannot execute without the device being kept powered on for the duration of the countdown (a Raspberry Pi would be an ideal computer to run the program on).  

My coding ability is fairly limited, so please feel free to build on this. 
