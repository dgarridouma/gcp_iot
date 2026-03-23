import datetime
from google.cloud import bigquery
import functions_framework

# filename: must be main.py
# functions_framework --target hello_world --debug
#
# http://127.0.0.1:8080 POST

@functions_framework.http
def hello_world(request):
    request_json = request.get_json() # must be sent as JSON (not str)
    request_json['when']=datetime.datetime.now()
    client = bigquery.Client()
    dataset_id = 'midataset'  # replace with your dataset ID
    table_id = 'mitabla'  # replace with your table ID
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)
    
    rows_to_insert = [ request_json]
    errors = client.insert_rows(table, rows_to_insert)  # API request

    return f'Insertado!'
