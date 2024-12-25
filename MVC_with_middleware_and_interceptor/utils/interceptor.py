from datetime import datetime

class Interceptor:
    @staticmethod
    def log_action(action, data=None, success=True):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if success else "FAILURE"
        print(f"[{timestamp}] Action: {action} | Status: {status}")
        if data:
            print(f"Details: {data}")
