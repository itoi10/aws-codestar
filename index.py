import datetime
import json


def handler(event, context):
    data = {
        "output": "CodePipelineテスト",
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }
    return {
        "statusCode": 200,
        "body": json.dumps(data),
        "headers": {"Content-Type": "application/json"},
    }
