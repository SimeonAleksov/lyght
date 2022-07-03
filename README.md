# light


[![pypi](https://img.shields.io/pypi/v/light.svg)](https://pypi.org/project/lyght//)
[![python](https://img.shields.io/pypi/pyversions/light.svg)](https://pypi.org/project/light/)
[![Build Status](https://github.com/SimeonAleksov/light/actions/workflows/dev.yml/badge.svg)](https://github.com/SimeonAleksov/light/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/SimeonAleksov/light/branch/main/graphs/badge.svg)](https://codecov.io/github/SimeonAleksov/light)



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
