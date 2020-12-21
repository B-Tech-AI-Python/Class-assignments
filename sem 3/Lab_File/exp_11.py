"""Write an Object-Oriented Python program to create two Time objects:
current Time, which contains the current time; and bread Time, which contains
the amount of time it takes for a bread maker to make bread. Then we'll use
add Time to figure out when the bread will be done. Write the print Time
function to display the time when the bread will be done by the bread maker."""

import datetime


class Time():

    def __init__(self, time):
        self.time = datetime.timedelta(
            hours=time[0], minutes=time[1], seconds=time[2])

    def __add__(self, obj):
        return self.time + obj.time


def input_time():
    hour = int(input("\nEnter hour: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    return (hour, minutes, seconds)


current_time = Time(input_time())
bread_time = Time(input_time())

print(f"\nThe current time is: {current_time.time}")
print(f"The bread time is: {bread_time.time}")

print("\nThe time the bread will be done by: ", end="")
print(current_time + bread_time)
