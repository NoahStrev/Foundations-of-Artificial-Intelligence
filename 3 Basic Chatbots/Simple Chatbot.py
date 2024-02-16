#This is a very simple chatbot in python
#It is rule based

import random

greetings = ['Hello', "What's up", "Howdy!", 'Greetings', 'Hey']

goodbyes = ['Bye!', 'See ya later', 'See you soon', 'Salutations', 'Ciao']

keywords = ['music', 'pet', 'book', 'game']

# the responses positionally match the keywords
responses = ['Music is so relaxing', 'Dogs are best friends', 'I pick one up once in a while',
             'I like to play video games']

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
        responses.append(new_keyword)

    #keep the loop going
    user = input("Say something (or type bye to quit):")
    user = user.lower()

print(random.choice(goodbyes))
