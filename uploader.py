#custom module
import credentials
import uploaderHelperFunctions as UHF

#account connection strings amd file data
storage_account_name   = credentials.storage_account_name
storage_account_key    = credentials.storage_account_key
storage_container_name = credentials.storage_container_name
local_file_name        = credentials.local_file_name
file_content_type      = credentials.file_content_type

#setting the unique blob file name 
filename = UHF.getTimeForFile()

#connecting to azure blob account
block_blob_service = UHF.BlobStorageConnection( storage_account_name , storage_account_key )


#calling function to uplaod file
UHF.uploadfile(block_blob_service,
            storage_container_name,
            filename,
            local_file_name,
            file_content_type)
