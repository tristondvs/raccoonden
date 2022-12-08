import requests, os, json, sys
from dotenv import load_dotenv

### load env vars from .env
### can we load these credentials in aws parameter store?
load_dotenv()

email = os.getenv('USER_EMAIL')
apikey = os.getenv('API_KEY')
zone = os.getenv('ZONE_ID')
pool_ids = ['d058132d42378dd050b239e9a365e45d', '71399e3cbf69c3850a0adf00084b59e8']
pool_nick = sys.argv[1]
action = sys.argv[2]

headers = {
    'X-Auth-Email': email,
    'Authorization': 'Bearer ' + apikey,
    'Content-Type': 'application/json',
}

### new function definition here
def main(pool_nick, action):
  pool_status = {}
    # determine pool id for provided pool name, query aws parameter store for json object?
    # for now we manually provide the json object below and parse it
  for i in range(len(pool_ids)):
    try:
      response = requests.get('https://api.cloudflare.com/client/v4/accounts/' + zone + '/load_balancers/pools/' + pool_ids[i], headers=headers)
      j = response.json()
      pool_status[i] = {
                  "pool_id": j["result"]["id"],
                  "pool_name": j["result"]["id"]
                  }
      if pool_status[i]["pool_name"] == pool_nick:
        global pool
        pool = pool_status["pool_id"]
      if action == 'enable':
        data = '{"enabled": true}'
      elif action == 'disable':
        data = '{"enabled": false}'

      if pool_status[i]["pool_name"] == pool_nick:
        pool = pool_status["pool_id"]
        print(zone, pool, data)
        requests.patch('https://api.cloudflare.com/client/v4/accounts/' + zone + '/load_balancers/pools/' + pool, headers=headers, data=data)

### determine list of pool names, list all pool ids for zone
### can we determine the pool ids and load them in aws parameter store? These should ideally never change unless torn down completely
### query status of all pools, determine if enabled or disabled
### does this step even matter; can we enable an already enabled pool without issue?
### can we force an action as mentioned above and avoid a choice?
### check status of pools after changes to verify
### can we also write this state elsewhere, so we can confirm the state without accessing cloudflare?
if __name__ == "__main__":
    main(pool_nick, action)
