# OOP Chat System
#1. User Class

class User:

    def __init__(self, username):
        self.username = username

    def join_chat(self, chatroom):
        chatroom.add_user(self)

    def leave_chat(self, chatroom):
        chatroom.remove_user(self)

    def send_message(self, chatroom, content):
        chatroom.send_message(self, content)


#2. Message Class
class Message():

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def display_message(self):
        print(self.sender.username + " : " + self.content)

# 3. ChatRoom Class

class ChatRoom:

    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def add_user(self, user):

        if user not in self.users:
            self.users.append(user)
            print(user.username, "joined the chatroom.")

        else:
            print(user.username, "is already in the chatroom.")

    def remove_user(self, user):

        if user in self.users:
            self.users.remove(user)
            print(user.username, "left the chatroom.")

        else:
            print(user.username, "is not in the chatroom.")

    def send_message(self, sender, content):

        if sender in self.users:

            message = Message(sender, content)

            self.messages.append(message)

            print(sender.username, "sent a message.")

        else:
            print(sender.username, "is not in the chatroom.")

    def show_history(self):

        print("\n--- Chat History ---")

        if len(self.messages) == 0:
            print("No messages yet.")

        else:
            for message in self.messages:
                message.display_message()


# Main Program

# Create users

user1 = User("Vijay")
user2 = User("Rahul")
user3 = User("Anil")


# Create chatroom

chatroom = ChatRoom("Python Chat")


# Users join the chatroom

user1.join_chat(chatroom)
user2.join_chat(chatroom)
user3.join_chat(chatroom)


# Users send messages

user1.send_message(chatroom, "Hello everyone!")

user2.send_message(chatroom, "Hi Vijay!")

user3.send_message(chatroom, "Hello guys!")


# Display chat history

chatroom.show_history()


# Rahul leaves the chatroom

user2.leave_chat(chatroom)


# Rahul tries to send a message after leaving

user2.send_message(chatroom, "I am back!")


# Display chat history again

chatroom.show_history()
