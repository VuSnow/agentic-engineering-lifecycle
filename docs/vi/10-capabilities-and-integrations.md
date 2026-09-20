# 10 — Capabilities độc lập provider và thiết kế sẵn sàng cho MCP

## Nguyên tắc

Method mô tả **capability cần có**, không ép vendor cụ thể cung cấp. Ví dụ: tìm document, đọc document có version, đề xuất task, tạo ticket khi được phép, kiểm tra repository/PR. Provider có thể là local file, REST API hoặc MCP tool. MCP là cơ chế integration, không phải source of truth của AELC.

## Đề xuất phân chia module

```text
src/aelc/capabilities/
  documents/              # hợp đồng search/read document
  tasks/                  # hợp đồng create/read/update work item
  source_control/         # hợp đồng repository / PR
  communication/          # tương lai, chỉ khi cần

src/aelc/integrations/
  mcp/                    # transport, discovery, auth context
  providers/
    atlassian/            # Confluence documents, Jira issues
    github/               # repository/PR/issues
    local/                # filesystem / local task artifacts
```

Ví dụ: onboarding đọc Confluence qua `DocumentProvider`, còn greenfield planning đề xuất Jira ticket qua `TaskProvider`. Workflow không hardcode tên MCP tool của provider trong core logic. Dùng adapter/capability registry và báo rõ những operation provider chưa hỗ trợ.

## Tool identity và authorization

Authentication GitHub/Atlassian để biết *member là ai* khác với credential/scope để *hành động trên repository/ticket*. Shared MCP technical account không chứng minh human nào yêu cầu operation. AELC phải attribution session độc lập và thực thi permission boundary trong runtime/provider policy; không chỉ dựa vào prompt.

Read-only retrieval có thể được project policy cho phép; tạo ticket, đổi sprint scope, xóa issue, merge và production deploy cần quy tắc authorization/approval riêng. Policy này chưa được chốt. Không mặc định cấp quyền ghi rộng.

## Untrusted content và provenance

External document, web page, ticket, repo file và tool output là dữ liệu, không phải chỉ thị có thể ghi đè security/approval rules của AELC. Ghi source URL/ID, version/revision, thời điểm truy xuất và access context liên quan; trang Confluence lấy về không tự động là đúng hoặc còn mới.

## Kế hoạch release

**MVP v0.1** cần giữ các ranh giới capability trong tư duy thiết kế, nhưng chưa phải implement Atlassian MCP, Jira ticket automation, remote document synchronization hay generic workflow engine. Chỉ định nghĩa interface khi use case đầu tiên thực sự cần dùng.
