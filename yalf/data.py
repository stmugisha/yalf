"""
Yalf data utils.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
## Load & parse pdf, .doc, .txt, .xlsx
## 1. Q&A workflow: pass the extracted data to llm(embed)
## -> get_vector_emneds -> for Q&A
#  opendevin style doc summarize, cite sources

# a class method to create a Car object by name.
# @classmethod
#	def checkBike(cls, name):
#	    if(name=="Bike"):
#		    return cls(name, 2)

## 2. Data annotation workflow
# data labeling (with paligemma models)
#
from __future__ import annotations

import os
from pypdf import PdfReader


class DataLoader:
	"""Abstract DataLoader class."""

	def __init__(self, dataset: os.PathLike):
		self.dataset = dataset

	def read_dataset(self):
		"""Read dataset from file."""
		pass

	@staticmethod
	def read_file(self, file):
		"""Checks file type and Reads it into memory.

		Args:
			file: dir/url to the the file to read.

		Returns:
			File content dictionary.
			Single page as key for text files and individual page numbers
			as keys for multi page pdf documents.
		"""
		# check mime type then use respective reader
		file_ext = file.rpartition(".")[-1]
		if file_ext == "txt":
			text = {}
			content = open(file, "r").read()
			text[0] = content
			return text

		elif file_ext == "pdf":
			text = {}
			content = PdfReader(file)
			for page in range(len(content.pages)):
				page_content = content.pages[page]
				text[page] = page_content.extract_text()

			return text

		elif file_ext in set(("doc", "docx")):
			text = {}

	@staticmethod
	def pdf_to_json(pdf_file):
		"""Read pdf file and parse to json format."""
		pass

	## load->chunk, Embed, Index<embeddings> <for eff. retrieval>
