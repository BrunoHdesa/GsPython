from datetime import datetime, timedelta

def exibir_horarios_ate_chegar():
    # Solicita ao usuário que digite um horário
    horario_str = input("Digite um horário no formato HH:mm:ss: ")

    try:
        # Converte a entrada do usuário para o formato de hora
        horario = datetime.strptime(horario_str, "%H:%M:%S")

        # Solicita ao usuário a quantidade de horas a subtrair
        horas_a_subtrair = int(input("Digite a quantidade de horas a subtrair: "))

        # Exibe todos os horários até chegar ao horário inicial
        for _ in range(horas_a_subtrair + 1):
            print(horario.strftime('%H:%M:%S'))
            horario -= timedelta(hours=1)

    except ValueError:
        print("Formato de horário inválido. Certifique-se de usar o formato HH:mm:ss.")

# Chama a função
exibir_horarios_ate_chegar()

