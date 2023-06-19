# __main__.py

import pathlib
import sys

from sitecheck.cli import read_args, display_check
from sitecheck.checker import site_online


def main():
    """Run sitechecker"""
    # parses user args and stores as user_args
    user_arg = read_args()
    # gets list of urls from function
    urls = _get_urls(user_arg)
    # checks if urls exist, otherwise throws error and closes
    if not urls:
        print('Err: no URLs provided', file=sys.stderr)
        sys.exit(1)
    # runs function to check synchronously
    _syncrhonous_check(urls)


# gets urls from arguments
def _get_urls(user_args):
    # stores list of urls from arguments
    urls = user_args.urls
    # if arg is a file, run _read_urls_from_file on the file
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls


# function to read urls from file, returns list of urls
def _read_urls_from_file(file):
    # converts arg to a pathlib path object
    file_path = pathlib.Path(file)
    # if the file is an actual file
    if file_path.is_file():
        # strip file line by line into list and return
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            # checks if urls has contents, returns if it does,
            # error will display if it does not
            if urls:
                return urls
            print(f'Err: invalid input file "{file}".', file=sys.stderr)
    # catches file not existing/can't be found/etc
    else:
        print(f'Err: input file not found.', file=sys.stderr)
    return[]


# function to check synchronously
def _synchronous_check(urls):
    # iterate through the urls
    for url in urls:
        # creates 'error' as empty string
        error =""
        # run the HEAD request, if no response then set 'result'
        # to fale, put the error to 'error'
        try:
            result = site_online(url)
        except Exception as E:
            result = False
            error = str(e)
        # runs display_check function with result, url, and error 
        display_check(result, url, error)


# checks if running as main, runs main function if so
if __name__ == "__main__":
    main()
