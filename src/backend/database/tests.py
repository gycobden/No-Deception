import chroma
from chroma import add_document, MetadataDict, get_document_by_id, find_and_print_similar_documents
from chromadb import Client, Collection
import pprint  # for pretty printing

# add test documents to chroma
add_document(
    "compsci.pdf",
    MetadataDict(
        id="123",
        embedding=[0.1, 0.2, 0.3],
        text_chunk="i really like computer science",
        source_title="computer science",
        source_author="evan mao"
    ).to_dict()
)

add_document(
    "math.txt",
    MetadataDict(
        id="456",
        embedding=[0.1, 0.4, 0.3],
        text_chunk="mathematics is fun",
        source_title="theory of mathematics",
        source_author="john lennon"
    ).to_dict()
)

add_document(
    "idk.pdf",
    MetadataDict(
        id="789",
        embedding=[9.8, 7.6, 5.4],
        text_chunk="life is all about tests, tests, and more tests",
        source_title="life is a test",
        source_author="aobert einterstein"
    ).to_dict()
)

add_document(
    "evilcompsci.txt",
    MetadataDict(
        id="111",
        embedding=[0.1, -0.2, 0.3],
        text_chunk="i hate computer science it is the worst subject ever",
        source_title="why i switched to informatics",
        source_author="bill gates"
    ).to_dict()
)

add_document(
    "nodeceptionm.pdf",
    MetadataDict(
        id="7777",
        embedding=[0.6, 0.2, 0.0],
        text_chunk="this project is pretty fun i think that the team is doing a great job",
        source_title="no deception evaluation",
        source_author="evan mao the GOAT"
    ).to_dict()
)

# get test document from chroma
print("\nDocument ID with ID 123 is: ")
pprint.pprint(get_document_by_id("123"))

# find and print similar documents of compsci.pdf
print("\nDocuments similar to compsci.pdf are: ")
results = find_and_print_similar_documents([0.1, 0.2, 0.3], n_results=3)

# find and print similar documents of the embedding vector [0.56, 0.25, -0.3]
print("\nDocuments similar to [0.56, 0.25, -0.3] are: ")
results = find_and_print_similar_documents([0.56, 0.25, -0.3], n_results=3)
