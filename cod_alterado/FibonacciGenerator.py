class FibonacciGenerator:
    def generate_sequence(self, n):
        if n <= 0:
            return []
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:n]

    def get_nth_number(self, n):
        if n <= 0:
            return None
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
