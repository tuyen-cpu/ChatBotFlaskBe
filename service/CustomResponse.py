class CustomResponse:
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

        @property
        def status():
            return self.status

        @status.setter
        def status(value):
            self.status = value

        @property
        def data():
            return self.data

        @data.setter
        def data(value):
            self.data = data

        @property
        def message():
            return self.message
