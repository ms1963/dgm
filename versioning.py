import os
from datetime import datetime

AGENT_DIR = "agents"

def save_version(agent_code, score, is_accepted):
    os.makedirs(AGENT_DIR, exist_ok=True)  # Ensure the directory exists
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    status = "accepted" if is_accepted else "rejected"
    filename = f"{AGENT_DIR}/agent_{ts}_{score}_{status}.py"
    with open(filename, "w") as f:
        f.write(agent_code)
    return filename
