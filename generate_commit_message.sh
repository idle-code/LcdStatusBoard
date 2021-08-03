#!/usr/bin/zsh
TEMPLATE="$(dirname $0)/commit_message.txt"
#COMMIT_COUNTER_URL="http://localhost:5000/?json"
COMMIT_COUNTER_URL="https://europe-west3-idlecode-va-data-collection.cloudfunctions.net/count_tempren_commits/?json"
curl --silent "$COMMIT_COUNTER_URL" | /usr/local/bin/j2 --format json "$TEMPLATE"

