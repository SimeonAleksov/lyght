_DEFAULT_PORTS  = {
    "http": 80,
    "https": 443,
}
_PROTOCOLS = ("http", )
_SECURE_PROTOCOLS = ("https", )


def get_protocols():
    return {
        'secure': _SECURE_PROTOCOLS,
        'default': _PROTOCOLS,
    }


def get_ports():
    return _DEFAULT_PORTS
