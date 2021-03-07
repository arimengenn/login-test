import getpass

CorrectUsername = "arimnegen"
CorrectPassword = "subrek" 

loop = 'true'
while (loop == 'true'):

    username = raw_input("Please enter your username: ")

    if (username == CorrectUsername):
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("Please enter your password: ")
            if (password == CorrectPassword):
                print "Logged in successfully as " + username
                loop = 'false'
                loop1 = 'false'
            else:
                print "Password incorrect!"

    else:
        print "Username incorrect!"