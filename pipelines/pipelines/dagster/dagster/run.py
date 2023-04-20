import pandas as pd
import requests

from dagster  import job, MetadataValue, Output, asset

def get_domain(url):
    return url.split("://")[1].split("/")[0]

@asset
def get_domain_of_url():
    data = pd.read_csv('original.csv')
    data['url_domain'] = data['url'].apply(get_domain)
    data.to_csv('result.csv')
    return data

@job
def run_dagster():
    get_domain_of_url()