# smart_stickies_product_page.py
#
# Streamlit Product-Info prototype powered by O3 (GPT-3.5-Turbo)
# --------------------------------------------------------------
# 1. pip install streamlit openai
# 2. streamlit run smart_stickies_product_page.py
# --------------------------------------------------------------

import streamlit as st
import openai
import time
from datetime import datetime

# ----------  Product “ground-truth”  ----------
PRODUCT = {
    "name": "SmartStickies™ NFC Tag",
    "image": "https://www.smart-stickies.com/_next/static/media/smart-sticky.4e8c1234.png",  # replace with real asset
    "price": "$19.99 (10-pack)",
    "spec_sheet": """
SmartStickies are peel-and-stick NFC tags for instant phygital engagement.
• ISO-14443 NFC Type 4 compliant
• Works through glass & plastic < 2 mm
• Custom 29 mm diameter, matte finish
• Data retention ≥ 10 years
• Water-resistant (IP67)
""".strip()
}

# ----------  Streamlit page setup  ----------
st.set_page_config(page_title=PRODUCT["name"], page_icon=":label:", layout="wide")
st.image(PRODUCT["image"], use_column_width=True)
st.title(PRODUCT["name"])
st.markdown(f"**Price:** {PRODUCT['price']}")

# ----------  API key + prompt controls  ----------
api_key = st.text_input("OpenAI API key", type="password")
default_prompt = (
    "Write a 40-word product tagline and a 4-bullet benefit list "
    "for the SmartStickies NFC Tag below. Keep the tone energetic, retail-friendly, no hype-words."
)
prompt = st.text_area("Custom prompt (optional)", value=default_prompt, height=100)
generate_btn = st.button("✨ Generate / Refresh Copy with O3")

# ----------  Placeholder areas  ----------
tagline_area = st.empty()
bullets_area = st.empty()
metrics_area = st.empty()

# ----------  Run O3 when the user clicks  ----------
if generate_btn:
    if not api_key:
        st.error("Please enter your OpenAI API key.")
        st.stop()

    openai.api_key = api_key
    system_msg = (
        "You are a marketing copywriter for Smart Stickies. "
        "Return Markdown only: a one-line tagline in **bold** then a bullet list."
    )

    user_prompt = prompt or default_prompt
    user_prompt += "\n\nPRODUCT SPECS:\n" + PRODUCT["spec_sheet"]

    start = time.perf_counter()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # ← O3 in the API
            temperature=0.7,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_prompt}
            ]
        )
    except Exception as e:
        st.error(f"O3 error: {e}")
        st.stop()

    duration_ms = (time.perf_counter() - start) * 1000
    ai_content = response.choices[0].message.content
    usage = response.usage  # has prompt_tokens & completion_tokens

    # ----------  Show results  ----------
    tagline_area.markdown(ai_content, unsafe_allow_html=True)
    metrics_area.caption(
        f"🕒 {duration_ms:,.0f} ms  |  "
        f"🔢 prompt {usage.prompt_tokens} tkn  |  "
        f"output {usage.completion_tokens} tkn  |  "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

# ----------  Static footer  ----------
st.markdown("---")
st.write(
    "SmartStickies instantly connects offline shoppers to digital experiences with a single tap—"
    "no app, no QR code, pure NFC magic."
)
st.caption("© 2025 SmartStickies Inc.")
