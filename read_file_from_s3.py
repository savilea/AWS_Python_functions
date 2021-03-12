import boto3, awswrangler as wr

def read_file_from_s3(s3_path):
    file_type = s3_path.split(".")[1:]
    s3_df=[]
    if file_type==['json']:
        s3_df = wr.s3.read_json(path=s3_path)
        print(s3_df)
    elif file_type==['csv']:
        s3_df = wr.s3.read_csv(path=s3_path)
        print(s3_df)
    elif file_type==['parquet']:
        s3_df = wr.s3.read_parquet(path=s3_path)
        print(s3_df)
    else:
        print('Unexpected file type')
    return s3_df


df = read_file_from_s3('s3://bucketname/filepath/filename.csv') 
