# AELC — Agentic Engineering Lifecycle

> AI tăng tốc công việc kỹ thuật; con người giữ quyền hiểu, phán đoán, sở hữu và chịu trách nhiệm đối với hệ thống.

**AELC là một engineering method được đề xuất, độc lập với agent harness**, nhằm đưa AI agents vào phát triển và bảo trì phần mềm. AELC không phải mô hình AI mới và không thay thế Claude Code, Codex, Copilot hay các kỹ sư sử dụng chúng.

AELC hướng đến việc giúp team phát triển phần mềm nhanh hơn, đồng thời duy trì năng lực hiểu hệ thống của con người, yêu cầu evidence cho kết luận của AI và bảo toàn knowledge dự án khi thành viên hoặc công cụ thay đổi.

## Phạm vi của AELC

- Phát triển dự án mới (greenfield), bao gồm tìm kiếm nhiều giải pháp và phân tích trade-off minh bạch.
- Triển khai tính năng trong dự án hiện có (brownfield).
- Điều tra và khắc phục lỗi trong dự án hiện có.
- Codebase Understanding và onboarding theo role.
- Những năng lực xuyên suốt: identity, project membership, human knowledge, evidence, accountability và tích hợp công cụ ngoài.

**Mốc triển khai đầu tiên là MVP v0.1: cài đặt toàn cục + khởi tạo project**, không phải hiện thực cả bốn workflow. Xem [Phạm vi MVP](docs/11-mvp-v0.1.md).

## Bắt đầu đọc từ đâu?

- **Coding agents:** đọc [AGENTS.md](AGENTS.md) trước.
- **Mục đích dự án:** [Project charter](docs/01-project-charter.md), [Objectives](docs/02-objectives.md) và [Scope](docs/03-scope-and-use-cases.md).
- **Kiến trúc:** [System architecture](docs/05-system-architecture.md) và [Repository structure](docs/06-repository-structure.md).
- **Cài đặt và cập nhật:** [Installation lifecycle](docs/07-installation-and-lifecycle.md).
- **An toàn và trách nhiệm:** [Human–agent contract](docs/04-principles-and-responsibility.md).
- **Toàn bộ tài liệu:** [Mục lục docs](docs/README.md).

## Trạng thái tài liệu

Bộ tài liệu này là **đường cơ sở thiết kế đã trao đổi**, không có nghĩa phần mềm tương ứng đã được viết hoặc chạy được. Đường dẫn, sơ đồ và câu lệnh CLI trong tài liệu mô tả hành vi dự kiến. Những lựa chọn chưa được chốt sẽ được ghi rõ là *đề xuất* hoặc *chưa quyết định*.

## Nguồn tài liệu chuẩn

`docs/` là nguồn tham chiếu chuẩn cho thiết kế và quyết định của framework. File riêng cho từng harness nên dẫn liên kết tới tài liệu này, không sao chép thành nhiều bản dễ mâu thuẫn. Knowledge riêng của một application project thuộc `.aelc/` của chính project đó, không nằm trong framework repository.
