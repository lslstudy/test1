# -*- coding: utf-8 -*-

""" lt exercise
"""

NUM_STR = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def two_sum(nums: list, target: int) -> list:
    """ leet code 1
    :return:
    """
    if not nums or target < nums[0]:
        return [-1, -1]
    exists = dict()
    for idx, elem in enumerate(nums):
        if target - elem in exists:
            return [exists[target-elem], idx]
        exists[elem] = idx
    return [-1, -1]


def two_link_sum(link1: ListNode, link2: ListNode) -> ListNode:
    """ (2 -> 4 -> 3) + (5 -> 6 -> 4) ===> (7 -> 0 -> 8)
    :return:
    """
    phead = pnode = ListNode(0)
    val = 0
    while link1 or link2 or val:
        if link1:
            val += link1.val
            link1 = link1.next
        if link2:
            val += link2.val
            link2 = link2.next
        pnode.next = ListNode(val % 10)
        val //= 10
        pnode = pnode.next
    return phead.next


def move_zeros(nums: list) -> list:
    """　将数组中的０移到数组后面，保持数组的其他非零元素的相对位置
        引入变量k记为０元素下标，时间 O(n), 空间O(1)
    """
    if not nums:
        return nums
    leftag = 0
    for i in range(len(nums)):
        if not nums[i]:
            continue
        nums[leftag] = nums[i]
        leftag += 1
    for i in range(leftag, len(nums)):
        nums[i] = 0
    return nums


def color_sort(nums: list) -> list:
    """ LeetCode75: 不适用排序函数对数组排序，排序顺序为红白蓝，分别使用０１２代替
            采用三路快排思想：０和１交换，１和２交换，当前为１
    """
    if not nums:
        return nums
    left, right = 0, len(nums)-1
    cur = 0
    while cur <= right:
        if nums[cur] == 2:
            nums[cur], nums[right] = nums[right], nums[cur]
            right -= 1
        elif nums[cur] == 1:
            cur += 1
        else:
            nums[cur], nums[left] = nums[left], nums[cur]
            left += 1
            cur += 1
    return nums


def swap_pairs(head: ListNode) -> ListNode:
    """ (1 -> 2 -> 3 -> 4 -> 5) => (2 -> 1 -> 4 -> 3 -> 5)
    """
    if not head or not head.next:
        return head
    first, second = head, head.next
    third = second.next
    head = second
    second.next = first
    first.next = swap_pairs(third)
    return head


def longest_repeated_sub_length(s: str) -> int:
    """ longest sub str without repeat character  "aabca"  =>  abc bca => 3
    """
    if not s or len(s) <= 0:
        return 0
    char_dict, res, st = dict(), 0, 0
    for idx, char in enumerate(s):
        # 不存在(不重复)时计算长度或者出现重复的字符时计算
        if char not in char_dict or char_dict[char] < st:
            res = max(res, idx - st + 1)
        else:
            st = char_dict[char] + 1
        char_dict[char] = idx
    return res


