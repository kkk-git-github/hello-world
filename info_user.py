import logging
import random
import sys
import time
import datetime
import traceback
import threading

class user:
  email = str()
  logging.info("User email (new):" + email)
  if email !=  ("@" and ".com"):
    time.sleep(300)
    print("Invalid email. Try again: (each session lasts 5 minutes)")
    print("Require: @ and .com in your email")
    logging.error("Not satisfied email." + datetime.time + "," + datetime.date)

  password = str()
  logging.info("User password (new):" + password)
  if len(password) < 8:
    time.sleep(600)
    print("Invalid password. Try again: (each session lasts 10 minutes)")
    print("Require: password length should be 8 or greater")
    logging.error("Not satisfied password." + datetime.time + "," + datetime.time)



