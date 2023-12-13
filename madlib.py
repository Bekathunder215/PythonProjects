#this project is for string concatination
#we want to create a string that says, my favorite car is ____
adjective = input("Give me an Adjective:  ")
adjective1 = input("Give me another Adjective:  ")
verb1 = input("Give me a verb:  ")
verb2 = input("Give me another verb:  ")
verb3 = input("Give me another verb:  ")
famous = input("Give me a famous person:  ")

madlib = f"Computer programming is so {adjective}! It makes me excited\
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous}!\
         In general, i like to {verb3} when it is raining, it make me \
            feel like the world is {adjective1}. Ok bye!"

print(madlib)