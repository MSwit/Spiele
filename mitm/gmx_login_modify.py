import io

from PIL import Image


def start(ScriptContext, argv):
    ScriptContext.log("testtest 123")
    #raise ValueError(" error geworfen")

def responseheaders(flow):
    flow.response.stream = modify
    #raise ValueError(HTTPFlow.response)

def response(ScriptContext, HTTPFlow):
    #ScriptContext.log("asdfasdfasdfasdfasdfasdasdfasdfsdf")
    source = "Kostenlos registrieren"
    dest = "Kostenlos registrieren22222"

    HTTPFlow.response.headers["newheader"] = "foo"
#    raise ValueError(HTTPFlow.response)
    if source in HTTPFlow.response.content:
        content = ScriptContext.response.content
        HTTPFlow.response.content = content.replace(source, dest)
    source = "wir lieben es"
    dest = "222222222"
    if source in HTTPFlow.response.content:
        content = ScriptContext.response.content
        HTTPFlow.response.content = content.replace(source, dest)
        raise ValueError("JUHU , " + source + " gefunden!!!")
    #if source in HTTPFlow.response.headers:
#        raise ValueError("JUHU , " + source + " gefunden!!!222")
