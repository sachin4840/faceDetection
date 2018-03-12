

import time
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

#connection function
def BlobStorageConnection( storage_account_name , storage_account_key):
    return BlockBlobService( account_name = storage_account_name ,account_key = storage_account_key)


#Uploader function 
def uploadfile(block_blob_service,
               storage_container_name,
               filename,
               local_file_name,
               file_content_type):
    
    print ("Uploading File.........")

    #uploading file
    block_blob_service.create_blob_from_path(storage_container_name,
                                            filename,
                                            local_file_name,
                                            content_settings = ContentSettings(content_type = file_content_type)
                                            )
    print ("file uploaded")
#uploader function end

def getTimeForFile():
    return time.asctime( time.localtime (time.time() ) )