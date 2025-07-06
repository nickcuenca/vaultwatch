from app.models import LoginLog
from app.tasks import send_alert

# Define rule functions here
def rule_geo_ip_mismatch(log: LoginLog) -> bool:
    # Placeholder: In real case, compare with past login locations
    return log.location not in ["California", "New York"]

def rule_failed_attempts(log: LoginLog) -> bool:
    # Placeholder: Count failed attempts from same IP
    return not log.success and log.ip_address == "192.168.1.1"  # Example ONLY!!!
    # In future: fetch last 5 login locations or IPs for user and compare


def check_anomalies(log: LoginLog):
    if rule_geo_ip_mismatch(log):
        send_alert.delay("geo_ip_mismatch", log.user_id)
    if rule_failed_attempts(log):
        send_alert.delay("brute_force", log.user_id)