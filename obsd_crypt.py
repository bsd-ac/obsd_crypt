# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _obsd_crypt
else:
    import _obsd_crypt

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def crypt_checkpass(password: str, hash: str) -> bool:
    r"""
    Check a password against a given hash.

    If both the hash and the password are the empty string,
    authentication is a success. Otherwise, the password is
    hashed and compared to the provided hash. If the hash is
    empty, authentication will always fail, but a default
    amount of work is performed to simulate the hashing operation.
    A successful match returns True and a failure returns False.

    :type password: string
    :param password: password to check.
    :type hash: string
    :param hash: hash to check against.

    :rtype: boolean
    :return: True If the hash validates the password.
    :rtype: boolean
    :return: False If the hash does not validate the password.
    """
    return _obsd_crypt.crypt_checkpass(password, hash)

def crypt_newhash(password: str, rounds: int = -1) -> str:
    r"""
    Return a new hash for a password.

    The provided password is randomly salted and hashed and returned
    as a string using the bcrypt algorith. The number of rounds
    can be any integer between 4 and 31, inclusive. If the number
    of rounds is not given or is negative, an appropriate number
    of rounds is automatically selected based on system performance.

    :type password: string
    :param password: password to hash.
    :type rounds: int, optional
    :param rounds: number of rounds to pass to bcrypt.

    :rtype: string
    :return: A new hash for the password.
    """
    return _obsd_crypt.crypt_newhash(password, rounds)


