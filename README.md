# Illumicell AI — Blood Cell Classifier (Technical Track)

A computer-vision model that reads a microscope image of a white blood cell and
identifies its type, plus a simple web interface with a confidence display and a
human-in-the-loop safety net. Built on the public **Kaggle Blood Cell Images**
dataset (~12,500 images, 4 cell types). No real patient data is used.

## Files
| File | What it is |
|---|---|
| `blood_cell_classifier.ipynb` | The Colab notebook: load → explore → prepare → split → train → evaluate → save |
| `streamlit_app.py` | Week 4 interface: upload an image, see prediction + confidence + review flag |
| `team_charter.md` | Day 1 team document (fill in your names) |
| `glossary.md` | Computer-vision terms in plain language |
| `problem_statement.md` | The one-paragraph problem statement + success definition |

## How to run the model (Colab)
1. Go to [colab.research.google.com](https://colab.research.google.com), open `blood_cell_classifier.ipynb`, save a copy to your shared team Drive folder.
2. **Runtime → Change runtime type → GPU.**
3. Run Section 1a once to download the Kaggle dataset (needs a free Kaggle account + API token).
4. **Runtime → Run all.** Training takes a few minutes on the GPU.
5. It prints your **test accuracy**, draws a **confusion matrix**, shows failures, and saves `blood_cell_model.keras` + `label_map.json`.

## How to run the interface
Download `blood_cell_model.keras` and `label_map.json` from Colab into this folder, then:
```bash
pip install streamlit tensorflow pillow numpy
streamlit run streamlit_app.py
```

## Results (fill these in)
- **Starting test accuracy:** ____%  (random guessing with 4 classes = 25%)
- **After improvement:** ____%
- **Most-confused pair:** ____ mistaken for ____
- **Improvement that helped most:** ____

## Honest scope
This is a learning prototype trained on public data. It is **not** a diagnostic
device and makes no clinical claims.
