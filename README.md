<p align="center">
  Lyght
</p>
<p align="center">
  <img src="https://img.shields.io/pypi/v/lyght?style=flat-square">
  <img src="https://img.shields.io/github/commit-activity/y/SimeonAleksov/lyght?style=flat-square">
  <img src="https://img.shields.io/pypi/dm/lyght?style=flat-square">
  <img src="https://img.shields.io/pypi/status/lyght?style=flat-square">
  <img src="https://img.shields.io/pypi/l/lyght?style=flat-square">
  <img src="https://img.shields.io/github/workflow/status/SimeonAleksov/lyght/dev%20workflow?style=flat-square">
  <img src="https://img.shields.io/github/issues/SimeonAleksov/lyght?style=flat-square">
  <img src="https://img.shields.io/github/issues-pr-closed/SimeonAleksov/lyght?style=flat-square">
  <img src="https://img.shields.io/codecov/c/github/SimeonAleksov/lyght?style=flat-square">
</p>



Lighting fast python web framework.


* Documentation: <https://SimeonAleksov.github.io/lyght>
* GitHub: <https://github.com/SimeonAleksov/lyght>
* PyPI: <https://pypi.org/project/lyght/>


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install lyght.

```bash
pip install lyght
```

## Usage

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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)



## Features

* TODO



## Authors

- [@SimeonAleksov](https://www.github.com/SimeonAleksov)
