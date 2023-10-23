#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page, page_size):
    """
    Return a tuple of the start and end index for a given page and page size.

    :param page: The current page number (1-indexed).
    :param page_size: The number of items per page.
    :return: A tuple of (start_index, end_index).
    """
    if page <= 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index
