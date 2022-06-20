from gql.schema import schema

QUERY = """
query Healthcheck($works: Boolean!, $value: Int) {
  healthcheck(works: $works, value: $value) {
    ok
  }
}
"""


async def test_healthcheck() -> None:
    resp = await schema.execute(QUERY, variable_values={"works": True})

    assert resp.errors is None
    assert resp.data is not None

    assert resp.data["healthcheck"] == {"ok": True}


async def test_healthcheck_should_fail() -> None:
    resp = await schema.execute(QUERY, variable_values={"works": False})

    assert resp.errors is not None


async def test_healthcheck_with_value() -> None:
    resp = await schema.execute(QUERY, variable_values={"works": True, "value": 666})

    assert resp.errors is None
    assert resp.data is not None
