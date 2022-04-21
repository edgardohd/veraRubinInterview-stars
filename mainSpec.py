import main
#
# from https://requests-mock.readthedocs.io/en/latest/pytest.html
def test(requests_mock):
    repo = "user/repoName"
    stars = 123456
    requests_mock.get(f"https://api.github.com/repos/{repo}", json={'stargazers_count': stars, 'anyOtherKey': 'anyOtherValue'})
    assert main.getStarsFromRepo("user/repoName") == stars
