#VERSION = (0, 5, 0, 'dev')
VERSION = (0, 5, 1)
__release__ = ''.join(['-.'[type(x) == int]+str(x) for x in VERSION])[1:]
__version__ = '.'.join((str(VERSION[0]), str(VERSION[1])))
