horas_trabalhadas = int(input('Insira a quantidade de horas trabalhadas na semana: '))
valor_hora_trabalhada = int(input('Insira o valor da hora trabalhada: '))
if(horas_trabalhadas < 40):
  salario_semanal = horas_trabalhadas*valor_hora_trabalhada
if(horas_trabalhadas > 40 and horas_trabalhadas < 60):
  salario_semanal = horas_trabalhadas*valor_hora_trabalhada + (horas_trabalhadas-40)*0.5*valor_hora_trabalhada
if(horas_trabalhadas > 60):
  salario_semanal = horas_trabalhadas*valor_hora_trabalhada + (horas_trabalhadas-60)*2*valor_hora_trabalhada
print(f'O salário semanal foi: {salario_semanal} reais')