#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.db import connections, OperationalError

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

def check_database_connections():
    RETRY_TIME = 30
    SLEEP_TIME = 1
    for c in connections.all():
        count = 1
        while True:
            try:
                print(f"Trying to connect to {c.alias}, retry count {count}.")
                c.ensure_connection()
            except OperationalError:
                print(f"Connect to db {c.alias} fail.")
                if count >= RETRY_TIME:
                    print("Up to retry limit.")
                    exit(1)
                sleep(SLEEP_TIME)
                count += 1
            else:
                print(f"Connect to db {c.alias} success.")
                break
        print()

def main():

    check_database_connections()
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
