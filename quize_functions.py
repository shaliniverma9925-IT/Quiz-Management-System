def show_question(question, number):

    print("\nQuestion", number)
    print(question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(i, ".", option)


def check_answer(question, answer):

    if question["options"][answer - 1] == question["answer"]:
        return True
    else:
        return False


def calculate_percentage(score, total):

    percentage = (score / total) * 100

    return percentage