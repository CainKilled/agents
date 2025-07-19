from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.zero_trust_installer import _is_trusted_host, _validate_requirements


def test_is_trusted_host() -> None:
    assert _is_trusted_host("https://pypi.org/simple", {"pypi.org"})
    assert not _is_trusted_host("https://evil.com", {"pypi.org"})


def test_validate_requirements(tmp_path: Path) -> None:
    req = tmp_path / "req.txt"
    req.write_text("package==1.0 --hash=sha256:deadbeef\n")
    _validate_requirements(req)

    req.write_text("package==1.0\n")
    with pytest.raises(ValueError):
        _validate_requirements(req)
