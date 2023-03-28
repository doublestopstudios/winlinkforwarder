#!/usr/bin/env python3
"""
Script by Double Stop Studios

This script will search through the designated messages folder to locate and send .mime files to the specified email address.

"""
import os
import smtplib
from email.message import EmailMessage
import shutil
import time


def messageHasBeenSent(message_id):
    with open("sentlist.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
        if message_id in lines:
            return True
        else:
            return False


def getMessageID(mime_file):
    try:
        with open(mime_file, 'r') as file:
            lines = [line.rstrip() for line in file]

            for i in lines:
                if i.startswith("Message-ID: "):
                    return i[12:]
            return "No ID"
    except PermissionError:
        return "Invalid File"
    
    

def getSubject(mime_file):
    try:
        with open(mime_file, 'r') as file:
            lines = [line.rstrip() for line in file]

            for i in lines:
                if i.startswith("Subject: "):
                    return i[9:]
            return "No Subject"
    except PermissionError:
        return "Invalid File"

def getBody(mime_file):
    body = ""
    found_start = False
    try:
        with open(mime_file, 'r') as file:
            lines = [line.rstrip() for line in file]

            for i in lines:
                if i.startswith("Content-Transfer-Encoding: quoted-printable"):
                    found_start = True
                    continue

                if i.startswith("[Message receipt requested]"):
                    return body

                if found_start:
                    if i.startswith("--boundary"):
                        return body
                    body += i
    except PermissionError:
        return "Invalid File"

def sendEmail(subject, body):
    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = email_address
    server.send_message(msg)
    print("Message sent with subject: " + subject)



#if os.path.exists("sentlist.txt"):
#    os.remove("sentlist.txt")

f = open("sentlist.txt", "a")
f.close()
    

print("--Winlink Forwarder--")

has_valid_path = False
messages_path = ""
email_address = ""
email_password = ""

if os.path.exists("session.txt"):
    load_previous = input("Load previously saved information? (Y/N)").lower()

    if load_previous == "y":
        with open("session.txt", 'r') as file:
            lines = [line.rstrip() for line in file]
            for i in lines:
                if i.startswith("path="): messages_path = i[5:]
                if i.startswith("email_address="): email_address = i[14:]
                if i.startswith("email_password="): email_password = i[15:]

            

while not has_valid_path:
    if len(messages_path) == 0:
        messages_path = input("Input the full path to your callsign's messages folder.\n(This would be the folder called 'messages' that includes '.mime' files)\nPath: ")

    if not os.path.exists(messages_path):
        print("The specified path does not exist, please check the path and try again")

    else:
        has_valid_path = True

while True:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    if len(email_address) == 0:
        email_address = input("Destination Gmail address: ")
    if len(email_password) == 0:
        email_password = input("Destination Gmail App Password: ")

    try:
        print(server.login(email_address, email_password))
        break

    except smtplib.SMTPAuthenticationError:
        print("Could not authenticate. Please check your credentials and try again")
        print("Google requires that you generate an 'app password' to access mail. Use your app password instead of your regular password\nFor more information see: https://support.google.com/accounts/answer/185833?hl=en")


os.remove("session.txt")
with open("session.txt", 'a') as file:
    file.write("path=" + messages_path.rstrip() + "\n")
    file.write("email_address=" + email_address.rstrip() + "\n")
    file.write("email_password=" + email_password.rstrip() + "\n")


print("Good email...")
print("Monitoring for messages...")


while True:
    time.sleep(1)
    directories = os.listdir(messages_path);

    for x in directories:

        subject = getSubject(messages_path + "/" + x)

        if subject != "Invalid File":

            body = getBody(messages_path + "/" + x)

            if body != "Invalid File":
                    if body != None:

                        if not messageHasBeenSent(getMessageID(messages_path + "/" + x)):
                        
                            body_without_twenty_equals = body.replace("=20", "")
                            body_without_equals = body_without_twenty_equals.replace("=", "")
                            body_with_newlines = body_without_equals.replace("&&", "\n")
                            sendEmail(subject, body_with_newlines)
                            #shutil.move(messages_path + "/" + x, "forwarded")

                            with open("sentlist.txt", 'a') as file:
                                file.write(getMessageID(messages_path + "/" + x) + "\n")

















