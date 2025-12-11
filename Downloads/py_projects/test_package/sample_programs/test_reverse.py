import pytest
import logging

log = logging.getLogger(__name__)

class TestReverse1:

    def test_steps(self):
        text = "apple"
        log.info("Using Slicing")
        reverse_text = text[::-1]
        log.info("reverse text: {}".format(reverse_text))

class TestReverse2:

    def test_steps(self):
        log.info("Using Reveres in-built")
        text = "apple"
        reversed_text = "".join(reversed(text))
        log.info("reverse text: {}".format(reversed_text))

class TestReverse3:

    def test_steps(self):
        log.info("Using Loop")
        text = "apple"
        rev = ""
        for ch in text:
            rev = ch + rev
        log.info("reversed text: {}".format(rev))