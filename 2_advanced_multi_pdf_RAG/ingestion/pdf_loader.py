import os
from pypdf import PdfReader

def load_documents(data_folder):

    documents = []

    for pdf_file in os.listdir(data_folder):
        pdf_path = os.path.join(data_folder,pdf_file)
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages):
            documents.append({
                "source": pdf_file,
                "page": page_num + 1,
                "text": page.extract_text()
            })

    return documents