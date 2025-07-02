import streamlit as st

# --- Product Data ---
PRODUCT = {
    "name": "SmartStickies™ NFC Tag",
    "image": "https://www.smart-stickies.com/_next/static/media/smart-sticky.4e8c1234.png",
    "price": "$19.99 (10-pack)",
    "description": "SmartStickies NFC tags instantly connect customers to digital experiences. Just tap—no app or QR code required.",
    "features": [
        "Instant tap-to-connect NFC",
        "Works through glass and plastic",
        "Water-resistant, durable, easy to use",
        "No battery, no maintenance, just stick and go!"
    ]
}

st.set_page_config(page_title=PRODUCT["name"], page_icon=":label:", layout="centered")

# Product image and name
st.image(PRODUCT["image"], width=320)
st.title(PRODUCT["name"])
st.subheader(PRODUCT["description"])
st.markdown(f"**Price:** {PRODUCT['price']}")

# Feature bullets
st.markdown("**Key Features:**")
for feat in PRODUCT["features"]:
    st.markdown(f"- {feat}")

# Divider
st.markdown("---")

# Existing O3-powered copy generator UI
api_key = st.text_input("OpenAI API key", type="password")
prompt = st.text_area("Custom prompt (optional)", value=(
    "Write a 40-word product tagline and a 4-bullet benefit list "
    "for the SmartStickies NFC Tag below. Keep the tone energetic, retail-friendly, no hype-words."
), height=100)
generate_btn = st.button("✨ Generate / Refresh Copy with O3")

if generate_btn:
    # O3 code here as before...
    pass  # (Insert O3 code from earlier)

st.markdown("---")
st.write("SmartStickies instantly connects offline shoppers to digital experiences with a single tap—no app, no QR code, pure NFC magic.")
st.caption("© 2025 SmartStickies Inc.")
