from datetime import timedelta

class RetryParams:
    MaxRetries = 10
    MaxDelay = timedelta(seconds=10)
    DefaultBackOffTime = timedelta(milliseconds=50)

    def __init__(self, retry_after=None, should_retry=True):
        self.should_retry = should_retry
        self.retry_after = retry_after or timedelta(0)

        # We don't allow more than MaxDelay seconds delay.
        if self.retry_after > self.MaxDelay:
            # We don't want to throw here though - if the server asks for more delay
            # than we are willing to, just enforce the upper bound for the delay
            self.retry_after = self.MaxDelay

    @classmethod
    def stop_retrying(cls):
        return cls(should_retry=False)

    @classmethod
    def default_back_off(cls, retry_count):
        if retry_count < cls.MaxRetries:
            return cls(cls.DefaultBackOffTime)
        else:
            return cls.stop_retrying()
        
    @property
    def should_retry(self):
        return self._should_retry

    @should_retry.setter
    def should_retry(self, value):
        self._should_retry = value

    @property
    def retry_after(self):
        return self._retry_after

    @retry_after.setter
    def retry_after(self, value):
        # You can add validation here if needed
        self._retry_after = value