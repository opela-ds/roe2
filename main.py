from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import re

app = FastAPI()

EMAIL = "24f1001750@ds.study.iitm.ac.in"

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    text = pytesseract.image_to_string(image)

    match = re.search(r'(\d{8})\s*[*xX×]\s*(\d{8})', text)
    if not match:
        return JSONResponse(status_code=400, content={"error": "Could not extract a valid expression"})

    num1, num2 = match.groups()
    result = int(num1) * int(num2)

    return {"answer": result, "email": EMAIL}
