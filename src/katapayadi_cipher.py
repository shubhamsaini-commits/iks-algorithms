def decode_katapayadi(word: str, reverse_output: bool = True) -> int:
    """
    Decodes a transliterated Sanskrit word into an integer using the Katapayadi cipher.
    
    Args:
        word (str): The hyphen-separated syllables of the word (e.g., "pa-ra-ma").
        reverse_output (bool): Historically, Katapayadi numbers are read right-to-left.
                               Defaults to True to respect the historical algorithmic rule.
                               
    Returns:
        int: The decoded numerical value.
    """
    
    # 1. The Historical Hash Map
    # K-group (1-9), T-group (1-9), P-group (1-5), Y-group (1-8)
    # Note: Simplified for basic IAST transliteration syllables
    katapayadi_map = {
        'ka': '1', 'ta': '1', 'pa': '1', 'ya': '1',
        'kha': '2', 'tha': '2', 'pha': '2', 'ra': '2',
        'ga': '3', 'da': '3', 'ba': '3', 'la': '3',
        'gha': '4', 'dha': '4', 'bha': '4', 'va': '4',
        'nga': '5', 'na': '5', 'ma': '5', 'sa': '5',  # 'sa' as in palatal sh
        'cha': '6', 'ta_': '6', 'sha': '6',           # 'ta_' for retroflex
        'chha': '7', 'tha_': '7', 'sa_': '7',         # 'sa_' for dental s
        'ja': '8', 'da_': '8', 'ha': '8',
        'jha': '9', 'dha_': '9',
        'nya': '0', 'na_': '0'                        # 'na_' for retroflex n
    }
    
    # 2. Input Sanitization
    word = word.lower().strip()
    syllables = word.split('-')
    
    decoded_str = ""
    
    # 3. $O(N)$ Parsing and Hash Map Lookup
    for syllable in syllables:
        if syllable in katapayadi_map:
            decoded_str += katapayadi_map[syllable]
        else:
            # If a syllable isn't found, we can either ignore it (vowels/spaces) 
            # or handle it based on strict Sanskrit grammar rules.
            pass
            
    # If the string is empty (no valid consonants found), return 0
    if not decoded_str:
        return 0
        
    # 4. Historical Right-to-Left Reversal
    if reverse_output:
        decoded_str = decoded_str[::-1]
        
    return int(decoded_str)


# ==========================================
# Testing the Implementation
# ==========================================
if __name__ == "__main__":
    # Test Case 1: The famous encoding of Pi (to 31 decimal places) starts with "go-pi-bha-gya"
    # Note: Complex conjuncts (like 'gya') usually take the value of the last consonant.
    # For this prototype, we'll test simple syllables.
    
    test_word = "pa-ra-ma" 
    # pa = 1, ra = 2, ma = 5
    # Forward: 125 -> Reversed (Historical): 521
    
    print("--- Katapayadi Decoder ---")
    
    historical_value = decode_katapayadi(test_word)
    modern_value = decode_katapayadi(test_word, reverse_output=False)
    
    print(f"Input Word: {test_word}")
    print(f"Direct Decoding (Left-to-Right): {modern_value}")
    print(f"Historical Decoding (Right-to-Left): {historical_value}")