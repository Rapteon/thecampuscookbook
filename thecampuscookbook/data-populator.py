import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thecampuscookbook.settings")

import django

django.setup()

from category.models import Category
from recipe.models import Recipe, Rating
from account.models import UserProfile

from django.contrib.auth.models import User
from django.db import IntegrityError

from django.contrib.auth.hashers import make_password

USERS = [
    {
        # id = 1
        "username": "admin",
        "email": "admin@example.com",
        "password": make_password("admin"),
        "is_superuser": True,
        "is_staff": True,
        "avatar": "images/avatars/admin.png",
    },
    {
        # id = 2
        "username": "janedoe",
        "email": "jane.doe@example.com",
        "password": make_password("jane.doe"),
        "avatar": "images/avatars/jane-doe.png",
    },
    {
        # id = 3
        "username": "johndoe",
        "email": "john.doe@example.com",
        "password": make_password("john.doe"),
        "avatar": "images/avatars/john-doe.png",
    },
]

CATEGORIES = [
    {
        "name": "Soup",
        "description": """Hearty soups from around the globe to keep you warm and satisfied.""",
    },  # id = 1
    {
        "name": "Main",
        "description": """Satisfy your hunger with our diverse selection of main course dishes, featuring hearty flavors and creative culinary ideas. """,
    },  # id = 2
    {
        "name": "Dessert",
        "description": """Satisfy your hunger with our diverse selection of main course dishes, featuring hearty flavors and creative culinary ideas.""",
    },  # id = 3
    {
        "name": "Starter",
        "description": """Delight your taste buds with our mouth-watering selection of appetizers that perfectly kick off any meal.""",
    },  # id = 4
    {
        "name": "Creative",
        "description": """Dive into a world of culinary innovation where every recipe is a canvas. Explore unique, fusion-style dishes that defy tradition.""",
    },  # id = 5
]

