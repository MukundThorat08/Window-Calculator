from math import floor

digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operand_list = ['+', '-', 'x', '÷', '%']


def evaluate(expression):
    expression = white_space_remover(expression)
    first_num, last_num, operand = expression_breaker(expression)
    output = operation_choicer(first_num, last_num, operand)
    return output_refiner(output)


def operation_choicer(num1, num2, operand) -> float:
    match operand:
        case '+':
            return float(num1) + float(num2)
        case '-':
            return float(num1) - float(num2)
        case 'x':
            return float(num1) * float(num2)
        case '÷':
            return float(num1) / float(num2)
        case '%':
            return float(num1) % float(num2)


def white_space_remover(expression: str):
    return ''.join(expression.split(' '))


def expression_breaker(expression_without_spaces: str) -> list:
    operand = get_operand(expression_without_spaces)
    numbers = expression_without_spaces.split(operand)
    return [numbers[0], numbers[1], operand]


def get_operand(expression: str):
    for value in expression:
        if value in operand_list:
            return value


def output_refiner(result: float) -> int or float:
    point_number = float(str(result).split('.')[1])
    if point_number == 0 or floor(point_number) == 0:
        return int(result)
    else:
        final_points = str(f"{result:.3f}")
        if str(point_number).find('0'):
            return float(final_points[0: str(point_number).find('0') + 1])
        else:
            return float(final_points)
