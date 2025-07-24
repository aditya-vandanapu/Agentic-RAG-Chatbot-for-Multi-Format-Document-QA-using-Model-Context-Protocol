import uuid
import json

def create_mcp_message(sender, receiver, msg_type, payload):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": msg_type,
        "trace_id": str(uuid.uuid4()),
        "payload": payload
    }

def pretty_print_mcp(msg):
    return json.dumps(msg, indent=2)
