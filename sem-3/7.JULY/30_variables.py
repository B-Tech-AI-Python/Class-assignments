var = 0


def func():
    var = 10

    def func_in():
        var = 20
        print("Inner function", var)
    func_in()
    print("Outer function", var)


print("Global variable", var)
func()

# %%
var = 0


def func():
    global var
    var = 10

    def func_in():
        var = 20
        print("Inner function", var)
    func_in()
    print("Outer function", var)


func()
print("Global variable", var)

# %%


def display(name, age=19):
    print("My name is {} and my age is {}".format(name, age))


display(name="Ishani", age=19)
display(name="Ishan", age=21)
display(name="Isha")
