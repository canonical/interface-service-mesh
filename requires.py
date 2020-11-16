from charms.reactive import Endpoint
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Auth:
    request_headers: List[str]
    response_headers: List[str]


class ServiceMeshRequires(Endpoint):
    def add_route(
        self, prefix, service, port, rewrite=None, ingress=False, auth: dict = None
    ):
        if rewrite is None:
            rewrite = prefix

        # Primitive schema checking
        if auth:
            auth = asdict(Auth(**auth))

        for relation in self.relations:
            relation.to_publish["route"] = {
                "prefix": prefix,
                "rewrite": rewrite,
                "service": service,
                "port": port,
                "ingress": ingress,
                "auth": auth,
            }
