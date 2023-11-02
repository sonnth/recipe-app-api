def distinct_str(str_input):
    if not str_input:
        return ''
    output = []
    for char in str_input:
        if ' ' != char and char not in output:
            output.append(char)
    return ''.join(output)
