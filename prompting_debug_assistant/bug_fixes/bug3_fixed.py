def get_user_age(users, name):
    if name not in users:
        return None
    return users[name]["age"]


def main():
    users = {
        "alice": {"age": 30},
        "bob": {"age": 25},
    }
    assert get_user_age(users, "alice") == 30
    assert get_user_age(users, "bob") == 25
    assert get_user_age(users, "charlie") is None
    print("alice:", get_user_age(users, "alice"))
    print("charlie:", get_user_age(users, "charlie"))
    print("All bug3 tests passed")


main()