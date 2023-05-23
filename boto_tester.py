import boto3
s3_client = boto3.resource('s3')

my_bucket = s3_client.Bucket('data-handling-public')

# visualize the contect of the bucket
#for file in my_bucket.objects.all():
#    print(file.key)

#s3_client = boto3.client('s3')

# Ofcourse, change the names of the files to match yours.
#s3_client.download_file('products.csv', 'data-handling-public', 'products.csv')

s3_client.Bucket('data-handling-public').download_file(Key='products.csv', Filename='products.csv')
import pandas as pd
pd.read_csv('products.csv')