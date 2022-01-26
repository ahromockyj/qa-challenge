import re

def validate_and_calculate(operation):
    match = re.search('(-*\d+)(\+|\-|\*|\~)(-*\d+)', operation)
    if match:
        num_one = int(match.group(1))
        operator = match.group(2)
        num_two = int(match.group(3))
    else:
        return "INVALID", 400

    if operator == '+':
        result = num_one + num_two
    elif operator == '-':
        result = num_one - num_two
    elif operator == '*':
        result = num_one * num_two
    elif operator == '~':
        result = num_one / num_two

    return int(result), 200