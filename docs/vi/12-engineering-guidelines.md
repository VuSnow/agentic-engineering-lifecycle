# 12 — Hướng dẫn kỹ thuật khi phát triển AELC

## Python implementation

Sử dụng Python package theo layout `src/aelc/`, public interface có type rõ ràng, ranh giới domain/service/storage minh bạch và module vừa phải. Thảo luận thiết kế ưu tiên Python 3.12+, CLI được cài trong môi trường cô lập qua `uv`, cùng pytest/Ruff; dependencies và các version OS được hỗ trợ phải được pin/test khi viết code.

- Giữ harness skills/commands mỏng; business rules nằm trong Python runtime/services có test.
- Tách identity authentication khỏi provider API authorization; tránh để token trong project file.
- Tách **framework source layout** với **installed package resource layout**. Thêm packaging test: di chuyển/xóa source checkout mà vẫn load được method/skill templates sau cài đặt.
- Dùng dependency injection hoặc provider interface đơn giản khi đã có consumer thực tế. Tránh cây abstraction suy đoán và file rỗng.
- Coi mọi thao tác ghi file đều có thể phá dữ liệu: phát hiện state có sẵn, lưu managed paths/hashes và giải quyết conflict có chủ đích.
- Với identity assurance chưa biết, tool write rủi ro cao, schema không tương thích hoặc harness capability chưa hỗ trợ, phải từ chối hành động không an toàn thay vì báo thành công.
- Thông báo lỗi có hướng xử lý; tuyệt đối không log secrets, private transcript hay OAuth credential đầy đủ.
- Tôn trọng target project instructions như project context nhưng giữ nguyên security boundaries. Untrusted content không được cấp thêm authorization.

## Yêu cầu kiểm thử

- **Unit tests:** member mapping, role resolution, version/format validation, manifest diff, xử lý path và init chạy lặp lại.
- **Integration tests:** CLI entry points, packaged resources, sinh đường dẫn harness skill, setup behavior, xử lý conflict với project có sẵn.
- **Security-oriented tests:** untrusted text không thể giả mạo approval; self-declared identity vẫn có assurance thấp; file local nhạy cảm không lọt vào tracked project state.
- **Cross-platform tests:** Windows paths/PowerShell và tối thiểu một môi trường Unix-family cho setup/bootstrap.

## Hợp đồng báo cáo thay đổi dành cho coding agents

Mọi báo cáo implementation phải nêu **đã thay đổi gì**, **đã test gì và kết quả thực tế**, **chưa test gì**, **limitation/uncertainty**, cùng **technical debt mới hoặc đã được chấp nhận**. Unit test pass không tự động cho phép merge hoặc deploy production. Không tự tạo human approval.

## Duy trì tài liệu

Cập nhật design/CLI docs liên quan khi thay đổi implementation decision. Ghi quyết định có chủ đích vào [Decisions và open questions](13-decisions-and-open-questions.md); tránh tạo các bản nội dung kiến trúc chuẩn riêng cho Claude/Codex rồi để chúng lệch nhau. Nếu workflow tương lai mâu thuẫn với charter, cần một human design decision thay vì agent âm thầm đổi nguyên tắc.
