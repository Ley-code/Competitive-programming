if __name__ == '__main__':
    N = int(input())
    final_list = []
    commands = []
    for i in range(N):
        commands.append(input().split())
        if commands[i][0]== "insert":
            final_list.insert(int(commands[i][1]),int(commands[i][2]))
        elif commands[i][0] == "print":
            print(final_list)
        elif commands[i][0] == "remove":
            final_list.remove(int(commands[i][1]))
        elif commands[i][0] == "append":
            final_list.append(int(commands[i][1]))
        elif commands[i][0] == "sort":
            final_list.sort()
        elif commands[i][0] == "pop":
            final_list.pop()
        elif commands[i][0] == "reverse":
            final_list.reverse()