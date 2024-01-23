from parser.models import ParsingResult


class ParsingRepository:
    @staticmethod
    def get_parsing_results():
        parsing_values = ParsingResult.objects.order_by('-created_at')[:10]
        return parsing_values