import os
import socket

import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType, LDAPSearchUnion, ActiveDirectoryGroupType

ALLOWED_HOSTS = [ 'localhost',
                  '127.0.0.2',
                  '127.0.0.1',
                  '172.16.16.54',
                  '.mpi.nl',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9-wp-n%6h0f3t73pv$^##rt1b8s6aanuqmjnoq4$+tp8=a9)b2'

ADMINS = (
    ('Admin', 'pavithra.srinivasa@mpi.nl'),
)

# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mpi-trackonline',
        'USER': 'mpi-trackonline-admin',
        'PASSWORD': 'mpitrackonlinead*min', # enter db password here
        'HOST': 'localhost',
        'PORT': '',
    }
}

os.environ['DJANGO_SERVER_TYPE'] = 'PROD'
SITE_ID = 1

#Email Settings
USER_ADMIN_EMAIL = 'pavithra.srinivasa@mpi.nl'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = 'mailhost.mpi.nl'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'pavithra.srinivasa@mpi.nl'  # All error messages will be sent here. For different email backends, refer to here: https://docs.djangoproject.com/en/1.11/topics/email/
EMAIL_HOST_PASSWORD = ''  #

# captcha settings
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

#LDAP settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    "django.contrib.auth.backends.ModelBackend",
)

AUTH_LDAP_CONNECTION_OPTIONS = { ldap.OPT_DEBUG_LEVEL: 1,
                                 ldap.OPT_REFERRALS: 0, }

AUTH_LDAP_SERVER_URI = 'ldap://nt00.mpi.nl:389'

AUTH_LDAP_BIND_DN = 'CN=onexptrack,CN=Users,DC=mpi,DC=nl'
AUTH_LDAP_BIND_PASSWORD = '2a7b1aa6c'
AUTH_LDAP_USER_SEARCH = LDAPSearch('cn=Users,dc=mpi,dc=nl', ldap.SCOPE_SUBTREE, '(mail=%(user)s)')

AUTH_LDAP_USER_ATTR_MAP = {
'username': 'userPrincipalName',
'first_name': 'givenName',
'last_name': 'sn',
'email': 'mail',
}

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
            "cn=Users,dc=mpi,dc=nl", ldap.SCOPE_SUBTREE, "(objectCategory=Group)"
            )
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType(name_attr="cn")

AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600  # 1 hour cache

#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#    'is_active': 'CN=Users, DC=mpi, DC=nl',
#    'is_staff': 'CN=Users, DC=mpi, DC=nl',
#}

