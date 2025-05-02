def format_name(f_name, l_name):
    """
    Take a first and lastname and format it to return the title case version of the name.
    :param f_name:
    :param l_name:
    :return:
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
