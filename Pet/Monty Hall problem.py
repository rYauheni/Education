print('\n' + 'Настоящий продукт позволяет виртуально-эмпирически доказать (или опровергнуть) парадокс Монти Холла'
      + '\n' + 'на основе закона больших чисел.' + '\n')
import random

attemp = 4
iteration = int(input('Укажите количество испытаний (должно быть не меньше 10000): '))
print()
while iteration < 10000:
    attemp -= 1
    if attemp % 10 == 1 and attemp % 100 != 11:
        word1 = 'ка'
    elif attemp % 10 == 2 and attemp % 100 != 12 \
            or attemp % 10 == 3 and attemp % 100 != 13 \
            or attemp % 10 == 4 and attemp % 100 != 14:
        word1 = 'ки'
    else:
        word1 = 'ок'
    if attemp > 1:
        print('Тебе же сказали, что количество испытаний должно составлять по меньшей мере 10000.'
              + '\n' + 'У нас тут вообще-то закон БОЛЬШИХ ЧИСЕЛ.' +
              '\n' + 'А у тебя осталась ' + str(attemp) + ' попыт' + word1 + '.')
        iteration = int(input('Попробуй ещё раз: '))
        print()
    elif attemp == 1:
        print('Я начинаю сомневаться в тових когнитивных способностях.'
              + '\n' + 'У тебя осталась ' + str(attemp) + ' попыт' + word1 + '.'
              + '\n' + 'И поверь мне, она будет последней.')
        iteration = int(input('Хорошо подумай, так сколько будет испытаний: '))
        print()
    else:
        break
if attemp >= 1:
    winChange = 0
    winNochange = 0
    result = ''
    observationalError = float(input('Необходимо указать степень сомнения в точности измерений - погрешность.'
                                     + '\n' + 'Рекомнедуемое значение погрешности от 0.0 до 2.0'
                                     + '\n' + 'Значение погрешности: '))
    print()
    for i in range(iteration):
        firstChoice = random.randint(1, 3)
        prize = random.randint(1, 3)
        if firstChoice == 1:
            if prize == 1:
                winNochange += 1
            elif prize == 2 or prize == 3:
                winChange += 1
        if firstChoice == 2:
            if prize == 2:
                winNochange += 1
            elif prize == 1 or prize == 3:
                winChange += 1
        if firstChoice == 3:
            if prize == 3:
                winNochange += 1
            elif prize == 1 or prize == 2:
                winChange += 1
    winRateChange = round((winChange / iteration * 100), 2)
    winRateNoChange = round((winNochange / iteration * 100), 2)
    if iteration % 10 == 1 and iteration % 100 != 11:
        word2 = 'я'
    else:
        word2 = 'й'
    print('Общее колиечстов испытаний: ' + str(iteration)
          + '\n' + 'Процент побед в случае изменения первоначального выбора: ' + str(winRateChange) + '.'
          + '\n' + 'Процент побед в случае сохранения первоначального выбора: ' + str(winRateNoChange) + '.')
    print()
    if winRateChange - observationalError <= 66.66 <= winRateChange + observationalError:
        result = 'CONFIRMED'
        print(f'Результат испытаний парадокса Монти Холла: {result}')
        print()
        print(f'Мы рады, что Вы были с нами на протяжении {iteration} испытани{word2}.')
    else:
        result = 'BUSTED'
        print(f'Результат испытаний парадокса Монти Холла: {result}')
        print()
        curiosity = input('Вы желаете узнать возможные причины опровержения парадокса?'
                          + '\n' + 'Укажите Y, если желаете, либо N, если Вам это не интересено: ').lower()
        print()
        if curiosity == 'n':
            print('Ную что ж...'
                  + '\n' + f'Мы в любом случае рады, что Вы были с нами на протяжении {iteration} испытани{word2}')
        elif curiosity == 'y':
            print('Возможные причины опровержения парадокса:'
                  + '\n' + '\t' + '1. Пиздит математика.'
                  + '\n' + '\t' + '2. Пиздит рандомизатор Python.'
                  + '\n' + '\t' + '3. Пиздит теория вероятностей (закон больших чисел).'
                  + '\n' + '\t' + '4. Вы избрали чрезмерно низкую степень сомнения в нашем продукте.'
                  + '\n' + '\t' + 'Нам, конечно, приятно, но попробуйте ещё раз пройти испытания'
                  + ' с указанием значения погрешности в диапазое от 1.0 до 2.0.')
            print()
            print(f'Что бы ни являлось причиной провала, мы в любом случае рады, что Вы были с нами '
                  f'на протяжении {iteration} испытани{word2}.')
else:
    print('Едрить ты бестолочь, конечно.')