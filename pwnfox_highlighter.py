from burp import IBurpExtender
from burp import IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        callbacks.setExtensionName("PwnFox Color Highlighter")
        callbacks.registerHttpListener(self)
        
        print("PwnFox Color Highlighter loaded.")
        print("Listening for 'X-Pwnfox-Color' header to highlight requests.")

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # We only process the request to set the highlight
        # Burp allows setting highlights on IHttpRequestResponse objects
        if not messageIsRequest:
            return

        # Get request headers
        request_info = self._helpers.analyzeRequest(messageInfo)
        headers = list(request_info.getHeaders())

        # Search for X-Pwnfox-Color header
        pwnfox_header = "X-Pwnfox-Color:"
        highlight_color = None

        for header in headers:
            if pwnfox_header.lower() in header.lower():
                # Extract color value and strip quotes/whitespace
                # Example: X-Pwnfox-Color: "red" -> red
                try:
                    color_val = header.split(":", 1)[1].strip().replace('"', '').replace("'", "").lower()
                    
                    # Burp supports: red, orange, yellow, green, cyan, blue, pink, magenta, gray
                    valid_colors = ["red", "orange", "yellow", "green", "cyan", "blue", "pink", "magenta", "gray"]
                    if color_val in valid_colors:
                        highlight_color = color_val
                    break
                except Exception as e:
                    print("Error parsing header: " + str(e))

        # Apply the highlight if found
        if highlight_color:
            messageInfo.setHighlight(highlight_color)
