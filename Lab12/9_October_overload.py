import datetime as dt

# %%
class Time:
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.time = dt.timedelta(hours=hour,minutes=minutes,seconds=seconds)
    
    def __add__(self, obj):
        return self.time + obj.time

def inputTime():

    print("\n\nENTER TIME", end="")
    while True:
        try:
            hour = int(input("Enter hour: "))
            if hour not in range(0,24):
                raise ValueError
                
            minutes = int(input("Enter minutes: "))
            if minutes not in range(0,61):
                raise ValueError
                
            seconds = int(input("Enter seconds: "))
            if seconds not in range(0,61):
                raise ValueError
                
            break
        
        except ValueError:
            print("Invalid value! Try again!")
    
    return hour, minutes, seconds


x, y, z = inputTime()
t1 = Time(x, y, z)

x, y, z = inputTime()
t2 = Time(x, y, z)

print("\nAdding times")
print(t1 + t2)

# %%
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.date = dt.date(year, month, day)
    
    def __add__(self, days):
        return self.date + dt.timedelta(days = days)
    
    def __gt__(self, ob):
        if self.date > ob.date:
            return f"{self.date} is greater than {ob.date}"
        
        elif self.date < ob.date:
            return f"{ob.date} is greater than {self.date}"
        
        else:
            return "Dates are equal"

def inputDate():
    
    thirtyOne = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]

    print("\n\nENTER DATE", end="")
    while True:
        try:
            year = int(input("Enter year: "))
                
            month = int(input("Enter month: "))
            if month not in range(1,13):
                raise ValueError
                
            day = int(input("Enter day: "))
            # thirty one day months
            if month in thirtyOne:
                if day not in range(1,32):
                    raise ValueError
                    
            # thirty day months
            elif month in thirty:
                if day not in range(1,31):
                    raise ValueError
            
            # february
            else:
                if (year % 4) == 0:
                   if (year % 100) == 0:
                       if (year % 400) == 0:
                           if day not in range(1,30):
                               raise ValueError
                       else:
                           if day not in range(1,29):
                               raise ValueError
                   else:
                       if day not in range(1,30):
                           raise ValueError
                else:
                   if day not in range(1,29):
                        raise ValueError
            
            # the end
            break
        
        except ValueError:
            print("Invalid value! Try again!")
    
    return year, month, day

x, y, z = inputDate()
d1 = Date(x, y, z)

days = int(input("Enter number of days you want to add to your date: "))

print("\nAdding days")
print(d1 + days)

# %%
x, y, z = inputDate()
d1 = Date(x, y, z)

x, y, z = inputDate()
d2 = Date(x, y, z)

print("\nComparing dates")
print(d1 > d2)

# %%
class Distance:
    def __init__(self, distance):
        self.distance = distance
    
    def __isub__(self, ob):
        self.distance -= ob.distance
        return self.distance

dist1 = Distance(10)
dist2 = Distance(5)

print(dist1.distance)

print(dist1 -= dist2)

print(dist1.distance)
