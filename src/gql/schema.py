import strawberry
from strawberry import Schema


@strawberry.type
class HealthcheckResult:
    ok: bool


@strawberry.type
class Query:
    @strawberry.field
    def healthcheck(self) -> HealthcheckResult:
        return HealthcheckResult(ok=True)


schema = Schema(
    query=Query,
)
