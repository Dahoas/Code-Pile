import json
import asyncio
import aiohttp
import time
import resource, sys
import requests

# https://cloud.google.com/storage/docs/reference/libraries#client-libraries-usage-python
from google.cloud import storage

# Schema: https://code.google.com/archive/schema

license_allowlist = set(["MIT License", 
                         "Apache License 2.0", 
                         "BSD 3-Clause \"New\" or \"Revised\" License", 
                         "Mozilla Public License 2.0", 
                         "BSD 2-Clause \"Simplified\" License", 
                         "ISC License", 
                         "The Unlicense", 
                         "Creative Commons Zero v1.0 Universal", 
                         "Eclipse Public License 1.0", 
                         "Artistic License 2.0", 
                         "BSD 3-Clause Clear License"])

def format_schema(bucket, project, json_filename):
    return "https://storage.googleapis.com/{}/{}/{}".format(bucket, project, json_filename)

def test():
    r_project = requests.get(format_schema("google-code-archive", "v2/code.google.com/hg4j", "project.json")).json()
    r_source = requests.get(format_schema("google-code-archive-source", "v2/code.google.com/hg4j", "source-archive.zip"))
    print(r_project.keys())
    print(type(r_source))
    print(r_source)

    storage_client = storage.Client()
    bucket = storage_client.create_bucket("storage.googleapis.com")
    

test()