def add(first_num, second_num):
    result = int(first_num) + int(second_num)
    return result


def subtract(first_num, second_num):
    result = int(first_num) - int(second_num)
    return result


def multiply(first_num, second_num):
    result = int(first_num) * int(second_num)
    return result


def divide(first_num, second_num):
    result = int(first_num) / int(second_num)
    return result

first_input = input('Enter first number: ')
second_input = input('Enter second number: ')
arithmetic_op = input('Please enter arithmetic operation(+-*/): ')


def final_result():
    if arithmetic_op == '+':
        fin_result = add(first_input, second_input)
        return fin_result
    elif arithmetic_op == '-':
        fin_result = subtract(first_input, second_input)
        return fin_result
    elif arithmetic_op == '*':
        fin_result = multiply(first_input, second_input)
        return fin_result
    elif arithmetic_op == '/':
        fin_result = divide(first_input, second_input)
        return fin_result
    else:
        print("Please enter one of this arithmetic operations (+-*/)")


print("%s + %s = %s" % (first_input, second_input, final_result()))

# why do you need to convert to int all functions ? better convert to float the input itself one time
# just know that you could just return the value without putting in 'result' variable
# I have done this without function, if you want to use function, better return once
# I entered 4-5, but got 4 + 5 = -1, you are printing '+' instead of the arithmetic operation entered by user
# there is not connection between
# you do not pass arithmetic_op to function, but are using it - it works, but better to pass it clearly
# better check invalid operation in the start and return from the function if an invalid value