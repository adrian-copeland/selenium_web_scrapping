import os
from pathlib import Path

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
    if not files:
        print("No files found in:", directory)
        return []

    ## sort files by creation time (newest first)
    files.sort(key=os.path.getctime, reverse=True)

    #return the last two
    return files[:2]



if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    print('current_dir', current_dir)
    parent_dir = current_dir.parent
    print('parent_directory', parent_dir)
    target_dir = parent_dir / "lists_downloaded"
    print('target directory', target_dir)


    print("Last two files", get_last_two_files(target_dir))
