def read_and_print_context(file_path, position):
    try:
        # Read the entire content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Check if the position is valid
        if position < 0 or position >= len(text):
            print("Invalid position. Please enter a valid index.")
            return
        
        # Calculate the start and end indices for slicing
        start_index = max(0, position - 20)
        end_index = min(len(text), position + 21)  # Adding 1 to include the target character
        
        # Extract the context
        context = text[start_index:end_index]
        
        # Print the context
        print(f"Context around position {position}:\n")
        print(context)
    
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = './documents/the-odyssey.txt'
    
    try:
        # position = int(input("Enter the character position you want to see context for (0-indexed): "))
        position = 2288
        read_and_print_context(file_path, position)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the position.")