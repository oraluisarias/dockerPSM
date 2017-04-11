#!/bin/bash
echo "Username: $1, Password: $2, Identity Domain: $3, Region $4"
[ -d /home/opc/.psm ] && rm -rf /home/opc/.psm
expect -c "spawn psm setup
expect \"Username:\"
send \"$1\r\"
expect \"Password:\"
send \"$2\r\"
expect \"Retype Password:\"
send \"$2\r\"
expect \"Identity domain:\"
send \"$3\r\"
expect \"Region ?us?:\"
send \"$4\r\"
expect \"Output format ?json?:\"
send \"\r\"
expect eof"