# Glossary (in our own words)

Week 1 deliverable. Rewrite these in *your* words before submitting — being able
to explain them plainly is what Week 5 is graded on.

- **Computer vision** — teaching a computer to understand pictures. Ours looks at a cell photo and says which type of cell it is.
- **Classification** — sorting each input into a category. Our four categories are the four white-blood-cell types.
- **Training** — showing the model thousands of labeled example images so it learns the visual patterns of each cell type.
- **Model** — the trained program: image goes in, a predicted cell type comes out.
- **Label** — the correct answer attached to a training image (e.g. "this is a lymphocyte").
- **Training set / test set** — we train on one batch of images and measure on a *separate* batch the model never saw, so the accuracy is real.
- **Accuracy** — the percentage of test images the model gets right. With 4 equal classes, random guessing is ~25%.
- **Confusion matrix** — a table showing which categories get mixed up. The diagonal is correct; off-diagonal cells are specific mistakes.
- **Confidence** — how sure the model is about a prediction. Low confidence means a human should double-check.
- **Transfer learning** — starting from a model already trained on millions of images and adapting it to our task. Much faster and more accurate than starting from scratch.
- **Data augmentation** — making more training examples by flipping/rotating/zooming images so the model generalizes better.
- **Human-in-the-loop** — keeping a person in the process to review the cases the model is unsure about. Essential in medical AI.
