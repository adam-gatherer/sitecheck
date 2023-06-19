# cli.py

import argparse

def read_args():
    """Reads the arguments/options from the command line"""
    # creates the argument parser
    parser = argparse.ArgumentParser(
            prog="sitechecker", description="Checks the availability of websites"
            )
    # adds the arguments for the parser
    parser.add_argument(
            "-u",
            "--urls",
            # sets the name for usage/hellp messages
            metavar="URLs",
            # tesll argparse to accept list of command line arguments 
            # after the -u/--url switches
            nargs="+",
            # sets the data type for the arguments
            type=str,
            # provides a default argument (ie, none)
            default=[],
            # help message for the user
            help="enter one or more URLs",
            )
    # as above, but lacking nargs as we only want one file to be read
    parser.add_arguement(
            "-f",
            "--file",
            metavar="FILE",
            type=str,
            default="",
            help="read URLs from file",
            )
    # returns the parsed arguments as a namespace object
    return parser.parse_args()

# function to display resuls, takes in 'result', 'url', and any errors
def display_check(result, url, error=""):
    """Displays the result of a check"""
    if result:
        print(f'Site {url} is online.')
    else:
        print(f'Site {url} is offline.\nErr: {error}')
