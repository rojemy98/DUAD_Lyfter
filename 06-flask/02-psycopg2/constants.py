"""
Application constants.

This module contains all valid status values used throughout
the application to avoid hardcoding strings in multiple places.
"""

# Valid statuses for cars
CAR_STATUS = [
    "Available",
    "Rented",
    "Maintenance"
]

# Valid statuses for users
USER_STATUS = [
    "Active",
    "Inactive",
    "Suspended"
]

# Valid statuses for rentals
RENTAL_STATUS = [
    "Active",
    "Completed"
]