from random import choices
from string import ascii_uppercase, digits

from obsd_crypt import crypt_checkpass, crypt_newhash


def test_newhash_default():
    pass_len = 24
    for i in range(15):
        password = ''.join(choices(ascii_uppercase + digits, k=pass_len))
        password_hash = crypt_newhash(password)
        assert (password_hash)
        print(password_hash)
        assert (crypt_checkpass(password, password_hash))

def test_newhash_neg():
    pass_len = 24
    for i in range(15):
        password = ''.join(choices(ascii_uppercase + digits, k=pass_len))
        password_hash = crypt_newhash(password, -1)
        assert (password_hash)
        print(password_hash)
        assert (crypt_checkpass(password, password_hash))

def test_newhash_pos():
    pass_len = 24
    for i in range(15):
        password = ''.join(choices(ascii_uppercase + digits, k=pass_len))
        password_hash = crypt_newhash(password, 10)
        assert (password_hash)
        print(password_hash)
        assert (crypt_checkpass(password, password_hash))
