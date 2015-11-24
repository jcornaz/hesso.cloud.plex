#!/usr/bin/env bash

sudo pip install -r requirements.txt
curl -o ./ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
chmod +x ./ecs-cli
./ecs-cli configure --region eu-west-1 --cluster plex_cluster

# MAC :
# sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-darwin-amd64-latest