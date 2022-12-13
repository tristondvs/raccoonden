Python 3.10.6

For Ubuntu 22.04.1, `prepare-env.sh` will perform these steps for you.

1. Install requirements tied to cloudflare api script
```
pip install -r requirements.txt
```

2. create .env file containing the following vars within this directory

```
USER_EMAIL='<email for cloudflare login>'
API_KEY='<api key with edit permissions for load balancer settings>'
ZONE_ID='<zone id tied to cloudflare account>'
```

Within the script or within your .env file, provide list of pool_ids within the specified zone. Future iterations of this script will work to pull these from smoething like aws paramter store.

```
pool_ids=['', '']
```

Pool Ids can be determined programatically from the cloudflare API, provided below is an example request that will return available pool ids for the specifed zone. For assistance refer to the Cloudflare API https://api.cloudflare.com/#load-balancer-pools-list-pools

```
curl -X GET "https://api.cloudflare.com/client/v4/accounts/<zone id>/load_balancers/pools" \
     -H "X-Auth-Email: <email address of user>" \
     -H "Authorization: Bearer <API token>" \
     -H "Content-Type: application/json"
```

example usage

```
python3 disable_pool.py <pool name> enable/disable
```
