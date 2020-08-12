import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        count = collections.Counter(s)
        stack = []
        visited = collections.defaultdict(bool)
        for c in s:
            count[c] -= 1
            if visited[c]:
                continue
            while stack and count[stack[-1]] and stack[-1] > c:
                visited[stack[-1]] = False
                stack.pop()
            visited[c] = True
            stack.append(c)
        return "".join(stack)
val=Solution()
S=input()
print(val.removeDuplicateLetters(S))
