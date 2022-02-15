from matplotlove import hearts


def main():
    while True:
        try:
            print('\n\nWelcome to matplotlove!! By chicolucio', end='\n\n')
            print('Press 2 for 2D or 3 for 3D')
            choice_2d_3d = input('Do you want a 2D or a 3D heart? ')
        except KeyboardInterrupt:
            print('\nNo more love :-(')
            break
        else:
            if choice_2d_3d == '2':
                options_2d = input('Choose a number between 1 and 4: ')
                if int(options_2d) in range(1, 5):
                    eval(f'hearts.Heart0{options_2d}().show()')
                    break
                else:
                    print('Invalid number', end='\n\n')
            elif choice_2d_3d == '3':
                options_3d = input('Choose a number between 1 and 2: ')
                if int(options_3d) in range(1, 3):
                    eval(f'hearts.Heart3d0{options_3d}().show()')
                    break
                else:
                    print('Invalid number', end='\n\n')
            else:
                print('Invalid answer', end='\n\n')


if __name__ == "__main__":
    main()
