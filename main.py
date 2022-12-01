N = int(input("Enter num of commands: "))
List = list()

for i in range(N):
    cmd = input("Enter command: ").split()

    if cmd[0] == 'insert':
        List.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print(List)
    elif cmd[0] == 'remove':
        List.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        List.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        List.sort()
    elif cmd[0] == 'pop':
        List.pop()
    elif cmd[0] == 'reverse':
        List.reverse()

    #1insert i e: Insert integer  at position .
    #2print: Print the list.
    #3remove e: Delete the first occurrence of integer .
    #4append e: Insert integer  at the end of the list.
    #5sort: Sort the list.
    #6pop: Pop the last element from the list.
    #7everse: Reverse the list.