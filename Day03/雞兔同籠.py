def getchickenAndRabbit(sum, feet):
    '''

    :param sum: 83
    :param feet: 240
    :return:
    '''
    if feet/4 <= sum <= feet/2:
        rabbit = (feet - sum * 2) / 2
        chicken = sum - rabbit
        return chicken, rabbit
    else:
        print("無法計算")
        return 0, 0


print(getchickenAndRabbit(83, 240))
c, r = getchickenAndRabbit(180, 240)
print(c, r)

