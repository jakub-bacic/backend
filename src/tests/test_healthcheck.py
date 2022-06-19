from gql.schema import schema

QUERY = """
query Healthcheck {
  healthcheck {
    ok
  }
}
"""


async def test_healthcheck() -> None:
    resp = await schema.execute(QUERY)

    assert resp.errors is None
    assert resp.data is not None

    assert resp.data["healthcheck"] == {"ok": True}
