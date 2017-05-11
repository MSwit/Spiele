import time
import io
from mitmproxy import http
from mitmproxy.script import concurrent

#global file# = open('"opponents.txt"', 'a');

#@concurrent  # Remove this and see what happens
def response(flow: http.HTTPFlow) -> None:
    searchString = 'opponents'
    content = flow.response.content.decode('utf-8')
    if(searchString in content):
        file = open('opponents.txt', 'a')
        file.write(content)
        file.flush()
        file.close()
