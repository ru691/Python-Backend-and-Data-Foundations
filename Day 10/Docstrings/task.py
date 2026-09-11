def format_name(f_name, l_name):
    """Take the first name and last name and format the name
    then return every word with a capital first letter"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

"""give the function we created a variable name so we can use it easily for the future"""
formatted_name = format_name("AnGeLa", "YU")

"""Calculate the number of letters inside the word/list"""
length = len(formatted_name)



