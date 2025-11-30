
email = input("Enter your Email: ")

index = email.index("@")

username = email[:index]
domain = email[index:]

print(f"Your username is {username} and domain is {domain}")