from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACaa5eab7ee62a7ce3eaa56459b5d38c69"
# Your Auth Token from twilio.com/console
auth_token  = "4b215ec813e01bc272da8597b4e40bf4"
client = Client(account_sid, auth_token)
call = client.calls.create(
    to="+15821994814",
    from_="+14782422580",
    url="http://demo.twilio.com/docs/voice.xml",
    method="GET",
    status_callback="https://www.myapp.com/events",
    status_callback_method="POST",
    status_callback_event=["initiated", "ringing", "answered", "completed"]
)
print(call.sid)
