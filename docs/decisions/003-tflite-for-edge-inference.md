---
status: accepted
date: 2026-04-18
---

# Use TF Lite for on-device ML inference

## Context and Problem Statement

Genre and mood classification runs on the Raspberry Pi 4 (ARM64, 4 GB RAM). A full TensorFlow installation is too heavy for this hardware.

## Considered Options

- TensorFlow Lite (`tflite-runtime`)
- Full TensorFlow
- ONNX Runtime
- External classification API (e.g. AcousticBrainz — now defunct)

## Decision Outcome

**Chosen: TF Lite (`tflite-runtime`).**

### Reasons

- `tflite-runtime` is ~1 MB vs ~500 MB for full TensorFlow — fits comfortably in 4 GB RAM alongside the API server
- Official ARM64 wheels available — no compilation needed on Pi
- Models trained in Keras (Google Colab, GPU) and exported via `tf.lite.TFLiteConverter` — single toolchain
- Inference latency target (2–5 sec per 30-sec clip) is achievable on Pi 4

### Consequences

- Model training must happen off-device (Google Colab); only inference runs on Pi
- `.tflite` model files are excluded from git and stored on Google Drive
- ONNX Runtime is a viable alternative but would require an extra conversion step from Keras
