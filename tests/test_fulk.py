from click.testing import CliRunner
import pytest
import fulk


@pytest.fixture(scope="module")
def runner():
    return CliRunner()

def test_fulk(runner):
    result = runner.invoke(fulk.main, ["-p", "test"])
    assert result.exit_code == 0
    assert "files renamed" in result.output

