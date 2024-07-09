from session21C import MongoDbHelper
from session21A import User
from tabulate import tabulate

def main():
    print("Welcome To MongoDb Test App:")
    dbHelper = MongoDbHelper()
    
    """    users = User()
    users.addUserDetail()
    document = vars(users)
    dbHelper.insert(document)
    """

    # query = {"email": "mohit@example.com"}
    users = dbHelper.fetch()
    for user in users:
        print(user)


if __name__ == "__main__":
    main()
    