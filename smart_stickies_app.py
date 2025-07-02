import streamlit as st

# Fake product info (replace with real data/images as needed)
PRODUCT = {
    "name": "SmartStickies™ NFC Tag",
    "image": "https://www.smart-stickies.com/assets/img/SmartStickies_hero.png",  # Example: public image link, update as needed!
    "tagline": "Tap. Connect. Experience the Future of Retail.",
    "description": (
        "SmartStickies™ lets you instantly connect shoppers to digital content—no app required! "
        "Transform any product or in-store display with our NFC-enabled stickers. "
        "Perfect for product info, self-checkout, loyalty programs, and more."
    ),
    "features": [
        "NFC tap-to-connect (no app needed)",
        "Works on any product or shelf",
        "Customizable digital actions (URL, SMS, map, email, promo)",
        "Secure & privacy-safe",
        "Quick to set up with our free mobile app",
        "Boosts in-store engagement and conversions"
    ],
    "price": "$19.99 (10-pack)",
    "video_url": "https://www.youtube.com/embed/XgYu7-DQjDQ"  # Replace with real promo/demo if available
}

st.set_page_config(page_title=PRODUCT["name"], page_icon=":label:")

# Product image
st.image(PRODUCT["image"], use_column_width=True)

# Product name and tagline
st.title(PRODUCT["name"])
st.subheader(PRODUCT["tagline"])

# Short description
st.write(PRODUCT["description"])

# Feature list
st.markdown("**Key Features:**")
for feature in PRODUCT["features"]:
    st.markdown(f"- {feature}")

# Price
st.markdown(f"### Price: {PRODUCT['price']}")

# Action buttons
col1, col2, col3 = st.columns(3)
with col1:
    st.button("Buy Now 🛒")
with col2:
    st.button("Learn More ℹ️")
with col3:
    st.button("Share 🔗")

# Promo/demo video (optional)
st.markdown("#### See SmartStickies in Action:")
st.video(PRODUCT["video_url"])

# Footer or legal
st.caption("© 2025 SmartStickies. All rights reserved.")
