# Loader not required here as we already read the text within the PDF_utils
# Might want to add loaders if want to get rid of that specific service
from langchain_text_splitters import RecursiveCharacterTextSplitter

def text_splitter(text: str )->list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)
    return chunks