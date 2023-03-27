def build_user_profile(first, last, **user_info):
    """Build a profile with first and last name and other user info."""
    user_info['First Name'] = first
    user_info['Last Name'] = last
    return user_info


me_profile = build_user_profile('Aaron', 'Brazier', City= 'Burlington', Country= 'Canada',
            Job= 'Tech Guy', )

him_profile = build_user_profile('Ryan', 'Bobart', Job= 'Clown', height= '5feet, '
              '3 inches',DOB= '09/11/1976')

print(me_profile)
print(him_profile)