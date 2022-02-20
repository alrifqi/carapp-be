def calculate_page_to_skip(page_size: int, page_num: int) -> int:
    return page_size * (page_num - 1)