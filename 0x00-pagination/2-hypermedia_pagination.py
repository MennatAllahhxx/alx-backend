#!/usr/bin/env python3
"""
Module contains index_range func
"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """AI is creating summary for get_page

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): items per page. Defaults to 10.

        Returns:
            List[List]: the appropriate page of the datase
        """
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)
        limit_idxes = index_range(page, page_size)
        self.dataset()
        return self.__dataset[limit_idxes[0]:limit_idxes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """AI is creating summary for get_hyper

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): items per page. Defaults to 10.

        Returns:
            dict: a dictionary containing set of key-value pairs
        """
        self.dataset()
        total_pages: int = math.ceil(len(self.__dataset) / page_size)
        data: List[List[str]] = self.get_page(page, page_size)
        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1
        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
