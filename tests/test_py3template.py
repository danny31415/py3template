import os

import vcr

from py3template.sample import Sample, ApiStuff

dir_name = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(dir_name)
vcr_fixture_dir = os.path.join(parent_dir, 'fixtures', 'vcr_cassettes')


def vcr_fixture(name):
    return os.path.join(vcr_fixture_dir, name)


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


@vcr.use_cassette(vcr_fixture('test_api.yaml'), record_mode='once')
def test_api():
    a = ApiStuff('http://demo.ckan.org/api/3/action/group_list')
    r = a.make_call({'id': 'data-explorer'})
    j = r.json()
    assert j['success'] == True
