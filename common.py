def read_input(input):

    lines = []

    try:
        with open(input, 'r', encoding='utf-8') as f:
            lines = f.readlines()

    except FileNotFoundError:
        print(f"'{input}': file not found.")
        return None
    except Exception as e:
        print(f"cause: {e}")
        return None

    return lines