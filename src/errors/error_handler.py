from src.http_types.http_response import HttpResponse
from .error_types.http_conflict import HttpConflictError
from .error_types.http_not_found import HttpNotFoundError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        return HttpResponse(
            body={
                "error": [{
                    "title": error.name,
                    "details": error.message
                }]
            }, 
            status_code=error.status_code
        )
    
    return HttpResponse(
        body={
            "error": [{
                "title": "Erro interno",
                "details": str(error)
            }]
        }, 
        status_code=500
    )