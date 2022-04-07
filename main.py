#Edgardo Huaracan 2022
import requests
import yaml

def main():
    dict = {}
    repos = ['freeCodeCamp/freeCodeCamp', '996icu/996.ICU', 'EbookFoundation/free-programming-books']
    # copied from https://www.thepythoncode.com/article/using-github-api-in-python
    for repo in repos:
        dict[repo] = getStarsFromRepo(repo)
    output = yaml.dump(dict, default_flow_style=False)
    print(output)
    return yaml.dump(output)

def getStarsFromRepo(repo):
    url = f"https://api.github.com/repos/{repo}"
    user_data = requests.get(url).json()
    stars_count = user_data['stargazers_count']
    #print(repo + ":" + str(stars_count))
    return stars_count


if __name__ == '__main__':
    main()

