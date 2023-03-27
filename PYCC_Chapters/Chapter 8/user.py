def build_user_profile(first, last, **user_info):
    """Build a profile with first and last name and other user info."""
    user_info['First Name'] = first
    user_info['Last Name'] = last
    return user_info

