# Imagine these are chat messages from your AI chat app!
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "I am great!"},
]

# Get only user messages
# JavaScript: messages.filter(m => m.role === "user")
user_messages = [m for m in messages if m["role"] == "user"]
print(user_messages)

# Get only content from all messages
# JavaScript: messages.map(m => m.content)
contents = [m["content"] for m in messages]
print(contents)
# ['Hello', 'Hi there!', 'How are you?', 'I am great!']

# Get content of user messages only
user_contents = [m["content"] for m in messages if m["role"] == "user"]
print(user_contents)
# ['Hello', 'How are you?']