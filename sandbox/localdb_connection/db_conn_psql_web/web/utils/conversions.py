from datetime import datetime

def js_date_to_py_datetime(t_js):
    return datetime.strptime(t_js, "%Y-%m-%dT%H:%M:%S.%f%z")