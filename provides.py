import json

from charms.reactive import Endpoint


class ServiceMeshProvides(Endpoint):
    def routes(self):
        return [
            json.loads(relation.joined_units.received_raw['route'])
            for relation in self.relations
            if relation.joined_units.received_raw.get('route')
        ]
