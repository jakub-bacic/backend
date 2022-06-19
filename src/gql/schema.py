import strawberry
import structlog
from strawberry import Schema

from app.logging import get_logger

logger = get_logger()


@strawberry.type
class HealthcheckResult:
    ok: bool


@strawberry.type
class Query:
    @strawberry.field
    def healthcheck(self, works: bool = True) -> HealthcheckResult:
        logger.warning("Handling healtcheck", test=123)
        if not works:
            raise ValueError("123")
        return HealthcheckResult(ok=True)


schema = Schema(
    query=Query,
)
