# This scripts demonstrates how to use mitmproxy's filter pattern in inline scripts.
# Usage: mitmdump -s "filt.py FILTER"

from mitmproxy import filt


def response(context, flow):
    flow.response.headers["newheader"] = ["foo"]
