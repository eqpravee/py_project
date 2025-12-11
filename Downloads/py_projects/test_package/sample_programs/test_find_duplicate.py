import pytest
import logging

log = logging.getLogger(__name__)

class TestFindDuplicate1:

    def test_steps(self):
        number = [1, 2, 3, 3, 4, 5]
        duplicate = []
        seen = []
        for num in number:
            if num in seen:
                duplicate.append(num)
            else:
                seen.append(num)
        log.info("seen: {}".format(duplicate))

class TestFindDuplicate2:
    