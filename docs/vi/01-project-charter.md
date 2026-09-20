# 01 — Project charter

## Định nghĩa

**AELC (Agentic Engineering Lifecycle)** là engineering method độc lập với harness, đưa AI agents vào vòng đời phát triển phần mềm nhưng vẫn giữ understanding, judgment, ownership và accountability ở con người. AELC kết hợp các định nghĩa method, Python runtime, global installer và những adapter mỏng cho các agent harness hiện có.

AELC **không phải** AI model, agent harness xây mới từ đầu, công cụ chấm điểm hiệu suất nhân viên hoặc cơ chế tự động cho phép merge code do AI sinh. Harness thực hiện phần công việc agent; AELC quy định context, trách nhiệm, verification, knowledge và project integration.

## Cam kết cốt lõi

> Giảm tối đa công việc làm lại, nhưng giữ tối đa sự hiểu biết thực sự của con người.

Agent đảm nhiệm exploration, research, tracing, hỗ trợ implementation và verification tốn thời gian khi khả thi. Human vẫn phải hiểu đủ những thay đổi quan trọng để phản biện kết luận, cân nhắc trade-off và sở hữu rủi ro hệ thống được chấp nhận. Human verification **không có nghĩa** mặc định làm lại toàn bộ việc của agent.

## Đối tượng hưởng lợi

- **Engineer:** exploration và implementation nhanh hơn mà không phải chấp nhận output thụ động.
- **Member mới:** onboarding theo role và xây được mental model về project có thể chứng minh.
- **Tech Lead/Senior:** giảm việc giải thích/review căn bản lặp lại và phát hiện nơi knowledge đang tập trung.
- **Team/tổ chức:** giảm phụ thuộc vào một, hai người nắm kiến thức then chốt và truy vết được ai chấp nhận thay đổi.

## Hình thái sản phẩm

Một bản cài AELC **toàn cục** có thể phục vụ nhiều project và nhiều agent harness. Project chỉ lưu shared context/configuration của chính nó và cấu hình harness bổ sung khi cần; identity và session state cá nhân được lưu tách biệt. Method và resource được update tập trung, còn project-schema migration là operation riêng.

## Kết quả kỳ vọng, không phải lời hứa tự động hóa hoàn toàn

Thành công là engineering work hữu ích được thực hiện nhanh hơn, có nhiều phương án giải quyết để so sánh, human giữ được hiểu biết, evidence truy vết được, risk/debt được chấp nhận minh bạch và knowledge được phân phối bền vững trong team. Điều này **không** đồng nghĩa mọi hoạt động đều tự động hay có thể loại bỏ hết lỗi của AI.

Xem [Objectives](02-objectives.md) và [MVP v0.1](11-mvp-v0.1.md) để phân biệt mục tiêu dài hạn với deliverable đầu tiên.
