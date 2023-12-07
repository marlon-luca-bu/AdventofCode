def process_string(input_string):
    lines = input_string.split('\n')

    total_sum = 0

    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            # Concatenate the first and last digit and convert to an integer
            number = int(digits[0] + digits[-1])
            print(number)
            total_sum += number
    print(total_sum)
    return total_sum


def word_to_digit(word):
    mapping = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    return mapping.get(word)


def find_solution(input_string):
    import re
    lines = input_string.split('\n')

    total_sum = 0

    converted = []

    for line in lines:
        converted = []
        word_and_digits = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)[0]
        if word_and_digits.isalpha():
            converted.append(word_to_digit(word_and_digits))
        else:
            converted.append(word_and_digits)
        line_rev = line[::-1]
        word_and_digits_rev = re.findall(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)', line_rev)[0]
        if word_and_digits_rev.isalpha():
            converted.append(word_to_digit(word_and_digits_rev[::-1]))
        else:
            converted.append(word_and_digits_rev)

        number = int(converted[0] + converted[-1])

        total_sum += number

    print(total_sum)