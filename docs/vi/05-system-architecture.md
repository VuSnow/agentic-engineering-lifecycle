# 05 — System architecture và ranh giới ownership

## Các layer ở mức conceptual

```text
AELC Method (principles, protocols, workflows, role definitions)
           |
AELC Python Runtime / CLI (identity, membership, sessions,
                           evidence, knowledge, accountability,
                           capabilities, installer)
           |
Harness adapters (Claude Code / Codex / Copilot / future harnesses)
           |
Existing agent harnesses + external systems (MCP, REST, local files)
```

Đây là **mô hình phân quyền sở hữu logic**, không phải yêu cầu implement mọi module ngay ở v0.1. Harness adapter chỉ là entry point mỏng gọi cùng một runtime/method; không viết thêm một hệ identity hoặc knowledge trong từng skill.

## Ranh giới lưu trữ và quyền sở hữu dữ liệu

| Vị trí | Trách nhiệm chuẩn | Quy tắc Git |
|---|---|---|
| **AELC framework package** | Python runtime, method definitions chung, adapter resources và templates. | Framework source repository. |
| **`.aelc/` của application project** | Project ID, shared policies, project knowledge đã verify, architecture decisions và work artifacts được chia sẻ. | Chỉ commit nội dung chung, không nhạy cảm, đã review. |
| **Config dành riêng cho harness** | Pointer/instruction/settings cần để tích hợp một harness. | Có thể nằm global hoặc local; không trở thành nguồn project state cạnh tranh. |
| **User-local AELC config/cache** | Identity reference hiện tại, project được chọn, session/cache local. | Ngoài project Git; credential lưu an toàn riêng. |
| **Shared AELC backend (tương lai)** | Mapping member đa thiết bị, evidence có access control, individual knowledge, team coverage và approval records tin cậy. | Service có kiểm soát truy cập, không phải file trong shared repo. |
| **GitHub/Jira/Confluence/...** | Repo/ticket/document gốc do chính hệ thống đó quản lý. | AELC lưu reference, version và provenance thay vì tự nhận sở hữu object gốc. |

**Lưu ý:** `.aelc/` là thư mục project canonical *được đề xuất*, không phải nơi lưu toàn bộ dữ liệu cá nhân. Tên tự khai trong file local không phải cơ chế authentication. Git commit không thay thế authenticated approval.

## Ranh giới dependency

- `identity/` xác thực và map member; `membership/` gắn member với project và role. Role không phải thuộc tính cố định của global human identity.
- `sessions/` attribution tương tác cho human, harness account, agent và task, có ghi rõ assurance/limitation.
- `evidence/` quản lý claim và provenance; `knowledge/` đánh giá demonstrated understanding dựa trên evidence. Không module nào âm thầm biến dữ liệu của module kia thành sự thật.
- `accountability/` ghi risk/debt/approval và thực thi quyền tương ứng khi cần.
- `capabilities/` định nghĩa interface document/task/source-control độc lập provider; `integrations/` hiện thực các adapter như MCP/REST/local.
- Agent không được tăng quyền chỉ bằng cách sửa project document hoặc prompt text.

## Portability

Member phải có thể dùng Claude Code trong một session rồi Codex ở session khác mà không tạo hai project state canonical hoặc hai member identity độc lập. Khả năng hỗ trợ giữa harness có thể khác nhau; adapter phải báo operation không hỗ trợ, không âm thầm giả định mọi harness tương đương.
