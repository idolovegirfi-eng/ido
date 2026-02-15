import streamlit as st

# הגדרת תצורה בסיסית לעמוד
st.set_page_config(page_title="איקס עיגול", page_icon="🎮")

st.title("משחק איקס עיגול ❌⭕")

# 1. אתחול משתני מצב המערכת (Session State)
if "board" not in st.session_state:
    st.session_state.board = [" "] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# 2. פונקציה לבדיקת ניצחון
def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # שורות
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # עמודות
        [0, 4, 8], [2, 4, 6]              # אלכסונים
    ]
    for c in win_conditions:
        if board[c[0]] == board[c[1]] == board[c[2]] and board[c[0]] != " ":
            return board[c[0]]
    
    if " " not in board:
        return "Tie" # תיקו
        
    return None

# 3. פונקציה לטיפול בלחיצה על משבצת (Callback)
def handle_click(index):
    # הפעולה תתבצע רק אם המשבצת ריקה ואין עדיין מנצח
    if st.session_state.board[index] == " " and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        
        # בדיקת מנצח אחרי המהלך
        st.session_state.winner = check_winner(st.session_state.board)
        
        # החלפת תור (רק אם המשחק ממשיך)
        if st.session_state.winner is None:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# --- יצירת לוח המשחק (Grid 3x3) ---
st.write("") # מרווח קל
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        
        # הגדרת התווית של הכפתור. 
        # השתמשתי בתו בלתי נראה "‎" למקרה שהמשבצת ריקה כדי למנוע אזהרות בסטרימליט.
        label = st.session_state.board[idx]
        if label == " ":
            label = "‎" 
            
        with cols[col]:
            st.button(
                label,
                key=f"btn_{idx}",
                on_click=handle_click,
                args=(idx,)
            )

# --- הצגת התוצאה וניהול סוף המשחק ---
st.write("---")
if st.session_state.winner:
    if st.session_state.winner == "Tie":
        st.subheader("המשחק הסתיים בתיקו! 🤝")
    else:
        st.subheader(f"המנצח הוא {st.session_state.winner}! 🎉")
        
    # כפתור לאיפוס המשחק
    if st.button("התחל משחק חדש", type="primary"):
        st.session_state.board = [" "] * 9
        st.session_state.current_player = "X"
        st.session_state.winner = None
        st.rerun()
else:
    st.subheader(f"תור השחקן: {st.session_state.current_player}")
