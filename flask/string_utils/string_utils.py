def get_6_digit_representation(code: str) -> str:
    '''
    Given a code, it fills it up with 0s to make it 6-digits.

    Parameters:
    code (str): The code to add 0s to.

    '''

    num_zeroes_needed = 6 - len(code)
    zeroes_str = ''

    for _ in range(num_zeroes_needed):
        zeroes_str = str(0) + zeroes_str

    return zeroes_str + code