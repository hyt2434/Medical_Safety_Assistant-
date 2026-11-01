# Báo cáo UI Prototype riêng

Phiên bản 1.2: ảnh PA2 được chụp từ frontend TypeScript đang chạy trong `apps/frontend`, thay cho bản HTML độc lập trước đây. Bộ ảnh PA1 được giữ nguyên. Để chụp lại, chạy `npm run capture:report` trong `apps/frontend`; script kiểm thử thành công rồi mới cập nhật 18 PNG và `sections/ui-images/capture-manifest.json`.

- `main.tex`: file chính, biên dịch bằng XeLaTeX.
- `metadata.tex`: tiêu đề và thông tin nhóm.
- `sections/ui-prototype.tex`: nội dung so sánh PA1/PA2 và 18 màn hình.
- `sections/ui-images/`: ảnh chụp đi kèm, đã có sẵn để upload cả thư mục.
- `sections/pa1-original/`: bản sao nguyên vẹn của bộ ảnh PA1 người dùng cung cấp tại `pa/pa1/ui-prototype/ui-prototype/`; đây là nguồn baseline đang dùng.
- `sections/pa1-images/`: ảnh chụp lại trước đây, không còn được báo cáo sử dụng.
- `main.pdf`: báo cáo UI độc lập, 37 trang A4 dọc, có ảnh PA1 và PA2 ở các trang liên tiếp.

Phần thay đổi và giao diện mới được mô tả bằng màu xanh dương; baseline PA1 màu đen. Lề trái/phải 1,2 cm, trên/dưới 1,6 cm.

Các mô tả đã được đối chiếu lại với bộ ảnh PA1 chính thức: PA1 đã có yêu cầu review, hàng chờ HCP, phản hồi và xác nhận lịch. Báo cáo không còn gọi các luồng này là hoàn toàn mới. Riêng nhập thuốc có cả ảnh intake và verification. Các màn hình không có ảnh tương ứng trong bộ cung cấp được ghi rõ; không suy ra rằng chức năng chưa từng tồn tại. Không dùng ảnh mobile chụp lại làm baseline vì bộ ảnh chính thức không có ảnh mobile.

Chạy trong thư mục này:

```powershell
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

Không cần Inkscape hay chuyển SVG. Báo cáo Use Case nằm riêng tại `../Use-Case-Specification/main.pdf`.
