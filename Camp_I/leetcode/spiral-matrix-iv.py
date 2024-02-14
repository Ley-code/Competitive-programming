# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for i in range(m)]
        curr = head
        x = 0
        y = 0
        rightB = n-1
        leftB = 0
        topB = 0
        bottomB = m-1
        while curr:
            while curr and y<=rightB:
                mat[x][y] = curr.val
                curr=curr.next
                y+=1
            y-=1
            x+=1
            topB+=1
            while curr and x<=bottomB:
                mat[x][y] = curr.val
                curr = curr.next
                x+=1
            x-=1
            y-=1
            rightB-=1
            while curr and y>=leftB:
                mat[x][y] = curr.val
                curr = curr.next
                y-=1 
            y+=1
            x-=1
            bottomB-=1
            while curr and x>=topB:
                mat[x][y] = curr.val
                curr = curr.next
                x-=1
            x+=1
            y+=1
            leftB+=1
        return mat