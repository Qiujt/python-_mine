
def push_it():
    print(push_it())

def pop_it():
    print(pop_it())

def view_it():
    print(view_it())

def show_menu():
    prompt='''(0) push it
(1) pop it
(2) view it 
(3) exit
Please input your choice(0/1/2/3):'''
    while  True:
        choice=input(prompt).strip()[0]
        if  prompt not  in  '0123':
            print('Invalid  input,Try again.')
            continue

        if choice=='3':
            break
        if choice=='0':
            push_it()
        elif choice=='1':
            pop_it()
        else:
            view_it()

if __name__ == '__main__':
    show_menu()