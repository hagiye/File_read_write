def read_and_modify_file():
    """
    Read a file, modify its content, and write to a new file with error handling.
    """
    try:
        # Get filename from user
        filename = input("Enter the filename to read: ")
        
        # Read the original file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print(f"Successfully read from '{filename}'")
        
        # Modify the content (you can customize this part)
        modified_content = modify_content(content)
        
        # Get output filename
        output_filename = get_output_filename(filename)
        
        # Write modified content to new file
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"Successfully wrote modified content to '{output_filename}'")
        print(f"Original file size: {len(content)} characters")
        print(f"Modified file size: {len(modified_content)} characters")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please check the filename and try again.")
    
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        print("You may not have the necessary permissions to access this file.")
    
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{filename}'.")
        print("The file may be in a different encoding or binary format.")
    
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again with a different file.")

def modify_content(content):
    """
    Modify the file content according to specific rules.
    Customize this function based on your needs.
    """
    # Example modifications:
    # 1. Convert to uppercase
    # 2. Add line numbers
    # 3. Remove extra whitespace
    
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        # Remove leading/trailing whitespace
        clean_line = line.strip()
        
        # Skip empty lines
        if not clean_line:
            continue
            
        # Add line number and convert to uppercase
        modified_line = f"{i}: {clean_line.upper()}"
        modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

def get_output_filename(original_filename):
    """
    Generate a modified output filename.
    """
    if '.' in original_filename:
        name, ext = original_filename.rsplit('.', 1)
        return f"{name}_modified.{ext}"
    else:
        return f"{original_filename}_modified"

def alternative_modification(content):
    """
    Alternative modification function - you can choose which one to use.
    This one reverses each line.
    """
    lines = content.split('\n')
    modified_lines = []
    
    for line in lines:
        if line.strip():  # Only process non-empty lines
            modified_line = line[::-1]  # Reverse the line
            modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

# Main program with menu
def main():
    print("📝 File Modification Program")
    print("=" * 40)
    
    while True:
        try:
            read_and_modify_file()
            
            # Ask if user wants to process another file
            another = input("\nDo you want to process another file? (yes/no): ").lower()
            if another not in ['yes', 'y', '']:
                print("Thank you for using the program! 👋")
                break
            print()
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye! 👋")
            break
        except Exception as e:
            print(f"Unexpected error in main program: {e}")
            break

# Run the program
if __name__ == "__main__":
    main()