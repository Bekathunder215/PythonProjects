#make a dictionary with key value pairs that hold the questions and the answers
#make a simple interface to grab the questions
#compare with the value of the pair

quiz_dict = {
    "question1" : {"question" : "What is the capital of France?",
    "answer" : "Paris"},
    "question2" : {"question" : "What is the capital of Greece?",
    "answer" : "Athens"},
    "question3" : {"question" : "What is the capital of Germany?",
    "answer" : "Berlin"},
    "question4" : {"question" : "What is the capital of Denmark?",
    "answer" : "Copenhagen"},
    "question5" : {"question" : "What is the capital of Italy?",
    "answer" : "Rome"},
    "question6" : {"question" : "What is the capital of Spain?",
    "answer" : "Madrid"},
    "question7" : {"question" : "What is the capital of Portugal?",
    "answer" : "Lisbon"},
    "question8" : {"question" : "What is the capital of Switzerland?",
    "answer" : "Bern"},
    "question9" : {"question" : "What is the capital of Austria?",
    "answer" : "Vienna"}
}

score = 0
#the quiz_dict is a dictionary of dictionaries
for key, value in quiz_dict.items():
    print("-------------------------------------------------------------")
    print(value["question"])
    answer = input("Your answer: ").lower()
    if answer == value["answer"].lower():
        print("Correct!!")
        score += 1
    else:
        print("False! Correct answer is: ", value["answer"])
    print("Current score: ", score, "/", len(quiz_dict))

print("-------------------------------------------------------------")
print("Score: ", score, "/", len(quiz_dict), f"which is {((score/len(quiz_dict))*100):.2f} %")