# 02 — Mục tiêu của AELC

Các nội dung dưới đây là **kết quả mục tiêu đã thống nhất ở mức định hướng**, không có nghĩa cách triển khai hoặc chỉ tiêu định lượng đã được chốt. Phương pháp đo lường vẫn là quyết định mở.

## Delivery và engineering decisions

1. **Tăng engineering productivity:** để agent đảm nhiệm repository exploration, code search, tracing, research, hỗ trợ test và execution lặp lại tốn thời gian; không yêu cầu human làm lại toàn bộ.
2. **Mở rộng solution space với chi phí research thấp hơn:** cho một problem, agent nghiên cứu nhiều architecture/library/pattern phù hợp, tài liệu và compatibility hiện tại, assumptions, PoC evidence và trade-offs. Human lựa chọn; không tự động áp dụng framework/pattern quen tay mà không kiểm tra tính phù hợp mới.
3. **Hỗ trợ bốn tình huống:** greenfield development, thêm feature trong brownfield, bug fixing trong brownfield và onboarding theo role dựa trên codebase understanding.

## Năng lực và trách nhiệm của con người

4. **Duy trì mental model:** con người phải đủ hiểu để giải thích behavior, failure mode, impact và trade-off quan trọng.
5. **Giảm cognitive dependency:** dùng teach-back có chọn lọc và câu hỏi challenge nhắm vào reasoning; tránh chỉ approve thụ động hoặc yêu cầu điều tra lại mọi bước của agent.
6. **Trách nhiệm của AI rõ ràng:** claim quan trọng phải có evidence truy vết được hoặc được đánh dấu là assumption/suy luận/chưa biết; báo cáo đúng verification đã chạy, giới hạn và điểm chưa chắc chắn cần human review.
7. **Giữ human/organizational accountability:** chấp nhận thay đổi và rủi ro phải thuộc người/tổ chức có thẩm quyền. Trách nhiệm pháp lý thực tế tùy luật, chức trách và hợp đồng áp dụng, không phát sinh chỉ từ cách framework ghi nhận approval.
8. **Làm technical debt hiện rõ:** nêu workaround, duplication, coupling, limitation, follow-up và quyết định có trách nhiệm về việc accept/reject debt còn lại.
9. **Verification theo risk:** độ sâu phụ thuộc criticality, complexity, novelty, blast radius, ảnh hưởng bảo mật/business, uncertainty và knowledge gap.

## Knowledge và khả năng duy trì của team

10. **Coi project knowledge là tài sản cấp một:** ghi nhận và duy trì domain, architecture, operations và bối cảnh các decision chung.
11. **Quản lý individual knowledge state:** phân biệt hiểu biết member đã chứng minh với yêu cầu chung của role.
12. **Nhận diện knowledge stale:** năng lực hoặc documentation từng đúng có thể lỗi thời sau khi code/design thay đổi.
13. **Quan sát team knowledge coverage:** phát hiện phụ thuộc vào một người, knowledge gap và critical subsystem thiếu coverage.
14. **Giảm bottleneck training/review ở senior:** agent hướng dẫn khám phá project và pre-review để senior tập trung vào high-risk design, mentoring sâu và judgment; không xóa bỏ human review.
15. **Rút ngắn onboarding theo role:** giúp member mới đạt working understanding và đóng góp hữu ích sớm hơn, không chỉ đọc nhanh tài liệu.
16. **Giảm phụ thuộc vào ít người giữ knowledge:** duy trì decision rationale, failure history và truyền knowledge trước khi senior/PM/key member chuyển việc hoặc rời dự án.
17. **Không biến knowledge assessment thành performance ranking:** đo demonstrated project understanding, không xếp hạng phẩm chất hoặc năng lực chung của nhân viên.
18. **Hỗ trợ theo role và knowledge state:** điều chỉnh độ sâu hướng dẫn/challenge theo trách nhiệm và evidence của member, không che giấu thông tin cần thiết.

## Độ tin cậy và mở rộng

19. **Identity và attribution đáng tin:** phân biệt human member, harness/platform account và agent thực thi, kể cả khi dùng chung harness account.
20. **Ưu tiên identity đã xác thực:** dùng company SSO hoặc provider project đang dùng như GitHub/Atlassian khi có; self-declared chỉ là fallback có assurance thấp hơn.
21. **Bảo toàn evidence provenance:** truy vết nguồn, timestamp/version, actor/session, verification thực tế, nguồn approval và uncertainty.
22. **Độc lập với harness và provider:** method vẫn hoạt động khi Claude Code, Codex, Copilot, MCP server hoặc ticket/document provider thay đổi.
23. **Cài đặt/cập nhật an toàn:** cài một lần, dùng nhiều project, update tập trung, không âm thầm ghi đè dữ liệu, approval hay file user sửa.

## Những gì AELC không hướng đến

AELC không nhằm thay engineer/senior, bảo đảm tuyệt đối tính đúng, xem claim của agent là chân lý, biến knowledge tracking thành giám sát/xếp hạng nhân sự, sao chép toàn bộ external systems để trở thành nguồn dữ liệu gốc mới hoặc yêu cầu mỗi project chứa một bản framework source.
