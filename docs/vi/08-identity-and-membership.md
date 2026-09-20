# 08 — Human identity, project membership và session attribution

## Phân biệt các identity

- **Human identity:** canonical AELC `member_id` của một người thực tế.
- **Platform identity:** account dùng cho Claude Code, Codex, Copilot hay platform khác; có thể được chia sẻ.
- **Agent identity:** agent/sub-agent thực hiện hành động hoặc tool execution identity.

Dùng chung harness account **không chứng minh** ai là human operator. Mọi attribution về knowledge hay accountability phải giữ thông tin về giới hạn assurance của session thực tế.

## External authentication và canonical mapping

Ưu tiên authentication do tổ chức quản lý (ví dụ company SSO nếu có), hoặc provider mà project đang dùng (GitHub/Atlassian), thay vì identity tự nhập. Sau khi authentication thành công, map **stable provider subject ID kèm provider/tenant context** vào canonical member ID nội bộ. Username, display name và email có thể thay đổi, không được dùng làm database key duy nhất.

Một member có thể liên kết nhiều external identity đã xác thực. Link/unlink/switch identity phải cần hành động xác thực rõ ràng; **không được âm thầm đổi member bằng cách sửa JSON**. Hạn chế OAuth scopes ở mức tối thiểu; authentication để xác định người dùng khác với permission dùng để đọc/ghi Jira, GitHub...

Self-declared fallback có thể phục vụ prototype hoặc team không có provider nhưng phải ghi nhãn rõ **unverified/assurance thấp hơn**; activity tương ứng không được giả dạng authentication record mạnh.

## Global identity khác project membership

Canonical member ID trả lời **“người này là ai?”**; membership trả lời **“người này là ai trong project?”**. Một người có thể là Backend Engineer ở project A, AI Engineer hoặc Tech Lead ở project B. Đổi role không tạo lại identity hoặc xóa knowledge history. Knowledge level không suy ra permission hay seniority.

## Local state không phải bằng chứng identity

Cache local minh họa có thể chứa `member_id`, provider reference và assurance status. File đó chỉ là cache/reference, **không phải bằng chứng authentication đáng tin độc lập**. Dùng authenticated session có tuổi thọ phù hợp, re-authentication khi cần và credential storage an toàn theo nền tảng. Shared OS account, cache bị copy, tài khoản bị chiếm quyền hoặc provider token dùng chung vẫn có rủi ro impersonation; external login *giảm* chứ không triệt tiêu rủi ro.

## Attribution record — conceptual

```text
human_member_id
identity_provider_subject_ref + assurance
project_id + project_role(s)
aelc_session_id
harness_name + platform_account_ref
agent_id + work_item_ref
activity_timestamp + evidence_refs
```

Identity, role, tool authorization và human approval là bốn thông tin khác nhau. Không cho phép LLM tạo trusted human approval chỉ bằng cách sinh văn bản hoặc sửa file local.

## Giới hạn của MVP

Có provider interface nhỏ, canonical member reference local, login/`whoami`/logout ở phần đã implement, project membership context và session attribution truy vết được. Enterprise SSO, đối soát identity đa thiết bị, central access control và approval audit mạnh có thể triển khai sau; không được tuyên bố MVP có các bảo đảm đó khi chưa thực hiện.
