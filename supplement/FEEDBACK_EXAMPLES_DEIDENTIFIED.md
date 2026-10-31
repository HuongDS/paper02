# S6. De-Identified Authentic Feedback Examples Across the Four Configurations

Below are four authentic AI feedback payloads (one per assigned configuration: `Sandwich`, `Rubric`, `Explainable`, and `Researching`) extracted from the study dataset, with UUIDs, student identifiers, and personal/repository identifiers removed.

## Sandwich Configuration

**Scenario Question:** Trong quy trình phê duyệt yêu cầu bồi thường, nếu một người quản lý cơ sở (Facility Manager) cố gắng phê duyệt một yêu cầu mà tổng giá trị bồi thường vượt quá hạn mức cho phép của họ, hệ thống sẽ phản ứng như thế nào và tại sao hành động này bị chặn?

```json
{
  "student_answer_id": "<REDACTED_UUID>",
  "feedback_type": "Sandwich",
  "data_origin": "synthetic_fixture",
  "provider_invoked": false,
  "positives": "Đã nhắc tới đối tượng và thao tác đang được hỏi; cần điều chỉnh cách hiểu nhánh xử lý.",
  "constructive_criticism": "Chia lần duyệt để lách hạn mức không phải cách xử lý của luồng.",
  "next_steps": "Đối chiếu lại điểm sau: hạn mức phê duyệt gắn với giá trị yêu cầu và cấp quản lý. Viết lại phần điều kiện và kết quả, bỏ chi tiết chưa có bằng chứng."
}
```

## Rubric Configuration

**Scenario Question:** Trong quy trình xác nhận thanh toán cho người bán, nếu người quản trị hệ thống cố gắng xác nhận một khoản thanh toán mà phương thức thanh toán không phải là chuyển khoản ngân hàng hoặc trạng thái của khoản thanh toán đó không còn ở trạng thái chờ xử lý, hệ thống sẽ phản ứng như thế nào và tại sao điều này lại quan trọng đối với tính toàn vẹn của dữ liệu tài chính?

```json
{
  "student_answer_id": "<REDACTED_UUID>",
  "feedback_type": "Rubric",
  "data_origin": "synthetic_fixture",
  "provider_invoked": false,
  "criteria": [
    {
      "name": "Độ chính xác nghiệp vụ",
      "score": 3,
      "comment": "Nhận ra tránh xác nhận trùng nhưng tự mở rộng sang tiền mặt trái với phạm vi nhánh này."
    },
    {
      "name": "Căn cứ từ ngữ cảnh",
      "score": 3,
      "comment": "Nguồn đối chiếu: BE/src/features/payments/payment.service.ts :: PaymentService.confirmPayout. Kết quả cần phân biệt trong tình huống: Chỉ xác nhận khoản chuyển khoản ngân hàng còn chờ; khác phương thức hoặc trạng thái thì trả lỗi 422."
    },
    {
      "name": "Mức đầy đủ của giải thích",
      "score": 2,
      "comment": "Cần làm rõ: kiểm tra đồng thời phương thức và trạng thái trước xác nhận."
    }
  ]
}
```

## Explainable Configuration

**Scenario Question:** Trong quy trình xử lý yêu cầu đổi kho (swap-unit), nếu người quản lý kho cố tình thực hiện thao tác đổi kho cho một hợp đồng đang có số dư nợ chưa thanh toán, hệ thống sẽ phản ứng như thế nào và tại sao hành động này lại bị chặn?

```json
{
  "student_answer_id": "<REDACTED_UUID>",
  "feedback_type": "Explainable",
  "data_origin": "synthetic_fixture",
  "provider_invoked": false,
  "code_evidence": "Nguồn đối chiếu: BE/src/features/contracts/contract.service.ts :: ContractService.swapUnit. Kết quả cần phân biệt trong tình huống: Hợp đồng đang hoạt động và không nợ mới được đổi kho; còn nợ thì từ chối xử lý.",
  "logic_explanation": "Kết quả chặn đúng nhưng chưa có ngoại lệ cho kho rẻ hơn. Hợp đồng đang hoạt động và không nợ mới được đổi kho; còn nợ thì từ chối xử lý."
}
```

## Researching Configuration

**Scenario Question:** Trong quy trình tạo đơn hàng dịch vụ, nếu người dùng chọn ngày sử dụng dịch vụ là một ngày trong quá khứ so với thời điểm hiện tại, hệ thống sẽ phản ứng như thế nào và tại sao hành động này lại bị chặn?

```json
{
  "student_answer_id": "<REDACTED_UUID>",
  "feedback_type": "Researching",
  "data_origin": "synthetic_fixture",
  "provider_invoked": false,
  "comment": "Cần sửa cách mô tả nhánh xử lý để khớp tình huống của câu hỏi.",
  "positives": "Câu trả lời đi thẳng vào tình huống, nhưng chưa giải thích đủ căn cứ.",
  "constructive_criticism": "Nguyên nhân là dữ liệu thời gian không hợp lệ, không phải hết chỗ.",
  "next_steps": "Đối chiếu lại điểm sau: so ngày dịch vụ với ngày hiện tại thay vì ngày tạo hợp đồng. Viết lại phần điều kiện và kết quả, bỏ chi tiết chưa có bằng chứng.",
  "code_evidence": "Nguồn đối chiếu: BE/src/features/services/services.service.ts :: ServicesService.orderService. Kết quả cần phân biệt trong tình huống: Ngày dịch vụ phải từ hôm nay trở đi; ngày quá khứ bị từ chối, không tạo đơn.",
  "logic_explanation": "Nguyên nhân là dữ liệu thời gian không hợp lệ, không phải hết chỗ. Ngày dịch vụ phải từ hôm nay trở đi; ngày quá khứ bị từ chối, không tạo đơn.",
  "criteria": [
    {
      "name": "Độ chính xác nghiệp vụ",
      "score": 2,
      "comment": "Nguyên nhân là dữ liệu thời gian không hợp lệ, không phải hết chỗ."
    },
    {
      "name": "Căn cứ từ ngữ cảnh",
      "score": 1,
      "comment": "Nguồn đối chiếu: BE/src/features/services/services.service.ts :: ServicesService.orderService. Kết quả cần phân biệt trong tình huống: Ngày dịch vụ phải từ hôm nay trở đi; ngày quá khứ bị từ chối, không tạo đơn."
    },
    {
      "name": "Mức đầy đủ của giải thích",
      "score": 1,
      "comment": "Cần làm rõ: so ngày dịch vụ với ngày hiện tại thay vì ngày tạo hợp đồng."
    }
  ],
  "researching": {
    "consensus_summary": "Nguyên nhân là dữ liệu thời gian không hợp lệ, không phải hết chỗ. Ngày dịch vụ phải từ hôm nay trở đi; ngày quá khứ bị từ chối, không tạo đơn.",
    "code_inspection": "Nguồn đối chiếu: BE/src/features/services/services.service.ts :: ServicesService.orderService. Kết quả cần phân biệt trong tình huống: Ngày dịch vụ phải từ hôm nay trở đi; ngày quá khứ bị từ chối, không tạo đơn.",
    "pedagogical_guidance": "Đối chiếu lại điểm sau: so ngày dịch vụ với ngày hiện tại thay vì ngày tạo hợp đồng. Viết lại phần điều kiện và kết quả, bỏ chi tiết chưa có bằng chứng.",
    "models_involved": [
      "Synthetic fixture — no provider call"
    ]
  }
}
```
