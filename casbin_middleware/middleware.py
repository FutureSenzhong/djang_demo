import casbin


class CasbinMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # load the casbin model and policy from files.
        # change the 2nd arg to use a database.
        self.enforcer = casbin.Enforcer("casbin_middleware/authz_model.conf", "casbin_middleware/authz_policy.csv")

    def check_permission(self, request):
        # change the user, path, method as you need.
        user = request.user.username
        if request.user.is_anonymous:
            user = 'anonymous'
        path = request.path
        method = request.method
        return self.enforcer.enforce(user, path, method)
