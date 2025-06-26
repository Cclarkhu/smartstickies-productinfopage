"""
SmartStickies Tag Generator – Streamlit App (uses OpenAI o3)
Run locally with:
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    streamlit run smart_stickies_app.py
"""
import os, streamlit as st, dotenv
from openai import OpenAI

dotenv.load_dotenv()                       # loads .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = "o3"

def generate(product, store, goal, tone, words):
    prompt = (
        f"Product: {product}\nStore type: {store}\nGoal: {goal}\nTone: {tone}\n"
        f"Word-count target: {words}\n\n"
        "Return JSON with keys 'headline', 'short_description', 'cta', "
        "'key_benefits' (array). Max 60 words total."
    )
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return resp.choices[0].message.content.strip()

st.set_page_config(page_title="SmartStickies Tag Generator", layout="centered")
st.title("🗒️ SmartStickies Tag Generator (o3)")

with st.form("form"):
"""
SmartStickies Tag Generator – Streamlit App (uses OpenAI o3)
Run locally with:
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    streamlit run smart_stickies_app.py
"""
import os, streamlit as st, dotenv
from openai import OpenAI

dotenv.load_dotenv()                       # loads .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = "o3"

def generate(product, store, goal, tone, words):
    prompt = (
        f"Product: {product}\nStore type: {store}\nGoal: {goal}\nTone: {tone}\n"
        f"Word-count target: {words}\n\n"
        "Return JSON with keys 'headline', 'short_description', 'cta', "
        "'key_benefits' (array). Max 60 words total."
    )
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return resp.choices[0].message.content.strip()

st.set_page_config(page_title="SmartStickies Tag Generator", layout="centered")
st.title("🗒️ SmartStickies Tag Generator (o3)")

with st.form("form"):
    product = st.text_input("Product name")
    store   = st.text_input("Store type")
    goal    = st.text_area("Engagement goal")
    tone    = st.selectbox("Tone", ["Friendly", "Professional", "Playful", "Luxury"])
    words   = st.slider("Approx. word-count", 20, 60, 40)
    submitted = st.form_submit_button("Generate")

if submitted:
    if not all([product, store, goal]):
        st.error("Please fill all fields.")
        st.stop()
    st.code(generate(product, store, goal, tone, words), language="json")

