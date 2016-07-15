# -*- coding: utf-8 -*-

import pytest
import sample

def test_dummy():
    assert(sample.dummy() == 1)

def test_dummy2():
    assert(sample.dummy() != 1)
