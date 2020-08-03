import schedule
import time
from datetime import datetime
from fbchat import Client
from fbchat.models import *

def sendit():
    client.send(Message(text=message), thread_id=thread.uid, thread_type=ThreadType.USER)

print('Please enter Facebook creds to continue \n')
client = Client(input('Email: '), input('Password:'))

person = input("\nWho are we chatting with:")
thread = client.searchForThreads(person)[0]
print('The UID of ' + person + ' is ' + str(thread.uid))

firstmessagetime = "9:00"
secondmessagetime = "17:00"
current_time = datetime.now().strftime("%-I:%M")
#song = "placeholder"
 
message = 'TEST yo ' + person + ' it is ' \
         + str(current_time) + \
         " and I'm thinking of you ❤️ " 

sendit()

schedule.every().day.at(firstmessagetime).do(sendit)
schedule.every().day.at(secondmessagetime).do(sendit)
while True:
    schedule.run_pending()
    time.sleep(10)

