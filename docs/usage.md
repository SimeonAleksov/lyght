# Usage

To use light in a project
#### An example lyght routing:

```python
from lyght.routes import Route, Routes


from example.controllers import MyController


home_routes = Route(
    path='/home',
    controller=MyController,
    name='example.home',
)


route_config = Routes(
    routes=[
        home_routes,
    ]
)
```
