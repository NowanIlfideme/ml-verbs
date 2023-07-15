"""Basic tests for importability."""


def test_import_minimal():
    """Ensures importability."""
    from ml_verbs import __version__

    assert isinstance(__version__, str)
