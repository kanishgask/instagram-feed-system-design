from collections import defaultdict
import heapq
import time

class Instagram:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.timestamp = 0

    def post(self, user_id, post_id):
        self.timestamp += 1
        self.posts[user_id].append((self.timestamp, post_id))

    def follow(self, follower_id, followee_id):
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if followee_id in self.following[follower_id]:
            self.following[follower_id].remove(followee_id)

    def get_feed(self, user_id):
        feed = []
        users = self.following[user_id] | {user_id}

        for user in users:
            for post in self.posts[user]:
                feed.append(post)

        return [post_id for _, post_id in heapq.nlargest(10, feed)]


# Example
if __name__ == "__main__":
    app = Instagram()
    app.post(1, 101)
    app.post(2, 102)

    app.follow(3, 1)
    app.follow(3, 2)

    print(app.get_feed(3))
