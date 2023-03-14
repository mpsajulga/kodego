print("If BAD = 10, DAC = 11, and CGI = 22 What is the value of OCCAM?")

BAD = 10
DAC = 11
CGI = 22

print("If we convert the letters for each alpha string to it's numerical value, we'd respectively get \n BAD: 2+1+4=7 \n DAC: 4+1+3=8 \n CGI: 3+7+9=19")
print("If we subtract the results from the given example: \n BAD: 10-7=3 \n DAC: 11-8=3 \n CGI: 22-19=3")
print("All of this establishes a pattern of: \n 1. An alpha to numeric conversion, \n 2. Adding the converted numbers, \n 3. And then adding 3")

def alpha_to_num(alpha_string):
    """
    Converts an alpha string to its corresponding numerical value.

    Args:
        alpha_string (str): The alpha string to convert.

    Returns:
        int: The corresponding numerical value of the alpha string.
    """
    # Convert the alpha string to uppercase for consistency
    alpha_string = alpha_string.upper()

    # Initialize a variable to hold the numerical value
    num_value = 0

    # Iterate through the characters in the string and add their values
    for char in alpha_string:
        # The ASCII value of 'A' is 65, so we subtract 64 to get its position in the alphabet
        char_value = ord(char) - 64
        num_value += char_value

    # Return the numerical value of the string
    return num_value


# Example usage
alpha_string = "OCCAM"
num_value = alpha_to_num(alpha_string)
final_value = num_value + 3
print(f"Therefore, if we put '{alpha_string}' to the same pattern. \n The numerical value which is {num_value} where we would then add '3' to have {final_value}.")