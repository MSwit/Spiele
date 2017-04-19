import time

from mitmproxy.script import concurrent

@concurrent  # Remove this and see what happens
def response(context, flow):
    searchString = "neue Produkte"
    searchString2 = "Wir lieben es"

    if(searchString in flow.response.content):
        flow.response.content = flow.response.content.replace(searchString, " <b>'modified -start</b> " +
         searchString + "<b> - end'</b>")
    if(searchString2 in flow.response.content):
        flow.response.content = flow.response.content.replace(searchString2, "<b>' modified -start</b> " +
         searchString2 + "<b> - end'</b>")
