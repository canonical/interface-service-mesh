from charms.reactive import Endpoint


class ServiceMeshProvides(Endpoint):
    def routes(self):
        return [
            relation.joined_units.received['route']
            for relation in self.relations
            if relation.joined_units.received_raw.get('route')
        ]
