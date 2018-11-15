from __future__ import unicode_literals
from .responses import ResourceGroupsResponse

url_bases = [
    "https?://resource-groups(-fips)?.(.+).amazonaws.com",
]

url_paths = {
    '{0}': ResourceGroupsResponse.dispatch,
}
