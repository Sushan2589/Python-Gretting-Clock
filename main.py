import time
Time=time.strftime("%H:%M:%S" )
print (Time)

Hour=int(time.strftime("%H"))


if Hour==6 and Hour>=7 and Hour<12:
  print("Good Morning!!")

elif Hour>=12 and Hour<=17:
 print("Good Afternoon!!")

elif Hour>=18 and Hour<=24:
  print("Good Evening, time to go to bed ")

else:
  print("Why are you awake????") 