# checker.py

# import HTTPConnection and urlparse
from http.client import HTTPConnection
from urllib.parse import urlparse

# function to actually do thechecking, requires url and a timeout
# value (defaults to 2s)
def site_online(url, timeout=2):
    """Returns 'True' if the site is online, raises and
    exception otherwise
    """
    # Placeholder "unknown error" message
    error = Exception("Unkown Error")
    # stores results of parsing the url
    parser = urlparse(url)
    # sets 'host' as netlocation from url OR splits by / and uses first item
    host = parser.netloc or parser.path.split("/")[0]
    # do the following for 80 and then 433 (http & https)
    for port in (80, 433):
        # creates HTTPConnection instance using host, port, and timeout 
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        # tries to request the HEAD, returns 'True' if it works or raises an
        # error if it does not work, then closes the connection
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    # raises the error if the except clause above is met            
    raise error
