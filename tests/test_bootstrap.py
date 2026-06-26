from archie.app.runtime import Runtime


def test_runtime_initial_state() -> None:
    runtime = Runtime()

    assert runtime.state.name == "STOPPED"
