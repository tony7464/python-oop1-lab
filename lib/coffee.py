#!/usr/bin/env python3


class Coffee:
    """A coffee drink sold alongside books in the store."""

    # These are the only cup sizes the shop offers.
    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        # Use the size setter so invalid sizes are caught right away.
        self.size = size
        self.price = price

    @property
    def size(self):
        """Return the drink size (Small, Medium, or Large)."""
        return self._size

    @size.setter
    def size(self, size):
        # Reject anything that is not one of the three menu sizes.
        if size in self.VALID_SIZES:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """Thank the customer and add $1 to the drink price."""
        print("This coffee is great, here\u2019s a tip!")
        self.price += 1
