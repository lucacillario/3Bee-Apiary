import os
import sys
import logging
from time import time, sleep


from django.db import connections
from django.db.utils import OperationalError


check_timeout = os.getenv("DB_CHECK_TIMEOUT", 30)
check_interval = os.getenv("DB_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"

start_time = time()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def mysql_is_ready():
    db_conn = connections['default']
    while time() - start_time < check_timeout:
        try:
            db_conn.cursor()
        except OperationalError:
            logger.info(f"DB isn't ready. Waiting for {check_interval} {interval_unit}...")
            sleep(check_interval)
        else:
            logger.info("DB is ready! ✨ 💅")
            return True

    return False


sys.exit(0) if mysql_is_ready() else sys.exit(1)
