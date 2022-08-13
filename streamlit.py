import random as rnd
import pandas as pd
import streamlit as st
import datetime

st.title('4W Generater')

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

last_week = st.multiselect(
    'Last week 4w',
    name_list
)



def check_last_week():
    if last_week == None:
        return ['paul', 'sosiu', 'kay', 'wingc']
    else:
        return last_week

b = check_last_week()


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


gen_time = st.slider('How many time you want to generate?', 1, 10, 4)

result_4w_table = []

def gen_time_function(how_many_time):
    global result_4w_table
    for i in range(how_many_time):
        empty_list = [[]]
        result_4w_table += empty_list

d = st.date_input(
    "When's Staturday you want to start",
    datetime.date(2022, 8, 13)
)

one_week = datetime.timedelta(days=7)



def main_function():
    global result_4w_table
    gen_time_function(gen_time)

    result_4w_table[0] = generate_4w(b)


    for i in range(1,len(result_4w_table)):
        result_4w_table[i]= generate_4w(result_4w_table[i-1])

    index_week = []
    for i in range(len(result_4w_table)):
        index_week.append(d+one_week*i)

    df = pd.DataFrame(
        result_4w_table,
        index=index_week,
        columns=[1,2,3,4]
    )

    st.dataframe(df)

if st.button('GEN!!!!!'):
    main_function()