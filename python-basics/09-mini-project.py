# 1. Accept username as input from terminal
username = input("Enter GitHub username: ")
display_dashboard(username)

# 2. Add error handling if user not found
# 3. Add total stars count across all repos
# 4. Save with timestamp in filename
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# save as "shivendra1308_20241015_123456.json"