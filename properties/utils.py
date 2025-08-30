from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try fetching from cache
    properties = cache.get('all_properties')
    
    if properties is None:
        # Cache miss → query database
        properties = list(Property.objects.all().values(
            "id", "title", "description", "price", "location", "created_at"
        ))
        # Store in Redis for 1 hour (3600s)
        cache.set('all_properties', properties, 3600)
    
    return properties
