import json
import api_shared.utils


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": api_shared.utils.get_text(),
        }),
    }
