import instaloader
from datetime import *

def main():
    load = instaloader.Instaloader()

    # Login or load session
    username = "USERNAME"
    password = "PASSWORD"
    load.login(username, password)        # (login)

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(load.context, username)
    choice = int(input("1. See who doesn't follow you back. \n2. See who hasn't liked any of your posts.\n"))
    if choice == 1:
        # GET FOLLOWERS AND FOLLOWING
        followers = getFollowers(profile)
        following = getFollowing(profile)

        # Get people who don't follow me back
        mismatch = difference(following, followers)
        for x in mismatch:
            print(x)
    elif choice == 2:
        #seeGhosts(username, profile)
        getSpecificPosts(username, load)

def getFollowers(profile):
    # Print list of followers
    count = 0
    followers = []
    print("Retrieving followers...")
    for followee in profile.get_followers():
        followers.append(followee.username)
        count = count + 1
    print("Follower Count:", count)
    return followers

def getFollowing(profile):
    # Print list of following
    count = 0
    following = []
    print("Retrieving following...")
    for follower in profile.get_followees():
        following.append(follower.username)
        count = count + 1
    print("Following Count:", count)
    return following

def difference(list1, list2):
    """
    Returns the elements in list1 that are not in list2.

    Parameters:
    list1 (list): The first list.
    list2 (list): The second list.

    Returns:
    list: A list of elements from list1 that are not in list2.
    """
    unique_items = []
    for item in list1:
        if item not in list2:
            unique_items.append(item)
    return unique_items

def seeGhosts(user, profile):
    # Load session previously saved with `instaloader -l USERNAME`:
    likes = set()
    print("Fetching likes of all posts of profile {}.".format(profile.username))
    for post in profile.get_posts():
        likes = likes | set(post.get_likes())

    print("Fetching followers of profile {}.".format(profile.username))
    followers = set(profile.get_followers())

    ghosts = followers - likes

    print("Storing ghosts into file.")
    with open("inactive-users.txt", 'w') as f:
        for ghost in ghosts:
            print(ghost.username, file=f)

def getSpecificPosts(user,load):
    posts = instaloader.Profile.from_username(load.context, user).get_posts()

    SINCE = datetime(2020, 5, 1)
    UNTIL = datetime(2023, 3, 1)

    for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
        print(post.date)
        L.download_post(post, "instagram")

if __name__ == "__main__":
    main()
