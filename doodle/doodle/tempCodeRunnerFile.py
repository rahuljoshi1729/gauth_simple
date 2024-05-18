SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id':config('GOOGLE_OAUTH_CLIENT_ID'),
            'secret': config('GOOGLE_OAUTH_CLIENT_SECRET'),
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
    }
}