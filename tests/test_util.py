import pytest

from trombone.cache import Cache
from trombone.util import filepaths_loader

PDFS_PATH_PATTERN = './tests/data/pdfs/*.pdf'
EXPECTED_FILE_PATHS = [
    './tests/data/pdfs/ESPAF_022014_E.pdf',
    './tests/data/pdfs/ESPAF_022015_E.pdf',
    './tests/data/pdfs/ESVIF_032018_E.pdf',
    './tests/data/pdfs/ESVIF_032018_E_copy.pdf',
]


@pytest.fixture
def cache(tmp_path):
    return Cache(str(tmp_path.stem))


@pytest.mark.parametrize('batch_size', [1, 2, 3])
def test_filepaths_loader(cache, batch_size):
    for filepaths in filepaths_loader(PDFS_PATH_PATTERN, batch_size, cache):

        assert len(filepaths) <= batch_size
        for filepath in filepaths:
            assert filepath in EXPECTED_FILE_PATHS
