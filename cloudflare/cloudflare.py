import requests, os, json
from dotenv import load_dotenv

### load env vars from .env
load_dotenv()

email = os.getenv('USER_EMAIL')
apikey = os.getenv('API_KEY')
zone = os.getenv('ZONE_ID')

headers = {
    'X-Auth-Email': email,
    'Authorization': 'Bearer ' + apikey,
    'Content-Type': 'application/json',
}

### determine list of pool names, list all pool ids for zone

def fetch_pools():
  response = requests.get('https://api.cloudflare.com/client/v4/accounts/' + zone + '/load_balancers/pools', headers=headers)
  j = response.json()
  if j["success"]:
    global pool_id
    pool_id = []
    for i in range(len(j["result"])):
      pool_id.append(j["result"][i]["id"])
  else: #print the errors returned if request fails
      print(j["errors"])
  print('Determined available pool ids: ' + str(pool_id))

### query status of all pools, determine if enabled or disabled

def fetch_pool_status(pool_id):
  #print(len(pool_id))
  global pool_status
  pool_status = {}
  for i in range(len(pool_id)):
    response = requests.get('https://api.cloudflare.com/client/v4/accounts/' + zone + '/load_balancers/pools/' + pool_id[i], headers=headers)
    j = response.json()
    if j["success"]:
      pool_status[i] = {
                "pool_id": j["result"]["id"],
                "pool_name": j["result"]["name"],
                "enabled": str(j["result"]["enabled"])
              }
    else:
      print(j["errors"])

### user input: choose pool and determine action

def user_choose_pool(pool_status):
  for i in range(len(pool_status)):
    print(i, pool_status[i])
  while True:
    global pool_choice
    pool_choice = input('Choose available pool index value above: ')
    if int(pool_choice) in range(len(pool_status)):
      # debug  
      #print('Pool id chosen was ' + pool_status[int(pool_choice)]["pool_id"] + ': ' + pool_status[int(pool_choice)]["pool_name"])
      break
    else:
      print('Pool selection not available')

#def change_pool_status(pool_status, pool_choice):
  


### check status of pools after changes to verify
    
fetch_pools()
fetch_pool_status(pool_id)
user_choose_pool(pool_status)
#change_pool_status(pool_status, pool_choice)
