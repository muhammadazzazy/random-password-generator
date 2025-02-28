from sys import exit
import random


def main() -> None:
    error_message: str = 'Please enter a correct value'
    exit_message: str = 'Bye!'
    lowercase_letters: str = ''
    for i in range(97, 123):
        lowercase_letters += chr(i)

    uppercase_letters: str = ''
    for i in range(65, 91):
        uppercase_letters += chr(i)

    special_characters: str = '!@#$%&*^|()_+'

    digits: str = ''
    for i in range(10):
        digits += str(i)
    while True:
        print('-- Password generator --')
        print('Choose option:')
        print('1: generate password')
        print('2: exit the program')
        try:
            user_input: str = input('Your choice: ')
            if user_input == '1':
                password_length: int = int(input('Provde password length: '))
                uppercase_choice: str = input(
                    'Use uppercase letters? (y/n): ').lower()
                digits_choice: str = input('Use digits? (y/n): ').lower()
                special_characters_choice: str = input(
                    'Use special characters? (y/n): ').lower()

                if all([uppercase_choice == 'n', digits_choice == 'n', special_characters_choice == 'n']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters, password_length))
                elif all([uppercase_choice == 'n', digits_choice == 'n', special_characters_choice == 'y']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters + special_characters, password_length))
                elif all([uppercase_choice == 'n', digits_choice == 'y', special_characters_choice == 'n']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters + digits, password_length))
                elif all([uppercase_choice == 'n', digits_choice == 'y', special_characters_choice == 'y']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters + digits + special_characters, password_length))
                elif all([uppercase_choice == 'y', digits_choice == 'n', special_characters_choice == 'n']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters + uppercase_letters, password_length))
                elif all([uppercase_choice == 'y', digits_choice == 'n', special_characters_choice == 'y']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters + uppercase_letters + special_characters, password_length))
                elif all([uppercase_choice == 'y', digits_choice == 'y', special_characters_choice == 'n']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters + uppercase_letters + digits, password_length))
                elif all([uppercase_choice == 'y', digits_choice == 'y', special_characters_choice == 'y']):
                    random_password: str = ''.join(random.sample(
                        lowercase_letters + uppercase_letters + digits + special_characters, password_length))
                else:
                    print(error_message)
                    continue
            elif user_input == '2':
                print(exit_message)
                exit()
            else:
                print(error_message)
        except ValueError:
            print(error_message)
        except KeyboardInterrupt:
            print(exit_message)
            exit()

        print(f'Generated password: {random_password}')


if __name__ == '__main__':
    main()
