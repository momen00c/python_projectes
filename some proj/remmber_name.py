import json

# وظيفة لاسترجاع اسم المستخدم المخزن
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

# وظيفة لطلب اسم مستخدم جديد
def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

# وظيفة لتحية المستخدم
def greet_user():
    username = get_stored_username()

    # التحقق من اسم المستخدم المخزن
    if username:
        print(f"Welcome back, {username}!")
        correct_username = input(f"Is {username} the correct username? (yes/no): ")
        if correct_username.lower() != 'yes':
            username = get_new_username()
    else:
        username = get_new_username()

    print(f"We'll remember you when you come back, {username}!")

# استدعاء الدالة
greet_user()
