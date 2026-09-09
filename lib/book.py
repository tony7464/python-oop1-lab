#!/usr/bin/env python3


class Book:
    """A book that a customer can browse in the store."""

    def __init__(self, title, page_count):
        # Store the title as-is, then use the setter so page_count is validated.
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Return the number of pages in the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        # Only accept whole numbers. If the value is not an int, explain why.
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Print a message when the reader flips to the next page."""
        print("Flipping the page...wow, you read fast!")
