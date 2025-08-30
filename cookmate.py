import google.generativeai as genai

genai.configure(api_key="AIzaSyC1qv_URnyKEbXuyYfmy-A6x4CnEpoWUBs")

model = genai.GenerativeModel("gemini-2.5-flash")

def get_recipe(ingredients):
    prompt = f"Suggest a creative, beginner-friendly recipe using only these ingredients: {ingredients}. Include a fun name and simple instructions."
    response = model.generate_content(prompt)
    return response.text

user_input = input("🍳 What ingredients do you have today?\n> ")

if user_input:
    print("\n🧠 CookMate AI is cooking up a recipe...\n")
    recipe = get_recipe(user_input)
    print("🍽️ Here's your dish:\n")
    print(recipe)
else:
    print("⚠️ You need to enter some ingredients!")