from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

text = """
def quicksort(arr):

    if len(arr) <= 1:
        return arr
    

    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

data = [3, 6, 8, 10, 1, 2, 1]
print("Sorted Array:", quicksort(data))
"""

splitter  = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 0
) 

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])