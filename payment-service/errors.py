class NetworkError(Exception):
    """Raised when there's a network error during a request.
    
    This could be due to various reasons including the server being down, or connectivity issues.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"Failed to retrieve balance for user {user_id}")


class InvalidResponseError(Exception):
    """Raised when the response from a request is not in the expected format or is invalid.

    This could be due to unexpected changes in the data model, or issues with the data itself.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"Invalid response format when retrieving balance for user {user_id}")
