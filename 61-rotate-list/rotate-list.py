class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head

        tail.next = head

        steps = length - k
        current = head

        for i in range(steps - 1):
            current = current.next

        new_head = current.next
        current.next = None

        return new_head