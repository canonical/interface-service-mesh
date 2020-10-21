Overview
========

This repository hosts code for the Service Mesh interface

Usage
=====

### Service Mesh provider

```yaml
# metadata.yaml
...
provides:
  service-mesh:
    interface: service-mesh
```

### Service Mesh requirer

```yaml
# metadata.yaml
...
requires:
  service-mesh:
    interface: service-mesh
```

### All Service Mesh charms

```yaml
# layer.yaml
includes:
  ...
  - "interface:service-mesh"
```

### Provider charm handling

``` python
routes = endpoint_from_name('service-mesh').routes()
```

### Requirer charm handling

``` python
@when('endpoint.service-mesh.joined')
def configure_mesh():
    endpoint_from_name('service-mesh').add_route(
        prefix='/foo',
        service=hookenv.service_name(),
        port=hookenv.config('port'),
    )
```
