print("Please enter your first name:")
username = input()
print(f"Greetings, {username}! What's the tip total for this week?")
weeks_tips = input()
print(f"{weeks_tips}! That's quite a hefty sum! Let's get that divvied up, shall we? \nHow many hours has the crew worked in total?")
crew_hours = input()
tip_hourly = float(weeks_tips)/float(crew_hours)
print(
    f"Alrighty! The hourly rate's looking like ${tip_hourly}\nNow for the payout! Who's getting tipped?")
username2 = input()
print(f"How many hours has {username2} worked?")
u2_hours = input()
u2_tips = float(tip_hourly)*float(u2_hours)
print(f"Looks like {username2} gets ${u2_tips}. Lucky them!")
