dict_semina = {
    'Algorithm' : '204',
    'DataAnalysis' : '207',
    'ArtificialIntelligence' : '302',
    'CyberSecurity' : 'B101',
    'Network' : '303',
    'Startup' : '501',
    'TestStrategy' : '105'}

n = int(input())

for i in range(n):
    input_str = input()
    if input_str in dict_semina:
        print(dict_semina[input_str])
