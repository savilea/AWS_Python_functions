import awswrangler as wr

def read_from_s3(file_type,s3_path):
    s3_df = []
    if file_type =='json':
        s3_df = wr.s3.read_json(path=s3_path )
        print(s3_df)
    elif file_type =='csv':
        s3_df = wr.s3.read_csv(path=s3_path )
        print(s3_df)
    elif file_type =='parquet':
        s3_df = wr.s3.read_parquet(path=s3_path )
        print(s3_df)
    else: s3_df('Unexpected file type')
    return df


df = read_from_s3('json','s3://bucketname/filepath/') 