#!/usr/bin/zsh
TEMPLATE="$(dirname $0)/commit_message.txt"
#COMMIT_COUNTER_URL="http://localhost:5000/?json"
COMMIT_COUNTER_URL="https://europe-west3-idlecode-va-data-collection.cloudfunctions.net/count_commits/?json"
curl "$COMMIT_COUNTER_URL" | j2 --format json "$TEMPLATE"

