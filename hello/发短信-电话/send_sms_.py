from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACaa5eab7ee62a7ce3eaa56459b5d38c69"
# Your Auth Token from twilio.com/console
auth_token  = "4b215ec813e01bc272da8597b4e40bf4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8613162062568",
    from_="+14782422580",
    body="逗比，快看短信")

print(message.sid)