# Deploy to AWS
You need to have a amazon web services account.

* Create a user : https://console.aws.amazon.com/iam/home?users#users
* Allow it the right to manage the containers
* Download the credentials file
* Put the credentials file in this folder with the name 'credentials.csv'

Then you can deploy the stack with :

```
pip install -r requirements.txt --upgrade
python deploy.py
```

(or you can specify the credentials file to use with : `python deploy.py <path-to-my-csv-file>`)
