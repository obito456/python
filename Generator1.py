#IF YOU WANT TO SET COUNT DOWN IN STOPWATCH FOR 5 SEC
import time

def stopwatch(count):
    while count>0:
        yield count
        time.sleep(2)
        count-=1
Num=stopwatch(5)
print(next(Num))
print(next(Num))
print(next(Num))
print(next(Num))
