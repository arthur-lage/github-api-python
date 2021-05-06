import requests

def get_data(user):
    api_url = "https://api.github.com/users/{}".format(user)
    response = requests.get(api_url)
    data = response.json()

    avatar = data["avatar_url"]
    user = data["login"]
    followers = data["followers"]
    following = data["following"]
    public_repos = data["public_repos"]

    print(f"""
    |===============================================================|
    |                      GITHUB PROFILE DATA                      |
    |===============================================================|
        User: {user}                                               
        Avatar: {avatar}                                           
        Followers: {followers}                                     
        Following: {following}                                     
        Public Repositories: {public_repos}                        
    |===============================================================|
    """)

get_data("arthur-lage")
