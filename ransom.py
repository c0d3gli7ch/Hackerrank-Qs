import re
import snoop
# @snoop
def ransom(note: str, mag: str) -> bool:
    ransom_counter = [0] * 26
    magazine_counter = [0] * 26
    
    for c in note:
        ransom_counter[ord(c) - ord('a')] += 1
    print(ransom_counter)
    for c in mag:
        magazine_counter[ord(c) - ord('a')] += 1
        
    for alphabet in range(26):
        if magazine_counter[alphabet] < ransom_counter[alphabet]:
            return False
    
    return True



ransom('ihgg','ch')
