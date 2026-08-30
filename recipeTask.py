class RecipeModel:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

class RecipeView:
    def show_recipe(self, recipe):
        print(f"название: {recipe.name}")
        print(f"автор: {recipe.author}")
        print(f"тип: {recipe.recipe_type}")
        print(f"описание: {recipe.description}")
        print(f"видео: {recipe.video_link}")
        print(f"ингредиенты: {', '.join(recipe.ingredients)}")
        print(f"кухня: {recipe.cuisine}")

class RecipeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        self.view.show_recipe(self.model)

ingredients_list = ["сметана", "яйца", "бекон", "сыр косичка", "перец"]
model = RecipeModel("нечто", "великий и не повторимый мачомен", "вторые блюда", "классическая паста(?)", "", ingredients_list, "итальянская(наверное, написано в описании)")
view = RecipeView()
controller = RecipeController(model, view)
controller.update_view()