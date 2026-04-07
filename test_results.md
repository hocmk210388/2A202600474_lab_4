Họ và tên: Mã Khoa Học

MSSV: 2A202600474

## Test case 1:

Ban: xin chào! tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Rất vui được đồng hành cùng bạn lên kế hoạch cho chuyến đi sắp tới. Việt Nam mình có nhiều nơi để đi lắm, tùy vào sở thích của bạn thôi!

Để mình gợi ý cho bạn dễ chọn nhé, bạn thích kiểu nào hơn:

1. **Thích biển xanh, cát trắng, nghỉ dưỡng sang chảnh?** -> Đà Nẵng hoặc Phú Quốc là "đỉnh" nhất.
2. **Thích không khí se lạnh, núi non hùng vĩ, trải nghiệm văn hóa?** -> Đà Lạt hoặc Sapa.
3. **Thích khám phá lịch sử, ẩm thực đường phố, không gian hoài cổ?** -> Hội An hoặc Huế.

Bạn đang ở đâu và dự định đi vào khoảng thời gian nào không? Có ngân sách dự kiến bao nhiêu để mình "đo ni đóng giày" các lựa chọn tốt nhất cho bạn nhé!

## Test case 2:
Ban: tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
Goi tool: search_flights{'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}
Trả lời trực tiếp

TravelBuddy: Chào bạn! Rất vui được hỗ trợ bạn lên kế hoạch cho chuyến đi Đà Nẵng. Dưới đây là thông tin các chuyến bay từ Hà Nội đi Đà Nẵng hiện có để bạn tham khảo nhé:

**Chuyến bay:**
1. **Vietnam Airlines:** 06:00 - 07:20 | Hạng phổ thông (economy) | 1.450.000đ
2. **Vietnam Airlines:** 14:00 - 15:20 | Hạng thương gia (business) | 2.800.000đ
3. **VietJet Air:** 08:30 - 09:50 | Hạng phổ thông (economy) | 890.000đ
4. **Bamboo Airways:** 11:00 - 12:20 | Hạng phổ thông (economy) | 1.200.000đ

Nếu bạn cần mình tư vấn thêm về khách sạn tại Đà Nẵng hoặc tính toán ngân sách cho chuyến đi này, hãy cho mình biết mức ngân sách dự kiến của bạn nhé! Chúc bạn chọn được chuyến bay ưng ý.

## Test case 3:
Ban: tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp !

TravelBuddy đang suy nghĩ...
Goi tool: search_flights{'origin': 'Hà Nội', 'destination': 'Phú Quốc'}
Goi tool: search_hotels{'city': 'Phú Quốc', 'max_price_per_night': 1000000}
Goi tool: calculate_budget{'total_budget': 5000000, 'expenses': 'vé máy bay:1100000,khách sạn:1600000'}
Trả lời trực tiếp

TravelBuddy: Chào bạn, với ngân sách 5 triệu cho chuyến đi 2 đêm từ Hà Nội đi Phú Quốc, mình thấy hoàn toàn khả thi và bạn còn dư một khoản kha khá để ăn uống, vui chơi đó!

Dưới đây là gợi ý để bạn tham khảo nhé:

**Chuyến bay:**
*   Hãng: VietJet Air
*   Thời gian: 16:00 - 18:15 (chuyến bay tiết kiệm nhất)
*   Giá vé: 1.100.000đ

**Khách sạn:**
*   Lựa chọn: Lahana Resort (Dương Đông)
*   Đánh giá: 4.0 sao, vị trí trung tâm thuận tiện
*   Giá: 800.000đ/đêm x 2 đêm = 1.600.000đ

**Tổng chi phí ước tính:** 2.700.000đ
*   Ngân sách ban đầu: 5.000.000đ
*   Số tiền còn dư: **2.300.000đ** (khoản này cực kỳ thoải mái để bạn chi tiêu cho việc ăn hải sản, thuê xe máy khám phá đảo và vé tham quan các điểm du lịch như VinWonders hay cáp treo Hòn Thơm).

**Gợi ý thêm:**
Với 2.3 triệu dư ra, bạn có thể dành:
- Khoảng 1 triệu cho việc ăn uống đặc sản Phú Quốc (bún quậy, gỏi cá trích, hải sản tại chợ đêm).
- Khoảng 500k để thuê xe máy vi vu khắp đảo trong 3 ngày.
- Còn lại 800k là ngân sách "thoải mái" cho vé tham quan hoặc cafe chill tại các beach bar.

Bạn thấy lịch trình này thế nào? Cần mình hỗ trợ thông tin gì thêm về các điểm vui chơi không?

## Test case 4:
Ban: tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Rất vui được hỗ trợ bạn tìm nơi lưu trú lý tưởng. 

Để mình có thể tư vấn những khách sạn phù hợp nhất với nhu cầu của bạn, bạn cho mình biết thêm một vài thông tin nhé:

1. Bạn định đi du lịch ở **thành phố/địa điểm nào**?
2. Bạn dự kiến đi vào **thời gian nào** (hoặc đi trong bao nhiêu đêm)?
3. **Ngân sách** tối đa cho mỗi đêm mà bạn mong muốn là bao nhiêu? (Hoặc bạn thích khách sạn 3 sao, 4 sao hay khu nghỉ dưỡng cao cấp?)

Bạn cứ chia sẻ, mình sẽ tìm ngay các lựa chọn tốt nhất cho bạn!

## Test case 5:
Ban: giải giúp tôi bài tập lập trình python về linked list 

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Rất tiếc là mình không thể hỗ trợ bạn giải bài tập lập trình hay các vấn đề liên quan đến kỹ thuật/lập trình được.

Vai trò của mình là trợ lý du lịch của **TravelBuddy**, chuyên hỗ trợ lên kế hoạch cho các chuyến đi, đặt vé máy bay, khách sạn và tư vấn ngân sách cho các chuyến du lịch tại Việt Nam thôi.

Nếu bạn đang lên kế hoạch cho một chuyến đi "xả hơi" sau khi làm bài tập, hãy cho mình biết nhé! Mình rất sẵn lòng hỗ trợ bạn tìm kiếm vé máy bay, khách sạn hoặc tính toán chi phí để chuyến đi của bạn trọn vẹn nhất. Bạn đang dự định đi đâu chơi nhỉ?
