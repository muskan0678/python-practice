# Emoji Converter - Basic Version ( no if , no loop)

msg = input("Enter your message: ")

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "😒")
msg = msg.replace(":D", "😁")
msg = msg.replace(":)", "😘")

print(msg)