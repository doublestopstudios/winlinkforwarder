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

NOTE: You must register an "app password" with your email address (as well as enable two-step verification). Otherwise, you will get authentication errors.

IMPORTANT: Due to the way Winlink handles newlines, you must use the character '&&' to denote newlines for the resulting email to contain them. The reason for this, is that Winlink's message editor inserts a newline at word wrap, rather than only inserting newlines when the Enter/Return key is pressed. Thus, the size of your screen dictates where newlines will be inserted. Winlink Forwarder attempts to solve this problem by blanketly removing all newlines and requiring the use of the '&&' token for newlines. Simply put, if you want your email to contain newlines, you must use '&&' when typing your message in Winlink. This will have the exact same effect as '<br>' in HTML: the characters will automatically be detected and replaced with a newline character. 


