import os

import pytest

from pytrombone import Trombone

TROMBONE_PATH = './bin/trombone-5.2.1-jar-with-dependencies.jar'


@pytest.fixture
def trombone():
    return Trombone(TROMBONE_PATH)


def test_get_version(trombone):
    output = trombone.get_version()

    assert 'version' in output


def test_run_coleman_liau_index(trombone):
    key_values = [
        ('tool', 'corpus.DocumentColemanLiauIndex'),
        ('file', './tests/data/pdfs/'),
        ('file', './tests/data/pdfs/ESVIF_032018_E.pdf'),
    ]

    output, _ = trombone.run(key_values)

    assert output != ""


def test_make_trombone_without_given_path():
    trombone = Trombone()

    assert os.path.exists(trombone.jar_path)
    output = trombone.get_version()
    assert 'version' in output


def test_run_with_wrong_trombone_path():
    with pytest.raises(FileNotFoundError):
        Trombone('./bad/file/path')


def test_run_with_wrong_file_path(trombone):
    key_values = [
        ('tool', 'corpus.DocumentColemanLiauIndex'),
        ('file', './bad/file/path'),
    ]

    output, err = trombone.run(key_values)

    assert output == ''
    assert 'FileNotFoundException' in err
