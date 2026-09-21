import logging
from typing import Any, Dict
from src.core.base import BaseComponent

logger = logging.getLogger("autonomous_engine")


class AutonomousEngine:
    """Supervisory Orchestrator คุมวงรอบชีวิตของระบบทั้งหมด"""

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.components: Dict[str, BaseComponent] = {}
        self.is_running = False

    def register(self, name: str, component: BaseComponent) -> None:
        """ลงทะเบียนชิ้นส่วนเข้าสู่วงจรควบคุม"""
        self.components[name] = component

    def start(self) -> None:
        """ปลุกทุก Component ขึ้นมาทำงานอย่างเป็นลำดับ"""
        logger.info("Engine booting up...")
        for name, comp in self.components.items():
            comp.initialize()
            logger.info(f"Component [{name}] online.")
        self.is_running = True

    def stop(self) -> None:
        """ชัตดาวน์ทุก Component ย้อนลำดับอย่างปลอดภัย"""
        logger.info("Engine shutting down...")
        for name, comp in reversed(list(self.components.items())):
            try:
                comp.shutdown()
                logger.info(f"Component [{name}] stopped.")
            except Exception as e:
                logger.error(f"Error stopping [{name}]: {e}")
        self.is_running = False