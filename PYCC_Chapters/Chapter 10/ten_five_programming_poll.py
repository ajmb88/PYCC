flag = True

poll_answers = []
all_answers = []

with open("programming_poll.txt", 'a') as poll:
    poll.write(f"\nProgramming Poll:")


while flag:
    question = input(f"\nHey, what do you like most about programming?: ")
    if question.lower() == 'q':
        flag = False
    elif question in poll_answers:
        print(f"\nThanks for your input, we'll make sure to note it down.")
        all_answers.append((question))
    else:
        print(f"\nThanks for your help with the questionare.")
        poll_answers.append(question)
        all_answers.append((question))
        with open("programming_poll.txt", 'w') as poll:
            poll.write(f"{question.title()}")

print(f"\nAll the answers from the poll are:")
for item in poll_answers:
    print(item)

print(f"\nAll answers from the poll are:")
for item in all_answers:
    print(item)


