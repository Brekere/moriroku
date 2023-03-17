restSuccess = "SUCCESS"
restError = "ERROR"
restWarning = "WARNING"

def create_response_data(restType, info_msg, list_error = None, data_result = None):
    if list_error is None:
        data_error = {"rest": restType, "info": info_msg}
        if data_result is not None:
            for d_r in data_result:
                data_error[d_r] = data_result[d_r]
    else:
        data_error = {"rest": restType, "info": info_msg, "list_error": list_error}
    return data_error