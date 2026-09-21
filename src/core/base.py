from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseComponent(ABC):
    """แม่พิมพ์พื้นฐานสำหรับทุกเสาหลักใน 12 Pillars"""

    @abstractmethod
    def initialize(self) -> None:
        """เตรียมความพร้อมทรัพยากรตอนบูตระบบ"""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """ทำลายและคืนทรัพยากรเมื่อปิดระบบแบบปลอดภัย"""
        pass


class BaseInboundTrap(BaseComponent):
    """แม่พิมพ์สำหรับตัวดักจับสัญญาณขาเข้า"""

    @abstractmethod
    def start_hook(self) -> None:
        pass

    @abstractmethod
    def stop_hook(self) -> None:
        pass


class BaseActuator(BaseComponent):
    """แม่พิมพ์สำหรับตัวลงมือกระทำระดับ OS/Native"""

    @abstractmethod
    def execute(self, action_name: str, payload: Dict[str, Any]) -> bool:
        pass