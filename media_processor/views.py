from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ExtractedText
from .serializers import ExtractedTextSerializer
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os


os.environ['TESSDATA_PREFIX'] = '/usr/local/share/tessdata'

class TextExtracter:
    def __init__(self, file, lang="eng+hin"):
        self.file = file
        self.lang = lang  

    def extract_text(self):
        if self.file.name.endswith('.pdf'):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                for chunk in self.file.chunks():
                    temp_pdf.write(chunk)
                temp_pdf.flush()
                images = convert_from_path(temp_pdf.name)
            
            extracted_text = ""
            for image in images:
                extracted_text += pytesseract.image_to_string(image, lang=self.lang)
            return extracted_text

        elif self.file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            extracted_text = pytesseract.image_to_string(Image.open(self.file), lang=self.lang)
            return extracted_text
        else:
            return None

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        extracted_text = TextExtracter(file).extract_text()
        if extracted_text is None or extracted_text.strip() == "":
            return Response({"error": "No text extracted, check the file quality or type."}, status=400)

        extracted_record = ExtractedText.objects.create(file_name=file.name, content=extracted_text)

        return Response({
            "message": "File processed successfully",
            "data": ExtractedTextSerializer(extracted_record).data
        })
