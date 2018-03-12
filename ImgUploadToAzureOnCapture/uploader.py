import credentials
import uploaderHelperFunctions as UHF
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = credentials.DIRECTORY_TO_WATCH
    
    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")
    
        self.observer.join()


class Handler(PatternMatchingEventHandler):
    patterns = ["*.jpg", "*.png"]
    
    #account connection strings amd file data
    storage_account_name   = credentials.storage_account_name
    storage_account_key    = credentials.storage_account_key
    storage_container_name = credentials.storage_container_name
    file_content_type      = credentials.file_content_type
    BACKUP_DIRECTORY = credentials.BACKUP_DIRECTORY
    
    #setting the unique blob file name 
    filename = UHF.getTimeForFile()+".jpg"
    
    #connecting to azure blob account
    block_blob_service = UHF.BlobStorageConnection( storage_account_name , storage_account_key )

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("File created at path - %s." % event.src_path)
            
            #calling function to uplaod file
            UHF.uploadfile(Handler.block_blob_service,
                        Handler.storage_container_name,
                        Handler.filename,
                        event.src_path,
                        Handler.file_content_type)
            
            #Move file to backup
            shutil.move(event.src_path, Handler.BACKUP_DIRECTORY)
            print ("File moved to backup")

if __name__ == '__main__':
    w = Watcher()
    w.run()