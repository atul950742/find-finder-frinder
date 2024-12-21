def find_common_friends(user1_friends, user2_friends):
    """
    Parameters:
    user1_friends (list): List of friends for user 1.
    user2_friends (list): List of friends for user 2.
    Returns:
    list: A list of common friends.
    """
    common_friends = set(user1_friends).intersection(user2_friends)
    return list(common_friends)
if __name__ == "__main__":
    user1_friends = ["shivendu","anshu","ritik","atul"]
    user2_friends = ["mohit","atul","rohit","shivendu"]
    common = find_common_friends(user1_friends, user2_friends)
    print("Common friends:", common)
