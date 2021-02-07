# Ishani Kathuria A023119819004

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

# to print the key along with the value
def display(**kwargs):
    for key,value in kwargs.items():
        print(key, value)

display(emp="Kelly", salary=9000)
