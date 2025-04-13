import streamlit as st
import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score == 5:
        return "Very Strong 💪"
    elif score >= 4:
        return "Strong ✅"
    elif score >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

# Streamlit UI
st.title("🔐 Password Strength Checker")

password_input = st.text_input("Enter your password:", type="password")

if password_input:
    strength = check_password_strength(password_input)
    st.write(f"**Password Strength:** {strength}")
    if strength == "Weak ❌":
        st.warning("Your password is weak. Consider using a mix of uppercase, lowercase, digits, and special characters.")
    elif strength == "Moderate ⚠️":
        st.info("Your password is moderate. Try to make it stronger by adding more complexity.")
    elif strength == "Strong ✅":
        st.success("Your password is strong!")
    else:
        st.success("Your password is very strong!")

