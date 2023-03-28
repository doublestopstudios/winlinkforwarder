# Winlink Forwarder

This script is intended to be used alongside the Winlink Global Radio Email client, where it will automatically pull received messages and upload them to a designated email address.

# What it's for

Winlink Forwarder is the solution to the question of how to get radio emails into your regular email account. You can be far away from any reliable computer, but as long as you have your radio, then you may send emails or automatic status updates by using Google's (or a third party's) email fowarding option. The script is simple and lightweight; requiring nothing more than Python on the target computer. When Winlink receives a message on the target computer, Winlink Forwarder will detect the message and pass it along to a designated email address, therefore alleviating any potential restrictions of sole radio-to-radio communication.

# How to use

1. Download and install Python 3.
2. Download Winlink Forwarder.py from this repository.
3. Follow the on-screen instructions and provide the necessary information for the forwarder to send messages to your email address.
4. Leave the script running, and maintain an active internet connection.
5. When the script is no longer needed, simply close the console window.

Once Winlink receives a message, Winlink Forwarder will detect this message and strip the information to form an email. The email will be sent FROM your email address, TO your email address: as if you sent yourself an email.

NOTE: You must register an "app password" with your email address (as well as enable two-step verification). 
