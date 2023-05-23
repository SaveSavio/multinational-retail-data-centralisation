"""
This is just a reminder for myself

1) I have to run
    >> aws configure --> this requires awscli to be installed
and access the key and secret I created previously. They are stored in the AWS study folder.

2) now awscli should be connected

3) import boto and initialize the resource method telling we are going to work on a s3 server

4) use the line below to download. Good instructions can be found here:
    
    https://www.gormanalysis.com/blog/connecting-to-aws-s3-with-python/

5) I have tried to have a look at the files inside the folder but was denied, this lead me to think that I did
    not have access to it
    
"""
import boto3

s3_client = boto3.resource('s3')

s3_client.Bucket('data-handling-public').download_file(Key='products.csv', Filename='products.csv')