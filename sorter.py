def sort(width, height, length, mass):
    
    '''
    This function sorts the package into the appropriate stack based on its dimensions and weight.
    It returns "STANDARD", "SPECIAL", or "REJECTED" based on the package's characteristics.
    Inputs:
        width (int, float, str): The width of the package in cm
        height (int, float, str): The height of the package in cm
        length (int, float, str): The length of the package in cm
        mass (int, float, str): The mass of the package in kg
    Returns:
        str: "STANDARD", "SPECIAL", or "REJECTED"
    Raises:
        ValueError: If any of the inputs are invalid or out of range
    '''
    try:
        # Function to check and convert numeric values
        def validate_numeric(value, param_name):
            if isinstance(value, (int, float)):
                if isinstance(value, int):
                    value = float(value)
            else:
                try:
                    '''Try to convert string to float'''
                    value = float(value)
                except (ValueError, TypeError):
                    raise ValueError(f"Invalid {param_name}: must be a valid number")
            
            '''Check for negative or zero values'''
            if value <= 0:
                raise ValueError(f"Invalid {param_name}: must be greater than zero")
                
            return value
        
        '''Validate and convert all inputs'''
        width = validate_numeric(width, "width")
        height = validate_numeric(height, "height")
        length = validate_numeric(length, "length")
        mass = validate_numeric(mass, "mass")
        
        '''Calculate Volume'''
        volume = width * height * length
        
        '''Check if package is bulky'''
        is_bulky = False
        if volume >= 1000000:  # volume in cm3
            is_bulky = True
        if width >= 150 or height >= 150 or length >= 150:  # dimensions in cm
            is_bulky = True
        
        '''Check if package is heavy'''
        is_heavy = False
        if mass >= 20:  # mass in kg
            is_heavy = True
        
        '''Assign Values'''
        if is_bulky and is_heavy:
            return "REJECTED"
        if is_bulky or is_heavy:
            return "SPECIAL"
        
        return "STANDARD"
        
    except ValueError as e:
        raise e
    except Exception as e:
        raise Exception("An unexpected error occurred while processing the package")
    
# # Sample Tests :
# print(sort(100, 100, 100, 10))    # integers
# print(sort(100.5, 100.5, 100.5, 10.5))  # floats
# print(sort("100", "100", "100", "10"))  # numeric strings

# # Invalid inputs that will raise errors:
# print(sort("abc", 100, 100, 10))
# print(sort(-100, 100, 100, 10))
# print(sort(0, 100, 100, 10))
# print(sort(None, 100, 100, 10))
# print(sort([], 100, 100, 10))
