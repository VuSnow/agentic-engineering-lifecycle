# 11 — MVP v0.1: Global installation và project initialization

## Kết quả cần đạt

Developer clone AELC source, chạy setup script phù hợp với OS, có Python CLI hoạt động cùng các global harness entry point được chọn, đi vào một application repository bất kỳ và khởi tạo AELC cho project **mà không copy AELC source vào đó**. Quá trình phải tôn trọng identity, membership, file có sẵn và khả năng bảo toàn dữ liệu.

## Trong phạm vi v0.1

1. Python package/CLI skeleton và đóng gói tối thiểu method/adapter resources.
2. `setup.sh` và `setup.ps1` là wrappers mỏng gọi chung một Python installer.
3. Phát hiện/chọn harness và entry point `aelc-init` do AELC quản lý cho **Claude Code và Codex**; adapter khác phát triển sau.
4. Abstraction human identity cơ bản: xác thực qua provider được chọn khi đã implement (ưu tiên ban đầu GitHub) hoặc đánh dấu rõ self-declared fallback; `whoami`/logout khi cần.
5. Project detection, project ID/config initialization, member role context và session attribution tối thiểu.
6. Idempotency, ghi file không phá dữ liệu, managed-file manifest, diagnostic checks và automated tests trên OS liên quan.
7. Metadata version/schema rõ ràng, kiểm tra compatibility cho các format v0.1 thực sự ghi ra.

## Chưa nằm trong phạm vi

- Workflow greenfield, feature, bug fix và onboarding chi tiết từng stage.
- Individual knowledge assessment tự động, team coverage dashboard, decay scoring và central organizational identity service.
- Human approval/legal/compliance workflow hoàn chỉnh hay production deployment automation.
- Atlassian MCP, ghi Jira ticket, đồng bộ Confluence và generic orchestration engine.
- Mọi tổ hợp adapter/platform, full update/migration/rollback platform hoặc custom LLM harness.

Tên command trong docs như `aelc init`, `aelc install`, `aelc doctor` và `/aelc-init` là **interface dự kiến**. Những command/flags nào thực sự có trong MVP phải được xác định bằng code và tests, không được mặc định đã implement toàn bộ chỉ vì tài liệu có nhắc đến.

## Acceptance criteria

- Setup chạy trên macOS/Linux và Windows trong những môi trường được tuyên bố hỗ trợ/đã test, không can thiệp vào Python environment của application project.
- AELC CLI vẫn load được packaged resources sau khi thư mục framework source đã clone được di chuyển hoặc xóa.
- Skill của harness được chọn có sẵn ở global scope qua cú pháp mà harness version hỗ trợ và gọi cùng Python CLI.
- Chạy init trong repo hiện có chỉ tạo project state tối thiểu dự kiến; application files và project harness instructions có sẵn không bị thay đổi.
- Init lần hai không duplicate project/member data, không ghi đè nội dung tùy chỉnh, không hỏi lại vô cớ nếu identity/session còn hợp lệ.
- Các human member khác nhau (khi có thể phân biệt bằng authentication) và các harness khác nhau có thể dùng chung project nhưng vẫn giữ distinct member/session attribution; phải công khai giới hạn của shared account/OS session.
- Không xuất hiện OAuth token, individual knowledge profile hay private chat transcript trong project artifacts được Git theo dõi.
- Installer biết chính xác file nào AELC quản lý và phát hiện user edit thay vì âm thầm ghi đè.
- Tests chứng minh hành vi đúng và các trường hợp lỗi tối thiểu: thiếu harness, project có sẵn, custom config có sẵn, login thất bại, install/init lặp lại và schema không được hỗ trợ.

## Thứ tự implementation đề xuất (không phải engineering workflow đã chốt)

CLI/package/resource loading → installer tối thiểu và một harness adapter → project init và local state → identity + role/session attribution → adapter thứ hai → cross-platform tests và docs. Mỗi thay đổi cần nhỏ và có test/evidence thực tế.
