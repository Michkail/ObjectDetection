from fastapi import FastAPI
from strawberry.asgi import GraphQL
from api.graphql import schema
from api.rest import router as rest_router

app = FastAPI()
graphql_app = GraphQL(schema)

app.include_router(rest_router, prefix="/api/v1")
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
