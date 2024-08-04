def get_glb_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except PermissionError:
        print(f"Error: You don't have permission to read '{file_path}'.")
        return None
    except IOError as e:
        print(f"Error reading '{file_path}': {e}")
        return None
