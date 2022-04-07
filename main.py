# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from pprint import pprint




def main():

    username = "EbookFoundation"
    repo = "free-programming-books"
    url = f"https://api.github.com/repos/{username}/{repo}"
    user_data = requests.get(url).json()
    stars_count = user_data['stargazers_count']
    print(stars_count)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
