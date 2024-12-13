from datetime import datetime
from typing import Union
class Post:
    """A representation of a blog post."""
    
    def __init__(self, id: Union[int, str], title: str, date: Union[datetime, str], content: str):
        """Initialize attributes."""
        self._id = id
        self._title = title
        self._date = date
        self._content = content

    @property
    def id(self):
        return self._id
    
    @property
    def content(self):
        return self._content
    
    @property
    def title(self):
        return self._title
    
    @property
    def date(self):
        return self._date
    
        