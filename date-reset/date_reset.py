import os
from datetime import datetime
from PIL import Image

def get_date_taken(path):
    """Gets the original date from the file's EXIF header, return datetime object"""
    timestamp = None
    try:
        original_time = Image.open(path)._getexif()[36867]
        if original_time:
            timestamp = datetime.strptime(original_time, '%Y:%m:%d %H:%M:%S')
    except:
        pass
    return timestamp

def get_file_dates(path):
    """Returns a dictionary of 3 differents times.

    There are file creation (ctime), modification (mtime) and original (exif) dates.
    """
    dates = {}
    dates['exif'] = get_date_taken(path)
    dates['mtime'] = datetime.utcfromtimestamp(os.path.getmtime(path))
    dates['ctime'] = datetime.utcfromtimestamp(os.path.getctime(path))
    return dates

if __name__== "__main__":
    dir = r'C:\Users\Alexandre\Desktop\Vielle Photos\\'
    with os.scandir(dir) as entries:
        for entry in entries:
            if get_date_taken(dir + entry.name) == "No Original date":
                print(entry.name)
            print(get_date_taken(dir + entry.name))