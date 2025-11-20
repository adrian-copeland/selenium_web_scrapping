import os
import pandas as pd

def get_last_two_files(directory: str):
    """ Get the last two files created in a given directory3
    =============
    Params:
    directory:str. Directory with the files of interest
    ===========
    Returns:
    Files: Last two files created in the given directory
    """
    ##list all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]

    ## sort files by creation time (newest first)
    files.sort(key=os.path.getctime, reverse=True)

    #return the last two
    return files[:2]



def online_offline_process(folder_connectplus_downloads_path: str, table_all_stores_path: str, final_storage_path: str):
    """  This function takes the last two lists downloaded from connect + and the fixed table of all stores.
    Returns a table with all the columns in table_all_stores plus five columns. four columns including the status and time
    of last connections from the two list and one final column with a final diagnostic. 
    ==========================
    Params:
    folder_connectplus_downloads_path: str. Path to the folder where the lists downloaded from connection plus are stored.
    table_all_stores_path: str. Path where the fixed list of all stores considered is stored.

    ========================
    Returns:
    None.
    Creates the resulting list in the folder final_storage_path.
    """


