from charms.reactive import Endpoint


class ServiceMeshRequires(Endpoint):
    def add_route(self, prefix, service, port, rewrite=None):
        if rewrite is None:
            rewrite = prefix

        for relation in self.relations:
            relation.to_publish['route'] = {
                'prefix': prefix,
                'rewrite': rewrite,
                'service': service,
                'port': port
            }
