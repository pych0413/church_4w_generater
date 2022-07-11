import random as rnd


name_list = [
    'paul',
    'sosiu',
    'kay',
    'wingc',
    'zcy',
    'mark',
    'doris',
    'lkh',
    'ykh'
]


b = ['paul', 'sosiu', 'kay', 'wingc']


def generate_4w(a):
    last_week_list = []
    last_week_list += a
    this_week_list = []
    for i in range(len(last_week_list)):
        choose_name_list = []
        choose_name_list += name_list
        choose_name_list.remove(last_week_list[i])
        for j in range(len(this_week_list)):
            while this_week_list[j] in choose_name_list:
                choose_name_list.remove(this_week_list[j])
        if i == 1 or i == 2:
            while 'ykh' in choose_name_list:
                choose_name_list.remove('ykh')
        this_week_list.append(rnd.choice(choose_name_list))
    return this_week_list

gen_time = int(input())

result_4w_table = []

def gen_time_function(how_many_time):
    global result_4w_table
    for i in range(how_many_time):
        empty_list = [[]]
        result_4w_table += empty_list

gen_time_function(gen_time)

result_4w_table[0] = generate_4w(b)
print(result_4w_table[0])
for i in range(1,len(result_4w_table)):
    result_4w_table[i]= generate_4w(result_4w_table[i-1])
    print(result_4w_table[i])

# print(result_4w_table)
