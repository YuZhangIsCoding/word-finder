from unittest import mock

import pytest

from word_finder import __main__


def test_main(tmpdir_factory):
    tmp_cache = str(tmpdir_factory.mktemp("tmp_cache"))
    with pytest.raises(SystemExit) as e:
        with mock.patch("sys.argv", ["", "mince", "--cache", tmp_cache]):
            __main__.main()

        assert e.type == SystemExit
        assert e.value.code == 0