RECIPES = [
    {
        # id = 1
        "user_id": 1,
        "title": "Tomato Soup",
        "origin": "Spain",
        "category_id": 1,
        "ingredients": "Tomatoes, onion, butter",
        "description": """To make this extra easy tomato soup, add butter, onion, a large can of tomatoes, and water to a large pot. (I usually use water in this soup, but stock or broth work, too). Remember, you can use fresh tomatoes – tips for using them are in the recipe below.
Bring everything to a low simmer and cook for 40 minutes. The photo and video show that our tomato soup becomes super creamy. That’s thanks to the butter. The onions also soften, which adds to the creaminess of our soup when blended.
Blend the soup until smooth. I typically use an immersion blender, but a regular blender works perfectly fine. Adjust the soup with salt and pepper, then grab a bowl and enjoy!
""",
        "preparation_time": "1hour",
        "average_rating": 0,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/tomato-soup.jpeg",
    },
    {
        # id = 2
        "user_id": 1,
        "title": "Garlic Butter Noodles with Chicken",
        "origin": "San Francisco",
        "category_id": 2,
        "ingredients": "8 ounces bucatini or linguine pasta, 4 tablespoons salted butter, 1/4 cup panko breadcrumbs, 1/8 teaspoon kosher salt, 1 pinch red pepper flakes, 1 teaspoon garlic paste, 1 teaspoon ginger paste, 1/8 cup low-sodium soy sauce, salt and freshly ground black pepper, 1/4 cup grated Parmesan cheese, 1/2 cup cubed cooked chicken, 2 green onions, 1/2 bunch cilantro (leaves only)",
        "description": """Bring a large pot of salted water to a boil. Add pasta and cook until barely tender with a bite, 8 to 10 minutes. Drain and set aside.
Meanwhile, in a saucepan, melt 1 tablespoon butter. Add panko, kosher salt, and red pepper flakes. Stir frequently until breadcrumbs turn golden brown, about 3 minutes. Remove breadcrumbs to a bowl and set aside.
Wipe out the saucepan and return to the stovetop. Melt remaining butter and add garlic paste and ginger paste, cooking briefly. Pour in soy sauce and season with black pepper. Stir, then gradually add Parmesan cheese to prevent clumping. Add cooked chicken and heat through for about 3 minutes.
Add pasta to the sauce, mix thoroughly, and season with salt or pepper. Serve in bowls topped with green onions, cilantro, and breadcrumbs.""",
        "preparation_time": "25 mins",
        "average_rating": 0,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/garlic-butter-noodles-with-chicken.jpeg",
    },
    {
        # id = 3
        "user_id": 2,
        "title": "Miso-Glazed Salmon with Stir-Fried Noodles",
        "origin": "Asian",
        "category_id": 2,
        "ingredients": "4 salmon fillets (about 140g each), sunflower oil (for greasing), 2 tsp brown miso paste, 2 tsp balsamic vinegar, 2 tsp soy sauce, 1 tsp Spanish smoked paprika, 200g dried rice noodles, 3 tbsp sunflower oil, 3 garlic cloves (finely grated), 25g ginger (finely grated), 8 spring onions (sliced), 2 medium red chillies (thinly sliced), 100g beansprouts, small pack of coriander (chopped), 1 tbsp fish sauce",
        "description": """Boil the noodles for 3 minutes in a large pan, then drain and rinse under cold water. Set aside to drain completely.
Heat the grill to high. Mix the miso paste, balsamic vinegar, soy sauce, and paprika to make the miso glaze. Brush over the salmon fillets and place them skin-side down on a greased baking tray. Grill for 6-8 minutes until just cooked through.
Heat oil in a wok and stir-fry the garlic, ginger, spring onions, and chillies for a few minutes until softened. Add the cooked noodles, beansprouts, and coriander. Toss until well combined, then turn off the heat. Stir in the fish sauce.
Serve the stir-fried noodles on plates, topped with the grilled miso-glazed salmon.""",
        "preparation_time": "30-35 mins",
        "average_rating": 0,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/miso-glazed-salmon-with-stir-fried-noodles.jpeg",
    },
    {
        # id = 4
        "user_id": 2,
        "title": "Norwegian Fiskesuppe",
        "origin": "Norway",
        "category_id": 2,
        "ingredients": "2 1/8 pints fish stock, 2 tbsp plain flour, 4 1/16 fl oz double cream, 2 carrots (cut into matchsticks), white wine vinegar, granulated sugar, 14 1/8 oz fish fillets (cut into 1/2 inch chunks), sea salt, freshly ground black pepper",
        "description": """Bring the fish stock to a simmer in a large saucepan over medium-high heat. Add the matchstick-cut vegetables and simmer for 3-4 minutes until softened.
Meanwhile, whisk the flour into the double cream. Remove the saucepan from the heat and gradually whisk in the flour and cream mixture to create a smooth soup. Add about 1 tsp of vinegar and a pinch of sugar, adjusting to taste for a balance between sweet and sour without overpowering the fish stock.
Return the pan to the heat, whisking as the soup comes to a boil. Reduce the heat to medium and add the fish chunks. Cook for 4-5 minutes, stirring occasionally, until the fish is just cooked through.
Season to taste with salt and pepper. Serve immediately with fresh white bread and butter. Optionally, garnish with chopped chives or whole shell-on prawns hooked onto the bowl.""",
        "preparation_time": "20-25 mins",
        "average_rating": 0,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/norwegian-fiskesuppe.jpeg",
    },
    {
        # id = 5
        "user_id": 3,
        "title": "Sumac Chicken Flatbreads with Mint Yogurt",
        "origin": "Middle Eastern",
        "category_id": 2,
        "ingredients": "6 skinless and boneless chicken thigh fillets (cut into strips), 2 tbsp olive oil, 2 tsp sumac, 160g green olives, 1 lemon (halved), 2 garlic cloves (crushed or grated), 1/2 tsp chilli flakes, 200g Greek yogurt, 4 tbsp gardeners mint sauce, 4 flatbreads, 1 little gem lettuce (shredded), cucumber (cubed), 80g pomegranate seeds",
        "description": """Cut the chicken into strips and place in a bowl with olive oil, chilli flakes, sumac, the juice of half a lemon, and crushed garlic. Mix well and let it marinate in the fridge for 10 minutes. Preheat the grill to high.
Once marinated, place the chicken on a baking tray and grill for 12-14 minutes until cooked and slightly charred. Warm the flatbreads for two minutes.
While the chicken grills, mix Greek yogurt with gardeners mint sauce and set aside.
To assemble, spread a large spoonful of mint yogurt onto each flatbread. Top with shredded lettuce, cucumber, grilled chicken, pomegranate seeds, and olives. Squeeze the remaining lemon half over the flatbreads and serve with extra mint yogurt and cucumber segments.""",
        "preparation_time": "30 mins",
        "average_rating": 0,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/sumac-chicken-flatbreads-with-mint-yogurt.jpeg",
    },
    {
        # id = 6
        "user_id": 3,
        "title": "Slow Cooker Creamy Chicken Soup",
        "origin": "Worldwide",
        "category_id": 1,
        "ingredients": "2 tbsp sunflower or vegetable oil, 2 onions (finely chopped), 2 garlic cloves (crushed), 65g plain flour, 1.25 litres hot chicken stock (made with 2 chicken stock cubes), 1 tsp dried mixed herbs, 1/4 tsp ground turmeric (optional), 4 boneless skinless chicken thigh fillets, 5 tbsp milk or single cream, salt and freshly ground black pepper, chopped fresh flatleaf parsley or chives (to serve)",
        "description": """Heat the oil in a large non-stick frying pan over medium-high heat. Fry the onions for 3–4 minutes until softened, stirring constantly. Add the garlic and cook for a few more seconds.
Transfer the onions and garlic to a slow cooker and toss with the flour. Stir in the chicken stock, mixed herbs, turmeric (if using), and black pepper. Add the whole chicken thigh fillets to the slow cooker, cover, and cook on High for 3–4 hours or Low for 5–7 hours until the chicken is very tender.
Remove the lid and shred the chicken using two forks. Stir in the milk or single cream and season with salt and pepper. Cover and cook on High for 15 minutes until heated through.
Sprinkle with fresh parsley or chives and serve with warm crusty bread.""",
        "preparation_time": "Over 2 hours",
        "average_rating": 0,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/slow-cooker-creamy-chicken-soup.jpeg",
    },
    {
        # id = 7
        "user_id": 2,
        "title": "Spiced Harissa Chickpea Soup",
        "origin": "Middle Eastern",
        "category_id": 1,
        "ingredients": "2 tbsp olive or sunflower oil, 1 large onion (finely sliced), 1 tsp ground cumin, 2 tbsp harissa paste (ideally rose harissa), 400g tin chopped tomatoes, 400g tin chickpeas or lentils (drained and rinsed), 600ml water or stock (made with 1 chicken or vegetable stock cube), salt and freshly ground black pepper",
        "description": """Heat the oil in a large saucepan and gently fry the onion for 6–8 minutes until softened and lightly browned, stirring regularly. Add the cumin and harissa paste, cooking for 1 more minute while stirring constantly.
Add the chopped tomatoes and bring to a simmer. Cook for 2 minutes, stirring frequently.
Tip in the chickpeas or lentils and pour in the water or stock. Bring to a simmer and cook for 5 minutes, stirring occasionally.
Season with salt and freshly ground black pepper. Serve hot.""",
        "preparation_time": "Less than 30 mins",
        "average_rating": 0,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/spiced-harissa-chickpea-soup.jpeg",
    },
    {
        # id = 8
        "user_id": 2,
        "title": "Grilled Vegetable Antipasti",
        "origin": "Italy",
        "category_id": 4,
        "ingredients": "Green pepper, red pepper, yellow pepper, courgettes, aubergines, garlic, thyme, olive oil, sherry vinegar",
        "description": """Put the peppers in a bowl with olive oil and seasoning. Heat a griddle pan over medium/high heat and cook the peppers in batches until soft and grill-marked, then transfer them to a covered bowl. Repeat with courgettes and aubergines, ensuring they are fully tender.
Once all vegetables are cooked, add garlic, thyme, sherry vinegar, and more olive oil to each bowl. Allow to marinate for at least 1 hour at room temperature before serving, or refrigerate for up to 3 days. Bring to room temperature before serving.""",
        "preparation_time": "30 minutes",
        "average_rating": 4,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/grilled-vegetable-antipasti.jpeg",
    },
    {
        # id = 9
        "user_id": 3,
        "title": "Sweet and Spicy Turkey Sandwich",
        "origin": "United States",
        "category_id": 5,
        "ingredients": "Hearty country bread, roasted turkey breast, pepperjack cheese, butter, strawberry preserves",
        "description": """Heat a small skillet over medium heat. Butter one side of each bread slice with one teaspoon butter. Place one slice, butter side down, in the skillet. Top with turkey and cheese slices, then place the second slice of bread on top, butter side up.
Cook until the first side is golden brown, then flip and brown the other side for 3-5 minutes per side, or until the cheese melts.
Remove the sandwich to a plate and top with strawberry preserves, or serve the preserves on the side.""",
        "preparation_time": "15 minutes",
        "average_rating": 5,  # Please add a record in Rating if updating this to non-zero
        "image_path": "images/recipes/sweet-and-spicy-turkey-sandwich.jpeg",
    },
    {
        "user_id": 2,
        "title": "Easy Apple Crumble",
        "origin": "United Kingdom",
        "category_id": 3,
        "ingredients": "plain_flour, salt, brown_sugar, unsalted_butter, apples, brown_sugar, plain_flour, ground_cinnamon",
        "description": """
            Preheat the oven to 180C/160C Fan/Gas 4.
            Place the flour, salt, and sugar in a large bowl and mix well. Taking a few cubes of butter at a time, rub into the flour mixture until it resembles breadcrumbs.
            Place the fruit in a large bowl and sprinkle over the sugar, flour, and cinnamon. Stir carefully.
            Butter a 24cm/9in ovenproof dish. Spoon the fruit mixture into the bottom, then sprinkle the crumble mixture on top.
            Bake for 40–45 minutes until the crumble is browned and the fruit mixture is bubbling.
            Serve with thick cream or custard.
            """,
        "preparation_time": "1 hour 30 minutes",
        "average_rating": 0,
        "image_path": "images/recipes/easy-apple-crumble.jpeg",
    },
]