def longest_sub_str(str1: str, str2: str) -> int:
    """ if str1[i] == str2[j] dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if str1[j] == str2[i]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[-1][-1]


def remove_nth_from_end(head: ListNode, n: int):
    """
    :return:
    """
    if not head and n <= 0:
        return
    pnode = ListNode(0)
    pnode.next = head
    first, second = pnode, pnode
    for i in range(n):
        if first.next:
            first = first.next
        else:
            return None
    while first.next:
        first = first.next
        second = second.next
    second.next = second.next.next
    return pnode.next


def merge_two_lists(node1: ListNode, node2: ListNode):
    """
    :return:
    """
    if not node1 or not node2:
        return node1 or node2
    pnode = phead = ListNode(0)
    while node1 and node2:
        if node1.val < node2.val:
            pnode.next = node1
            node1 = node1.next
        else:
            pnode.next = node2
            node2 = node2.next
        pnode = pnode.next
    pnode.next = node1 or node2
    return phead.next


def generate_parenthesis(n: int) -> list:
    if n <= 0:
        return []
    answer = []

    def helper(left, right, result):
        if left == n and right == n:
            answer.append(result)
            return
        if left < n:
            helper(left+1, right, result+"(")
        if left > right and right < n:
            helper(left, right+1, result+")")
    helper(left=0, right=0, result="")
    return answer


def nums_combine(n: int) -> list:
    if n < 0:
        return []
    answer = []

    def helper(nums: str, result: str):
        if not nums:
            answer.append(result)
            return
        char, nums = nums[:1], nums[1:]
        for x in NUM_STR[char]:
            helper(nums, result+x)
    helper(str(n), "")
    return answer


def in_order(root: TreeNode):
    """ in order tree
    :return:
    """
    if not root:
        return []
    answer = []

    def helper(node: TreeNode):
        if not node:
            return
        helper(node.left)
        answer.append(node.val)
        helper(node.right)
    helper(node=root)
    return answer


def in_order_traverse(root: TreeNode):
    if not root:
        return []
    answer = []
    stack, cur = [], root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            node = stack.pop()
            answer.append(cur.val)
            cur = node.right
    return answer


def pre_order_traverse(root: TreeNode):
    if not root:
        return []
    stack, answer = [root], []
    while stack:
        node = stack.pop()
        answer.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return answer


def post_order_traverse(root: TreeNode):
    if not root:
        return []
    stack, stack2, answer = [root], [], []
    while stack:
        node = stack.pop()
        stack2.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while stack2:
        answer.append(stack2.pop().val)
    return answer


def post_traverse(root: TreeNode):
    if not root:
        return
    stack, stack2, ans = [root], [], []
    while stack:
        node = stack.pop()
        stack2.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while stack2:
        ans.append(stack2.pop().val)
    return ans


def find_largest_kth(root: TreeNode, k: int) -> int:
    """ Given a binary search tree and find largest Kth elem
    :return:
    """
    if not root or k <= 0:
        return -1

    # in_order
    seq = in_order(root)
    return seq[-k] if len(seq) >= k else -1


def array_to_tree(arr: list):
    """ Given an sorted array and generate binary tree
    :return:
    """
    if not arr:
        return
    left, right = 0, len(arr) - 1
    mid = (left + right) >> 1
    node = TreeNode(val=arr[mid])
    node.left = array_to_tree(arr[0:mid])
    node.right = array_to_tree(arr[mid+1:])
    return node


def print_reverse_link(link: ListNode) -> list:
    """ print reversal linkedlist
    :return:
    """
    if not link:
        return []
    answer, stack = [], []
    while link.next:
        stack.append(link.val)
        link = link.next
    while stack:
        answer.append(stack.pop())
    return answer


def my_sqrt(t: int) -> float:
    """
    :return:
    """
    if t <= 0:
        return 0
    if t == 1:
        return 1
    left, right = 0, t
    mid = (left + right) / 2
    print(mid, type(mid))
    while left <= right:
        tmp = mid * mid
        if abs(tmp - t) == 0.01 or abs(t - tmp) == 0.01:
            return mid
        elif mid * mid > t:
            right = mid - 0.01
        else:
            left = mid + 0.01
        mid = (left+right) / 2
    return -1


def valid_pop_order(pu: list, po: list) -> bool:
    """ 验证出栈顺序是否是入栈顺序的一种
    :return:
    """
    if not pu and not po:
        return True
    stack = []
    for elem in pu:
        stack.append(elem)
        while stack and stack[-1] == po[0]:
            stack.pop()
            po.pop(0)
    return False if stack else True


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_rec(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for it in graph[start] - visited:
        dfs_rec(graph, it, visited)
    return visited


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for it in graph[vertex] - set(path):
            if it == goal:
                yield path + [it]
            else:
                stack.append((it, path+[it]))


def tree_width(root: TreeNode):
    """ the width of tree
    :return:
    """
    if not root:
        return 0
    if not root.left or not root.right:
        return 1
    width, queue = 1, [root]
    while queue:
        loop_cnt = len(queue)
        width = max(loop_cnt, width)
        for _ in range(loop_cnt):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return width


def max_slide_window_value(arr: list, n: int) -> list:
    """ Given an arr and find max_value for each slide window
    :return:
    """
    if not arr or n <= 0:
        return [0]
    if len(arr) < n:
        return [max(arr)]
    answer = []
    for i in range(len(arr) - n + 1):
        window = arr[i:i+n]
        answer.append(max(window))
    return answer


class Queue:
    """ user define queue implements with two stacks
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack1 = []
        self.stack2 = []

    def put(self, elem, *args):
        self.stack1.append(elem)
        for arg in args:
            self.stack1.append(arg)

    def get(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            elem = self.stack1.pop()
            self.stack2.append(elem)
        if len(self.stack2) == 0:
            return -1
        return self.stack2.pop()


def hamming_weight(n: int) -> int:
    """ Given an Integer and return count(1) of bit
    :return: n & (n-1) : remove last right bit=1
    """
    answer = 0
    while n != 0:
        answer += 1
        n = n & (n-1)
    return answer


def find_last_kth_elem(head: ListNode, k: int) -> int:
    if not head or k <= 0:
        return -1
    fast, slow = head, head
    while k != 0:
        if not fast.next:
            return -1
        fast = fast.next
        k -= 1
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow.val


def reverse_str(s: str) -> str:
    """ reverse strings,
    :return:
    """
    if not s:
        return ""
    if len(s) == 1:
        return s
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)


