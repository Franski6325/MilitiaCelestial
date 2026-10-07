from militiacelestial.cli import app


def test_import_main() -> None:
    import militiacelestial.__main__ as main

    assert main.app is app
