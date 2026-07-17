def generate_pingala_combinations(n: int, current_meter: str = "", results: list = None) -> list:
    """
    Recursively generates all Pingala binary combinations (Laghu/Guru) for a given length 'n'.
    Laghu = '0', Guru = '1'.
    """
    if results is None:
        results = []
        
    # Base Case: When the meter reaches the required length, add it to results
    if len(current_meter) == n:
        results.append(current_meter)
        return results
        
    # Recursive Step 1: Add a Laghu (0)
    generate_pingala_combinations(n, current_meter + "0", results)
    
    # Recursive Step 2: Add a Guru (1)
    generate_pingala_combinations(n, current_meter + "1", results)
    
    return results

print(generate_pingala_combinations(3))