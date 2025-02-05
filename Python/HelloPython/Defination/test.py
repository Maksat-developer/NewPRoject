message_1 = 'Global Variable (shares same name as a local variable'

def myFunc():
    message_1 = 'local Variable (shares same name as a global variable'
    print('\nINSIDE THE FUNCTION')
    print(message_1)


# CALLING THE FUNCTION
myFunc()

# PRINTING MESSAGE 1 OUTSIDE THE FUNCTION
print('\nOUTSIDE THE FUNCTION')
print(message_1)

