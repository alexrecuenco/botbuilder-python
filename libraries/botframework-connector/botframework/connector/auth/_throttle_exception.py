from botframework.connector.retry_action import RetryParams


class ThrottleException(Exception):
    def __init__(self, message=None, inner_exception=None):
        super().__init__(message)
        self.inner_exception = inner_exception
        self.retry_params = None

    @property
    def retry_params(self):
        return self._retry_params

    @retry_params.setter
    def retry_params(self, value):
        if not isinstance(value, RetryParams) and value is not None:
            raise ValueError("RetryParams must be an instance of RetryParams class or None.")
        self._retry_params = value
