class HttpNotFoundError(Exception):
    def __init__(self, messsage: str) -> None:
        super().__init__(messsage)
        self.message = messsage
        self.name = "Not Found"
        self. status_code = 404