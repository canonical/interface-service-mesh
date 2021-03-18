from dataclasses import dataclass, asdict
from typing import List

from provide_interface import ProvideAppInterface
from require_interface import RequireAppInterface

SERVICE_MESH_SCHEMA = """
prefix:
  type: string
rewrite:
  type: string
service:
  type: string
port:
  type: number
ingress:
  type: boolean
auth:
  type: object
"""


@dataclass
class Auth:
    request_headers: List[str]
    response_headers: List[str]


class ServiceMeshRequires(ProvideAppInterface):
    SCHEMA = SERVICE_MESH_SCHEMA

    def add_route(
        self, prefix, service, port, rewrite=None, ingress=False, auth: dict = {}
    ):
        if rewrite is None:
            rewrite = prefix

        # Primitive schema checking
        if auth:
            auth = asdict(Auth(**auth))

        self.update_relation_data(
            {
                "prefix": prefix,
                "rewrite": rewrite,
                "service": service,
                "port": port,
                "ingress": ingress,
                "auth": auth,
            }
        )


class ServiceMeshProvides(RequireAppInterface):
    SCHEMA = SERVICE_MESH_SCHEMA

    def routes(self):
        return self.data
