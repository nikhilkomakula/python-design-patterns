"""
The Observer pattern is used when a change in one object must be reflected in other objects without knowing how many objects need to be changed.
"""

class Observer:
    def update(self, message: str) -> None:
        raise NotImplementedError

class Subscriber(Observer):
    def __init__(self, name: str) -> None:
        self._name = name
    
    def update(self, message: str) -> None:
        print(f"{self._name} received: {message}")

class Blog:
    def __init__(self) -> None:
        self._subscribers = set()

    def add_subscriber(self, subscriber: Observer) -> None:
        self._subscribers.add(subscriber)

    def remove_subscriber(self, subscriber: Observer) -> None:
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, post: str) -> None:
        for subscriber in self._subscribers:
            subscriber.update(post)

    def write_post(self, post: str) -> None:
        self.notify_subscribers(post)


# create a blog post
my_blog = Blog()

# create subscriber objects
subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")

# add subscribers to blog
my_blog.add_subscriber(subscriber1)
my_blog.add_subscriber(subscriber2)

# write a new blog post
my_blog.write_post("My New Blog Post")