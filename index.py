import datetime
import json


def handler(event, context):
    data = {
        "output": "CodePipeline Test",
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }
    return {
        "statusCode": 200,
        "body": json.dumps(data),
        "headers": {"Content-Type": "application/json"},
    }
