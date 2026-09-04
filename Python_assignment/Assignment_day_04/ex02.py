class InvalidPhoneNumberError(Exception):
    pass


def register_contact(phonebook, name, phone_input):

    # Name validation
    if not isinstance(name, str) or not name or not all(
        ch.isalpha() or ch == " " for ch in name
    ):
        raise ValueError(
            "Contact name must be a non-empty alphabetic string."
        )

    
    try:
        int(phone_input)

        if len(phone_input) != 10:
            raise InvalidPhoneNumberError(
                "Phone number must contain exactly 10 digits."
            )

    except ValueError:
        raise InvalidPhoneNumberError(
            "Phone number must contain digits only."
        )

    
    phonebook[name] = phone_input

    return phonebook


phonebook = {}

name = input("Enter contact name: ")
phone_input = input("Enter phone number: ")

try:
    register_contact(phonebook, name, phone_input)
    print("Contact registered successfully!")
    print(phonebook)

except ValueError as e:
    print(e)

except InvalidPhoneNumberError as e:
    print(e)