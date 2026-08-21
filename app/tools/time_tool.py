from datetime import datetime
from zoneinfo import ZoneInfo
def get_current_time(timezone: str = "Asia/Shanghai"):

    return datetime.now(ZoneInfo(timezone)).strftime(
        "%Y-%m-%d %H:%M:%S"
        )