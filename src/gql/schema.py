import strawberry
import structlog
from strawberry import Schema


logger = structlog.get_logger()


@strawberry.type
class HealthcheckResult:
    ok: bool


@strawberry.type
class Query:
    @strawberry.field
    def healthcheck(self) -> HealthcheckResult:
        logger.warning("Handling healtcheck", test=123)
        raise ValueError("123")
        return HealthcheckResult(ok=True)


schema = Schema(
    query=Query,
)
