def dfs(node, result, folder):
    if -1 in node:
        result.append(folder)
        return
    for char in node:
        if char !=-1:
            dfs(node[char], result, folder+"/"+char)


class Solution:
    def removeSubfolders(self, folder):
        # -> List[str]:
        self.root = {}
        for sub in folder:
            tmp = self.root
            sub = sub.split("/")[1:]
            for char in sub:
                if char not in tmp:
                    tmp[char] = {}
                tmp = tmp[char]
            tmp[-1] = True
        result = []
        dfs(self.root, result, "")
        return result


sol = Solution()
folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
folder = ["/a","/a/b/c","/a/b/d"]
folder = ["/a/b/c","/a/b/ca","/a/b/d"]
sol.removeSubfolders(folder)
