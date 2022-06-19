from gql.schema import schema

QUERY = """
query Healthcheck {
  healthcheck {
    ok
  }
}
"""


async def test_healthcheck():
    resp = await schema.execute(QUERY)

    assert resp.errors is None
    assert resp.data["healthcheck"] == {"ok": True}
