# 03 — Phạm vi và các use case chính

## Bốn tình huống mục tiêu

| Use case | Giá trị kỳ vọng | Trách nhiệm của human |
|---|---|---|
| **Greenfield development** | Hỗ trợ toàn SDLC; nghiên cứu nhiều giải pháp cho một problem, tra cứu tài liệu/framework hiện tại khi có thể, so sánh assumptions, chi phí và trade-offs; hỗ trợ implementation và maintenance. | Quyết định requirements, architecture, risk và thay đổi được chấp nhận; hiểu trade-off quan trọng. |
| **Brownfield feature** | Khám phá code và constraints hiện hữu, phân tích impact, triển khai/test behavior mới, chỉ ra regression risk và debt. | Đảm bảo behavior đúng business intent và phù hợp toàn hệ thống; review các thay đổi và risk quan trọng. |
| **Brownfield bug fix** | Trace code/log, reproduce khi có thể, đề xuất root cause và fix, chạy test khả dụng, công khai uncertainty. | Duy trì mental model về nguyên nhân, điều kiện lỗi, fix và risk còn lại; cho phép thay đổi theo thẩm quyền. |
| **Role-based onboarding** | Điều chỉnh phạm vi khám phá project cho AI Engineer, Backend Engineer, Tech Lead, BA, QA...; rút ngắn thời gian đóng góp và giảm việc senior phải giải thích lặp lại. | Chứng minh understanding qua teach-back có chọn lọc, scenario và công việc thực tế; senior calibrate khi cần. |

**Codebase Understanding** là capability tái sử dụng cho onboarding, feature và bug fixing. Không đồng nhất nó với onboarding: onboarding chọn lát cắt cần hiểu theo role và tạo evidence về understanding của member.

## Các mối quan tâm xuyên suốt

Human identity/project membership; attribution hoạt động của agent; shared project knowledge; evidence về knowledge từng member; verification theo risk; accountability; technical debt; installation/versioning; tích hợp document, ticket, source control và công cụ ngoài.

## Chưa quy định ở giai đoạn này

Chưa thống nhất workflow chi tiết từng stage, bộ câu hỏi cố định, công thức lựa chọn architecture, approval matrix bắt buộc, knowledge score hoặc chính sách production automation. Hãy phát triển từng workflow sau cùng với quyết định cụ thể của human/team; không được tự suy diễn các chi tiết đó từ overview này.

## Vertical slice đầu tiên

Bắt đầu bằng **global installation + project initialization**; sau đó dùng Codebase Understanding/Onboarding để kiểm nghiệm identity, role, project context, teach-back và evidence. Đây là thứ tự triển khai được đề xuất, không phải yêu cầu phải xây toàn bộ kiến trúc tương lai trong v0.1.
