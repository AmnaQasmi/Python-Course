""" Install an extarnal module and use it to perform an operation of your interest ? """

import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()