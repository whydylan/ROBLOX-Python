import requests

# Add everyone that you would like to keep on your friend(s) list! (User ID)

whitelist = []

# Enter the account cookie and detail(s) that you would like to use for unfriending!

details = {
    'Cookie' : "",
}

# From here on, this is code that should only be adjusted if you know what you are doing!

information = {
    'CSRF' : None,
    'Account' : None
}

# All function(s) that are to be used within this script to unfriend player(s) and grab friend(s) and more

def grabCSRFToken(Cookie: str):
    req = requests.post('https://auth.roblox.com/v1/authentication-ticket', headers = {"Cookie" : f".ROBLOSECURITY={Cookie}"})

    if 'x-csrf-token' in req.headers:
        csrfToken = req.headers['x-csrf-token']

        return csrfToken

    return None

def getUserFriends(ID: int):
    response = requests.get(f'https://friends.roblox.com/v1/users/{ID}/friends?userSort=0')

    if 'data' in response.json():
       return response.json()['data']
    
    return None

def grabUserAccountDetails(Cookie: str, CSRF: str):
    response = requests.get('https://users.roblox.com/v1/users/authenticated', cookies = {'.ROBLOSECURITY': Cookie, "X-CSRF-TOKEN": CSRF})
    
    if 'id' in response.json():
        return [response.json()['id'], response.json()['name']]
    
    return None

# The main script, which does the unfriending and grab(s) the CSRF token to use in the header(s).

information['CSRF'] = grabCSRFToken(details['Cookie'])
information['Account'] = grabUserAccountDetails(details['Cookie'], information['CSRF'])

if information['CSRF'] != None:
    for friend in getUserFriends(information['Account'][0]):
        if not friend['id'] in whitelist:
            response = requests.post(f"https://friends.roblox.com/v1/users/{friend['id']}/unfriend", headers = {"X-CSRF-TOKEN" : information['CSRF'], "Cookie" : f".ROBLOSECURITY={details['Cookie']}"})
            
            print(f'Removed Friend: {friend["displayName"]} (@{friend["name"]}) (ID: {friend["id"]})')

    print('Friend(s) list removal has been completed!')
else:
    print('There was an issue grabbing your CSRF token? (Cookie Invalid?)')




