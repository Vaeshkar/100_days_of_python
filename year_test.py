year = int(input("What's your year of birth? "))

# there is no range before 1980, resulting in None1994

# range of years 1980 till 1994
if year >= 1946 and year < 1965:
    print("You are a Baby Boomer.")
if year >= 1965 and year < 1980:
    print("You are a generation X.")
elif year >= 1980 and year <= 1994:
    print("You are a millennial.")
# range of years beyond 1994
elif year > 1994:
    print("You are a Gen Z.")
