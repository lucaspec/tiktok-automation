# Automated tiktok clip creation
This is a small repo to easily create tiktok clips using OCR, TTS and video compilation

## Get started 

install packages
```bash
pip install -r requirements.txt
```

run generation script
```bash
./generate_vid.sh
```

the output video will be found in output folder

**NOTE:** Make sure to download [tesseract.exe](https://tesseract-ocr.github.io/tessdoc/Downloads.html) and link its path at the start of ocr.py


## Adjust to your own needs

1. Paste cropped text images to /texts folder
2. Change text path in ocr.py
3. Generate video as described above