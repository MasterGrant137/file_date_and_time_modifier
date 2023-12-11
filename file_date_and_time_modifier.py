from os import listdir, path, stat, utime
from subprocess import call
from datetime import datetime, timedelta
from re import search

def shift_datetime(file_birthtime: float, shift_amt: int | float, unit: str) -> datetime:
    if unit in ['days', 'hours', 'minutes', 'seconds']:
        delta = timedelta(seconds=0)
        if unit == 'days': delta = timedelta(days=shift_amt)
        if unit == 'hours': delta = timedelta(hours=shift_amt)
        if unit == 'minutes': delta = timedelta(minutes=shift_amt)
        if unit == 'seconds': delta = timedelta(seconds=shift_amt)

        file_birthtime = datetime.fromtimestamp(file_birthtime)

        return file_birthtime + delta
    else: 
        print('Check the unit you are using.')

def modify_file(dir_path: str, shift_amt: int | float, unit: str) -> None:
    for file_name in listdir(dir_path):
        file_abs_path = path.join(dir_path, file_name)

        acceptable_extensions = ['.mov', '.mp4', '.mpeg', '.jpeg', '.jpg', '.png']
        extension = search(r'\.\w+', file_abs_path).group(0).lower()
 
        if extension in acceptable_extensions:
            file_birthtime = stat(file_abs_path).st_birthtime
            shifted_datetime = shift_datetime(file_birthtime, shift_amt, unit)
            
            birthtime_formatted_adjusted_datetime = shifted_datetime.strftime('%m/%d/%Y %H:%M:%S')
            metadata_formatted_adjusted_datetime = shifted_datetime.strftime('%Y:%m:%d %H:%M:%S')
            file_data_formatted_adjusted_datetime = shifted_datetime.timestamp()

            print('birthtime BEFORE', datetime.fromtimestamp(stat(file_abs_path).st_birthtime), 'mod time BEFORE', path.getmtime(file_abs_path))

            set_birthtime_cmd = f'SetFile -d "{birthtime_formatted_adjusted_datetime}" "{file_abs_path}"'
            call(set_birthtime_cmd, shell=True)
            utime(file_abs_path, (datetime.now().timestamp(), file_data_formatted_adjusted_datetime))

            print('birthtime AFTER', datetime.fromtimestamp(stat(file_abs_path).st_birthtime), 'mod time AFTER', path.getmtime(file_abs_path))

            set_metadata_cmd = [
                'exiftool',
                '-overwrite_original',
                f'-CreationDate="{metadata_formatted_adjusted_datetime}"',
                f'-FileModifyDate="{metadata_formatted_adjusted_datetime}"',
                f'-CreateDate="{metadata_formatted_adjusted_datetime}"',
                f'-ModifyDate="{metadata_formatted_adjusted_datetime}"',
                f'-MediaCreateDate="{metadata_formatted_adjusted_datetime}"',
                f'-MediaModifyDate="{metadata_formatted_adjusted_datetime}"',
                f'-TrackCreateDate="{metadata_formatted_adjusted_datetime}"',
                f'-TrackModifyDate="{metadata_formatted_adjusted_datetime}"',
                f'-TrackCreateDate="{metadata_formatted_adjusted_datetime}"',
                f'-TrackModifyDate="{metadata_formatted_adjusted_datetime}"',
                file_abs_path
            ]
            call(set_metadata_cmd)
        else:
            print(f'Skipped unacceptable extension: {extension}')

modify_file('/Users/alejandrocarrizosagrant/Desktop/test_folder', 9, 'hours')