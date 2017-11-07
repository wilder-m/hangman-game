def hangman_game():
    import random

    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    tries = 0 #keep track of the number of guesses the computer makes
    exceptions = " .\'" #these are all the special characters you will accept
    guessed = exceptions #initialize guessed to include all the exceptions
    out = '' #initialize the output
    win = False #use a fixed variable to flag when you've won
    
    #ask the user for a secret phrase
    secret = raw_input("enter your secret phrase:  ")
    
    #check to make sure they only enter letter and numbers
    for letter in secret.lower():
        if letter not in alpha:
            if letter not in exceptions:
                secret = raw_input("only use letters and numbers. no special characters. please try again.  ")
    #display an output of the hangman phrase in dashes
    for letter in secret.lower():
        if letter in guessed:
            out += letter
        else:
            out += '-'
    print out

    #this computer starts guessing letters
    
''' Miguel you need to repair the code below this line by replacing anything in <<>> brackets with the correct value.
When you are done filling in all the brackets erase lines 29, 30 and 54 and test the program to see if it works.
    while win == <<what goes here? True or False>>:
        guess = random.choice(alpha)
        
        print 'I\'m guessing ' + guess
        alpha.remove(guess) #this is how you take a letter out of a list
        guessed <<what goes here?>> guess  #this is how you add the letter to guessed
        #check the phrase for the letter guessed            
        if guess in secret.lower():
            out = '' #repeat the display output with the new letter guessed
            for letter in secret.lower():
                if letter in guessed:
                    out += letter
                else:
                    out += '-'
            print out
            if '-' in out: #checks to see whether or not all the letters are guessed
                win = <<True or False?>>
            else:
                print 'I got it in ' + str(tries) + ' tries'
                win = <<True or False?>>   #this will break the while loop
        else:
            print "that was no good. I\'m going to try again" 
        tries += <<what number goes here?>> #counts the number of tries
Erase this line when you are done '''
            
            