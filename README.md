# light


[![pypi](https://img.shields.io/pypi/v/lyght?style=for-the-badge)](https://img.shields.io/pypi/v/lyght?style=for-the-badge)
[![activity](https://img.shields.io/github/commit-activity/y/SimeonAleksov/lyght?style=for-the-badge)](https://img.shields.io/github/commit-activity/y/SimeonAleksov/lyght?style=for-the-badge)
[![downloads](https://img.shields.io/pypi/dm/lyght?style=for-the-badge)](https://img.shields.io/pypi/dm/lyght?style=for-the-badge)

[![status](https://img.shields.io/pypi/status/lyght?style=for-the-badge)](https://img.shields.io/pypi/status/lyght?style=for-the-badge)
[![license](https://img.shields.io/pypi/l/lyght?style=for-the-badge)](https://img.shields.io/pypi/l/lyght?style=for-the-badge)
[![Build Status](https://img.shields.io/github/workflow/status/SimeonAleksov/lyght/dev%20workflow?style=for-the-badge)](https://img.shields.io/github/workflow/status/SimeonAleksov/lyght/dev%20workflow?style=for-the-badge)
[![issues](https://img.shields.io/github/issues/SimeonAleksov/lyght?style=for-the-badge)](https://img.shields.io/github/issues/SimeonAleksov/lyght?style=for-the-badge)
[![prs](https://img.shields.io/github/issues-pr-closed/SimeonAleksov/lyght?style=for-the-badge)](https://img.shields.io/github/issues-pr-closed/SimeonAleksov/lyght?style=for-the-badge)
[![codecov](https://img.shields.io/codecov/c/github/SimeonAleksov/lyght?style=for-the-badge)](https://img.shields.io/codecov/c/github/SimeonAleksov/lyght?style=for-the-badge)



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
