#dict for english dictionary with definition in key value pairs
#get input from user
#print definition
import PyDictionary

word_dict = PyDictionary.PyDictionary()
while True:
    word = input("Enter a word: ")
    if word.lower() == "" or word == "exit":
        print("Goodbye")
        break
    else:
        meaning = word_dict.meaning(word)
        print(meaning)
        for key, value in meaning.items():
            for val in range(len(value)):
                print(f"As {key} : {value[val]}")
