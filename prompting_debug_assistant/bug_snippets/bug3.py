def get_user_age(users, name):
    return users[name]["age"]


def main():
    users = {
        "alice": {"age": 30},
        "bob": {"age": 25},
    }
    print(get_user_age(users, "alice"))
    print(get_user_age(users, "charlie"))


main()