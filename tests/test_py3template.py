from py3template.sample import Sample


def test_dummy():
    assert 1 == 1


def test_sample():
    s = Sample(1)
    assert s.data == 1
