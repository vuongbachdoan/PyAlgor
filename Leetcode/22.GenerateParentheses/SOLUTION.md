### Giải thích thuật toán giải bài `22. Generate Parentheses`

Bài toán 22. Generate Parentheses yêu cầu tạo ra tất cả các tổ hợp hợp lệ của dấu ngoặc đơn "(" và ")" cho một số lượng cặp ngoặc nhất định. Ví dụ, với n = 3, ta cần tạo ra các chuỗi như "((()))", "(()())", v.v.

Thuật toán sử dụng trong giải pháp phổ biến là quay lui (backtracking). Ý tưởng chính là duy trì một chuỗi đang được xây dựng, đồng thời theo dõi số lượng ngoặc mở và đóng còn lại.

#### 1. Phân tích bài toán:

Input: Số lượng cặp ngoặc n.
Output: Danh sách các chuỗi hợp lệ gồm n cặp ngoặc đơn "(" và ")".
Điều kiện hợp lệ:
Số lượng ngoặc mở phải luôn nhỏ hơn hoặc bằng số lượng ngoặc đóng.
Chuỗi kết quả không được chứa ngoặc đóng trước ngoặc mở.
#### 2. Giải thích thuật toán:

##### Hàm `generateParenthesis(n)`:

- Lặp qua tất cả các chuỗi có độ dài 2 * n (mỗi cặp ngoặc đơn được biểu diễn bởi 1 ký tự).

- Gọi hàm đệ quy backtrack để kiểm tra xem chuỗi đó có hợp lệ hay không.

##### Hàm đệ quy `backtrack(s, left, right)`:

- **Điều kiện dừng**:

Nếu độ dài chuỗi s bằng 2 * n, tức là đã sử dụng hết tất cả các cặp ngoặc, thêm chuỗi s vào danh sách kết quả.

- **Điều kiện tiếp tục**:

Nếu số lượng ngoặc mở (left) nhỏ hơn n, thêm ngoặc mở "(" vào chuỗi s và tăng left lên 1. Gọi đệ quy backtrack với chuỗi mới và các giá trị cập nhật.

Nếu số lượng ngoặc đóng (right) nhỏ hơn left, tức là chuỗi vẫn hợp lệ, thêm ngoặc đóng ")" vào chuỗi s và tăng right lên 1. Gọi đệ quy backtrack với chuỗi mới và các giá trị cập nhật.