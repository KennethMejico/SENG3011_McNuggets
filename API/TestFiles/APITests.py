import db_manager

def test_get_all_reports():
    db_manager.teardown()
    db_manager.setup()

if __name__ == "__main__":
    test_get_all_reports()
