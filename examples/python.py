"""LinkedIn Ad Library Scraper - Python example.

Requires: apify-client, APIFY_TOKEN env var.
    pip install apify-client
"""

import os
import sys

from apify_client import ApifyClient

TOKEN = os.environ.get('APIFY_TOKEN')
if not TOKEN:
    print('Set APIFY_TOKEN env var. Get one at https://console.apify.com/account/integrations')
    sys.exit(1)

company = sys.argv[1] if len(sys.argv) > 1 else 'HubSpot'

client = ApifyClient(TOKEN)
run = client.actor('agnes.developer.queen/linkedin-ad-library-scraper').call(
    run_input={
        'companies': [company],
        'maxAdsPerSearch': 20,
        'proxyConfiguration': {'useApifyProxy': True, 'apifyProxyGroups': ['RESIDENTIAL']},
    }
)

count = 0
for ad in client.dataset(run['defaultDatasetId']).iterate_items():
    print('\t'.join(str(ad.get(k)) for k in ('advertiserName', 'adFormat', 'headline', 'totalImpressions', 'adUrl')))
    count += 1
print(f'{count} ads')
