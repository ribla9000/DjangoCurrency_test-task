from testTask.core.response import create_response
from django.http import HttpRequest, JsonResponse
from parser.repository.parsing import ParsingRepository
from .tasks import make_request_to_exchangerate_api


shceduled_task = make_request_to_exchangerate_api.delay()


def get_parsed_values(request: HttpRequest):
    v = ParsingRepository.get_parsing_results()
    if v is None:
        return create_response(code=404, message="Parsed values hasn't been founded")
    payload = create_response(data=list(v.values()))
    return JsonResponse(payload, safe=False)
