"""
Illumicell AI — Blood Cell Classifier interface (Week 4).

A person uploads a microscope image of a white blood cell; the app shows the
predicted cell type, how confident the model is, and — the important part for
medical AI — flags low-confidence images for a human to review instead of
trusting the prediction (human-in-the-loop).

Run locally:
    pip install streamlit tensorflow pillow numpy
    streamlit run streamlit_app.py

You need the two files exported by the notebook in this same folder:
    blood_cell_model.keras
    label_map.json
"""

import json
import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf

# --- Config -----------------------------------------------------------------
IMG_SIZE = (128, 128)          # must match the notebook
CONFIDENCE_THRESHOLD = 0.70    # below this -> flag for human review. Tune it.

st.set_page_config(page_title="Illumicell Cell Classifier", page_icon="🔬")


@st.cache_resource
def load_model_and_labels():
    model = tf.keras.models.load_model("blood_cell_model.keras")
    with open("label_map.json") as f:
        # JSON keys are strings; convert back to int -> name
        label_map = {int(k): v for k, v in json.load(f).items()}
    return model, label_map


def predict(model, label_map, image: Image.Image):
    img = image.convert("RGB").resize(IMG_SIZE)
    arr = np.expand_dims(np.array(img), axis=0).astype("float32")
    probs = model.predict(arr, verbose=0)[0]
    order = np.argsort(probs)[::-1]  # most likely first
    return [(label_map[int(i)], float(probs[i])) for i in order]


# --- UI ---------------------------------------------------------------------
st.title("🔬 Blood Cell Classifier")
st.caption(
    "Learning prototype on the public Kaggle Blood Cell Images dataset. "
    "**Not a medical device** and not for clinical use."
)

try:
    model, label_map = load_model_and_labels()
except Exception as e:
    st.error(
        "Could not load the model. Make sure `blood_cell_model.keras` and "
        f"`label_map.json` are in this folder.\n\nDetails: {e}"
    )
    st.stop()

uploaded = st.file_uploader(
    "Upload a microscope image of a white blood cell",
    type=["png", "jpg", "jpeg", "bmp"],
)

if uploaded is not None:
    image = Image.open(uploaded)
    st.image(image, caption="Uploaded image", width=300)

    if st.button("Classify"):
        ranked = predict(model, label_map, image)
        top_name, top_conf = ranked[0]

        # Human-in-the-loop safety net
        if top_conf < CONFIDENCE_THRESHOLD:
            st.warning(
                f"⚠️ Low confidence ({top_conf*100:.1f}%). "
                "**Flagged for human review** — do not trust this prediction."
            )
        else:
            st.success(f"Prediction: **{top_name}**")

        st.metric("Confidence", f"{top_conf*100:.1f}%")

        # Show every class so an honest 'it's between two types' is visible
        # and the true class can never be hidden below the cut-off.
        st.subheader("All predictions")
        for name, conf in ranked:
            st.write(f"{name}")
            st.progress(min(max(conf, 0.0), 1.0))
            st.caption(f"{conf*100:.1f}%")

st.divider()
st.caption(
    f"Images with top confidence below {CONFIDENCE_THRESHOLD*100:.0f}% are routed "
    "to a human. Tune this threshold by looking at confidence on your test images."
)
