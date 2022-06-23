email_id = input("Please enter your email id:\n").strip()

username = email_id[:email_id.index('@')]

domain = email_id[email_id.index('@')+1:]

print(f"Your user name is {username} and your domain name {domain}")