from fastapi.responses import HTMLResponse

class ShoeView:
    @staticmethod
    def render_shoe(shoe) -> HTMLResponse:
        html = f"""
        <html>
            <body>
                <h1>обувь</h1>
                <p><b>тип:</b> {shoe.gender}</p>
                <p><b>вид:</b> {shoe.shoe_type}</p>
                <p><b>цвет:</b> {shoe.color}</p>
                <p><b>цена:</b> {shoe.price}</p>
                <p><b>производитель:</b> {shoe.manufacturer}</p>
                <p><b>размер:</b> {shoe.size}</p>
            </body>
        </html>
        """
        return HTMLResponse(content=html)

class RecipeView:
    @staticmethod
    def render_recipe(recipe) -> HTMLResponse:
        ingredients_html = "".join([f"<li>{i}</li>" for i in recipe.ingredients])
        html = f"""
        <html>
            <body>
                <h1>рецепт: {recipe.name}</h1>
                <p><b>автор:</b> {recipe.author}</p>
                <p><b>тип:</b> {recipe.recipe_type}</p>
                <p><b>описание:</b> {recipe.description}</p>
                <p><b>видео:</b> <a href="{recipe.video_link}">{recipe.video_link}</a></p>
                <p><b>ингредиенты:</b></p>
                <ul>{ingredients_html}</ul>
                <p><b>кухня:</b> {recipe.cuisine}</p>
            </body>
        </html>
        """
        return HTMLResponse(content=html)