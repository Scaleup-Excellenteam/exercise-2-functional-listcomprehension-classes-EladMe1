class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def read_inbox(self, username, num_messages=None):
        # Retrieve the user's inbox
        inbox = self.boxes[username]
        # Check if the inbox is empty
        if not inbox:
            return []
        # Determine the number of messages to read
        if num_messages is None:
            num_messages = len(inbox)
        # Retrieve the specified number of messages from the inbox
        messages_to_read = inbox[-num_messages:]
        for message in messages_to_read:
            # Mark the retrieved messages as read
            message['read'] = True
        return messages_to_read

    def search_inbox(self, username, search_string):
        # Get the user's inbox, or an empty list if the user doesn't exist
        inbox = self.boxes.get(username, [])
        # Use a list comprehension to filter messages that contain the search string in the body or title
        result = [message for message in inbox if search_string in message['body'] or search_string in message['title']]

        return result

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        if recipient not in self.boxes:
            raise KeyError("Recipient does not exist.")
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': f"Message from {sender}",
            'body': message_body,
            'sender': sender,
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id
