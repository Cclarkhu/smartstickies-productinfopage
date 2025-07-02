# smart_stickies_app.py
# -------------------------------------------------------------
# 1. pip install streamlit openai
# 2. streamlit run smart_stickies_app.py
#    (Paste your OpenAI API key when prompted)
# -------------------------------------------------------------
import streamlit as st
import openai, time, datetime

# ----------  RETAIL PRODUCT DATA  ----------
PRODUCT = {
    "name": "EcoSole Running Sneakers",
    "image": "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?"
             "auto=format&fit=crop&w=800&q=80",           # Replace with your own
    "price": "$59.99",
    "description": (
        "EcoSole Running Sneakers are crafted from 75 % recycled materials. "
        "They’re lightweight, water-resistant, and come in four vibrant colours—"
        "perfect for daily runs and weekend adventures."
    ),
    "specs": [
        "75 % recycled plastic upper",
        "Moisture-wicking bamboo liner",
        "Slip-resistant EcoGrip™ sole",
        "Weight: 0.55 lb (size 9)",
        "Sizes: US 6–13"
    ]
}

# ----------  STREAMLIT PAGE SETUP  ----------
st.set_page_config(page_title=PRODUCT["name"], page_icon="🛍️", layout="centered")
st.image(PRODUCT["image"], use_column_width=True)
st.title(PRODUCT["name"])
st.subheader(PRODUCT["description"])
st.markdown(f"### Price : {PRODUCT['price']}")

# ----------  STATIC SPECS  ----------
with st.expander("📋 Full Specifications"):
    for spec in PRODUCT["specs"]:
        st.markdown(f"- {spec}")

st.markdown("---")

# ----------  O3 PROMPT & BUTTON  ----------
api_key = st.text_input("OpenAI API Key", type="password")
prompt_default = (
    "Write a 40-word product tagline followed by a 4-bullet benefit list "
    "for the item below. Tone: energetic, retail-friendly, no hype-words."
)
prompt = st.text_area("Custom prompt (optional)", prompt_default, height=100)
if st.button("✨ Generate Copy with O3"):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
        st.stop()

    openai.api_key = api_key
    user_prompt = (
        prompt.strip() + "\n\nPRODUCT SPECS:\n" +
        "\n".join(PRODUCT["specs"])
    )

    start = time.perf_counter()
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",        # ← O3 in the API
            temperature=0.7,
            messages=[
                {"role": "system",
                 "content": "You are a marketing copywriter for a retail brand. "
                            "Return Markdown only: one bold tagline then a bullet list."},
                {"role": "user", "content": user_prompt}
            ]
        )
    except Exception as e:
        st.error(f"O3 error: {e}")
        st.stop()

    duration_ms = (time.perf_counter() - start) * 1000
    out = resp.choices[0].message.content
    usage = resp.usage

    st.markdown("---")
    st.markdown("## 🖋️ AI-Generated Copy")
    st.markdown(out, unsafe_allow_html=True)
    st.caption(
        f"⌛ {duration_ms:,.0f} ms · "
        f"Tokens in {usage.prompt_tokens} out {usage.completion_tokens} · "
        f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
    )

st.markdown("---")
st.caption("© 2025 Smart Stickies Inc.  — Demo retail page powered by O3 (GPT-3.5 Turbo)")
