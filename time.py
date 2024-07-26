import time
timestamp = int(time.strftime('%H'))
print(timestamp)


if timestamp<10:
    print("good morning")
elif (timestamp>10 & timestamp<15):
    print("good afternoon")

else:
    print("good night")
    