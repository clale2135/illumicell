# Problem statement & success definition

## The build we chose
**Option A — The Cell Classifier** (the guideline's recommended first build).

## Problem statement (one paragraph)
Reading microscope images by hand is slow, and there aren't enough trained
technicians to do it at scale. We are building a computer-vision model that looks
at a microscope image of a single white blood cell and automatically identifies
its type (eosinophil, lymphocyte, monocyte, or neutrophil). It stands in for the
kind of automated, machine-readable microscopy Illumicell does. We train and test
only on the public Kaggle Blood Cell Images dataset — never real patient samples.

## Input and output
- **Input:** one microscope image of a white blood cell.
- **Output:** the predicted cell type **and** a confidence score, with low-confidence images flagged for human review.

## What "good output" is (how we measure success)
- **Primary metric:** overall accuracy on a held-out test set the model never trained on.
- **Deeper look:** a confusion matrix, so we know *which* cell types get mixed up, not just a single number.
- **Honesty:** the model is allowed to be unsure — when confidence is below our threshold, it says "needs human review" rather than guessing. An honest "not sure" beats a confident wrong answer.
- **Baseline to beat:** random guessing with 4 classes is ~25%; a working model should be well above that.

## Scope / disclaimer
This is a learning prototype on public data, not a medical device, and it makes
no clinical claims.
