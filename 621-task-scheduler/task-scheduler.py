class Solution:
    def leastInterval(self, tasks, n):
        freq = [0] * 26

        for task in tasks:
            index = ord(task) - ord('A')
            freq[index] += 1

        max_freq = 0

        for i in range(26):
            if freq[i] > max_freq:
                max_freq = freq[i]

        count_max = 0

        for i in range(26):
            if freq[i] == max_freq:
                count_max += 1

        answer = (max_freq - 1) * (n + 1) + count_max

        total_tasks = 0

        for task in tasks:
            total_tasks += 1

        if answer < total_tasks:
            answer = total_tasks

        return answer
        