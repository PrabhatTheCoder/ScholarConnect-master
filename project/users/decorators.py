from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import reverse
from functools import wraps



def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_group(user):
        if user.groups.filter(name__in=group_names).exists() or user.is_superuser:
            return True
        return False

    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if in_group(request.user):
                return view_func(request, *args, **kwargs)
            else:
                # Render a template with an error message
                error_message = "You don't have permission to access this page."

                return render(request, 'users/access_error.html', {'error_message': error_message})

        return wrapped_view

    return decorator
