from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport


class ApiClient:
    __instance: Client | None = None
    __transport: AIOHTTPTransport = AIOHTTPTransport(
        url="wss://api.toweroffantasy.info/graphql"
    )

    @classmethod
    def get_instance(cls) -> Client:
        if cls.__instance is None:
            cls.__instance = Client(transport=cls.__transport)
        return cls.__instance
