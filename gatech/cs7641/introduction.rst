Supervised Learning
===================

**Definition**
- **Supervised learning**: learn from labeled examples (each input has a known "right answer").
- Algorithm generalizes to new inputs.

**Regression** (continuous output)
- Example: predict **housing price** from size (Portland dataset).
- Fit **linear** vs **quadratic** model → different predictions for new house (e.g. 750 sq ft).
- **Regression problem**: predict a **continuous-valued** output (price as real/scalar).

**Classification** (discrete output)
- Example: **breast tumor** malignant (1) vs benign (0) from tumor size.
- Can extend to multi-class (0 = benign, 1/2/3 = cancer types).
- Plot alternatives: malignant (X) vs benign (O) on a line; or **age + tumor size** in 2D with a separating line.
- Real datasets use many features (clump thickness, cell size uniformity, cell shape, …).
- Some problems need an **infinite number of features**; **SVM** uses a math trick so the computer need not store them all.

**Recap**
- **Supervised**: every training example has a label (price, malignant/benign, …).
- **Regression** → continuous output; **classification** → discrete output.

**Problem type quiz**
- Sell count of identical items in 3 months → **regression** (continuous count).
- Per-account hacked or not → **classification** (0/1 discrete labels).


Unsupervised Learning
=====================

**Definition**
- Data **without** labels (or all same label); algorithm finds **structure** in data.
- Opposite of supervised: no per-example "correct answer" given.

**Clustering**
- Partition data into groups (clusters).
- Applications:
  - **Google News**: cluster articles on same story (e.g. BP oil spill).
  - **Genomics / DNA microarrays**: group individuals by gene expression patterns.
  - **Data centers**: which machines work together.
  - **Social networks**: cohesive friend groups.
  - **Market segmentation**: discover customer segments from unlabeled data.
  - **Astronomy**: galaxy-formation theories from clustering.

**Cocktail party problem (source separation)**
- Multiple speakers, two microphones → overlapping recordings.
- **Unsupervised** algorithm separates sources (e.g. English vs Spanish counting).
- Implementable in **one line** in Octave/Matlab (after research); prototype in Octave, port to C++/Java once working.
- Silicon Valley workflow: prototype in Octave/Matlab (fast iteration, built-in linear algebra e.g. SVD).

**Unsupervised vs supervised (examples)**
- Spam with labeled spam/non-spam → **supervised**.
- News clustering → **unsupervised**.
- Market segments from customer data only → **unsupervised**.
- Diabetes yes/no (like tumor labels) → **supervised**.


Supervised Learning — Reference Detail
--------------------------------------

**Housing regression setup**
- Input :math:`x` = size (sq ft); output :math:`y` = price ($1000s).
- Training set gives :math:`(x^{(i)}, y^{(i)})` with correct prices.
- New house :math:`x_{\mathrm{new}}` → predict :math:`y_{\mathrm{new}}` via learned function (line, polynomial, etc.).

**Classification setup**
- Output :math:`y \in \{0,1\}` (benign/malignant) or :math:`y \in \{0,1,2,3\}` (multi-class cancer types).
- 1D: tumor size only; 2D: size + patient age; high-D: clump thickness, uniformity of cell size/shape, marginal adhesion, …
- **Support Vector Machine**: kernel trick handles very large (conceptually infinite) feature spaces without explicit storage.

**Infinite features**
- More features → more cues for prediction.
- Challenge: storing infinite feature vectors.
- SVM: mathematical trick (covered later) to work in rich feature spaces efficiently.


Unsupervised Learning — Reference Detail
----------------------------------------

**Clustering vs classification**
- Clustering: no labels; discover groups (e.g. news topics, customer segments).
- Classification: labeled training examples required.

**Cocktail party / blind source separation**
- :math:`m` microphones, :math:`n` speakers → mixed recordings.
- Unsupervised algorithm infers separate sources (ICA-style).
- Octave prototype: research distilled to short code; production often reimplemented in C++/Java after validation.

**When to use which**
- Labeled outcomes (price, spam, disease) → supervised.
- Structure discovery only (segments, article groups, gene types) → unsupervised.
