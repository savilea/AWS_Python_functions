import awswrangler as wr


def write_parquet_file_to_athena(df,partition_cols,database,tablename,s3_path):
    wr.s3.to_parquet(
        df=df,
        path= s3_path,
        dataset=True,
        schema_evolution =True,
        mode = 'overwrite_partitions',
        partition_cols=partition_cols,
        database=database, # Athena/Glue database
        table= tablename, # Athena/Glue table
        )
    print( tablename + ' data written to data lake' )
    
    
    
    
write_parquet_file_to_athena(df,['id','type'],'glue_database','glue_table','s3://s3_bucket/prefix/')