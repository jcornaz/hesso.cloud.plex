#!/usr/bin/env bash

sudo pip install -r requirements.txt
curl -o ./ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest

chmod +x ./ecs-cli

# MAC :
# sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-darwin-amd64-latest