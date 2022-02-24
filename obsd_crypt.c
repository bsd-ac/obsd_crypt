#include "obsd_crypt.h"

#include <pwd.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

bool obsd_checkpass(const char *password, const char *hash) {
	return crypt_checkpass(password, hash) == 0;
}

char *obsd_newhash(const char *password, int rounds) {
	char *hash;
	int err;

	hash = (char *)calloc(1, _PASSWORD_LEN);
	if (!hash) {
		return NULL;
	}

	if(rounds > 999)
		rounds = 999;

	char pref[12] = "bcrypt,";
	if(rounds == -1)
		snprintf(pref + 7, 5, "%s", "a");
	else
		snprintf(pref + 7, 5, "%d", rounds);

	int e = crypt_newhash(password, pref, hash, _PASSWORD_LEN);
	if (e == -1) {
		free(hash);
		return NULL;
	}
	return hash;
}
