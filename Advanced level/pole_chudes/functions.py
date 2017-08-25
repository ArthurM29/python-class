def open_letter(answer, letter, guess_word):
    """ convert guess_word into a list, replace '*' with the letter in correct position and return a new string """
    letter_list = list(guess_word)
    # retrieve indexes of all occurences of the letter in correct_word
    indexes = [index for index, char in enumerate(answer) if char == letter]
    for index in indexes:
        letter_list[index] = letter
    return ''.join(letter_list)


def import_questions():
    """ read given file and return dictionary with question:answer pairs """
    source_file = r'/Users/amanasyan/Documents/Python-projects/python-class/Advanced level/pole_chudes/questions.txt'
    questions_answers = {}
    for line in open(source_file):
        question, answer = line.split(':')
        questions_answers[question] = answer.strip().upper()   # trim new line character '\n' at the end
    # TODO close the file
    return questions_answers

