"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def get_random_ingredients(kind=None):
    """
    :param function: 수학적 표현으로 입력된 함수
    :type function: str
    :param center: 테일러 급수의 전개 중심
    :type center: int
    :param orders: 테일러 급수의 차수 목록
    :type orders: list[int]

    :return: None
    :rtype: None
    """
