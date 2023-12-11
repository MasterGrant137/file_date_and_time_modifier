#### modify_file
- loop through file names on first level of directory 
- constrain modifiable files: ['.mov', '.mp4', '.mpeg', '.jpeg', '.jpg', '.png']
- concatenate directory absolute path with file name to get file absolute path
- pass original time to shift_datetime helper function
- use shell to change birthtime and metadata and python to change mod time
- add print statements to track progress
- args: 
    + dir_path: str => concatenated with file name
    + shift_amt: int | float => pass to helper function 
    + unit: str => pass to helper function
- return: None

#### shift_datetime
- constrain acceptable units: ['days', 'hours', 'minutes', 'seconds']
- use conditionals to target the correct unit kwarg for `timedelta`
- add +/- shift amount as the value to `timedelta` kwarg
- add `timedelta` to file birthtime
- args:
    + file_birthtime: float => `datetime` in milliseconds-since-Unix-epoch format
    + shift_amt: int | float => `timedelta` accepts both integer and float
    + unit: str => used for conditionals
- return: `datetime`