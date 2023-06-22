URL='http://zabbix.104.197.160.56.sslip.io/api_jsonrpc.php'
HEADER='Content-Type:application/json'
ZABBIX_USER="Admin"
ZABBIX_PASS="zabbix"
EVENT_ID="1989"
ACTION="6"
MESSAGE="Evento Acknowledged via API"


autenticacao()
{
    JSON='
    {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "username": "'$ZABBIX_USER'",
        "password": "'$ZABBIX_PASS'"
    },
    "id": 1,
    "auth": null
}
    '
    curl -s -X POST -H "$HEADER" -d "$JSON" "$URL" | cut -d '"' -f8
}
TOKEN=$(autenticacao)

echo $TOKEN

# Verifica se o evento está acknowledged
check_ack()
{
    JSON='{
  "jsonrpc": "2.0",
  "method": "event.get",
  "params": {
    "output": "extend",
    "eventid": ["1989"],
    "select_acknowledges": "extend",
    "acknowledged": "0"
  },
  "auth": "'$TOKEN'",
  "id": 1
}'
    curl -s -X POST -H "$HEADER" -d "$JSON" "$URL" 
}

event_ack()
{
    JSON='
    {
    "jsonrpc": "2.0",
    "method": "event.acknowledge",
    "params": {
        "eventids": "'$EVENT_ID'",
        "action": "'$ACTION'",
        "message": "'$MESSAGE'"
    },
    "auth": "'$TOKEN'",
    "id": 1
}
    '
    curl -X POST -H "$HEADER" -d "$JSON" "$URL"
    echo $JSON
}

event_ack