def q_sort(arr: list) -> list:
    """ quick sort
    :param arr:
    :return:
    """
    if not arr:
        return []
    if len(arr) <= 1:
        return arr
    last = arr.pop()
    left, right = [], []
    for item in arr:
        if item < last:
            left.append(item)
        else:
            right.append(item)
    return q_sort(left) + [last] + q_sort(right)


def binary_search(arr: list, target: int) -> int:
    """ Given a sorted array and find target elem index if exists
    """
    left, right = 0, len(arr) - 1
    mid = (left + right) >> 1
    while left < right:
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def climb_stairs(high: int) -> int:
    """ climb stairs with condition n=1 or n=2,
        same with fibonacci
    :return:
    """
    if high <= 0:
        return 0
    if high == 1:
        return 1
    arr = [0] * high
    arr[0], arr[1] = 1, 2
    for i in range(2, high, 1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[-1]


def max_sub_array_sum(arr: list) -> int:
    answer, cur = float("-inf"), float("-inf")
    for elem in arr:
        if cur > 0:
            cur += elem
        else:
            cur = elem
        answer = max(answer, cur)
    return answer


def unique_path(board: list) -> int:
    """ given a board and find total path from [0, 0] to [m, n]
        dp[m, n] = dp[m-1, n] + dp[m, n-1]
    :return:
    """
    if not board:
        return 0
    dp = [[1] * len(board[0]) for _ in range(len(board))]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


def unique_path_2(board: list) -> int:
    """ given a board and find total path from [0, 0] to [m, n]
        if board[i-1][j-1] == 1:
            dp[i, j] = 0
        else:
            dp[i, j] = dp[i-1, j] + dp[i, j-1]
    :return:
    """
    if not board:
        return 0
    dp = [[1] * len(board[0]) for _ in range(len(board))]
    for i in range(1, len(board), 1):
        for j in range(1, len(board[0]), 1):
            if board[i-1][j-1] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


def min_path_sum(grid: list) -> int:
    """ Given a grid and find min path sum from [0,0] to [m, n]
        dp[i, j] = min(dp[i, j-1], dp[i-1, j]) + grid[i, j]
    :param grid:
    :return:
    """
    if not grid:
        return 0
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(1, len(grid[0])):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for j in range(1, len(grid)):
        dp[j][0] = dp[j-1][0] + grid[j][0]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]


def min_triangle(t: list) -> int:
    """ dp[i, j] = min(dp[i+1, j], dp[i+1, j+1]) + t[i][j]
    :return:
    """
    if not t:
        return 0
    dp = [[0] * len(t[-1]) for _ in range(len(t))]
    dp[-1] = t[-1]
    for i in range(len(t) - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + t[i][j]
    return dp[0][0]


def unique_binary_search_tree(n: int) -> int:
    """ given a and structurally unique bst
        dp[i] =
    :return:
    """
    if n <= 0:
        return 0
    answer = [1] * (n+1)
    for i in range(1, n+1):
        for j in range(i+1):
            answer[i] += answer[j-1] * answer[i-j]
    return answer[n]


def max_rectangle(matrix: list) -> int:
    """ 求matrix 中矩阵面积最大

    :return:
    """
    pass


def max_profit_1(arr: list) -> int:
    """ given an array with stock price, and return max profile
        note:
            k=1

        dp[i][1][0] = max(dp[i-1][1][0], dp[i][1][1] + arr[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i][0][0] - arr[i])
                    = max(dp[i-1][1][1], -arr[i])
    :return:
    """
    if not arr:
        return -1
    dp_i_0, dp_i_1 = 0, float("-inf")
    for i in range(len(arr)):
        dp_i_0 = max(dp_i_0, dp_i_1 + arr[i])
        dp_i_1 = max(dp_i_1, -arr[i])
    return dp_i_0


def max_profit_k(arr: list) -> int:
    """ given an array with stock price, and return max profit with k -> float("inf")
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + arr[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - arr[i])
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + arr[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - arr[i])
    :return:
    """
    if not arr:
        return -1
    dp_i_0, dp_i_1 = 0, float("-inf")
    for i in range(len(arr)):
        # 和昨天状态有关，可以操作多次,必须保留昨天状态
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + arr[i])
        dp_i_1 = max(dp_i_1, tmp - arr[i])
    return dp_i_0


def max_profit_cold(arr: list) -> int:
    """ k -> +infinity with cold down
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + arr[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - arr[i])
    :return
    """
    if not arr:
        return -1
    dp_i_0, dp_i_1 = 0, float("-inf")
    per_2_0 = 0
    for i in range(len(arr)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + arr[i])
        dp_i_1 = max(dp_i_1, per_2_0 - arr[i])
        per_2_0 = tmp
    return dp_i_0


