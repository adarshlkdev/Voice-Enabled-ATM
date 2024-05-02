import time
import pyttsx3

engine = pyttsx3.init()

# Get list of voices
voices = engine.getProperty('voices')

# Set speech rate
engine.setProperty('rate', 150)  # Speed percent (can go over 100)

# Use the second voice
engine.setProperty('voice', voices[1].id)


engine.say("Please insert your Card")
engine.runAndWait()

time.sleep(5)

password = 1234

engine.say("Please enter your 4 digit pin")
engine.runAndWait()

pin = int(input("Please enter your 4 digit pin: "))

balance = 5000

if pin == password:
        print('''
              1 -> Balance Enquiry
              2 -> Withdrawl Money
              3 -> Exit
              ''')
        
        try:
              engine.say('Please enter your choice')
              engine.runAndWait()
              option = int(input("Please enter your choice :"))
              

        except:
              engine.say('Please enter your valid option')
              engine.runAndWait()
              print('Please enter your valid option')  

        if option == 1:
              print("Your current balance " , balance) 
              engine.say('Transaction successful.')
              engine.runAndWait()
            

        elif option == 2:
              engine.say('Please enter your amount to withdraw : ')  
              engine.runAndWait()
              withdraw_amount = int(input('Please enter your amount')) 


              balance -= withdraw_amount

              print(withdraw_amount , "debited from your account")
        

              print("Your updated balance is " ,balance)
              engine.say('Transaction successful.')
              engine.runAndWait() 
             

        else:
              engine.say('Invalid option selected') 
              engine.runAndWait()
              print('Invalid option selected') 
              
                    

else:
    engine.say('Wrong pin entered , Plz try again later')
    engine.runAndWait()
    print('Wrong pin entered , Plz try again later')


engine.say('Thanks for using our service') 
engine.runAndWait()
print('Thanks for using our service') 
        





