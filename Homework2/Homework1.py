#This is a very simple chatbot in python
#It is rule based

import random

greetings = ['Hello', "What's up", "Howdy!", 'Greetings', 'Hey']

goodbyes = ['Bye!', 'See ya later', 'See you soon', 'Salutations', 'Ciao']

# the responses positionally match the keywords
#Keywords and responses need to be loaded from the respective files
#open the file and read the contents

keywords = []
with open ('chatbotkeywords.txt','r') as loadwords:
    for line in loadwords:
        curr_keyword = line[:-1]
        keywords.append(curr_keyword)

responses = []
with open ('chatbotresponses.txt','r') as loadresponses:
    for line in loadresponses :
        curr_response = line[:-1]
        responses.append(curr_response)
        
print(random.choice(greetings))
user = input("Say something (or type bye to quit):")
user = user.lower()

while(user != "bye"):
    keyword_found = False
    for index in range(len(keywords)):
        if keywords[index] in user :
            print('Bot:', responses[index])
            keyword_found = True

    if(keyword_found == False):
        new_keyword = input("I'm not sure how to respond. What keyword should I respond to?").lower()
        keywords.append(new_keyword)
        new_response = input('How should I respond to ' + new_keyword + "?")
        responses.append(new_response)

    #keep the loop going
    user = input("Say something (or type bye to quit):")
    user = user.lower()

print(random.choice(goodbyes))

#Save the intel
with open('chatbotkeywords.txt','w') as filehandle:
    for listitem in keywords :
        filehandle.write(listitem + "\n")

with open('chatbotresponses.txt','w') as filehandle2:
    for listitem in responses :
        filehandle2.write(listitem + "\n")
