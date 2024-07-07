import logging


class IgnoreSpecificTemplateError(logging.Filter):
    def filter(self, record):
        return not any(
            msg in record.getMessage()
            for msg in ['hide_label', 'placeholder', 'autofocus']
        )