RATINGS = [
    {"recipe_id": 1, "user_id": 3, "rating": 0},
    {"recipe_id": 2, "user_id": 2, "rating": 0},
    {"recipe_id": 3, "user_id": 3, "rating": 5},
    {"recipe_id": 4, "user_id": 3, "rating": 0},
    {"recipe_id": 5, "user_id": 2, "rating": 0},
    {"recipe_id": 6, "user_id": 2, "rating": 1},
    {"recipe_id": 7, "user_id": 3, "rating": 3},
    {"recipe_id": 8, "user_id": 3, "rating": 4},
    {"recipe_id": 9, "user_id": 3, "rating": 5},
]


def on_integrity_error(data):
    print(f"Already exists: {data}")


def add_user(user_data):
    try:
        user, _ = User.objects.get_or_create(
            username=user_data["username"], email=user_data["email"]
        )
        user.password = user_data["password"]
        user.is_superuser = user_data.get("is_superuser", False)
        user.is_staff = user_data.get("is_staff", False)

        print(f"Creating user: {user}")
        user.save()

        profile, _ = UserProfile.objects.get_or_create(user=user)
        print(f"Creating profile: {profile}")
        profile.avatar.name = user_data["avatar"]
        profile.save()

    except IntegrityError:
        on_integrity_error(user_data)


