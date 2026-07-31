# Illumicell AI — Blood Cell Classifier

An educational computer-vision project that classifies a microscope image as
an eosinophil, lymphocyte, monocyte, or neutrophil. It uses the public Kaggle
Blood Cell Images dataset and includes a Streamlit interface with prediction
confidence and a human-review warning.

This is not a medical device and must not be used for diagnosis.

## Results

- Random-guessing baseline: 25%
- Week 3 model at 128 × 128: 45.9% test accuracy
- Fine-tuned 128 × 128 model: 46.2% test accuracy
- Selected Week 4 model at 224 × 224: 57.4% test accuracy
- Improvement over Week 3: 11.5 percentage points
- Most-confused pair: monocyte predicted as eosinophil
- Monocyte-to-eosinophil errors: reduced from 347 to 232
- Test set size: 2,487 images

Increasing input resolution from 128 × 128 to 224 × 224 produced the largest
improvement. Full measurements and the final confusion matrix are stored in
`final_results.json` and the executed notebook.

## Confidence and human review

The interface flags predictions below 50% confidence for human review. On the
test set, this threshold:

- Flagged 599 images (about 24%)
- Accepted 1,888 images (about 76%)
- Reached 64.4% accuracy among accepted predictions

Confidence is not a guarantee of correctness. Testing found a confident wrong
prediction, demonstrating that the review threshold cannot catch every error.

## Files

| File | Purpose |
|---|---|
| `blood_cell_classifier.ipynb` | Executed Colab notebook with preparation, training, evaluation, improvements, graphs, and written analysis |
| `blood_cell_model.keras` | Original repository model retained for the team |
| `Akhil_week3.keras` | Week 3 baseline model using 128 × 128 images |
| `blood_cell_model_224_week4.keras` | Selected Week 4 model used by Streamlit |
| `final_results.json` | Accuracy, threshold, and final confusion-matrix measurements |
| `label_map.json` | Numerical output-to-cell-name mapping |
| `streamlit_app.py` | Upload and prediction interface |
| `requirements.txt` | Tested local Python dependencies |

## Run the prediction interface on Windows

Open PowerShell in this project folder. A short environment path avoids a
Windows path-length problem that TensorFlow can encounter inside OneDrive.

1. Create an environment:

   ```powershell
   python -m venv "$env:USERPROFILE\illumicell-env"
   ```

2. Activate it:

   ```powershell
   & "$env:USERPROFILE\illumicell-env\Scripts\Activate.ps1"
   ```

3. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

4. Start Streamlit:

   ```powershell
   python -m streamlit run streamlit_app.py
   ```

5. Open `http://localhost:8501`, upload a JPG or PNG cell image, and click
   **Classify**.

The app loads `blood_cell_model_224_week4.keras`, resizes the image to
224 × 224 using bilinear interpolation, displays all four probabilities, and
flags confidence below 50%.

## Reproduce training in Colab

1. Upload `blood_cell_classifier.ipynb` to Google Colab.
2. Select **Runtime → Change runtime type → T4 GPU**.
3. Create a Kaggle legacy API key and upload `kaggle.json` only when requested.
4. Run the notebook cells in order.
5. Never commit `kaggle.json`; it contains private account credentials.

The notebook creates separate training, validation, and test datasets. The
provided TEST directory remains separate until evaluation.

## Interface test record

- Neutrophil: correctly predicted at 81.0%
- Eosinophil: correctly predicted at 33.7% and flagged for review
- Monocyte: correctly predicted at 69.8%
- Lymphocyte example: incorrectly predicted as monocyte at 51.6%

These tests confirm that uploading, prediction, ranked probabilities, and the
human-review warning work, while also showing the model's limitations.

## Dataset limitation

The Kaggle collection contains augmented images derived from a much smaller
set of original images. Similar augmented versions may make results look better
than performance on genuinely new patients or laboratories. No clinical claims
are made.
