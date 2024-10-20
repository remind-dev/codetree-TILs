shift_right = 0
shift_left = 1

n, m ,q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

r, d = input().split()
r = int(r)

def shift(row, curr_dir):
    if curr_dir == shift_right:
        arr[row].insert(0, arr[row].pop())
    else:
        arr[row].insert(m-1, arr[row].pop(0))

def same(row1, row2):
    return any([arr[row1][col] == arr[row2][col] for col in range(m)])

def flip(curr_dir):
    return shift_right if curr_dir == shift_left else shift_left

def simulate(start_row, start_dir):
    shift(start_row, start_dir)

    start_dir = flip(start_dir)

    curr_dir = start_dir
    for row in range(start_row, 0, -1):
        if same(row, row-1):
            shift(row-1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break

    curr_dir = start_dir
    for row in range(start_row, n-1):
        if same(row, row+1):
            shift(row+1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break
                    
for _ in range(q):
    simulate(r-1, shift_right if d == 'L' else shift_left)

for row in range(n):
    for col in range(m):
        print(arr[row][col], end = " ")
    print()