from packaging import version

try:
    from functools import cache
except ImportError:  # Python < 3.9
    from functools import lru_cache

    cache = lru_cache(maxsize=None)


def pkg_metadata(package):
    from importlib.metadata import metadata as m

    return m(package)


@cache
def pkg_version(package):
    from importlib.metadata import version as v

    return version.parse(v(package))
