from py3template.sample import Sample


def test_dummy():
    assert 1 == 1


def test_sample():
    s = Sample(1)
    assert s.data == 1


def test_sample_stdout(capsys):
    s = Sample(1)
    s.print_data()
    out, err = capsys.readouterr()
    assert out == "1\n"
