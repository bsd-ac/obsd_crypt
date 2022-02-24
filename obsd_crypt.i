%module obsd_crypt
%{
#define SWIG_FILE_WITH_INIT
#include "obsd_crypt.h"
%}

%rename(crypt_checkpass) obsd_checkpass;
bool obsd_checkpass(const char *password, const char *hash);

%rename(crypt_newhash) obsd_newhash;
%newobject obsd_newhash;
char *obsd_newhash(const char *password, int rounds = -1);
