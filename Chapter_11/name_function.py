#!../ENV/bin/python


def get_formatted_name(first, last, middle=""):
    """Generate a formatted full name"""
    if middle:
        full_name = first + " " + middle + " " + last
        return full_name.title()
    else:
        full_name = first + " " + last
        return full_name.title()
