score =0
questions =[{"q":"What is 2 + 2?", "a":"4"},
            {"q":"What is the capital of France?", "a":"Paris"},
            {"q":"What is the largest planet in our solar system?", "a":"Jupiter"},
            {"q":"What is the chemical symbol for water?", "a":"H2O"},
            {"q":"What language are we learning?", "a":"Python"}
]
for question in questions:
    print(f"\nQuestion {question["q"]}")
    try:
       answer = input("Enter your answer: ").lower()
    except ValueError:
        print("Please type correct input ")
    if question["a"].lower() == answer:
        print("correct answer ")
        score += 1
    else:
        print(f"Wrong! correct answer is {question['a']}")
print(f"You got {score}/{len(questions)}")
if score >=4 :
        print("Great")
else:
        print("Keep practicing")