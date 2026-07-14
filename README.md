# VisionAero — Drone Landing Zone Safety Detection

A Flask web app that classifies terrain from an image (or live capture) and scores it for drone landing safety, using a CNN (ResNet/ResNeXt-based) feature extractor combined with a Random Forest classifier, plus Grad-CAM explainability.

## Features
- Terrain classification (road, grass, forest, building, water, rocky)
- Risk scoring and landing recommendation per terrain type
- Grad-CAM heatmap overlay for model explainability
- Prediction history log with confidence and risk breakdown

## Tech Stack
- Flask (backend/web server)
- TensorFlow / Keras (CNN feature extractor)
- scikit-learn (Random Forest classifier)
- OpenCV (image processing, Grad-CAM overlay)

## Project Structure
```
├── app.py                  # Flask app entry point
├── gradcam.py               # Grad-CAM heatmap generation
├── train.py                  # Model training script
├── model/
│   ├── best_weights.h5        # Trained CNN weights
│   └── rf_model.pkl           # Trained Random Forest classifier
├── labels.pkl                # Class label encoder
├── templates/                # HTML templates (index, result, history, about)
├── static/                   # CSS/JS/uploaded images
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

## Notes
- The trained model files (`model/best_weights.h5`, `model/rf_model.pkl`) are included in this repo for convenience. If they grow beyond GitHub's file size limits in the future, consider [Git LFS](https://git-lfs.com/).
