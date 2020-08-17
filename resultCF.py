def cf_res(res, error_code, data):
    res["error_code"] = error_code
    res["data"] = data

    return res