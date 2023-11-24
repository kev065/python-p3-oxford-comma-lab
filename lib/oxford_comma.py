def oxford_comma(items):
    if len(items) == 0: # Check if the list is empty
        return "" # If it is, return an empty string
    elif len(items) == 1: # Check if the list contains only 1 item
        return items[0] # If so, return the single item
    elif len(items) == 2: # Check if the list contains 2 items
        return f"{items[0]} and {items[1]}" # If it does, join the 2 items with the word "and" in between them
    else:
        oxford_str = ", ".join(items[:-1]) # If the list contains more than 2 items, join all the items except the last one with a comma and a space 
        return f"{oxford_str}, and {items[-1]}" # Then, add the last item to the string with the word "and" before it, and return the resulting string
