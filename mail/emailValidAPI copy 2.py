# pip install pyIsEmail==1.0.1
import requests
from key
# from email_validator import validate_email, EmailNotValidError

email = "my+aasdfddress@example.org"

def validate(email):
    try:

        # Check that the email address is valid. Turn on check_deliverability
        # for first-time validations like on account creation pages (but not
        # login pages).
        emailinfo = validate_email(email, check_deliverability=False)
        

        # After this point, use only the normalized form of the email address,
        # especially before going to a database query.
        email = emailinfo.normalized
        print(f"{email} is valid")
    except EmailNotValidError as e:

        # The exception message is human-readable explanation of why it's
        # not a valid (or deliverable) email address.
        print(str(e))
        print(f"{email} is invalid")

validate(email)