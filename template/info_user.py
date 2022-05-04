import logging
import sys
import time
import datetime

class user:
  email = str(input("Enter your password: "))
  logging.info("User email (new):" + email)
  if email !=  ("@" and ".com"):
    time.sleep(300)
    print("Invalid email. (each session lasts 5 minutes)")
    print("Require: @ and .com in your email")
    logging.error("Not satisfied email." + datetime.time + "," + datetime.date)
    sys.exit()

  password = str(input("Enter your email: "))
  logging.info("User password (new):" + password)
  if len(password) < 8:
    time.sleep(600)
    print("Invalid password. (each session lasts 10 minutes)")
    print("Require: password length should be 8 or greater")
    logging.error("Not satisfied password." + datetime.time + "," + datetime.time)
    sys.exit()

usernew1 = user()