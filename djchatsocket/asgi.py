import os
from django.core.asgi import get_asgi_application
import socketio

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djchatsocket.settings')
django_app = get_asgi_application()

# Import socketio_events after Django is initialized
from chat.socketio_events import sio

# Create Socket.IO ASGI application
application = socketio.ASGIApp(sio, django_app)