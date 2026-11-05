# 07-filehandling.py

# ===== WRITE A FILE =====
# Like fs.writeFileSync in Node.js!
with open("test.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("I am learning FastAPI and AI!\n")
    file.write("This is my AI journey!")

print("File written successfully!")

# ===== READ A FILE =====
# Like fs.readFileSync in Node.js!
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# ===== READ LINE BY LINE =====
with open("test.txt", "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")

# ===== APPEND TO FILE =====
# Like adding to existing file!
with open("test.txt", "a") as file:
    file.write("\nNew line added!")

print("Line appended!")

# ===== READ AFTER APPEND =====
with open("test.txt", "r") as file:
    print(file.read())

# ===== WRITE JSON FILE =====
# Very important for AI apps!
import json

data_details = {
    "name": "Shivendra",
    "role": "AI Engineer",
    "skills": ["React", "Python", "AI"],
    "tools": [
        {"name": "Groq", "free": True},
        {"name": "OpenAI", "free": False}
    ]
}

with open("data.json", "w") as file:
    json.dump(data_details, file, indent=4)

print("JSON file written!")

# ===== READ JSON FILE =====
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"])
    print(loaded_data["skills"])
    print(loaded_data["tools"])