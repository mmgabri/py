def process_string(input_string, filename):
    # Divide a string em partes usando espaços em branco como delimitadores
    parts = input_string.split(' ')
    
    with open(filename, 'w') as file:
        # Percorre cada parte e grava no arquivo
        for part in parts:
            if part:  # Verifica se a parte não está vazia
                file.write(part + '\n')  # Adiciona uma nova linha após cada parte
    
    print(f"Texto gravado no arquivo {filename}.")

# Exemplo de uso
input_string = "Este é um exemplo de string que será gravada."
filename = "output.txt"
process_string(input_string, filename)
