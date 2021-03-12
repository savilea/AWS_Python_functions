import boto3

def create_glue_database(db_name,description):
    client = boto3.client('glue')
    response = client.create_database(
        DatabaseInput={
            'Name': db_name,
            'Description': description
            }) 
    print(response)
    return response

create_glue_database('new-glue-database','new glue db created via create_glue_database function') 