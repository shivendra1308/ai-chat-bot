# 03-functions.py

# ===== BASIC FUNCTION =====
# JavaScript: function greet(name) { return `Hello ${name}` }
def greet(name):
    return f"Hello {name}"

print(greet("Shivendra"))

# ===== DEFAULT PARAMETERS =====
# JavaScript: function greet(name, role = "Developer") {}
def greet_with_role(name, role="Developer"):
    return f"Hello {name}, you are a {role}"

print(greet_with_role("Shivendra"))
print(greet_with_role("Shivendra", "AI Engineer"))

# ===== MULTIPLE RETURN VALUES =====
# JavaScript: return { name, age }  (object)
# Python can return multiple values directly!
def get_user_info():
    name = "Shivendra"
    age = 25
    role = "AI Engineer"
    return name, age, role

name, age, role = get_user_info()
print(f"Name: {name}, Age: {age}, Role: {role}")

# ===== ARROW FUNCTION = LAMBDA =====
# JavaScript: const add = (a, b) => a + b
add = lambda a, b: a + b
print(add(10, 20))

# ===== FUNCTION WITH LIST =====
def get_skills(skills):
    for skill in skills:
        print(f"Skill: {skill}")

get_skills(["React", "Python", "AI"])