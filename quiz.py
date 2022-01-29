import random
import os

history = []
res_ok = 0
res_err = 0


def user_input_int(question, min_value=0, default=None):
    """ Return integger user input """

    retry = False
    value = None

    try:
        value = input(question)

        # Optionally return default value
        if not value and default:
            return default

        value = int(value)
    except ValueError:
        print('Invalid input!')
        retry = True

    if value and min_value and value < min_value:
        print('Minimum acceptable input is', min_value)
        retry = True

    if retry:
        return user_input_int(question=question, min_value=min_value, default=default)

    return value


def generate_equation(max_table):
    """ Generate a new equation that has not been asked previously """

    while True:
        a = random.randrange(2, max_table + 1)
        b = random.randrange(2, 12)

        # Check if these values exist in the history
        if (min(a, b), max(a, b)) in history:
            # print('%d x %d exists in history' % (a, b))
            continue

        # Add values to history
        history.append((min(a, b), max(a, b)))

        # Reverse a and b randonly
        (c, d) = (a, b) if random.randrange(1, 2) == 1 else (d, c)

        break

    return c, d


def validate(a, b, response):
    """ Validate user provided result """

    global res_ok, res_err

    if response == a*b:
        print('✩◝(◍⌣̎◍)◜✩')
        print('Correct')
        res_ok = res_ok + 1
    else:
        print('(╥_╥)')
        print('Incorrect! The correct answer is %d x %d = %d' %
              (a, b, a*b))
        res_err = res_err + 1


if __name__ == '__main__':
    os.system("clear")
    max_table = user_input_int("Enter maximum table (2 to 12) ", min_value=2)
    number_eq = user_input_int(
        "Enter number of questions to ask? (default: 10) ", default=10)

    for i in range(number_eq):
        a, b = generate_equation(max_table)

        print()
        print('Question', i+1)
        response = user_input_int("%d x %d = " % (a, b))

        os.system("clear")
        validate(a, b, response)

    print()
    print('*********')
    print('** END **')
    print('*********')
    print()

    print('Total correct answers: %d (%d%%)' %
          (res_ok, round(res_ok / number_eq * 100)))
    print('Total incorrect answers: %d (%d%%)' %
          (res_err, round(res_err / number_eq * 100)))
