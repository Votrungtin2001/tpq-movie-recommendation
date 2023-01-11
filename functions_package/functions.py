import pandas

def get_suggestions():
    data = pandas.read_csv('datasets/main_data.csv')
    return list(data['movie_title'].str.capitalize())

# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')
    my_list[-1] = my_list[-1].replace('"]','')
    return my_list