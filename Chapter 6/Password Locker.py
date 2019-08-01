#! python3
import sys,pyperclip

if len(sys.argv) < 2:
    print("Please provide account name")
    sys.exit()


account = sys.argv[1]

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
 'luggage': '12345'}

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for "+account+" copied on clipboard")
else:
    print("There is no account named "+ account)



