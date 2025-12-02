import streamlit as st
import time

# ================= CẤU HÌNH TRANG WEB =================
st.set_page_config(page_title="Free MemberShip Liên Quân Mobile", page_icon="🎁", layout="wide")

# // Giấu cái menu của Streamlit đi cho giống web thật //
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# // Khởi tạo biến trạng thái (Để nhớ xem đã bị lừa chưa) //
if 'bi_lua' not in st.session_state:
    st.session_state.bi_lua = False
if 'ten_nan_nhan' not in st.session_state:
    st.session_state.ten_nan_nhan = ""

# ================= PHẦN 1: GIAO DIỆN DỤ DỖ (LÚC CHƯA BẤM) =================
if not st.session_state.bi_lua:
    st.image("https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif", width=100)
    st.title("🎁 Nhận Quà Free 🎁")
    st.warning("⚠️ MemberShip Liên Quân Mobile VN!")
    
    st.write("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("💎 Gói quà bao gồm:")
        st.write("- 36 quân huy")
        st.write("- Qi tiệc bãi biển")
        st.write("- Lauriel công chúa rau má ")
        
    with col2:
        # // Form nhập liệu để dụ nó //
        with st.form("form_nhan_qua"):
            st.write("### 📝 ĐIỀN THÔNG TIN ĐỂ NHẬN")
            ten = st.text_input("Nhập Tên hoặc Nickname của bạn:", placeholder="Ví dụ: Sang Gay Lọ")
            id_game = st.text_input("Nhập ID Game:", placeholder="UID: 12345678")
            server = st.selectbox("Chọn Server:", ["Việt Nam", "Quốc Tế", "Mặt Trăng" , "Thanh Hóa"])
            
            nut_nhan = st.form_submit_button("🚀 BẤM ĐỂ NHẬN NGAY")
            
            if nut_nhan:
                if not ten:
                    st.error("Nhập tên vào đi cu!")
                else:
                    # // LƯU TÊN NẠN NHÂN VÀ CHUYỂN TRẠNG THÁI //
                    st.session_state.ten_nan_nhan = ten.upper() # Viết hoa cho to
                    
                    # // Hiệu ứng loading giả trân //
                    with st.spinner("⏳ Đang kết nối đến máy chủ Garena..."):
                        time.sleep(2)
                    with st.spinner("🔓 Đang bẻ khóa bảo mật..."):
                        time.sleep(2)
                    with st.spinner("🎁 Đang gửi quà về túi đồ..."):
                        time.sleep(1)
                    
                    # // Kích hoạt cú lừa //
                    st.session_state.bi_lua = True
                    st.rerun() # Load lại trang ngay lập tức

# ================= PHẦN 2: GIAO DIỆN TROLL (SAU KHI BẤM) =================
else:
    # // CSS tạo hiệu ứng nhấp nháy 7 màu (Đau mắt vcl) //
    css_hieu_ung = f"""
    <style>
        /* Hiệu ứng nền chớp tắt */
        .stApp {{
            animation: background_flash 0.5s infinite;
        }}
        
        @keyframes background_flash {{
            0% {{background-color: black;}}
            25% {{background-color: red;}}
            50% {{background-color: blue;}}
            75% {{background-color: yellow;}}
            100% {{background-color: black;}}
        }}

        /* Hiệu ứng chữ phóng to thu nhỏ đổi màu */
        .troll-text {{
            font-size: 80px;
            font-weight: 900;
            text-align: center;
            text-transform: uppercase;
            font-family: 'Arial Black', sans-serif;
            margin-top: 15%;
            animation: text_disco 0.2s infinite;
            text-shadow: 4px 4px 0px #000;
        }}

        @keyframes text_disco {{
            0% {{color: #ff0000; transform: scale(1) rotate(-5deg);}}
            25% {{color: #00ff00; transform: scale(1.2) rotate(5deg);}}
            50% {{color: #0000ff; transform: scale(1) rotate(-5deg);}}
            75% {{color: #ffff00; transform: scale(1.2) rotate(5deg);}}
            100% {{color: #ff00ff; transform: scale(1) rotate(-5deg);}}
        }}
        
        .sub-text {{
            font-size: 30px;
            color: white;
            text-align: center;
            font-weight: bold;
        }}
    </style>
    """
    
    # // Bơm CSS vào web //
    st.markdown(css_hieu_ung, unsafe_allow_html=True)
    
    # // HIỆN CHỮ TROLL TO ĐÙNG //
    ten = st.session_state.ten_nan_nhan
    st.markdown(f'<div class="troll-text">{ten}<br>YÊU<br>PHAN OANH ❤️</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-text">(Trốn đi đâu được!)</div>', unsafe_allow_html=True)
    st.balloons() # // Bắn bóng bay chúc mừng //
    
    # // Nút bấm để quay lại (nếu nó cay quá muốn thoát) //
    if st.button("Xin lỗi anh Quân , em chừa rồi"):
        st.session_state.bi_lua = False
        st.rerun()