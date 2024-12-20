# find-finder-frinder
python language....15 lines 
def find_common_friends(user1_friends, user2_friends):
    """
    Finds the common friends between two users.

    parameters:
        user1_friends (list): List of friends for user 1.
        user2_friends (list): List of friends for user 2.

    Returns:
        list: A list of common friends.
    """
    # Convert the lists to sets to find the intersection
    common_friends = set(user1_friends).intersection(user2_friends)
    
    # Convert the set back to a list for the result
    return list(common_friends)
if __name__ == "__main__":
    # Friends lists for two users
    user1_friends = ["shivendu","anshu","ritik","atul"]
    user2_friends = ["mohit","atul","rohit","shivendu"]
    common = find_common_friends(user1_friends, user2_friends)
    print("Common friends:", common)
