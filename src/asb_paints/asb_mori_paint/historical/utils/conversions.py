from datetime import datetime

def js_date_to_py_datetime(t_js):
    date_time = ""
    try:
        date_time = {"success": datetime.strptime(t_js, "%Y-%m-%dT%H:%M:%S.%f%z")}
        #date_time = datetime.strptime(t_js, "%Y-%m-%dT%H:%M:%S.%f%z")
    except Exception as e:
        date_time = {"error": "conversion-error-time", "exception": str(e), "class": e.__class__.__name__}
        print("Error:" + str(e))
    return date_time

def js_date_to_py_date(t_js):
    date_time = js_date_to_py_datetime(t_js)
    if "success" in date_time:
        date_time["success"] = date_time["success"].date()
    return date_time