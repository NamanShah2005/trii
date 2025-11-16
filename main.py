def main():
    import sys

    def r1():
        t = sys.stdin.readline()
        if not t:
            return None
        t = t.strip()
        if t == "":
            return None
        try:
            return int(t)
        except:
            return None

    def rlist():
        z = sys.stdin.readline()
        if not z:
            return []
        z = z.strip()
        if z == "":
            return []
        p = z.split()
        out = []

        def go(i):
            if i == len(p):
                return out
            try:
                q = int(p[i])
                out.append(q)
            except:
                out.append(0)
            return go(i + 1)

        return go(0)

    def fsum(a):
        if not a:
            return 0
        h = a[0]
        t = a[1:]
        if h <= 0:
            x = h * h
            x = x * x
        else:
            x = 0
        return x + fsum(t)

    def solve(n):
        if n == 0:
            return []
        x = r1()
        arr = rlist()
        if x is None:
            f = -1
        else:
            if len(arr) != x:
                f = -1
            else:
                f = fsum(arr)
        return [f] + solve(n - 1)

    total = r1()
    ans = solve(total)

    def pr(i):
        if i == len(ans):
            return
        print(ans[i])
        pr(i + 1)

    pr(0)


if __name__ == "__main__":
    main()
