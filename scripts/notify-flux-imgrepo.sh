#!/usr/bin/env sh

WEBHOOK_URL="https://webhook.flux.klavionik.net/hook/0bacd89674884e13132c6c41c3e343283d647526c9209206976a29c59ab17d76"
HASH_FUNCTION=sha256
REQUEST_BODY=$@

HASH=$(printf "$REQUEST_BODY" | openssl dgst -"$HASH_FUNCTION" -r -hmac $IMGREPO_WEBHOOK_TOKEN | awk '{print $1}')
curl "$WEBHOOK_URL" -X POST -H "X-Signature: $HASH_FUNCTION=$HASH" -d "$REQUEST_BODY"
