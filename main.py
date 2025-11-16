def main():
    import sys

    def read_int():
        line = sys.stdin.readline()
        if not line:
            return None
        return int(line.strip())

    def read_ints():
        line = sys.stdin.readline()
        if not line:
            return []
        return list(map(int, line.strip().split()))

    def process_case(n):
        if n == 0:
            return []
        X = read_int()
        nums = read_ints()

        if len(nums) != X:
            return [-1] + process_case(n - 1)

        def calc_sum(arr):
            if not arr:
                return 0
            y = arr[0]
            return (y ** 4 if y <= 0 else 0) + calc_sum(arr[1:])

        return [calc_sum(nums)] + process_case(n - 1)

    N = read_int()
    results = process_case(N)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
