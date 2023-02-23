from twilio.rest import Client

# Account SID, Auth Token, and WhatsApp sandbox phone number
account_sid = 'AC961e3ccfe8aefb21fda61415e2b769b9' 
auth_token = 'c9634ab0b1c5043621b3668eed8546a3'
twilio_number = '+18609011642'


def send_message(workout):
    ''' Initializes a Twilio client, and sends the workout's details as an SMS. '''
    client = Client(account_sid, auth_token)
 
    message = client.messages.create( 
                from_=twilio_number,
                body=workout.to_str(),      
                to='+4915127014722' 
                )
    print(message.sid)
