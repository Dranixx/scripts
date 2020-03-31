import os
import time
from datetime import datetime, timedelta
from PIL import Image

TEN_MINUTES = timedelta(minutes=10)

"""Restores file's creation and modification dates back to the original 
value from EXIF.
usage: date_reset.py [Folder path]
""" 

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
    """Returns a dictionary of 3 differents times of the file.

    Theses times are file access (atime), modification (mtime) and original (exif) dates.
    """
    dates = {}
    dates['exif'] = get_date_taken(path)
    dates['mtime'] = datetime.utcfromtimestamp(os.path.getmtime(path))
    dates['atime'] = datetime.utcfromtimestamp(os.path.getctime(path))
    return dates

def set_file_dates(path, dates):
    """"Set file modification and access dates to the specified value"""
    os.utime(path, (time.mktime(dates['exif'].utctimetuple()),)*2)

def fix_file_date(path):
    """Reads file's EXIF header, gets the earliest date and sets it to the file"""
    dates = get_file_dates(path)
    if (dates['exif']):
        cmp_time = lambda x, y: x - y > TEN_MINUTES
        diff = [cmp_time(dates[x], dates['exif']) for x in ('mtime', 'atime')]
        if(sum(diff)):
            set_file_dates(path, dates)
        return dates, diff
    else:
        return dates, None

if __name__== "__main__":
    dir = r'C:\Users\Alexandre\Desktop\Vielle Photos\test\\'
    with os.scandir(dir) as entries:
        for entry in entries:
            try:
                dates, diff = fix_file_date(dir + entry.name)
            except Exception as e:
                print(e)
                diff = None
            print(dir + entry.name + ' - ', end='')
            if not diff:
                print("SKIP, NO EXIF")
            else:
                if (sum(diff) != 0):
                    print('SET TO "%s" (updated M:%d, C:%d)' % (dates['exif'].strftime('%Y:%m:%d %H:%M:%S'), diff[0], diff[1]))
                else:
                    print('OK')