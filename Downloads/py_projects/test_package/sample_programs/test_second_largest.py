import pytest
import logging

log = logging.getLogger(__name__)

class TestSecondLargest1:

    def test_steps(self):
        log.info("Using sorted method")
        text = [1, 2, 4, 22, 95, 101]
        text = sorted(text)
        log.info("Sorted text: {}".format(text))
        second_largest = text[-2]
        log.info("second largest:{}".format(second_largest))

class TestSecondLargest2:

    def test_steps(self):
        log.info("Using Loop")
        text = [1, 2, 4, 22, 95, 101]
        first = float('-inf')
        second = float('-inf')
        for ch in text:
            if ch > first:
                second = first
                first = ch
            elif ch > second and ch != first:
                second = ch

        log.info("second largest:{}".format(second))

class TestSecondLargest3:

    def test_steps(self):
        log.info("Using Max")
        text = [1, 2, 4, 22, 95, 101]
        remove_largest = text.remove(max(text))
        log.info("remove largest: {}".format(remove_largest))
        second_largest = max(text)
        log.info("second largest:{}".format(second_largest))