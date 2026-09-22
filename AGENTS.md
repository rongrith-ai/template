# Agent Guidelines & Engineering Protocols (12 Pillars Standard)

เอกสารนี้คือกฎเหล็กและมาตรฐานวิศวกรรมกลางสำหรับ AI Agent (Worker) ทุกตัวในทุกโปรเจกต์ที่ใช้แม่แบบนี้

---

## 1. Operating Protocol (ลำดับขั้นตอนปฏิบัติงาน)
1. **System Governance: อ่านและยึดข้อกำหนดใน AGENTS.md เป็นแนวทางหลัก พร้อมทั้งศึกษาพิมพ์เขียว 12 เสาหลักจาก docs/ARCHITECTURE.md ก่อนวางโครงสร้างโค้ดเสมอ
2. **Task Intake:** อ่าน Scope, Functional Requirements และเงื่อนไขการทดสอบจาก `FEEDBACK.md` เท่านั้น (ห้ามเพิ่ม Scope เอง)
3. **Execution Plan:** แตกรายการงานย่อยเป็น Checkbox ลงใน `TASK.md` ก่อนเริ่มแตะโค้ด และอัปเดตสถานะ `[x]` ทุกครั้งที่เสร็จแต่ละข้อย่อย
4. **Verification First:** เขียนหรือปรับปรุง Automated Test ใน `tests/` ควบคู่เสมอ และต้องรัน `pytest` ผ่านครบ 100% ก่อนส่งมอบงาน
5. **Architectural Immutability:** ห้าม Agent แก้ไข เพิ่มเติม หรือลบไฟล์ใน `docs/` (`ARCHITECTURE.md`, `FEEDBACK_TEMPLATE.md`) และห้ามดัดแปลงโครงสร้างโฟลเดอร์หลักเด็ดขาด เว้นแต่จะได้รับคำสั่งเฉพาะจากมนุษย์

---

## 2. Universal Engineering Standards
* **Encoding Guard:** ทุกไฟล์โค้ด, ไฟล์คอนฟิก, เอกสาร Markdown, และ I/O Logging Streams ต้องบังคับใช้รหัสภาษา `UTF-8` อย่างเด็ดขาด
* **Zero Regression:** การเพิ่มฟีเจอร์หรือแก้บั๊กต้องไม่กระทบต่อฟังก์ชันเดิมที่ผ่านการทดสอบแล้ว
* **Robust Input Handling:** อินพุตจากภายนอก (Hardware Signals, Event Hooks, API Callbacks) ต้องมีกลไก Debounce, Queue หรือ Lock ป้องกัน Race Condition
* **Path Sanitization:** ห้ามใช้ Hardcoded Absolute Path ให้ใช้ Relative Path ผ่าน `pathlib.Path` อ้างอิงจาก Project Root เสมอ

---

## 3. Universal Directory Layout & Roles
* `src/` — รหัสต้นฉบับของโปรแกรม (แยก Core Logic, Handlers, Interfaces ตาม 12 เสาหลัก)
* `tests/` — ชุดทดสอบระบบอัตโนมัติ (Unit, Integration, Mocks)
* `configs/` — ไฟล์ตั้งค่าถาวรของระบบ (Configuration Schemas, Settings)
* `data/artifacts/` — ไฟล์สื่อและผลลัพธ์ระหว่างทาง (รูปแคป, บันทึกเสียง, มัลติมีเดีย, ข้อมูลนำเข้าชั่วคราว)
* `data/runtime/` — ข้อมูลสถานะขณะโปรแกรมทำงาน (Logs, Ephemeral States, PID) โดยมี `.gitkeep` รักษาโครงสร้าง
* `data/cache/` — ข้อมูลแคชชั่วคราวและผลลัพธ์การคำนวณซ้ำ
* `docs/` — เอกสารสถาปัตยกรรมและเทมเพลตมาตรฐาน (`ARCHITECTURE.md`, `FEEDBACK_TEMPLATE.md`)

---

## 4. Runtime Logging & State Policy
* บันทึก Execution Log ลงใน `data/runtime/app.log` (UTF-8) เสมอ พร้อมระบุ Timestamp และ Log Level (INFO, WARNING, ERROR)
* สถานะชั่วคราวของเซสชันหรืออินเทอร์เฟซ (Ephemeral State) ให้บันทึกเป็น JSON ภายใน `data/runtime/`
* ข้อมูลทั้งหมดใน `data/` (ยกเว้น `.gitkeep`) ต้องถูก Ignore ไม่ให้อัปโหลดขึ้น Version Control

---

## 5. Clean Handoff & UAT Preparation Protocol
เมื่อดำเนินการ Step 4 (Implementation & Test ผ่าน 100%) และอัปเดต `TASK.md` เสร็จสิ้น Agent ต้องปฏิบัติตามลำดับส่งมอบงานให้มนุษย์ (PO/Tester) ดังนี้:

1. **Targeted Process Cleanup (ห้ามกวาดล้าง Python ทั้งเครื่อง):**
   - ตรวจสอบและยุติเฉพาะ Background Process / CDP Worker ที่โปรเจกต์นี้สร้างขึ้นเท่านั้น (โดยอ้างอิงจาก PID ใน `data/runtime/app.pid` หรือ Port/Session ของโปรเจกต์)
   - ห้ามรันคำสั่งฆ่าโปรเซสแบบกวาดล้าง (เช่น `taskkill /IM python.exe /F`) เด็ดขาด
2. **Terminal Reset:**
   - เคลียร์หน้าต่าง Terminal ให้สะอาดเรียบร้อย
3. **Single-Action UAT Trigger:**
   - ในรายงานสรุปส่งมอบงานข้อสุดท้าย Agent ต้องจัดเตรียม **"คำสั่งบรรทัดเดียวพร้อมกด Enter"** สำหรับให้ User ก๊อปปี้ไปรัน เพื่อเริ่มระบบและทดสอบ UAT หน้างานได้ทันที เช่น:
     > `python src/main.py`