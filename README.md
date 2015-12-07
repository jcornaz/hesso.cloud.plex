# hesso.cloud.plex

## Introduction

Very small project for deploying a Plex Media Server into an Amazon S3 infrastructure.

This project provides:

* scripts for deploying 3 virtual machines
  * 1 virtual machine containing Plex Media Server
  * 1 virtual machine as storage for Plex Media Server
  * 1 virtual machine as web server for managing medias through a small single page application.
* scripts for hosting the small single page application for managing medias of Plex Media Server.

## How to install

### Prerequisites

You need credentials from Amazon S3 for running scripts for deployment purposes

### Credentials

You can create a YAML file containing your credentials whether you don't have the private/public keys infrastructure yet.

### Install

```python deploy/deploy.py <storage_name> <credentials_path>```

The <credentials_path> should be a YAML file like this : 
```
id: <your_aws_access_id>
key: <your_aws_access_key>
```
