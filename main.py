# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests




def main():
    repos = ['freeCodeCamp/freeCodeCamp', '996icu/996.ICU', 'EbookFoundation/free-programming-books']
    # copied from https://www.thepythoncode.com/article/using-github-api-in-python
    for repo in repos:
        url = f"https://api.github.com/repos/{repo}"
        user_data = requests.get(url).json()
        stars_count = user_data['stargazers_count']
        print(repo + ":" + str(stars_count))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
