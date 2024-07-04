"""
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

from __future__ import annotations

## chat<rag>, image/video(ocr, vqa, labeling), audio workflows



* need for particular return types from llm responses e.g. prompt > response.attribute_1, .... response.attribute_n > artifacts(images,audio/video) 
	* return formats can be passed to llms at prompt time.

* need for workflows/pipelines for generation of different responses to various tasks. Done to improve granularity. workflows can also be passed at prompt time. (These can be thought of as steps/guidelines to produce very detailed and accurate responses).
		* create base workflows for image/text/audio/video data labeling. 
		* task specific workflows (prompting(cot, ICL) templates maybe) e.g. architectural/interior/exterior design. (problem > constraints > best practices/existing solutions > solution)

* create a document type to represent an input doc/file e.g.
	"""
	@dataclass
	class Document(metaclass=_BackwardCompatible):
		""
		Base data class containing some data to be queried.

		Can contain text snippets, tables, and file paths to images or audios. Documents can be sorted by score and saved
		to/from dictionary and JSON.

		:param id: Unique identifier for the document. When not set, it's generated based on the Document fields' values.
		:param content: Text of the document, if the document contains text.
		:param dataframe: Pandas dataframe with the document's content, if the document contains tabular data.
		:param blob: Binary data associated with the document, if the document has any binary data associated with it.
		:param meta: Additional custom metadata for the document. Must be JSON-serializable.
		:param score: Score of the document. Used for ranking, usually assigned by retrievers.
		:param embedding: dense vector representation of the document.
		:param sparse_embedding: sparse vector representation of the document.
		

		id: str = field(default="")
		content: Optional[str] = field(default=None)
		dataframe: Optional[DataFrame] = field(default=None) ## support diff files instead of only dataframe
		#blob: Optional[ByteStream] = field(default=None)
		meta: Dict[str, Any] = field(default_factory=dict)
		score: Optional[float] = field(default=None)
		embedding: Optional[List[float]] = field(default=None) # np.array
		sparse_embedding: Optional[SparseEmbedding] = field(default=None)
	"""
	"""
	@dataclass
	class GeneratedAnswer:
    data: str
    query: str
    documents: List[Document]
    meta: Dict[str, Any] = field(default_factory=dict)
	"""

# self improving lm pipelines. reliable lm systems. stacking instead of isolation