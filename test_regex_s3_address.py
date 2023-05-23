import re
s3_address = 's3://data-handling-public/products.csv'
start = 's3://'
end = '/'
bucket = re.search('%s(.*)%s' % (start, end), s3_address).group(1)
print(bucket)