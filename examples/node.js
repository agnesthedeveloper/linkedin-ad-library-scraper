// LinkedIn Ad Library Scraper - Node.js example
// Requires: Node 18+, APIFY_TOKEN env var
//     npm install apify-client

import { ApifyClient } from 'apify-client';

const TOKEN = process.env.APIFY_TOKEN;
if (!TOKEN) {
    console.error('Set APIFY_TOKEN env var. Get one at https://console.apify.com/account/integrations');
    process.exit(1);
}

const company = process.argv[2] || 'HubSpot';

const client = new ApifyClient({ token: TOKEN });
const run = await client.actor('agnes.developer.queen/linkedin-ad-library-scraper').call({
    companies: [company],
    maxAdsPerSearch: 20,
    proxyConfiguration: { useApifyProxy: true, apifyProxyGroups: ['RESIDENTIAL'] },
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const ad of items) {
    console.log([ad.advertiserName, ad.adFormat, ad.headline, ad.totalImpressions, ad.adUrl].join('\t'));
}
console.log(`${items.length} ads`);
