from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

test=["hare krishna hare krishna krishna krishna hare hare hare ram hare ram ram ram hare hare",
      "om shri mahaganapataye namah",
      "har har mahadev jay shiv sambhu",
      "jay mata di bolo jay mata di"]
test1=r.choice(test)
print("***** Typing Speed *****")
print(test1)
print()
print()

time1=time()
testinput=input(" Enter : ")
time2=time()

print('Speed: ', speed_time(time1,time2,testinput), "w/sec")
print("Error: ", mistake(test1,testinput))

