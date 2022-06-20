from typing import Optional

import strawberry
from strawberry import Schema

from app.logging import bind_context, get_logger

logger = get_logger()


def something() -> None:
    logger.info("Within something")


@strawberry.type
class HealthcheckResult:
    ok: bool


@strawberry.type
class Query:
    @strawberry.field
    def healthcheck(
        self, works: bool = True, value: Optional[int] = None
    ) -> HealthcheckResult:
        logger.warning("Handling healtcheck")

        if value:
            bind_context(value=value)
        if not works:
            raise ValueError("123")
        something()
        return HealthcheckResult(ok=True)


@strawberry.type
class AddResult:
    result: int


@strawberry.type
class Mutation:
    @strawberry.field
    def add_numbers(self, a: int, b: int) -> AddResult:
        return AddResult(result=a + b)


schema = Schema(
    query=Query,
    mutation=Mutation,
)
