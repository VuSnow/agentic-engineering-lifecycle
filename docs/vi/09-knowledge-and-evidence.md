# 09 — Knowledge model, evidence và team coverage

## Ba tầng knowledge khác nhau

1. **Project knowledge:** domain rules, architecture, codebase maps, operational lessons, lý do quyết định; dùng chung và review/version khi phù hợp.
2. **Role expectations:** một role cần hiểu những phần nào của hệ thống và sâu đến đâu.
3. **Individual knowledge:** understanding về các vùng project mà một member cụ thể đã chứng minh; hai người cùng role không nhất thiết có cùng state.

Checklist kỹ năng chung (“biết Kafka”) là chưa đủ. Điều cần biết là *project này* sử dụng Kafka ra sao, retry thế nào, có thể fail như thế nào và vì sao các thiết kế đó được chọn.

## Các chiều của knowledge state

Các mức hiểu biết đề xuất: **Unknown, Aware, Working, Deep**. **Stale là chiều freshness/status riêng**, không phải mức cao hơn Deep. Một member có thể từng đạt “Deep, cần revalidation” sau khi subsystem redesign. Assessment rubric chính xác và thuật toán decay vẫn chưa quyết định.

- **Aware:** biết component/mục đích và tìm được thông tin liên quan.
- **Working:** có thể đóng góp an toàn tại area đó với review thông thường.
- **Deep:** có thể lý giải decision, trade-offs, failure modes quan trọng và review công việc người khác trong area đó.

## Evidence không phải số lượng activity

“Member yêu cầu agent hoàn thành mười payment tickets” chứng minh có activity, **không tự chứng minh người đó có Payment Deep knowledge**. Evidence về understanding có thể gồm teach-back bằng lời member, scenario reasoning, tracing đúng, diagnosis độc lập, giải thích failure path hoặc reviewed change có phần đóng góp human xác định được.

Agent có thể đề xuất assessment và viện dẫn evidence; member/lead có thẩm quyền phải có thể xem, sửa, phản biện và calibrate. Không sinh bảng xếp hạng người với người, performance score tổng quát hoặc báo cáo giám sát nhân viên.

## Teach-back mà không làm mất productivity

Agent có thể investigate, trace, research và guide trước. Sau đó yêu cầu member dựng lại *mental model quan trọng*, challenge gap bằng một scenario có trọng tâm. Task nhỏ, risk thấp có thể cần rất ít hoặc không cần teach-back chính thức; thay đổi architecture hoặc production risk cao có thể yêu cầu review sâu hơn. Không bắt member chạy lại mọi lệnh và tìm kiếm của agent.

## Evidence provenance — conceptual fields

```text
claim + scope + status (observed/inferred/unverified)
source reference + version/commit + retrieved/observed at
human/agent/session + identity assurance
verification method + actual result + limitations
knowledge assertion supported (if applicable)
review/calibration/approval actor and time (if required)
```

Summary do AI sinh hoặc CI xanh **không** chứng minh understanding của một cá nhân. Trang Confluence có thể đã cũ; lưu reference tới version gốc và đánh dấu shared knowledge downstream là có thể stale khi nguồn/code thay đổi.

## Team coverage

Tech Lead cần individual view (“member này có thể làm việc an toàn ở đâu?”) và team view (“knowledge quan trọng đang tập trung tại đâu?”). Coverage target có thể đòi hỏi hơn một member có demonstrated working knowledge của critical subsystem, nhưng **ngưỡng cụ thể do project policy quyết định**, không có default chung cho mọi project.

## Privacy và access

Individual evidence và session content cần access control phù hợp; phải chốt retention và cơ chế phản biện trước khi centralize dữ liệu. Không commit personal profile, raw private chat, secret hay approval không verify vào shared project Git. Shared project knowledge đã xác thực có thể commit khi được duyệt cho nhóm người đọc tương ứng.

## Trạng thái triển khai

File này định nghĩa semantics mục tiêu. Full assessment, decay, team dashboard và shared backend đều **nằm ngoài MVP v0.1**.
