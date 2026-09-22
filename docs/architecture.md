
# 12 Core Fundamentals Architecture

สถาปัตยกรรมระบบ 12 เสาหลักแบบแยกหน้าที่ขาดจากกัน (Strict Separation of Concerns):

1. **Finite State Machine (FSM):** คุมสถานะของระบบ (`src/fsm/`) ป้องกันสเตตทับซ้อน
2. **Inbound Trap:** ดักจับ Event ขาเข้าจากฮาร์ดแวร์/OS (`src/interception/inbound/`)
3. **IPC Bus:** บัสสื่อสารสองทางแบบ Real-time เช่น WebSocket/CDP (`src/ipc/`)
4. **Pure Logic:** ตรรกะและกฎเกณฑ์บริสุทธิ์ ไร้ผลข้างเคียง (`src/logic/`)
5. **Watchdog:** เฝ้าระวังชีพจรโปรเซส ดักจับค้าง สั่ง Fail-Safe (`src/watchdog/`)
6. **Outbound Proxy:** มิดเดิลแวร์ดัดแปลงคำสั่งขาออกหรือสคริปต์แทรกแซง DOM (`src/interception/outbound/`)
7. **Actuation:** ตัวลงมือกระทำจริงกับ OS ผ่าน Native API (`src/actuation/`)
8. **Sensory:** ประสาทสัมผัสรับรู้อินพุตดิบ เช่น ไมค์, จอ, ตำแหน่งเคอร์เซอร์ (`src/sensory/`)
9. **Telemetry:** กล่องดำบันทึกประวัติและสตรีม Log (src/telemetry/, data/runtime/app.log)
10. **Config Matrix:** พิมพ์เขียวและค่าคงที่ของระบบ (`configs/`)
11. **State Historian:** บัฟเฟอร์และหน่วยความจำชั่วคราว (data/artifacts/, data/runtime/)
12. **Orchestrator:** สมองกลางควบคุมการปลุกและหมุนวงจรระบบ (`src/core/engine.py`, `src/app.py`)
