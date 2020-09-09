DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail',
            'DB_USER': 'retail_user',  # we pass all these as an environ variable (production)
            'DB_PASS': '#Abcd4321'
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail',
            'DB_USER': 'retail_user',
            'DB_PASS': '#Abcd4321'
        }
    }
}