# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_misc.ipynb (unless otherwise specified).

__all__ = ['AttrDict']

# Cell
class AttrDict(dict):
    """ Access dictionary elements as attributes. """
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self