def max_profile_fee(arr: list, fee: int) -> int:
    """ k -> + infinity with free
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + arr[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - arr[i] - fee)
    :return:
    """
    if not arr:
        return -1
    dp_i_0, dp_i_1 = 0, float("-inf")
    for i in range(len(arr)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + arr[i])
        dp_i_1 = max(dp_i_1, tmp - arr[i] - fee)
    return dp_i_0


def max_profit_2(arr: list) -> int:
    """ k = 2
        dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + arr[i])
        dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - arr[i])
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + arr[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - arr[i])
    :return:
    """
    if not arr:
        return -1
    dp_i_10, dp_i_20 = float("-inf"), float("-inf")
    dp_i_11, dp_i_21 = 0, 0
    for i in range(len(arr)):
        dp_i_20 = max(dp_i_20, dp_i_21 + arr[i])
        dp_i_21 = max(dp_i_21, dp_i_10 - arr[i])
        dp_i_10 = max(dp_i_10, dp_i_11 + arr[i])
        dp_i_11 = max(dp_i_11, -arr[i])
    return dp_i_20


def edit_distance(word1: str, word2: str) -> int:
    """  dp[i][j] = dp[i-1][j-1] if word1[i-1] == word[j-1]
         dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
         dp[i][j] represent word1 pre i trans to word2 pre j edit distance
    :return:
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
    print(dp)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[m][n]


def longest_common_sub(word1: str, word2: str) -> int:
    """ longest common sub str length
        dp[i][j] = dp[i-1][j-1] + 1 if word1[i] == word2[j]
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    :return:
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


def max_asc_num(num):
    """ 找到给定数字的最大递增数字 eg: 1243 -> 1239, 1234 -> 1234
    """
    if num < 10:
        return num
    arr = [x for x in str(num)]
    size = len(arr)
    flag = size - 1
    for i in range(size-1, 0, -1):
        if arr[i-1] > arr[i]:
            arr[i-1] = str(int(arr[i-1])-1)
            flag = i
    print("flag = ", flag)
    for i in range(flag, size):
        arr[i] = "9"
    return int("".join(arr))


def max_common_array(A: list, B: list) -> int:
    if not A or not B:
        return 0
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    res = 0
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(dp[i][j], res)
    print("\n".join([str(x) for x in dp]))
    return res


def min_consist_of_coin(target: int) -> int:
    """ find min count of coins which sum coins value equal target
        dp[i] = min(dp[i-1], dp[target-3], dp[target-5]) + 1
    """
    coins = [1, 3, 5]
    if not target:
        return -1
    dp = [0] * (target+1)
    for i in range(1, target + 1):
        pass


if __name__ == '__main__':
    # ans = generate_parenthesis(n=3)
    # print(ans)
    #
    # ans = nums_combine(n=23)
    # print(ans)
    #
    # ans = my_sqrt(t=2)
    # print(ans)
    #
    # b_ans = valid_pop_order(pu=[1, 2, 3, 4, 5], po=[3, 5, 4, 2, 1])
    # print(b_ans)

    # slide = max_slide_window_value(arr=[2, 3, 4, 2, 6, 2, 5, 1], n=3)
    # print(slide)
    # assert slide == [4, 4, 6, 6, 6, 5]
    #
    # s = "hellpo"
    # s = reverse_str(s=s)
    # print(s)
    #
    # arr = [2, 3, 4, 2, 6, 2, 5, 1]
    # ans = q_sort(arr=arr)
    # print(ans)

    # high = climb_stairs(high=10)
    # print(high)

    # arr = [2, 1, 3, 1, 4]
    # max_sum = max_sub_array_sum(arr=arr)
    # print(max_sum)
    #
    # max_profit = max_profit_1(arr=arr)
    # print(max_profit)
    #
    # max_profit = max_profit_k(arr=arr)
    # print(max_profit)
    #
    # max_profit = max_profit_cold(arr=arr)
    # print(max_profit)
    #
    # max_profit = max_profile_fee(arr=arr, fee=1)
    # print(max_profit)
    #
    # max_profit = max_profit_2(arr=arr)
    # print(max_profit)

    # t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    # ans = min_triangle(t=t)
    # print(ans)
    #
    # ans = longest_sub_str(str1="abcda", str2="abdefa")
    # print(ans)

    # ans1 = sub_length(s="abcabcd")
    # print(ans1)

    # queue = Queue(capacity=10)
    # queue.put(1, 2, 3, 4, 5)
    # print(queue.get(), queue.get(), queue.get(), queue.get(), queue.get(), queue.get())
    # nums = [2, 0, 2, 1, 1, 0]
    # print(csort(nums))
    # print(move_zero(nums))
    # s = "abacdabc"
    # print(longest_sub_len(s))

    # print(max_asc_num(9999))

    print(max_common_array([1, 2, 3, 2, 1], [1, 2, 3, 2, 1]))