def add_category(category_data):
    try:
        category, _ = Category.objects.get_or_create(**category_data)
        print(f"Creating category: {category}")
        category.save()
    except IntegrityError:
        on_integrity_error(category_data)


def add_recipe(recipe_data):
    try:
        user_id = recipe_data["user_id"]
        user = User.objects.filter(id__exact=user_id)[0]
        user_profile = UserProfile.objects.filter(user=user)[0]

        category_id = recipe_data["category_id"]
        category = Category.objects.filter(id__exact=category_id)[0]
        recipe, _ = Recipe.objects.get_or_create(
            user_profile=user_profile,
            title=recipe_data["title"],
            origin=recipe_data["origin"],
            category_id=category,
            ingredients=recipe_data["ingredients"],
            description=recipe_data["description"],
            preparation_time=recipe_data["preparation_time"],
            average_rating=recipe_data["average_rating"],
        )
        try:
            recipe.image.name = recipe_data["image_path"]
            recipe.save()
        except FileNotFoundError as e:
            print(e.filename)

        print(f"Creating recipe: {recipe}")
        recipe.save()
    except IntegrityError:
        on_integrity_error(recipe_data)


def add_rating(rating_data):
    try:
        recipe_id = rating_data["recipe_id"]
        recipe = Recipe.objects.filter(id__exact=recipe_id)[0]

        user_id = rating_data["user_id"]
        user = User.objects.filter(id__exact=user_id)[0]
        user_profile = UserProfile.objects.filter(user=user)[0]

        rating_data = {**rating_data}
        rating_data["user_profile"] = user_profile
        rating_data["recipe"] = recipe
        rating, _ = Rating.objects.get_or_create(
            recipe=recipe, user_profile=user_profile, rating=rating_data["rating"]
        )
        print(f"Created rating: {rating}")
        rating.save()
    except IntegrityError:
        on_integrity_error(rating_data)


def populate():
    for user_data in USERS:
        add_user(user_data)

    for category_data in CATEGORIES:
        add_category(category_data)

    for recipe_data in RECIPES:
        add_recipe(recipe_data)

    for rating_data in RATINGS:
        add_rating(rating_data)


if __name__ == "__main__":
    populate()
