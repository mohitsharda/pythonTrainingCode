from session21C import MongoDbHelper
from session21A import User
users = User()

def main():
    print("Welcome To MongoDb Test App:")
    dbHelper = MongoDbHelper()

    """
    user = User()
    user.add_user_details()
    document = vars(user)
    dbHelper.insert(document)
    """

    # query = {"email": "mohit@example.com"}
    users = dbHelper.fetch()
    for user in users:
        print(user)


if __name__ == "__main__":
    main()
    