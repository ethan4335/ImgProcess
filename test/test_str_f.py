class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        # 通过Counter直接获取T当中的字符构成
        counter = Counter(t)
        n, m = len(s), len(counter)
        l, start, end = 0, 0, 0
        cur = defaultdict(int)
        matched = 0
        flag = False
        # 记录合法的字符串的长度
        ans_len = 0x3f3f3f3f #无穷大
        for i in range(n):
            if s[i] not in counter:
                continue

            # 记录字符出现次数
            cur[s[i]] += 1
            # 当数量匹配上的时候，计算匹配的个数matched+1
            if cur[s[i]] == counter[s[i]]:
                matched += 1

            # 如果已经找到了合法的区间，尝试缩短区间的长度
            while l <= i and matched == m:
                if i - l + 1 < ans_len:
                    flag = True
                    start, end = l, i + 1
                    ans_len = i - l + 1

                # 弹出左侧元素
                c = s[l]
                if c in counter:
                    cur[c] -= 1
                    if cur[c] < counter[c]:
                        matched -= 1

                l += 1

        return "" if not flag else s[start: end]

if __name__ == '__main__':
    s = Solution()
    print('out:',s.minWindow('attabrtarr','tar'))

