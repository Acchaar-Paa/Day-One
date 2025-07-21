# 🎮 PROJECT NAME: ATM MACHINE SIMULATOR (No GUI — Pure Terminal)
# 🔓 Concept:
# Simulate a basic ATM machine — the kind you'd see in real life — using just what you’ve learned (Variables, Strings, Loops, Conditionals, Functions, Lists/Dictionaries).

# You will build logic of an actual ATM:
# Deposit, Withdraw, Check Balance, PIN system, and basic security.

# 💡 FEATURES TO BUILD:
# ✅ 1. Login System with PIN
# Ask user to enter a 4-digit PIN

# If correct → proceed

# If wrong → allow 3 attempts then lock the session

# ✅ 2. Main Menu
# Show options:

# markdown
# Copy
# Edit
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Transaction History
# 5. Exit
# Use loop until they choose exit.

# ✅ 3. Balance System
# Set initial balance to ₹5000

# When depositing, add to balance

# When withdrawing, subtract

# If withdrawal is more than balance → show error

# ✅ 4. Transaction History
# Store each deposit/withdrawal in a list:

# python
# Copy
# Edit
# ["Deposited ₹1000", "Withdrew ₹500"]
# Show this if user selects that option.

# ✅ 5. Functions
# Each action (check balance, deposit, withdraw, etc.) must be a separate function. Prove you understood chapter 8.

# ✅ 6. Exit Confirmation
# When exiting, ask: “Are you sure? (yes/no)”
# If “no” → return to menu
# If “yes” → show “Thank you. Goodbye 👋”

# 🧠 WHAT THIS PROJECT TESTS YOU ON:
# Deep real-world logic

# Data tracking (history list)

# Loops, If-Else

# Functions + return

# Error handling (wrong pin, wrong input)

# Thinking like a real developer

# 🎉 BONUS IDEAS (if you want to go further):
# Allow changing the PIN

# Add fake delay using for loop with dots (print(".", end=""))

# Support multiple users with dictionary like:

# python
# Copy
# Edit
# accounts = {
#     "1234": {"balance": 5000, "history": []},
#     "5678": {"balance": 8000, "history": []}
# }