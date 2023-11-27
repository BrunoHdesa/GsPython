from datetime import datetime, timedelta

def criar_agenda_tomar_remedio():
    # Pede ao usuário para inserir o intervalo de doses e a quantidade de dias para tomar o remédio
    intervalo_doses = float(input("Digite o intervalo de doses em horas: "))
    total_dias = int(input("Digite a quantidade de dias que precisa tomar o remédio: "))

    # Horario agora
    agora = datetime.now()

    # Exibe a agenda com os horários no formato de 24 horas
    formato = "%H:%M"
    print("\nAgenda de administração do remédio:")
    for hora in range(24):
        horario = agora + timedelta(hours=hora * intervalo_doses)
        print(f" {horario.strftime(formato)} - Tomar o remédio")

    # Calcula e exibe o último dia para tomar o remédio
    ultimo_dia = agora + timedelta(days=total_dias - 1)
    print(f"\nÚltimo dia para tomar o remédio: {ultimo_dia.strftime('%Y-%m-%d')}")

#criar_agenda_tomar_remedio()

from datetime import datetime, timedelta

def somar_horarios():
    horario_atual = datetime.strptime(input("Digite um horário (HH:MM): "), "%H:%M")
    meia_noite = datetime.strptime("00:00", "%H:%M")
    tomar = int(input("Digite de quantas em quantas horas voce deve tomar o remedio: "))
    print("\nHorários para tomar o remédio:")

    while horario_atual < meia_noite + timedelta(days=1):
        print(horario_atual.strftime("%H:%M"))
        horario_atual += timedelta(hours=tomar)

# Exemplo de uso da função
somar_horarios()
