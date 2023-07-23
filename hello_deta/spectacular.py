exclude_paths = [
    '/schema',
]


def preprocessing_filter(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        if path not in exclude_paths:
            filtered.append((path, path_regex, method, callback))
    return filtered


settings = {
    'PREPROCESSING_HOOKS': ['LTCS.spectacular.preprocessing_filter'],
    'TITLE': 'LTCS API',
    'VERSION': '1.0.0',
    'SWAGGER_UI_SETTINGS': {
        'defaultModelsExpandDepth': -1
    }
}
