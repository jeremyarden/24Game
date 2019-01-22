import timeit

def product(opr, x):
    y = []
    for _ in range(x):
        if len(y) == 0:
            for z in opr:
                y.append(z)
        else:
            temp = []
            for j in y:
                for k in opr:
                    temp.append(j+k)
            y = temp.copy()
    return y

def permute(numbers):
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return [numbers]
    x = []
    for i in range(len(numbers)):
        y = numbers[i]
        remain = numbers[:i]  + numbers[i+1:]

        for z in permute(remain):
            x.append([y] + z)
    return x

def solve(numbers):
    perm = permute(numbers)
    op = product(['+', '-', '*', '/'], 3)
    temp = []
    for i in perm:
        for j in op:
            temp.append(f"(({i[0]} {j[0]} {i[1]}) {j[1]} {i[2]}) {j[2]} {i[3]}")
            temp.append(f"({i[0]} {j[0]} ({i[1]} {j[1]} {i[2]})) {j[2]} {i[3]}")
            temp.append(f"{i[0]} {j[0]} ({i[1]} {j[1]} ({i[2]} {j[2]} {i[3]}))")
            temp.append(f"{i[0]} {j[0]} (({i[1]} {j[1]} {i[2]}) {j[2]} {i[3]})")
            temp.append(f"({i[0]} {j[0]} {i[1]}) {j[1]} ({i[2]} {j[2]} {i[3]})")

    result = []
    for k in temp:
        try:
            test = eval(k)
            if (test == 24):
                result.append(k)
        except ZeroDivisionError:
            pass
    
    return result 
    
def main():
    inp = [int(x) for x in input("Masukan 4 angka dipisahkan dengan spasi : ").split()]
    start = timeit.default_timer()
    res = solve(inp)
    stop = timeit.default_timer()
    for solutions in res:
        print(solutions)
    print(f"Runtime: {stop - start} seconds")
    print(f"{len(res)} solutions found for {inp[0]} {inp[1]} {inp[2]} {inp[3]}")

main()