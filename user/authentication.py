from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
from . import models

class CustomUserAuth(authentication.BaseAuthentication):
    """
    Custom authentication class using JSON Web Tokens (JWT).

    This class performs user authentication by decoding JWT tokens.

    Attributes:
        None

    Methods:
        authenticate: Decodes the JWT token and returns a user if authenticated.
    """

    def authenticate(self, request):
        """
        Authenticate the user using JWT token.

        Args:
            request (HttpRequest): The request object.

        Returns:
            tuple: A tuple containing the user and None, or None if authentication fails.
        """
        token = request.COOKIES.get('jwt')

        if not token:
            return None
        
        try: 
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except: 
            raise exceptions.AuthenticationFailed("Unauthorized")
        
        user = models.User.objects.filter(id=payload["id"]).first()

        return (user, None)
