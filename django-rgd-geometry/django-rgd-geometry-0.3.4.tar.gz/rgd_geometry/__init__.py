from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution('django-rgd-geometry').version
except DistributionNotFound:
    # package is not installed
    __version__ = None
