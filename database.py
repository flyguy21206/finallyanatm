# This is the database
# Create a record
# Read record
# Update record
# Delete record
# CRUD
# Search records to find user

import os
import validation_user_account_number

user_db_path = "data/user_records/"


def create(account_number_from_user, first_name, last_name, email, password, ):

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(account_number_from_user):

        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(account_number_from_user) + ".txt", "x")

    except FileExistsError:

        file_contents = read(user_db_path + str(account_number_from_user) + ".txt")
        if not file_contents:
            delete(account_number_from_user)
        print("This file already exists")
        # delete(account_number_from_user)
        # check file exists

    else:

        f.write(str(user_data))
        completion_state = True
 
    finally:

        f.close()
        return completion_state

    # create a file
    # name of file would be account_number_from_user.txt
    # place file in data folder
    # add user details to the file
    # return true
    # close file


def update(account_number_from_user, balance):

    print("Update user record")
    
    # find user with account number
    # retrieve file contents
    # update file contents
    # save file
    # return True
    # close file


def read(account_number_from_user):
    # find user with account number
    # retrieve file contents
    # print file contents
    # close file
    is_valid_account_number = validation_user_account_number.account_number_validation(account_number_from_user)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(account_number_from_user) + ".txt", "r")
        else:
            f = open(user_db_path + account_number_from_user, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User already exists")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def delete(account_number_from_user):

    is_delete_successful = False

    if os.path.exists(user_db_path + str(account_number_from_user) + ".txt"):

        try:

            os.remove(user_db_path + str(account_number_from_user) + ".txt")
            is_delete_successful = True
            print("it worked")

        except FileNotFoundError:

            print("user does not exist")

        finally:
            print("ok")
            return is_delete_successful

    # find user with account number
    # retrieve file contents
    # delete user record(file)
    # return true if deleted
    # close file


def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number_from_user):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number_from_user) + ".txt":

            return True

    return False


def authenticated_user(account_number, password):

    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False


