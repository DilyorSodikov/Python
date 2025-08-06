import re
import time
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import pytz

# 1. Age Calculator
def age_calculator():
    birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
        today = date.today()
        diff = relativedelta(today, birth_date)
        print(f"You are {diff.years} years, {diff.months} months, and {diff.days} days old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# 2. Days Until Next Birthday
def days_until_next_birthday():
    birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
        today = date.today()
        next_birthday = birth_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        days_remaining = (next_birthday - today).days
        print(f"{days_remaining} day(s) until your next birthday.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# 3. Meeting Scheduler
def meeting_scheduler():
    current_dt_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))
    try:
        current_dt = datetime.strptime(current_dt_str, "%Y-%m-%d %H:%M")
        end_dt = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)
        print(f"The meeting will end at: {end_dt}")
    except ValueError:
        print("Invalid date/time format.")

# 4. Timezone Converter
def timezone_converter():
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz_str = input("Enter your current timezone (e.g., Asia/Tashkent): ")
    to_tz_str = input("Enter target timezone (e.g., America/New_York): ")
    try:
        naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        from_tz = pytz.timezone(from_tz_str)
        to_tz = pytz.timezone(to_tz_str)
        local_dt = from_tz.localize(naive_dt)
        target_dt = local_dt.astimezone(to_tz)
        print(f"Converted time: {target_dt.strftime('%Y-%m-%d %H:%M')} in {to_tz_str}")
    except Exception as e:
        print("Error in conversion:", e)

# 5. Countdown Timer
def countdown_timer():
    target_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    try:
        target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
        while True:
            now = datetime.now()
            if target_time <= now:
                print("Time's up!")
                break
            remaining = target_time - now
            print(f"Time remaining: {remaining}", end="\r")
            time.sleep(1)
    except ValueError:
        print("Invalid datetime format.")

# 6. Email Validator
def email_validator():
    email = input("Enter email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email.")
    else:
        print("Invalid email.")

# 7. Phone Number Formatter
def phone_number_formatter():
    number = input("Enter 10-digit phone number (e.g., 1234567890): ")
    cleaned = re.sub(r'\D', '', number)
    if len(cleaned) == 10:
        formatted = f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
        print("Formatted number:", formatted)
    else:
        print("Invalid number.")

# 8. Password Strength Checker
def password_strength_checker():
    password = input("Enter password: ")
    strength = []
    if len(password) >= 8:
        strength.append("✔️ Minimum length")
    else:
        strength.append("❌ Minimum length")
    if re.search(r'[A-Z]', password):
        strength.append("✔️ Uppercase letter")
    else:
        strength.append("❌ Uppercase letter")
    if re.search(r'[a-z]', password):
        strength.append("✔️ Lowercase letter")
    else:
        strength.append("❌ Lowercase letter")
    if re.search(r'\d', password):
        strength.append("✔️ Digit")
    else:
        strength.append("❌ Digit")
    print("\nPassword strength check:")
    for s in strength:
        print(s)

# 9. Word Finder
def word_finder():
    text = input("Enter text: ")
    word = input("Enter word to find: ")
    matches = [m.start() for m in re.finditer(rf'\b{re.escape(word)}\b', text, re.IGNORECASE)]
    if matches:
        print(f"'{word}' found at positions: {matches}")
    else:
        print(f"No occurrences of '{word}' found.")

# 10. Date Extractor
def date_extractor():
    text = input("Enter text: ")
    pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b'
    dates = re.findall(pattern, text)
    if dates:
        print("Dates found:", dates)
    else:
        print("No dates found.")

# Menu to run each task
def main():
    tasks = {
        "1": ("Age Calculator", age_calculator),
        "2": ("Days Until Next Birthday", days_until_next_birthday),
        "3": ("Meeting Scheduler", meeting_scheduler),
        "4": ("Timezone Converter", timezone_converter),
        "5": ("Countdown Timer", countdown_timer),
        "6": ("Email Validator", email_validator),
        "7": ("Phone Number Formatter", phone_number_formatter),
        "8": ("Password Strength Checker", password_strength_checker),
        "9": ("Word Finder", word_finder),
        "10": ("Date Extractor", date_extractor),
    }

    while True:
        print("\n--- Homework Tasks ---")
        for k, v in tasks.items():
            print(f"{k}. {v[0]}")
        print("0. Exit")

        choice = input("Choose a task (0-10): ")
        if choice == "0":
            break
        task = tasks.get(choice)
        if task:
            print(f"\nRunning: {task[0]}")
            task[1]()  # Run the function
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
