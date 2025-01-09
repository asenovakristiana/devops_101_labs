from starlette.requests import Request
import traceback
import uuid


def dump_request(request: Request, response, error: str = None, exception=None, process_time=None):
    status_code = response.status_code if response else None
    result = {
        'message': f"{request.method} {str(request.url)} {status_code}",
        'path': request.path_params,
        'query': request.query_params,
        "http_code": status_code,
        'url': str(request.url),
        'method': str(request.method),
        'source_ip': request.client.host,
        'error': error,
        'exception': type(exception).__name__ if error else None,
        'process_time': process_time.total_seconds(),
        'traceback': traceback.format_exc().split('\n') if error else [],
        'headers': dict(request.headers)
    }

    # noinspection PyProtectedMember
    if 'token' in request.state._state:
        result['token'] = request.state.token

    if 'trace-id' in request.headers:
        result['trace-id'] = request.headers['trace-id']
    else:
        result['trace-id'] = uuid.uuid4()

    return result