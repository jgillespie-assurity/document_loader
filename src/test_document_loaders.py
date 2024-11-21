from langchain_community.document_loaders import (
    WebBaseLoader,
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    Docx2txtLoader,
    UnstructuredEPubLoader,
    UnstructuredMarkdownLoader,
    UnstructuredXMLLoader,
    UnstructuredRSTLoader,
    UnstructuredExcelLoader,
)

def web_loader():
    # document contains all text on page
    loader = WebBaseLoader('https://www.gutenberg.org/files/1727/1727-h/1727-h.htm')
    data = loader.load()

    print(data)

def pdf_loader():
    # documents separated by pages, images ignored
    loader = PyPDFLoader(file_path='./documents/somatosensory.pdf', extract_images=False)
    data = loader.load()

    print(data)

def csv_loader():
    # documents separated by rows
    loader = CSVLoader(file_path='./documents/country_full.csv')
    data = loader.load()

    print(data)

def rst_loader():
    # document separated by elements
    loader = UnstructuredRSTLoader(file_path='./documents/rst.rst', mode="elements")
    data = loader.load()

    print(data)

def xml_loader():
    # document contains just text within tags (tags stripped)
    loader = UnstructuredXMLLoader(file_path='./documents/cd_catalog.xml')
    data = loader.load()

    print(data)

def markdown_loader():
    # document contains just text (markdown stripped)
    loader = UnstructuredMarkdownLoader(file_path='./documents/README.md')
    data = loader.load()

    print(data)

def epub_loader():
    # document contains just text (images ignored)
    loader = UnstructuredEPubLoader(file_path='./documents/childrens-literature.epub')
    data = loader.load()

    print(data)

def doc_loader():
    # document contains all text, including text from tables (images ignored)
    loader = Docx2txtLoader(file_path='./documents/file-sample_1MB.docx')
    data = loader.load()

    print(data)

def excel_loader():
    # document contains all text row by row, cells separated by space
    loader = UnstructuredExcelLoader(file_path='./documents/file_example_XLSX_100.xlsx')
    data = loader.load()

    print(data)

def text_loader():
    # document contains all text
    loader = TextLoader(file_path='./documents/the-odyssey.txt')
    data = loader.load()

    print(data)

excel_loader()
