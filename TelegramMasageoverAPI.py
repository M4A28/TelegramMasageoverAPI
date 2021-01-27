from telethon import TelegramClient, sync, events 

api_id = 'XXXXX'
api_hash = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
myphone = '+XXXXXXXXX'
massge = "Hell word " 
resevers = '+ZZZZZZZZZ'

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
