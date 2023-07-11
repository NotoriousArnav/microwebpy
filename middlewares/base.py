class BaseMiddleware(object):
    name = "Base Middleware"
    import_name = "base_middleware"
    def __call__(self, request):
        return request


