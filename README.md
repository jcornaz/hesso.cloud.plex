# hesso.cloud.plex
Very small project for deploying a Plex Media Server into an Amazon S3 infrastructure.

## Status
This was a school project. It is no longer maintained and no support will ever be provided.

The project is available to anyone interested by studying, modifing or using it. However, be aware that it might contains bugs or errors, and some resources might be missing (data or credentials).

Please note that the language and technologies might have been new for the contributors when developping the project. Time frame and project requirement are also very different than most *real-world* project. 

**Coding style is not representative of current style of the contributors**

## Introduction
This project provides:

* scripts for deploying 3 virtual machines
  * 1 virtual machine containing Plex Media Server
  * 1 virtual machine as storage for Plex Media Server
  * 1 virtual machine as web server for managing medias through a small single page application.
* scripts for hosting the small single page application for managing medias of Plex Media Server.

## How to install

### Prerequisites

You need credentials from Amazon S3 for running scripts for deployment purposes

### Install

You need to
* Create and download a ssh keypair from AWS
* Create a YAML config file (see bellow)
* Install the dependences (you need python, pip and : `pip install -r requirements.txt`)
* `python deploy.py config-file`

The config file should look like this :
```
access:
  id: <aws-access-id>
  key: <aws-access-key>
  ssh_key: <path-to-the-ssh-key>

elastic_ips:
  plex: <publicip-for-the-media-server>
  file_uploader: <publicip-for-the-web-server>

bucket_name: <S3-storage-bucket-name>
```

By default if you don't precise the path to the config file, the script will try to use a 'config.yaml' file.
