import sys
from info import get_user_info, print_events

if len(sys.argv) != 2:
    print('''usage:
    events <github username>''')
    sys.exit()

user_name = sys.argv[1]
user_data = get_user_info(user_name)

print_events(user_data , user_name)



