import streamlit as st

# כותרת לאפליקציה
st.title("מחשבון בסיסי ב-Streamlit")

# קבלת שני מספרים מהמשתמש
num1 = st.number_input("הכנס מספר ראשון:", value=0.0)
num2 = st.number_input("הכנס מספר שני:", value=0.0)

# בחירת פעולה מתוך רשימה נפתחת (Dropdown)
operation = st.selectbox(
    "בחר פעולה חשבונית:", 
    ["חיבור (+)", "חיסור (-)", "כפל (*)", "חילוק (/)"]
)

# יצירת כפתור. הקוד תחת ה-if ירוץ רק כאשר ילחצו על הכפתור
if st.button("חשב"):
    result = None
    
    # בדיקה איזו פעולה נבחרה וביצוע החישוב
    if operation == "חיבור (+)":
        result = num1 + num2
    elif operation == "חיסור (-)":
        result = num1 - num2
    elif operation == "כפל (*)":
        result = num1 * num2
    elif operation == "חילוק (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("שגיאה: לא ניתן לחלק באפס!")
            
    # אם יש תוצאה תקינה, נציג אותה בצבע ירוק
    if result is not None:
        st.success(f"התוצאה היא: {result}")
