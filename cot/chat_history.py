class Node:
    def __init__(self, message, next=None):
        self.message = message
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, message):
        if not self.head:
            self.head = Node(message)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(message)

    def get_all_messages(self):
        messages = []
        current = self.head
        while current:
            messages.append(current.message)
            current = current.next
        return messages
    
    def find_message(self, keyword):
        """
        Find the most recent message containing the specified keyword.
        """
        current = self.head
        last_match = None
        while current:
            if keyword in current.message:
                last_match = current.message
            current = current.next
        return last_match
    
    def get_message_by_index(self, index):
        """
        Get the message at a specific index (0-based).
        """
        current = self.head
        current_index = 0
        while current:
            if current_index == index:
                return current.message
            current = current.next
            current_index += 1
        return None


# Create an instance of LinkedList
chat_history = LinkedList()

# Append some messages
chat_history.append("User: Hi!")
chat_history.append("Bot: Hello! How can I help you today?")
chat_history.append("User: I need help with cybersecurity.")
chat_history.append("Bot: What specific cybersecurity issue are you facing?")

# Get all messages
print(chat_history.get_all_messages())

# Find a message containing a keyword
print(chat_history.find_message("cybersecurity"))

# Get a message by index
print(chat_history.get_message_by_index(1))  # 0-based index

