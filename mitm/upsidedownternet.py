"""
This script rotates all images passing through the proxy by 180 degrees.
"""
import io

from PIL import Image

def start(ScriptContext, argv):
    ScriptContext.log("testtest 123")

def response(ScriptContext, HTTPFlow):
    ScriptContext.log("asdfasdfasdfasdfasdfasdasdfasdfsdf")
    if HTTPFlow.response.headers.get("content-type", "").startswith("image"):
        s = io.BytesIO(HTTPFlow.response.content)
        img = Image.open(s).rotate(180)
        s2 = io.BytesIO()
        img.save(s2, "png")
        HTTPFlow.response.content = s2.getvalue()
        HTTPFlow.response.headers["content-type"] = "image/png"
        print("                                        JUHU, hier sollte was passiert sein")
