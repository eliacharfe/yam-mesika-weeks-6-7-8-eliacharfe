

class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,

            # Add boolean 'read' key to check whether the user has read the message.
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, number_of_messages=0):
        """
        Get username and an optional parameter N for the first N messages to read from the inbox
        of the user. If the messages were not read yet, return the messages (the first N messages)
        if the messages were read already return nothing. If the N is not sent or it is bigger than
        the actual number of messages, return all messages in the inbox.
        :param username: The name of the user.
        :param number_of_messages: The number of messages to read from the first message.
        :return: List of the body of the N first messages (or all the messages in the inbox).
        """
        max_messages = self.boxes[username][-1]['id']
        if not number_of_messages or number_of_messages > max_messages:
            number_of_messages = max_messages
        list_messages = []
        for i in range(0, number_of_messages):
            if not self.boxes[username][i]['read']:
                list_messages.append(self.boxes[username][i]['body'])
                self.boxes[username][i]['read'] = True
        return list_messages


def show_example():
    """Show example of using the PostOffice class."""

    # Change from tuple to list because PostOffice expect a list and not a tuple
    users = ['Newman', 'Mr. Peanutbutter']
    post_office = PostOffice(users)
    post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='How are you?',
    )
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Newman'])

    print("Unread messages:")
    print(post_office.read_inbox('Newman'))
    print(post_office.read_inbox('Newman', 3))


if __name__ == '__main__':
    show_example()



# return [print(self.boxes[username][i]['body'] for i in range(0, number_of_messages)]