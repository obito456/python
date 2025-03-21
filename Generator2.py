#IF YOU WANT TO SET COUNT DOWN IN STOPWATCH FOR 5 SEC without yield
import time

def stopwatch(count):
    while count>0:
        print(count)
        time.sleep(2)
        count-=1
Timer=stopwatch(5)
