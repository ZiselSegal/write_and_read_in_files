#1
def print_file_contents(file_name):
    with open('example.txt','r') as f:
        print(f.read())
# print_file_contents('example.txt')

#2
def write_to_new_file(file_name,str_to_write):
    with open(file_name,'w') as f:
        f.write(str_to_write)
# write_to_new_file('test.txt','hello world')

#3
def copy_file_content(file_name1,file_name2):
    with open(file_name1,'r') as f1:
        reader = f1.read()
    with open(file_name2,'w') as f2:
        f2.write(reader)
# copy_file_content('example.txt','test.txt')

#4
def get_file_lines_amount(file_name):
    with open(file_name,'r') as f:
        counter = 0
        for line in f:
            counter += 1
        return counter
# print(get_file_lines_amount('example.txt'))

#5
def get_amount_matching_words(file_name,word_to_check):
    with open(file_name,'r') as f:
        word_lst = (f.read().split())
        print(word_lst)
        counter = 0
        for word in word_lst:
            if word_to_check in word:
                counter += 1
        return counter
# print(get_amount_matching_words('test.py','hello'))

#6
#check question 3

#7
def swap_file_string(file_name,string_to_swap,string_to_insert):
    with open(file_name,'r') as f1:
        reader = f1.read()
        final = reader.replace(string_to_swap,string_to_insert)
    with open(file_name,'w') as f2:
        f2.seek(0)
        f2.write(final)
# swap_file_string('example.txt','hello world','zisel')

#8
def write_new_lines(file_name,str_lst):
    with open(file_name,'a') as f:
        for str in str_lst:
            f.writelines(str + '\n')
# write_new_lines('test.txt',['a','b','c'])

#9
def get_funcs_amount(file_name):
    with open(file_name,'r') as f:
        counter = 0
        for line in f:
            if line.startswith('def'):
                counter += 1
        print(f'amount of functions in file {counter}')
# get_funcs_amount('work.py')

#10
def copy_files_to_file(file_name,files_list):
    combined_files = []
    for file in files_list:
        with open(file,'r') as f:
            combined_files.append(f.read())
    with open(file_name,'w') as f:
        for file in combined_files:
            f.write(file + '\n')
# copy_files_to_file('test2.txt',['test.txt','example.txt'])
