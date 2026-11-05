# 06-classes.py

# ===== CLASS BASICS =====
# JavaScript:
# class User {
#     constructor(name, age) {
#         this.name = name
#         this.age = age
#     }
# }

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name} and I am {self.age} years old"

    def is_adult(self):
        return self.age >= 18

# Create object
# JavaScript: const user = new User("Shivendra", 25)
user = User("Shivendra", 25)

print(user.greet())
print(user.is_adult())

# ===== CLASS WITH DEFAULT VALUES =====
class AITool:
    def __init__(self, name, company, free=False):
        self.name = name
        self.company = company
        self.free = free

    def describe(self):
        status = "Free" if self.free else "Paid"
        return f"{self.name} by {self.company} — {status}"

# Create objects
groq = AITool("Groq", "Groq Inc", free=True)
chatgpt = AITool("ChatGPT", "OpenAI", free=False)
gemini = AITool("Gemini", "Google", free=True)

print(groq.describe())
print(chatgpt.describe())
print(gemini.describe())

# ===== LIST OF OBJECTS =====
tools = [groq, chatgpt, gemini]

# Get only free tools
free_tools = [tool for tool in tools if tool.free]
for tool in free_tools:
    print(tool.describe())

# ===== INHERITANCE =====
# JavaScript: class PremiumUser extends User {}
class Developer(User):
    def __init__(self, name, age, skills):
        super().__init__(name, age)  # JavaScript: super(name, age)
        self.skills = skills

    def introduce(self):
        return f"I am {self.name}, I know {', '.join(self.skills)}"

dev = Developer("Shivendra", 25, ["React", "Python", "AI"])
print(dev.introduce())
print(dev.greet())  # inherited from User!