# 02-datatypes.py

# ===== ARRAYS = LISTS =====
# JavaScript: const skills = ["React", "JS", "CSS"]
skills = ["React", "JS", "CSS", "Python"]

print(skills)
print(skills[0])        # React
print(len(skills))      # 4 (length)

# Add item
# JavaScript: skills.push("FastAPI")
skills.append("FastAPI")
print(skills)

# Remove item
# JavaScript: skills.pop()
skills.pop()
print(skills)

# Loop through
# JavaScript: skills.forEach(skill => console.log(skill))
for skill in skills:
    print(skill)

# ===== OBJECTS = DICTIONARIES =====
# JavaScript: const user = { name: "Shivendra", age: 25 }
user = {
    "name": "Shivendra",
    "age": 25,
    "skills": ["React", "Python"],
    "is_developer": True
}

print(user)
print(user["name"])         # Shivendra
print(user["skills"])       # ['React', 'Python']

# Add new key
# JavaScript: user.salary = 50000
user["salary"] = 50000
print(user)

# Loop through object
# JavaScript: Object.keys(user).forEach(key => ...)
for key, value in user.items():
    print(f"{key} → {value}")