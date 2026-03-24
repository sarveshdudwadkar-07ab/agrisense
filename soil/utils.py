def analyze_soil(ph, nitrogen, phosphorus, potassium):

    fertilizer = "Balanced NPK fertilizer recommended"

    # ACIDIC SOIL (common in Konkan, Kerala, NE India)
    if ph < 5.5:

        field_crops = "Rice, Finger Millet (Ragi), Maize, Tapioca"
        fruits = "Mango, Pineapple, Banana, Jackfruit, Papaya"
        trees = "Coconut, Arecanut, Rubber, Bamboo"
        vegetables = "Ginger, Turmeric, Chilli, Brinjal"

        fertilizer = "Apply lime and organic compost to reduce acidity"

    # NEUTRAL SOIL (best agricultural soil)
    elif 5.5 <= ph <= 7.5:

        field_crops = "Rice, Wheat, Maize, Sorghum, Pearl Millet, Barley"
        fruits = "Mango, Banana, Guava, Papaya, Pomegranate, Orange, Lemon"
        trees = "Neem, Teak, Bamboo, Coconut"
        vegetables = "Tomato, Onion, Potato, Cabbage, Cauliflower, Chilli"

        if nitrogen < 40:
            fertilizer = "Apply Nitrogen fertilizer (Urea)"
        elif phosphorus < 40:
            fertilizer = "Apply Phosphorus fertilizer (DAP)"
        elif potassium < 40:
            fertilizer = "Apply Potassium fertilizer (MOP)"

    # ALKALINE SOIL
    else:

        field_crops = "Barley, Cotton, Mustard, Sorghum, Pearl Millet"
        fruits = "Date Palm, Ber (Indian Jujube), Pomegranate"
        trees = "Acacia, Prosopis, Neem"
        vegetables = "Spinach, Beetroot, Onion"

        fertilizer = "Add gypsum and organic manure"

    crop_recommendation = f"""
Field Crops: {field_crops}

Fruits: {fruits}

Trees / Plantation: {trees}

Vegetables & Spices: {vegetables}
"""

    return crop_recommendation, fertilizer