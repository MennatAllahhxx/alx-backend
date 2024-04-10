#!/usr/bin/env python3
"""
Module contains index_range func
"""


def index_range(page: int, page_size: int) -> tuple:
    """AI is creating summary for index_range

    Args:
        page (int): page number
        page_size (int): items per page

    Returns:
        tuple: (start_idx, end_idx)
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
