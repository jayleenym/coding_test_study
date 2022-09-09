from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    match = 0
    
    for vals in zip(*strs):
        if len(set(vals)) == 1:
            match += 1
        else:
            break
    
    return strs[0][:match]

