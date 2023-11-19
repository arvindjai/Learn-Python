def greet(fx):
    def mfx(*args, **kwargs):
        print("Welcome")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet

def hello():
    print("Hello World!")

@greet
def add(a,b):
    print(a+b)

hello()
add(3,4)