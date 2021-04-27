

def account_number_validation(account_number_from_user):

    if account_number_from_user:

        try:
            int(account_number_from_user)

            if len(str(account_number_from_user)) == 10:
                return True

        except ValueError:
            print("Could not locate Account Number.")
            print("Please verify and try again, or register for access")
            return False

        except TypeError:
            print("Account number entered is in invalid format")
            print("Please verify and try again, or register for access")
            return False

        else:
            print('Account Number must be 10 digits')
            return False

# def validate_registration_entered(input):
    # check if list
    # check each item in list to ensure they are correct data types

# def validate_password_entered(input):
# check if string
# check if matches database

# def validate_welcome_question(input):
    # check if int
    # show error message if not correct data type, prevent TypeError

# def validate_main_Menu_option(input):
# check if int
# show error message if not correct data type, prevent TypeError
