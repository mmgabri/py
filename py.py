def process_string(input_string, filename):
    # Localiza o índice do primeiro espaço em branco
    space_index = input_string.find(' ')
    
    if space_index != -1:
        # Se encontrar um espaço, grava a string até o primeiro espaço no arquivo
        with open(filename, 'w') as file:
            file.write(input_string[:space_index])
        print(f"Texto gravado no arquivo {filename}.")
    else:
        print("Nenhum espaço em branco encontrado na string.")

# Exemplo de uso
input_string = "Este é um exemplo de string."
filename = "output.txt"
process_string(input_string, filename)
