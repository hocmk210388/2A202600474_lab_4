from langchain_core.tools import tool

# ============================================================
# MOCK DATA – Dữ liệu giả lập hệ thống du lịch
# Lưu ý: Giá cả có logic (VD: cuối tuần đắt hơn, hạng cao hơn đắt hơn)
# Sinh viên cần đọc hiểu data để debug test cases.
# ============================================================

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}

def _format_vnd(amount: int) -> str:
    return f"{amount:,}".replace(",", ".") + "đ"

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    - origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    - destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')

    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    Nếu không tìm thấy chuyến bay, trả về thông báo không có chuyến.
    """
    flights = FLIGHTS_DB.get((origin, destination))
    if flights:
        lines = [f"Các chuyến bay từ {origin} đến {destination}:"]
        for i, flight in enumerate(flights, start=1):
            lines.append(
                f"{i}. {flight['airline']} | {flight['departure']} - {flight['arrival']} | "
                f"{flight['class']} | {_format_vnd(flight['price'])}"
            )
        return "\n".join(lines)

    reverse_flights = FLIGHTS_DB.get((destination, origin))
    if reverse_flights:
        lines = [
            f"Không tìm thấy chuyến bay chiều {origin} -> {destination}.",
            f"Hiện có các chuyến bay chiều ngược lại ({destination} -> {origin}):",
        ]
        for i, flight in enumerate(reverse_flights, start=1):
            lines.append(
                f"{i}. {flight['airline']} | {flight['departure']} - {flight['arrival']} | "
                f"{flight['class']} | {_format_vnd(flight['price'])}"
            )
        return "\n".join(lines)

    return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."


@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.

    Tham số:
    - city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    - max_price_per_night: giá tối đa mỗi đêm (VND), mặc định không giới hạn

    Trả về danh sách khách sạn phù hợp với tên, số sao, giá, khu vực, rating.
    """
    hotels = HOTELS_DB.get(city)
    if not hotels:
        return f"Không tìm thấy dữ liệu khách sạn tại {city}."

    filtered = [h for h in hotels if h["price_per_night"] <= max_price_per_night]
    filtered.sort(key=lambda h: h["rating"], reverse=True)

    if not filtered:
        return (
            f"Không tìm thấy khách sạn tại {city} với giá dưới "
            f"{_format_vnd(max_price_per_night)}/đêm. Hãy thử tăng ngân sách."
        )

    lines = [f"Khách sạn tại {city} (<= {_format_vnd(max_price_per_night)}/đêm):"]
    for i, hotel in enumerate(filtered, start=1):
        lines.append(
            f"{i}. {hotel['name']} | {hotel['stars']} sao | {hotel['area']} | "
            f"rating {hotel['rating']} | {_format_vnd(hotel['price_per_night'])}/đêm"
        )
    return "\n".join(lines)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    - total_budget: tổng ngân sách ban đầu (VND)
    - expenses: chuỗi mô tả các khoản chi, mỗi khoản cách nhau bởi dấu phẩy,
    định dạng 'tên khoản:số tiền' (VD:
    'vé máy bay:890000,khách sạn:650000')
    Trả về bằng chi tiết các khoản chi và số tiền còn lại.
    Nếu vượt ngân sách, cảnh báo rõ ràng số tiền thiếu.
    """
    try:
        parsed_expenses = {}
        raw_items = [item.strip() for item in expenses.split(",") if item.strip()]

        if not raw_items:
            return "Lỗi định dạng expenses: vui lòng nhập ít nhất 1 khoản theo dạng 'tên:số_tiền'."

        for item in raw_items:
            if ":" not in item:
                return (
                    "Lỗi định dạng expenses: mỗi khoản phải theo dạng 'tên:số_tiền', "
                    f"nhưng nhận được '{item}'."
                )
            name, amount_text = item.split(":", 1)
            name = name.strip()
            amount_text = amount_text.strip()
            if not name:
                return "Lỗi định dạng expenses: tên khoản chi không được để trống."
            if not amount_text.isdigit():
                return (
                    "Lỗi định dạng expenses: số tiền phải là số nguyên dương, "
                    f"nhưng nhận được '{amount_text}'."
                )
            parsed_expenses[name] = parsed_expenses.get(name, 0) + int(amount_text)

        total_expenses = sum(parsed_expenses.values())
        remaining = total_budget - total_expenses

        lines = ["Bảng chi phí:"]
        for name, amount in parsed_expenses.items():
            lines.append(f"- {name}: {_format_vnd(amount)}")
        lines.extend(
            [
                "---",
                f"Tổng chi: {_format_vnd(total_expenses)}",
                f"Ngân sách: {_format_vnd(total_budget)}",
                f"Còn lại: {_format_vnd(remaining)}",
            ]
        )
        if remaining < 0:
            lines.append(f"Vượt ngân sách {_format_vnd(abs(remaining))}! Cần điều chỉnh.")
        return "\n".join(lines)
    except Exception as exc:
        return f"Lỗi xử lý ngân sách: {exc}"



#     Chú ý:

# - search_flights: phải xử lý tuple key, thứ tự ngược chiều
# - search_hotels: phải lọc + sắp xếp, không chỉ lookup
# - calculate_budget: phải parse chuỗi, xử lý format lỗi, tính toán thực sự
# - 3 tools có MỐI LIÊN HỆ: kết quả flights → input cho budget → quyết định hotels