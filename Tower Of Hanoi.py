class Stack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top =-1
        self.array = [0]*capacity

    def createstack(capacity):
        stack = stack(capacity)
        return stack

def push(stack, disk):
        if stack[1] != stack[0] - 1:
            stack[1] += 1
            stack[2][stack[1]] = disk

def pop(stack):
        if stack[1] == -1:
            return None
        disk = stack[2][stack[1]]
        stack[2][stack[1]] = 0
        stack[1] -= 1
        return disk

def move_disks(n, source, dest, aux):
    total_moves = 2**n - 1
    poles = [source, dest, aux]

    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            src, dst = source, dest
        elif move % 3 == 2:
            src, dst = source, aux
        else:
            src, dst = aux, dest
        
        if src[1] == -1:
            push(src, pop(dst))
        elif dst[1] == -1:
            push(dst, pop(src))
        else:
            src_top = pop(src)
            dst_top = pop(dst)
            
            if src_top > dst_top:
                push(src, src_top)
                push(src, dst_top)
            else:
                push(dst, dst_top)
                push(dst, src_top)

        print(f"Move {move}:")
        print(f"Source: {source}")
        print(f"Aux: {aux}")
        print(f"Dest: {dest}")
        print("")
    
n = 3
source = [n, -1, [0, 0, 0]]
aux = [n, -1, [0, 0, 0]]
dest = [n, -1, [0, 0, 0]]

for disk in range(n, 0, -1):
    push(source, disk)

print("Initial State:")
print(f"Source: {source}")
print(f"Aux: {aux}")
print(f"Dest: {dest}")
print("")

move_disks(n, source, dest, aux)
