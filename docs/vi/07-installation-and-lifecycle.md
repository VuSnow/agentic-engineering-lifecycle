# 07 — Global installation, project initialization và update

## Trải nghiệm người dùng đã thống nhất

Member clone **framework** một lần, chạy `setup.sh` trên macOS/Linux hoặc `setup.ps1` trên Windows, nhận được AELC CLI và các harness entry point đã chọn. Sau đó member có thể vào **bất kỳ** application project nào và gọi skill/command `aelc-init` (hoặc `aelc init`) mà không cần copy framework source vào project.

Câu lệnh minh họa (việc được viết trong docs **không đồng nghĩa đã implement**):

```bash
git clone <AELC_REPOSITORY_URL>
cd aelc
./setup.sh
# Trong application repository:
aelc init
```

```powershell
git clone <AELC_REPOSITORY_URL>
cd aelc
.\setup.ps1
```

`<AELC_REPOSITORY_URL>` là placeholder, chưa phải địa chỉ repository đã phát hành.

## Setup scripts và Python installer

`setup.sh` và `setup.ps1` chỉ nên là **bootstrap wrappers mỏng**: kiểm tra prerequisites, chuẩn bị môi trường Python cô lập, cài CLI/resources, sau đó gọi chung một Python installer. Tránh hai bộ business logic riêng cho Unix và Windows. Thiết kế ban đầu đề xuất Python 3.12+ và môi trường `uv tool` cô lập, nhưng phải chốt và kiểm thử cách phân phối trước khi xem đó là hợp đồng implementation.

Installer cần phát hiện harness đã cài, cho phép user chọn rõ ràng, chỉ cài/update entry point thuộc quyền quản lý của AELC, lưu installation manifest/version/hash và kiểm tra kết quả. CLI vẫn phải chạy khi máy không có harness. User có thể chọn một hoặc nhiều harness được hỗ trợ.

## Global, project và member

- **Global:** CLI, method resources, harness skills/commands; một installation phục vụ nhiều repo.
- **Per-project:** `.aelc/` chứa project configuration/knowledge chung, thêm harness-specific settings tối thiểu khi cần.
- **Per-member:** identity/session/cache nằm ngoài shared project data có version, credential được lưu an toàn.

Cú pháp gọi và vị trí skill tùy harness adapter và **phải được xác minh với harness version đã cài**. Tên dự kiến gồm `/aelc-init` cho Claude Code và skill tương ứng trên Codex; không giả định mọi harness đều có slash command hoặc đọc cùng thư mục trên mọi OS/version.

## Trách nhiệm của `aelc init`

- Phát hiện repository hiện tại và `.aelc/project.yaml` có sẵn.
- Resolve authenticated member identity nếu có; nếu dùng self-declared fallback phải gắn nhãn rõ.
- Resolve project membership/role; không suy ra quyền hoặc role từ prompt user có thể tự sửa.
- Chỉ khởi tạo phần config/local context còn thiếu và không xung đột.
- Giữ nguyên state project do người khác đã init; giải thích đâu là shared/private và không ghi token/individual knowledge vào file Git-tracked.
- Chỉ tạo harness-specific context **khi cần**, không ghi đè project instructions.

Init phải **idempotent**: chạy lại sẽ nhận diện và dùng lại project data, không nhân đôi state. Không âm thầm import project lên backend AELC hoặc bật quyền MCP quá rộng.

## Update gồm ba operation độc lập

1. **Framework/runtime update:** thay AELC executable và packaged method resources theo nguồn phát hành đã chọn/pin.
2. **Harness integration update:** reconcile skill files và manifest do AELC quản lý; nếu user đã sửa file managed, cảnh báo và giải quyết conflict minh bạch thay vì ghi đè.
3. **Project/data migration:** so sánh project schema và knowledge/evidence schema, preview/backup rồi migrate qua một operation riêng an toàn; global update không được âm thầm sửa toàn bộ repository.

Các command dự kiến: `aelc update`, `aelc doctor`, `aelc project migrate`, `aelc uninstall`. Flags, package feed, rollback và migration mechanism **chưa được chốt**.

## Các điều bất biến về an toàn

- Install và init có thể chạy nhiều lần mà không duplicate skills/member identity hoặc thay thế file theo cách phá dữ liệu.
- Update nên atomic hoặc có khả năng recovery trong mức khả thi; kiểm tra compatibility và bảo toàn dữ liệu member/project.
- Framework version, project schema và knowledge/evidence schema là các loại version riêng; version pinning và compatible ranges cần quyết định sau.
- Uninstall chỉ gỡ file installer quản lý; mặc định giữ project knowledge và individual history.
- Không commit secret, token cache hoặc personal assessment logs. Manifest hash chỉ để phát hiện file thay đổi, **không** phải bằng chứng xác thực user.
