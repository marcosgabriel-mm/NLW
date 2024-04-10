class HttpConflictError(Exception):
    def __init__(self, messsage: str) -> None:
        super().__init__(messsage)
        self.message = messsage
        self.name = "Conflict"
        self. status_code = 409