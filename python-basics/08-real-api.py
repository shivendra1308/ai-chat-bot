# 09-mini-project.py
# Mini Project — AI Tools Dashboard
# Fetching real data from a public API!

from datetime import datetime
import requests
import json

# ===== FETCH REAL GITHUB USER DATA =====
def get_github_user(username   ):
    response = requests.get(f"https://api.github.com/users/{username}")
    
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "username": data["login"],
            "followers": data["followers"],
            "following": data["following"],
            "public_repos": data["public_repos"],
            
            "bio": data["bio"]
        }
    else:
        return None

# ===== FETCH USER REPOSITORIES =====
def get_github_repos(username  ):
    response = requests.get(
        f"https://api.github.com/users/{username}/repos"
    )
    
    if response.status_code == 200:
        repos = response.json()
        
        # Get top 5 repos by stars
        sorted_repos = sorted(
            repos,
            key=lambda r: r["stargazers_count"],
            reverse=True
        )
        
        return [
            {
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "language": repo["language"],
                "description": repo["description"]
            }
            for repo in sorted_repos[:5]
        ]
    else:
        return []

# ===== DISPLAY DASHBOARD =====
def display_dashboard(username ):
    print("=" * 50)
    print(f"  GITHUB DASHBOARD FOR: {username}")
    print("=" * 50)

    # Get user info
    user = get_github_user(username)
    
    if user:
        print(f"\n👤 Name        : {user['name']}")
        print(f"🔗 Username    : {user['username']}")
        print(f"👥 Followers   : {user['followers']}")
        print(f"➡️  Following   : {user['following']}")
        print(f"📁 Repos       : {user['public_repos']}")
        print(f"📝 Bio         : {user['bio']}")
    else:
        print("User not found!")
        return

    # Get repos
    print("\n" + "=" * 50)
    print("  TOP 5 REPOSITORIES")
    print("=" * 50)

    repos = get_github_repos(username  )
    
    total_stars = sum(repo["stars"] for repo in repos)
    print(f"\n⭐ Total Stars  : {total_stars}")

    for i, repo in enumerate(repos, start=1):
        print(f"\n{i}. {repo['name']}")
        print(f"   ⭐ Stars      : {repo['stars']}")
        print(f"   💻 Language   : {repo['language']}")
        print(f"   📝 Description: {repo['description']}")

    # Save to JSON file
    data = {
        "user": user,
        "top_repos": repos
    }

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"{username}_{timestamp}_dashboard.json", "w") as file:
        json.dump(data, file)

    print("\n" + "=" * 50)
    print(f"✅ Dashboard saved to {username}_{timestamp}_dashboard.json")
    print("=" * 50)

# ===== RUN IT =====
# Change this to any GitHub username!
# 
username = input("Enter GitHub username: ")
display_dashboard(username)