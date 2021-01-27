from telethon import TelegramClient, sync, events 
# your api id 
api_id = 'XXXXX'
# your api hash 
api_hash = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# your phone number 
myphone = '+XXXXXXXXX'
# the number of resever you can just use account username 
resevers = '+ZZZZZZZZZ'
massge = "Hell word " 


def SendTelgramMasage(api_id, api_hash, myphone, resever, Masge,):
    client = TelegramClient('session', api_id, api_hash) 
    client.connect() 
    if not client.is_user_authorized(): 
        client.send_code_request(myphone) 
        client.sign_in(phone, input('Web login code: ')) 
    try: 
            client.send_message(resever, Masge) 
            return True 
    except Exception as err: 
        print(err); 
        return False
    client.disconnect()
    

SendTelgramMasage(api_id, api_hash, myphone, resevers, massge)
