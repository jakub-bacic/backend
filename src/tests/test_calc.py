from gql.schema import schema

QUERY = """
mutation Calc($a: Int!, $b: Int!) {
  addNumbers(a: $a, b: $b) {
    result
  }
}
"""


async def test_add() -> None:
    resp = await schema.execute(QUERY, variable_values={"a": 1, "b": 100})

    assert resp.errors is None
    assert resp.data is not None

    assert resp.data["addNumbers"]["result"] == 101
