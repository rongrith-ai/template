from src.core.base import BaseComponent
from src.core.engine import AutonomousEngine


class DummyComponent(BaseComponent):

    def __init__(self):
        self.initialized = False

    def initialize(self) -> None:
        self.initialized = True

    def shutdown(self) -> None:
        self.initialized = False


def test_engine_lifecycle():
    engine = AutonomousEngine()
    dummy = DummyComponent()
    engine.register("dummy", dummy)

    engine.start()
    assert engine.is_running is True
    assert dummy.initialized is True

    engine.stop()
    assert engine.is_running is False
    assert dummy.initialized is False