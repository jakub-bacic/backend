from strawberry.asgi import GraphQL

from .schema import schema

graphql_app = GraphQL(schema=schema)
