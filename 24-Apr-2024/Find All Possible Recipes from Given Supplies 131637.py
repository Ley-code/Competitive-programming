# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = {food:0 for food in recipes}
        for i in range(len(recipes)):
            for ingre in ingredients[i]:
                graph[ingre].append(recipes[i])
                indegree[recipes[i]]+=1
        recipes = set(recipes)
        queue = deque(supplies)
        ans = []
        while queue:
            food = queue.popleft()
            for nei in graph[food]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
                    if nei in recipes:
                        ans.append(nei)
        return ans
        