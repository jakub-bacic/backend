import logging
import sys

import structlog
from structlog.processors import CallsiteParameter
from logfmter import Logfmter


def configure():
    # structlog.configure(
    #     processors=[
    #         structlog.stdlib.filter_by_level,
    #         structlog.stdlib.add_logger_name,
    #         structlog.stdlib.add_log_level,
    #         structlog.stdlib.PositionalArgumentsFormatter(),
    #         structlog.processors.StackInfoRenderer(),
    #         structlog.processors.format_exc_info,
    #         structlog.processors.UnicodeDecoder(),
    #         # Transform event dict into `logging.Logger` method arguments.
    #         # "event" becomes "msg" and the rest is passed as a dict in
    #         # "extra". IMPORTANT: This means that the standard library MUST
    #         # render "extra" for the context to appear in log entries! See
    #         # warning below.
    #         structlog.stdlib.render_to_log_kwargs,
    #     ],
    #     logger_factory=structlog.stdlib.LoggerFactory(),
    #     wrapper_class=structlog.stdlib.BoundLogger,
    #     cache_logger_on_first_use=True,
    # )
    #
    # logging.getLogger("uvicorn").handlers = []
    #
    # handler = logging.StreamHandler(sys.stdout)
    # handler.setFormatter(Logfmter())
    #
    # root_logger = logging.getLogger()
    # root_logger.addHandler(handler)

    logging.getLogger("uvicorn").handlers = []
    logging.getLogger("strawberry").handlers = []

    timestamper = structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S")
    shared_processors = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        timestamper,
    ]

    structlog.configure(
        processors=shared_processors + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    formatter = structlog.stdlib.ProcessorFormatter(
        # These run ONLY on `logging` entries that do NOT originate within
        # structlog.
        foreign_pre_chain=shared_processors,
        # These run on ALL entries after the pre_chain is done.
        processors=[
            # Remove _record & _from_structlog.
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            # structlog.dev.ConsoleRenderer(),
            # structlog.processors.JSONRenderer(),
            structlog.processors.LogfmtRenderer(),
        ],
    )

    handler = logging.StreamHandler()
    # Use OUR `ProcessorFormatter` to format all `logging` entries.
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)
