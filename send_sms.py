from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACde7cb3f61cb74e0b3a780f971587afd9"
# Your Auth Token from twilio.com/console
auth_token  = "576edad0db53953149ae648cfe91ba00"


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16318383229", #the phone number to send the message to
    from_="+19166941490", #DO NOT CHANGE
    body="Hello Laura. How are you today? Would you like some food?") #Message to Send. Should indclude. Someone needs help and what they need. 

print(message.sid)


