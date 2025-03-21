class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
       
        in_degree = {}  
        graph = defaultdict(list)  

        for i, recipe in enumerate(recipes):
            in_degree[recipe] = len(ingredients[i]) 
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)  

        
        queue = deque(supplies)  
        possible_recipes = set(supplies) 

        
        result = []
        while queue:
            ingredient = queue.popleft()
            
            
            if ingredient in in_degree:
                result.append(ingredient)
            
            
            for recipe in graph[ingredient]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:  
                    queue.append(recipe)  

        return result  