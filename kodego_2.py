print("These contain two identical sets of characters, but in one line, one character in the two sets is different. Which row has the difference?")


string_one = "wreo;:einfads[sasdfk | wreo;:einfads[sasdfk"
stg_1_p_1 = "wreo;:einfads[sasdfk"
stg_1_p_2 = "wreo;:einfads[sasdfk"

string_two = "gmijeoitg!j’elrkd*lfjspd | gmijeoitg!j’elrkd*lfjspd"
stg_2_p_1 = "gmijeoitg!j’elrkd*lfjspd"
stg_2_p_2 = "gmijeoitg!j’elrkd*lfjspd"

string_three = "riojij^rditjii;d$rjtongoi | riojij^rditjji;d$rjtongoi"
stg_3_p_1 = "riojij^rditjii;d$rjtongoi"
stg_3_p_2 = "riojij^rditjji;d$rjtongoi"

string_four = "oeihat/oidfoi{oiaweuriso | oeihat/oidfoi{oiaweuriso"
stg_4_p_1 = "oeihat/oidfoi{oiaweuriso"
stg_4_p_2 = "oeihat/oidfoi{oiaweuriso"

string_five = "a}]eaklsjiejla”eae;aejlkjlil | a}]eaklsjiejla”eae;aejlkjlil"
stg_5_p_1 = "a}]eaklsjiejla”eae;aejlkjlil"
stg_5_p_2 = "a}]eaklsjiejla”eae;aejlkjlil"

def string_difference(string1, string2):
    """
    Calculates the different character(s) between two literal strings of the same length.

    Args:
        string1 (str): The first string to compare.
        string2 (str): The second string to compare.

    Returns:
        str: The different character(s) between the two strings, or an empty string
             if the strings are identical.
    """
    # Initialize an empty string to hold the differences
    differences = ""

    # Iterate through the characters in the strings and compare them
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            differences += string2[i]

    # Return the differences or an empty string if there are none
    return differences


# Example usage
string1 = "riojij^rditjii;d$rjtongoi"
string2 = "riojij^rditjji;d$rjtongoi"
differences = string_difference(string1, string2)
if differences:
    print(f"The different character(s) between '{string1}' and '{string2}' is/are '{differences}'.")
else:
    print(f"The strings '{string1}' and '{string2}' are identical.")