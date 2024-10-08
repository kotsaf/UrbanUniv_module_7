team1_name = 'Повелители Питона'
team2_name = 'Укротители байтов'
team1_num = 7
team2_num = 8
score_1 = 39
score_2 = 42
team1_time = 3026.05
team2_time = 3026.06

tasks_total = score_1 + score_2

time_avg1 = round((team1_time / score_1), 2)
time_avg2 = round((team2_time / score_2), 2)
time_avg = round((team1_time + team2_time) / tasks_total, 4)

if time_avg1 > time_avg2:
    challenge_result = 'победа команды Повелители Питона!'
elif time_avg1 < time_avg2:
    challenge_result = 'победа команды Укротители байтов!'
else:
    challenge_result = 'ничья!'


print("В команде %(team1_name)s участников: %(team1_num)s!" % {'team1_name': team1_name, 'team1_num': team1_num})
print("В команде %(team2_name)s участников: %(team2_num)s!" % {'team2_name': team2_name, 'team2_num': team2_num})
print("Итого сегодня в командах участников: "
      "%(team1_num)s и %(team2_num)s!" % {'team1_num': team1_num, 'team2_num': team2_num})

print('Команда {team1_name} решила задач: {score_1}!'.format(team1_name = team1_name, score_1 = score_1))
print('Команда {team2_name} решила задач: {score_2}!'.format(team2_name = team2_name, score_2 = score_2))
print(f'{team1_name} решили задачи за {team1_time}с !'.format(team1_name = team1_name, team2_time = team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')



