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
visionaero-drone-landing/
├── app.py
├── gradcam.py
├── train.py
├── download_images.py
├── download_test_images.py
├── organize_dataset.py
├── rename_folders.py
├── requirements.txt
├── README.md
├── Dockerfile
├── labels.pkl
├── history.json
├── confusion_matrix.png
├── training_curves.png
├── model/
│   ├── best_weights.h5
│   └── rf_model.pkl
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   └── about.html
└── static/
    └── uploads/         
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
