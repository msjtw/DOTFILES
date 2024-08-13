import json

ret = {}
ret['text'] = 'now'
ret['tooltip'] = "tip"
ret['class'] = "weather",
ret['percentage'] = "0"

print(json.dumps(ret))