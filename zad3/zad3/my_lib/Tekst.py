import re
def word_count(text):

    if not isinstance(text, str):
        raise TypeError("text must be str")
    return len([w for w in text.strip().split() if w])


def is_palindrome(text):

    if not isinstance(text, str):
        raise TypeError("text must be str")
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


def slugify(text):
    if not isinstance(text, str):
        raise TypeError("text must be str")
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text.strip("-")
