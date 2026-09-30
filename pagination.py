"""Small, dependency-free pagination helpers."""


def has_next_page(total_items: int, offset: int, page_size: int) -> bool:
    """Return whether any items remain after the current page."""
    if total_items < 0 or offset < 0 or page_size < 0:
        raise ValueError("total_items and offset must be nonnegative; page_size must be positive")
    return offset + page_size < total_items
