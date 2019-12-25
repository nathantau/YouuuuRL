import string

class Mapper():

    possible_characters = '0123456789' + string.ascii_lowercase + string.ascii_uppercase

    @classmethod
    def generate_dict(cls, possible_characters:list) -> {}:
        '''
        Generates a dictionary with characters mapped to their corresponding numerical value.

        Parameters:
        possible_characters (list): List of possible characters in 6-digit URL

        Returns:
        dict: Dictionary mapping
        '''

        dictionary = {}
        
        for i in range(len(possible_characters)):
            dictionary[possible_characters[i]] = i

        return dictionary

    @classmethod
    def from_base_62_encoded(cls, base62: int, dictionary: dict) -> int:
        '''
        Returns a decimal number from a given base-62 number.
        Uses self-defined mathematical operations for computations.

        Parameters:
        base62 (str): Base 62 representation of number
        dictionary (dict): dictionary with characters mapped to their corresponding numerical value.

        Returns:
        int: Decimal representation of number
        '''

        ans = 0
        base62 = base62[::-1]

        for i in range(len(base62)):
            char = base62[i]
            idx = dictionary[char]

            ans += (62 ** i) * idx

        return ans

    @classmethod
    def to_base_62(cls, decimal: int) -> str:
        '''
        Given a 10-digit base 10 number, this function returns its base-62 representation string

        Parameters:
        decimal (int): Base 62 number

        Returns:
        str: String representation using base 62
        '''

        