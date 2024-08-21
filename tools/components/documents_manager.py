from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List
from dotenv import load_dotenv, find_dotenv
from tools.components.base import Component, Canvas
import streamlit as st
import uuid
import tempfile
import os


load_dotenv(find_dotenv())


class DocumentProcessor(Component):
    def __init__(self, canvas: Canvas):
        super().__init__(canvas)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
        )
        self.uploaded_files = None
        self._reset_button = None
    
    def run(self):
        """
        Main function to run the document processor.
        """
        self.get_element('instructions').write(f"Upload PDFs to generate probe questions")
        self.uploaded_files = self.get_element('canvas').file_uploader(
            'Choose a PDF',
            type = 'pdf',
            accept_multiple_files=True
        )
        
        if self.uploaded_files:
            self.get_element('instructions').write('Press `Done` to complete')
    
    def ingest_documents(self) -> List[Document]:
        """
        Writes streamlit objects and returns a list of documents. Renders a file uploader to upload PDFs by converting them to temporary files.
        """
        pages = []
        if self.uploaded_files: 
            self.get_element('status').text("Uploading...")
            for file in self.uploaded_files:
                # Generate unique hex
                unique_id = uuid.uuid4().hex
                
                # Append UID to original file name, preserving extension
                original_name, file_extension = os.path.splitext(file.name)
                temp_file_name = f"{original_name}_{unique_id}{file_extension}"
                temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)
                
                # Write uploaded PDF to temp file with modified name
                with open(temp_file_path, 'wb') as f:
                    f.write(file.getvalue())
                
                # Load PDF and extract pages using PyPDFLoader
                loader = PyPDFLoader(temp_file_path)
                pages = loader.load_and_split(self.text_splitter)
                
                # Delete Temp file after
                os.unlink(temp_file_path)
            
            # Update status
            self.get_element('status').text(f"Successfully loaded {len(pages)} pages from {len(self.uploaded_files)} PDFs.")
            self.get_element('instructions').write('Press `Done` to complete')
        return pages
