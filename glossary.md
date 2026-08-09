# Glossary 

Week 1 deliverable. Rewrite these in *your* words before submitting — being able
to explain them plainly is what Week 5 is graded on.

- **Computer vision** — defined by enabling the ability of a computer to interpret, analyse and extract important information from digital images, effectively allowing machines to gain sight. 
In our case it would be the recognition of the cell type after looking at its image.
- **Classification** — In Computer vision and machine learning classification is to sort visual images in predefined classes. In our case the four categories are the four white-blood-cell types.
- **Training** — the process of giving a computer-learning-algorithm a big dataset of images so it can learn to recognize patterns, features and objects on its own. In our case this would be to show the model thousands of labeled cell type images.
- **Model** — is a computer program that looks at data, learns patterns and makes predictions. Our trained program: image goes in, a predicted cell type comes out.
- **Label** — the expected answer or tag assigned to a virtual picture, such as identifying an object in an image, this helps the computer what to look out for during training (e.g. "this is a lymphocyte").
- **Training set / test set** — is the portion of data given to a machine learning model so it call learns patterns and makes prediction 
- **Accuracy** — a perfomance calculation that measures the percentage of correct predictions makes out of its total prediction . With 4 equal classes, random guessing is ~25%.
- **Confusion matrix** — a table showing which categories get mixed up. The diagonal is correct; off-diagonal cells are specific mistakes.
- **Confidence** — how sure the model is about a prediction. Low confidence means a human should double-check.
- **Transfer learning** — starting from a model already trained on millions of images and adapting it to our task. Much faster and more accurate than starting from scratch.
- **Data augmentation** — making more training examples by flipping/rotating/zooming images so the model generalizes better.
- **Human-in-the-loop** — keeping a person in the process to review the cases the model is unsure about. Essential in medical AI.
