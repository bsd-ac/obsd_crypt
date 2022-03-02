%module obsd_crypt
%{
#define SWIG_FILE_WITH_INIT
#include "obsd_crypt.h"
%}

%rename(crypt_checkpass) obsd_checkpass;
/**
 * Check a password against a given hash.
 *
 * If both the hash and the password are the empty string,
 * authentication is a success. Otherwise, the password is
 * hashed and compared to the provided hash. If the hash is
 * empty, authentication will always fail, but a default
 * amount of work is performed to simulate the hashing operation.
 * A successful match returns True and a failure returns False.
 *
 * @param password password to check.
 * @param hash hash to check against.
 *
 * @return True If the hash validates the password.
 * @return False If the hash does not validate the password.
 */
bool obsd_checkpass(const char *password, const char *hash);

%rename(crypt_newhash) obsd_newhash;
%newobject obsd_newhash;
/**
 * Return a new hash for a password.
 *
 * The provided password is randomly salted and hashed and returned
 * as a string using the bcrypt algorith. The number of rounds
 * can be any integer between 4 and 31, inclusive. If the number
 * of rounds is not given or is negative, an appropriate number
 * of rounds is automatically selected based on system performance.
 *
 * @param password password to hash.
 * @param rounds number of rounds to pass to bcrypt.
 *
 * @return A new hash for the password.
 */
char *obsd_newhash(const char *password, int rounds = -1);
