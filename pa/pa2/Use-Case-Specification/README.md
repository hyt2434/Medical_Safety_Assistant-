# Use-Case Specification

File chính: `main.tex`. Biên dịch bằng **XeLaTeX**; font đang dùng là Times New Roman.

## Nội dung

- `metadata.tex`: thông tin báo cáo và nhóm.
- `sections/01-use-case-model.tex`: 18 sơ đồ, mỗi sơ đồ trên một trang ngang.
- `sections/02-use-case-specifications.tex`: các bảng đặc tả, mỗi UC bắt đầu ở trang mới.
- `sections/images/UC_01.svg` đến `UC_18.svg`: ảnh nguồn.
- `sections/images/UC_01.pdf` đến `UC_18.pdf`: bản vector dùng để chèn vào LaTeX.
- `sections/03-use-cases-combined.tex`: bản đang được main sử dụng, hình model trước rồi đến bảng đặc tả của từng UC, toàn bộ A4 dọc.
- `combine_sections.py`: tạo lại bản ghép từ đặc tả gốc; build.ps1 tự chạy script này. Chỉnh nội dung đặc tả ở `sections/02-use-case-specifications.tex` để không bị ghi đè khi build lại.
- `sections/04-ui-prototype.tex`: 18 màn hình UI kèm so sánh PA1/PA2; nội dung thay đổi và màn hình mới được mô tả bằng xanh dương.
- `sections/ui-images/`: bản sao ảnh chụp UI để upload báo cáo độc lập.
- `main.pdf`: báo cáo đã biên dịch và kiểm tra, hiện có 48 trang, gồm Use Case và phần UI prototype.

## Biên dịch

Nếu ảnh PDF đã có, chỉ cần chạy trong thư mục này:

```powershell
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

Khi thay đổi SVG, cài dependency Python một lần rồi chạy script để chuyển ảnh và biên dịch:

```powershell
python -m pip install -r requirements.txt
powershell -NoProfile -ExecutionPolicy Bypass -File .\build.ps1
```

Script cần Python, PyMuPDF, XeLaTeX và latexmk. ExecutionPolicy ở lệnh trên chỉ áp dụng cho tiến trình chạy script, không thay đổi thiết lập hệ thống.

## Upload lên trình soạn LaTeX

Upload `main.tex`, `metadata.tex` và toàn bộ thư mục `sections/`, bao gồm các ảnh PDF. Chọn `main.tex` làm tài liệu chính và XeLaTeX làm compiler. Đường dẫn ảnh tính từ thư mục chứa `main.tex` là `sections/images/`.

Bản hiện tại dùng ảnh PDF vector nên không cần Inkscape hoặc shell escape. Giữ SVG để chỉnh sửa và tạo lại ảnh khi cần. Mỗi UC có hình ở trên và đặc tả ở dưới. UC-02, UC-03, UC-04, UC-05, UC-06, UC-14 và UC-18 tiếp tục phần Alternative Flows ở trang kế tiếp để tránh tách riêng phần Post-conditions. Hai file section gốc được giữ làm nguồn tham khảo; main chỉ nạp section ghép.

Ảnh model rộng tối đa 19 cm, cao tối đa 60% vùng nội dung, giữ nguyên tỷ lệ trên A4 dọc. Lề báo cáo hiện là 1,2 cm trái/phải và 1,6 cm trên/dưới. Phần UI dùng ảnh vừa chiều rộng và giới hạn chiều cao để giữ mô tả cùng ảnh trên một trang.

Quy ước màu phần UI: baseline PA1 màu đen; mô tả thay đổi PA2 và nhãn màn hình mới màu xanh dương (`instructionblue`). Ảnh giữ màu giao diện gốc. Khi cập nhật ảnh trong prototype, thay bản sao tương ứng ở `sections/ui-images/` rồi biên dịch lại; không cần chạy script tạo phần so sánh để chỉnh nội dung LaTeX trực tiếp.

## B?o c?o UI ?? t?ch ri?ng

B?n UI ch?nh th?c n?m t?i `../ui-prototype-report/main.tex` v? `../ui-prototype-report/main.pdf` (22 trang). Ch?nh n?i dung t?i `../ui-prototype-report/sections/ui-prototype.tex`. Ph?n UI c? trong th? m?c Use Case kh?ng c?n ???c main n?p.
