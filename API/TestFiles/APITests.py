import db_manager
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import APIController

def test_search():
    db_manager.setup()
    db_manager.teardown()

if __name__ == "__main__":
    test_search()
