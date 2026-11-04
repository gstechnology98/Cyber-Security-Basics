is_active = True 
is_loggoin = False

user_profile = None

if is_active and not is_loggoin:
    print("User is active but not logged in.")


if user_profile is None:
    print("User profile is not set.")