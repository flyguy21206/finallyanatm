# This is latest ATM project for Re-skill Americans-FINAL

import random
import validation_user_account_number
import database
from getpass import getpass
import os
from datetime import datetime


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def register():
    print("****Register*****")

    first_name = input("Please enter your first name? \n")
    last_name = input("Please enter your last name? \n")
    email = input("Please enter your email address? \n")
    password = getpass("Please create a password \n")

    account_number = generate_account_number()

    is_new_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_new_user_created:
        # using database module to create and store user record
        print("Your Account has been created")
        print(" ** ==== **** ===== ****")
        print("Your account number is: %d" % account_number)
        print("Please login to make a transaction")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong. Please try again")
        init()


def init():
    print("Welcome to Your Favorite Bank")
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    print("Today's date is " + dt_string)
    have_account = int(input("Do you have an account with us? 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    elif ValueError:
        print("Please select a valid option")
        init()

    elif TypeError:
        print("Please select a valid option")
        init()

    else:
        print('Invalid option, Please try again')
        init()


def deposit_operation(user, account_number_from_user):
    current_user_balance = user[4]
    balance_before_deposit = float(current_user_balance)
    try:
        deposit_amount = input("How much would you like to deposit? \n")
        deposit_amount = float(deposit_amount)
    except ValueError:
        print("please select a valid amount")
        deposit_operation(user, account_number_from_user)
    except TypeError:
        print("please select a valid amount")
        deposit_operation(user, account_number_from_user)
    else:
        new_user_balance = (balance_before_deposit + deposit_amount)
        updated_user_details = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(new_user_balance)
        user_db_path = "data/user_records/"
        with open(user_db_path + str(account_number_from_user) + ".txt", "w") as bank_files:

            bank_files.write(str(updated_user_details))
            print("Your new balance is " + str(new_user_balance))
            bank_files.close()

            logout(account_number_from_user)


def withdrawal_operation(user, account_number_from_user):
    current_user_balance = user[4]
    balance_before_withdraw = float(current_user_balance)

    try:
        withdrawal_amount = input("How much would you like to Withdraw? \n")
        formatted_amount = float(withdrawal_amount)
        if balance_before_withdraw < formatted_amount:
            print("Insufficient funds")
            main_menu(user, account_number_from_user)
    except ValueError:
        print("please select a valid amount")
        withdrawal_operation(user, account_number_from_user)
    except ValueError:
        print("please select a valid amount")
        withdrawal_operation(user, account_number_from_user)
    else:
        bal_after_withdraw = (balance_before_withdraw - formatted_amount)
        updated_user_details = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(bal_after_withdraw)
        user_db_path = "data/user_records/"
        with open(user_db_path + str(account_number_from_user) + ".txt", "w") as bank_files:

            bank_files.write(str(updated_user_details))
            print("Your new balance is " + str(bal_after_withdraw))
            bank_files.close()
            logout(account_number_from_user)


def current_balance_displayed(user, account_number_from_user):
    print("Your current balance is " + user[4])
    main_menu(user, account_number_from_user)


def logout(account_number_from_user):
    print("Have a nice day!")
    delete_auth_file(account_number_from_user)
    init()


def create_auth_file(account_number_from_user):
    user_auth_path = "data/auth_sessions/"
    with open((user_auth_path + "active" +
               str(account_number_from_user) + ".txt"), "w") as new_auth:
        new_auth.write("is logged in")
        new_auth.close()


def delete_auth_file(account_number_from_user):
    user_auth_path = "data/auth_sessions/"
    os.remove(user_auth_path + "active" + str(account_number_from_user) + ".txt")


def main_menu(user, account_number_from_user):

    create_auth_file(account_number_from_user)

    print("Hello " + (user[0]))

    selected_option = int(input("Please select an option (1) Deposit (2) Withdrawal (3) Balance (4) Logout  \n"))

    if selected_option == 1:

        deposit_operation(user, account_number_from_user)
    elif selected_option == 2:

        withdrawal_operation(user, account_number_from_user)
    elif selected_option == 3:

        current_balance_displayed(user, account_number_from_user)
    elif selected_option == 4:

        logout(account_number_from_user)
    elif ValueError:

        print("Please select a valid option")
        main_menu(user, account_number_from_user)
    elif TypeError:

        print("Please select a valid option")
        main_menu(user, account_number_from_user)
    else:

        print("Invalid option selected")
        main_menu(user, account_number_from_user)


def login():
    print("Please login to your account")

    account_number_from_user = input("Please enter your account number? \n")

    is_valid_account_number = validation_user_account_number.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("Please enter your password? \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:

            main_menu(user, account_number_from_user)

        else:
            print("Login failed")
            print("Please check your account number and password and try again")

        return account_number_from_user


init()
