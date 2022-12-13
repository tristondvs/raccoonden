import requests, os, json, sys
from dotenv import load_dotenv

### load env vars from .env
### can we load any or all of these credentials in aws parameter store?
### for now, manually provide list of pool_ids for the specified zone
load_dotenv()

email = os.getenv('USER_EMAIL')
apikey = os.getenv('API_KEY')
zone = os.getenv('ZONE_ID')
pool_ids=['', '']

# accept params passed during execution
pool_nick = sys.argv[1]
action = sys.argv[2]

# modify header
headers = {
    'X-Auth-Email': email,
    'Authorization': 'Bearer ' + apikey,
    'Content-Type': 'application/json',
}

def main(pool_nick, action):
  # define data based on action provided
  if action == 'enable':
    data = '{"enabled": true}'
  elif action == 'disable':
    data = '{"enabled": false}'
  # determine pool id for provided pool name, query aws parameter store for json object?
  # for now we define the json object and later parse it for pool_id
  pool_status = {}
  for i in range(len(pool_ids)):
    response = requests.get('https://api.cloudflare.com/client/v4/accounts/' + zone + '/load_balancers/pools/' + pool_ids[i], headers=headers)
    j = response.json()
    pool_status[i] = {
                "pool_id": j["result"]["id"],
                "pool_name": j["result"]["name"]
                }
    if pool_status[i]["pool_name"] == pool_nick:
      pool = pool_status[i]["pool_id"]
      break
      
  print(f'Performing action {data} against pool {pool_nick}')
  requests.patch('https://api.cloudflare.com/client/v4/accounts/' + zone + '/load_balancers/pools/' + pool, headers=headers, data=data)


### TODO:
### can we determine the pool ids and load them in aws parameter store? These should ideally never change unless torn down completely
### check status of pools after changes to verify the change was made; is this incredibly vital?
### can we also write this state elsewhere, so we can confirm the state without accessing cloudflare again?

if __name__ == "__main__":
    main(pool_nick, action)
