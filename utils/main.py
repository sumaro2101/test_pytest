from functions import open_json, sorting_by_executed, sorting_by_string, output_trans

json_load = open_json()
sort_ex = sorting_by_executed(json_load)
sort_five = sorting_by_string(sort_ex)
out_trans = output_trans(sort_five)

for i in out_trans:
    print(i)
