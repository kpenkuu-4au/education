team1 = 'Волшебники Данных'
team2 = 'Мастера кода'
team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
result1 = f'победа команды {team1}'
result2 = f'победа команды {team2}'
challenge_result = None
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = result1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = result2
tasks_total = score_1 + score_2
time_avg = (team1_time // score_1 + team2_time // score_2) // 2
print('В команде %s участников: %s!' % (team2, str(team1_num)))
print("Итого сегодня в командах участников: %s и %s!" % (str(team1_num), str(team2_num)))
print('{} решила задач - {}'.format(team1, str(score_1)))
print('{} решили задачи за {} c.'.format(team1, str(team1_time)))
print(f'Команды решили {score_1} и {score_2} задач.')
print('Результат битвы: {}!'.format(challenge_result))
print(f'Сегодня было решено {tasks_total} задач, в среднем по {format(time_avg, '.1f')} секунды на задачу!')
