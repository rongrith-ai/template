# Agent System Constitution

## 1. Architectural Invariant
- โค้ดทุกบรรทัดต้องจัดเก็บลงในโฟลเดอร์ตามความรับผิดชอบของ 12 เสาหลักใน `docs/architecture.md`
- ห้ามปนเปื้อน Logic เข้ากับ Actuation (Logic ต้องเป็น Pure Function เท่านั้น)
- ทุก Component หลักต้องสืบทอดแม่พิมพ์จาก `src/core/base.py`

## 2. Process Cleanup & Telemetry
- สคริปต์รันหรือตัว `app.py` ต้องบันทึก stdout/stderr ลง `runtime/latest_run.log` เสมอ
- ก่อนและหลังรัน ต้องมั่นใจว่าไม่มี Background Process ค้าง

## 3. Sprint Lifecycle Flow
1. **Intake Feedback:** อ่าน `FEEDBACK.md` ก่อนเริ่มงานทุกครั้ง สรุปแผนลง `TASK.md`
2. **Execute & Verify:** แก้ไขโค้ดและรันชุดทดสอบ `pytest tests/` ต้องผ่าน 100% (Zero Regression)
3. **Archive & Clean:** ย้ายงานที่เสร็จไปเก็บในประวัติ แล้วเคลียร์ `FEEDBACK.md`