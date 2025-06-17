def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        a= float(a) 
        b= float(b)
        if operator == "+":
            return a+b
        elif operator== "-":
            return a-b
        elif operator == "/":
            if b==0:
                raise ZeroDivisionError
            return a/b
        elif operator =="*":
            return a*b
        elif operator =="**":
            return a**b
        elif operator== "%":

            if b==0:
                raise ZeroDivisionError
            return a%b
        else:
            raise ValueError("Unsupported opertor")
            
    

    except ZeroDivisionError :
        return f"ERROR : Division by zero"
    except ValueError as ve:
        return f"ERROR : {ve}"
    except TypeError:
        return "ERROR : invalid type error"
    except Exception as e:
        return f"Error : unexpected exception {e}"

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+")) # unexpected exception could not convert string to float: 'five'    this should return value error only not type error[if we convert the string to float it raises]
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"
