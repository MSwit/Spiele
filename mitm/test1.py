import time

from mitmproxy.script import concurrent

@concurrent  # Remove this and see what happens
def response(context, flow):
    # You don't want to use mitmproxy.ctx from a different thread
    #print("handle request: %s%s" % (flow.request.host, flow.request.path))
    raise
    print("handle response: %s" % (flow.response.content))
    content = flow.response.content
    # print("request.content == %s" % (flow.response.content-type))
    searchString = "lieben es"
    if(searchString in content):
        #print("request.content == %s" % (content))
        time.sleep(1)
    #print("start  request: %s%s" % (flow.request.host, flow.request.path))
