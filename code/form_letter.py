def print_form_letter(name,date,hour):
    print('Dear',name+',')
    print()
    print('Congratulations you have been invited to a job interview on',date,'at',hour,'pm')
    print('Hope to see you there!')
    print()
    print('Sincerely,')
    print('The Management')
    print('-'*40)

hour = 1
print_form_letter('Nan Wang','7/1/23',hour)
print_form_letter('Zheng Zheng','7/1/23',hour+1)
print_form_letter('Karen Mai','7/1/23',hour+2)