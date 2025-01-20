    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next :
            head = head.next
            fast = fast.next.next
            if fast == head:
                return True
        False
        