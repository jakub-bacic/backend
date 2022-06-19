from starlette.applications import Starlette

from app import logging
from gql.app import graphql_app


def create_app() -> Starlette:
    logging.configure()

    app = Starlette()
    app.add_route("/graphql", graphql_app)
    app.add_websocket_route("/graphql", graphql_app)

    return app
