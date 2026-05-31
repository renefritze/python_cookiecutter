#!/usr/bin/env python
import re
import sys

EMAIL_REGEX = r"^[a-zA-Z\d._%+\-]+@[a-zA-Z\d.\-]+\.[a-zA-Z]{2,}$"


def _validate_input():
    author_email = "{{ cookiecutter.email }}"
    if not re.match(EMAIL_REGEX, author_email):
        print(f"Invalid email: {author_email}")
        sys.exit(1)


if __name__ == "__main__":
    _validate_input()
