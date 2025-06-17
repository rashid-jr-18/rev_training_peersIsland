def process_data(data, index):
    """
    Processes data with error handling.
    
    :param data: List of numbers (strings that should be converted to int)
    :param index: Index to divide with
    :return: Processed result or error message
    """
    try:
        numbers = []                 

        for item in data:            
                
          numbers.append(int(item))   


        
        divisor = numbers[index]

        
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        result=[]
        for i in data :
            value=int(i)/divisor
            result.append(value)
        return result

            


    except ZeroDivisionError:
        return "ERROR: Division by zero"
    except ValueError:
        return "ERROR: Invalid value in data - cannot convert to integer"
    except IndexError:
        return "ERROR: Index out of range"
    except Exception as e:
        return f"ERROR: Unexpected exception - {e}"
    

print(process_data(["10", "20", "0", "40"], 2))       # ➤ ERROR: Division by zero
print(process_data(["10", "abc", "30"], 1))           # ➤ ERROR: Invalid value in data - cannot convert to integer
print(process_data(["10", "20"], 5))                  # ➤ ERROR: Index out of range
print(process_data(["100", "200", "300"], 1))         # ➤ [0.5, 1.0, 1.5]

