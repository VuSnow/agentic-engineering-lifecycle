# 04 — Nguyên tắc phối hợp giữa human và agent

## Cân bằng productivity với understanding

AELC phải tránh cả hai cực đoan:

- **Human → agent → approve mà không hiểu:** output có thể nhanh hơn nhưng gây cognitive dependency và rủi ro ẩn.
- **Human tự điều tra đầy đủ → agent làm lại:** gần như không tăng productivity.

Nguyên tắc ưu tiên: **agent làm phần investigation tốn thời gian và hướng dẫn member; member diễn giải lại mental model quan trọng bằng lời của mình; agent kiểm tra understanding và chỉ ra gap**. Câu hỏi challenge nên kiểm tra reasoning/failure mode thay vì học thuộc. Độ sâu tùy risk và knowledge liên quan của người thực hiện. Đây là nguyên tắc, **không phải workflow từng stage đã chốt**.

## AI responsibility: các nghĩa vụ có thể quan sát

Output của agent phải phân biệt:

- **Đã quan sát/xác minh:** được hỗ trợ bởi source, command output, test result hay evidence xác định được.
- **Suy luận:** kết luận có lập luận, nêu assumptions cùng evidence ủng hộ và trái chiều.
- **Chưa biết/chưa verify:** phải nói rõ để kiểm tra tiếp hoặc chuyển human quyết định.

Với output quan trọng, báo cáo thay đổi gì và vì sao, assumptions, alternatives/trade-offs liên quan, test/check đã thực sự chạy, test/check chưa chạy, residual risk, ảnh hưởng bảo mật/vận hành và technical debt đã biết. Escalate uncertainty có impact lớn; không bịa tool run, citation, approval hay cam kết đúng tuyệt đối.

“AI responsibility” là **nghĩa vụ hành vi và evidence trong method**, không có nghĩa agent là chủ thể pháp lý/tổ chức thay người hoặc team chịu trách nhiệm.

## Human và organizational accountability

Human/team có thẩm quyền quyết định residual risk có chấp nhận được không và thay đổi có được merge/deploy theo project policy hay không. Accountability với production change và nghĩa vụ pháp lý tuân theo thẩm quyền tổ chức và luật áp dụng; AELC không thể tự gán trách nhiệm pháp lý cho một cá nhân chỉ bằng cách ghi nhận approval.

Không suy ra acceptance từ câu do LLM sinh (“Alice đã approve”), file user tự sửa hoặc một commit đơn lẻ. Với hành động cần approval theo policy, phải có sự kiện phê duyệt human đủ tin cậy. **Knowledge không đồng nghĩa permission:** member có thể hiểu sâu hệ thống nhưng không có quyền deploy.

## Verification và technical debt

Human verification không yêu cầu làm lại mọi thao tác AI. Hãy xem evidence nguồn và kiểm tra độc lập các khu vực mà impact, uncertainty hoặc thiếu evidence đòi hỏi. CI xanh là evidence, không phải chứng minh mọi thứ đều đúng. Debt còn lại nếu được chấp nhận phải có mô tả, lý do, tác động, owner/team và điều kiện hoặc kế hoạch xem xét lại.

## Nguyên tắc ngắn gọn

> Không có AI claim quan trọng nào thiếu evidence. Không có production change nào thiếu người/tổ chức chịu trách nhiệm. AI phải giải trình; human phải sở hữu quyết định.

Xem [Knowledge và evidence](09-knowledge-and-evidence.md) để phân biệt activity với demonstrated understanding của member.
