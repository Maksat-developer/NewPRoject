# Global Variable

message_global = "message from global variable"


def myFunction():

    print("\nInside the func")
    # you can use global variable inside the func
    print(message_global)
    message_local = 'message from local variable!'
    print(message_local)


myFunction()

print('\nOUTSIDE THE FUNCTION')

# global variables are available outside the func    
