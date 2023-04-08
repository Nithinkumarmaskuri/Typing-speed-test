import time
import random

strings=["rcb is not just a team,its an emotion","my self an actor","virat is my fav cricketer","kholi is the best underrated batsmen in the world"]
random_index=random.randint(0,len(strings)-1)
strings[random_index]

string = strings[random_index]
print(string)
word_count=len(string.split())
print(word_count)

while True:
    random_index=random.randint(0,len(strings)-1)
    string = strings[random_index]
    print(string)
    t0=time.time()
    inpuit_text=str(input('write the sentence:'))
    t1=time.time()
    
    if inpuit_text=='0':
        print("take care")
        break
    
    correct_words=len(set(inpuit_text.split())&set(string.split()))
    accuracy=correct_words/word_count
    time_taken=t1-t0
    wps=word_count/time_taken
    wpm=wps/60
    print('WPS:',wps ,'WPM:',wpm,"ACCURACY:",accuracy*100,"TIME TAKEN",time_taken,'\n')
    
    print("thank you")
    
    
    
    
    
    
    





    
