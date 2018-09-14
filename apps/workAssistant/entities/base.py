class BaseResponse:
    def __init__(self, errCode, errMsg, result=None):
        self.result = result
        self.errCode = errCode
        self.errMsg = errMsg