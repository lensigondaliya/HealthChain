def clean_html(text):
    """
    Cleans and standardizes HTML input across the project.

    - Converts input to string
    - Removes extra whitespace
    - Ensures consistent formatting

    Args:
        text: Raw HTML/text input

    Returns:
        Cleaned text string
    """
    if not text:
        return ""

    # convert to string
    text = str(text)

    # remove extra spaces
    text = text.strip()

    return text


def normalize_quantity(value):
    """
    Ensure numbers are always integers when possible
    """
    try:
        return int(value)
    except:
        return value