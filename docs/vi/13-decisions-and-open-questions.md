# 13 — Design baseline và những quyết định còn mở

File này phân biệt **định hướng đã thống nhất** với **lựa chọn implementation** còn cần quyết định. Không âm thầm biến proposal thành requirement bắt buộc.

## Đường cơ sở thiết kế đã thống nhất

- AELC viết bằng Python, độc lập harness và cài toàn cục; application project không cần chứa bản sao AELC source.
- `setup.sh` (macOS/Linux) và `setup.ps1` (Windows) bootstrap cùng Python installer/CLI.
- Global harness entry points gọi AELC runtime; canonical project context không bị nhân bản giữa `.claude/`, `.agents/` hay thư mục harness khác.
- `.aelc/` của project chứa config/knowledge có thể chia sẻ; identity local private và individual evidence không nằm trong shared project content được Git theo dõi.
- Ưu tiên external authentication; self-declared identity là fallback có trust thấp hơn được đánh dấu minh bạch. Role/membership là thuộc tính theo project.
- Agent cung cấp evidence, báo uncertainty/debt và escalate risk; human/tổ chức có thẩm quyền chấp nhận change và residual risk.
- Bốn use case dài hạn: greenfield, brownfield feature, brownfield bug fixing, role-based onboarding; codebase understanding là nền dùng chung.
- MVP v0.1 chứng minh global install và project init trước khi xây workflow chi tiết, dashboard hoặc MCP automation.

## Đề xuất, chưa chốt

- Phân phối CLI qua `uv tool`; Python 3.12+; dependencies, release channel và phương thức update chính xác.
- SQLite local trước, shared backend sau; storage backend/schema và các chi tiết identity assurance policy.
- Default skill paths và cú pháp gọi cho từng harness; adapter phải kiểm tra version/OS cùng vị trí được hỗ trợ thực tế.
- Tên Python module cụ thể, file format schema, cách tạo project ID và phân loại role.
- Kỹ thuật/rubric đánh giá teach-back, freshness, knowledge coverage threshold và approval gate.

## Cần quyết định trước khi implement phần tương ứng

1. **Packaging:** giữ `method/`, `harnesses/` ở root và bundle resources rõ ràng, hay di chuyển runtime templates vào `src/aelc/resources/`?
2. **Identity:** provider flow nào được hỗ trợ đầu tiên; liên kết member giữa thiết bị/tổ chức thế nào; operation nào cần assurance mức nào?
3. **Project ID và membership:** sinh ID và verify role ra sao; nhiều repo được map vào một project thế nào?
4. **Harness scope:** Claude/Codex version và installation nào sẽ được v0.1 test? Báo capability không hỗ trợ thế nào?
5. **Manifest/conflict:** policy install/update khi user chỉnh skill hoặc project đã có AGENTS/CLAUDE instructions là gì?
6. **Update/migration:** cách pin release, rollback, compatibility range và migration schema đầu tiên.
7. **Evidence privacy:** retention, consent/visibility, source access, cơ chế challenge/correction và quyền truy cập central storage.
8. **Workflows:** stage contracts và acceptance criteria chi tiết sẽ được phát triển lần lượt với human sau foundation.
9. **MCP tool policy:** action Jira/Confluence nào chỉ đọc, action nào cần approval để ghi, role nào có quyền cho phép?

## Cách chốt một quyết định

Ghi option được chọn, alternatives và trade-offs, owner/ngày quyết định, module bị ảnh hưởng và nhu cầu migration; cập nhật canonical design doc và tests tương ứng. Không biến các ví dụ minh họa trong chat cũ thành hard requirement một cách tùy tiện.
