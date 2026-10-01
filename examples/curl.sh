#!/usr/bin/env bash
# LinkedIn Ad Library Scraper - curl example
# Requires: APIFY_TOKEN env var, jq

set -euo pipefail

if [ -z "${APIFY_TOKEN:-}" ]; then
    echo "Set APIFY_TOKEN env var first. Get one at https://console.apify.com/account/integrations"
    exit 1
fi

COMPANY="${1:-HubSpot}"

curl -s -X POST \
    "https://api.apify.com/v2/acts/agnes.developer.queen~linkedin-ad-library-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
    -H "Content-Type: application/json" \
    -d "{\"companies\": [\"${COMPANY}\"], \"maxAdsPerSearch\": 20, \"proxyConfiguration\": {\"useApifyProxy\": true, \"apifyProxyGroups\": [\"RESIDENTIAL\"]}}" \
    | jq -r '.[] | [.advertiserName, .adFormat, .headline, .totalImpressions, .adUrl] | @tsv'
