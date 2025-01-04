# #52.	Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh

email = "nitish24singh@gmail.com"

# Split the email at the '@' symbol and take the first part
username = email.split('@')[0]

print(f"The username is: {username}")
