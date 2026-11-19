import pandas as pd
from pathlib import Path

path = Path("data/expense_training_data.csv")
df = pd.read_csv(path)

new_examples = {
    "Food": [
        "Ordered chicken biryani for lunch",
        "Paid for family dinner at restaurant",
        "Bought fresh fruits from market",
        "Purchased milk eggs and bread",
        "Ordered pizza for dinner",
        "Bought vegetables for home cooking",
        "Paid restaurant breakfast bill",
        "Purchased snacks from grocery store",
        "Ordered burgers through food delivery",
        "Bought rice flour and cooking oil",
        "Paid for takeaway food",
        "Bought chicken from meat shop",
        "Purchased coffee from cafe",
        "Had lunch at university cafeteria",
        "Bought sandwiches for breakfast",
        "Ordered Chinese food online",
        "Purchased bakery items and cake",
        "Paid for ice cream",
        "Bought groceries for weekly meals",
        "Ordered shawarma for dinner",
        "Purchased bottled water and juice",
        "Paid for office lunch",
        "Bought fresh fish for dinner",
        "Purchased spices for cooking",
        "Paid for food at a local cafe",
        "Bought breakfast from a restaurant",
        "Ordered pasta for lunch",
        "Purchased fruits and vegetables",
        "Bought biscuits and snacks",
        "Paid for family groceries",
        "Purchased cooking ingredients",
        "Ordered food for guests",
        "Bought yogurt and cheese",
        "Paid for dinner delivery",
        "Purchased tea and coffee supplies"
    ],

    "Transport": [
        "Booked a ride using Uber",
        "Paid for Careem trip",
        "Filled petrol in motorcycle",
        "Filled diesel in car",
        "Paid monthly bus pass",
        "Purchased railway ticket",
        "Paid for airport taxi",
        "Paid motorcycle repair transport charges",
        "Bought fuel for vehicle",
        "Paid local rickshaw fare",
        "Purchased motorway toll ticket",
        "Paid parking charges at mall",
        "Booked intercity bus ticket",
        "Paid metro train fare",
        "Purchased car engine oil",
        "Paid vehicle registration fee",
        "Paid for car wash",
        "Booked taxi to university",
        "Paid fuel station bill",
        "Purchased bicycle repair parts",
        "Paid highway toll charges",
        "Booked ride to office",
        "Paid public transport fare",
        "Purchased motorcycle helmet",
        "Paid for vehicle servicing",
        "Bought petrol for car trip",
        "Paid van fare to college",
        "Purchased train travel ticket",
        "Paid airport parking fee",
        "Booked a ride home",
        "Paid for vehicle inspection",
        "Purchased car wiper blades",
        "Paid bus fare to work",
        "Bought fuel for generator transport",
        "Paid rickshaw charges"
    ],

    "Shopping": [
        "Purchased a new pair of sneakers",
        "Bought a casual shirt from clothing store",
        "Ordered a mobile phone case",
        "Purchased wireless headphones",
        "Bought a wristwatch",
        "Ordered a new backpack",
        "Purchased jeans from mall",
        "Bought a leather wallet",
        "Purchased a laptop stand",
        "Ordered a phone charger",
        "Bought sunglasses",
        "Purchased a winter jacket",
        "Ordered home decoration items",
        "Bought a new handbag",
        "Purchased a computer mouse",
        "Bought a keyboard for laptop",
        "Ordered household storage boxes",
        "Purchased a bedsheet set",
        "Bought new sandals",
        "Purchased a school bag",
        "Ordered a power bank",
        "Bought a pair of trousers",
        "Purchased a water bottle",
        "Bought a new cap",
        "Ordered a tablet cover",
        "Purchased a gaming mouse",
        "Bought a travel suitcase",
        "Purchased kitchen utensils",
        "Ordered a desk lamp",
        "Bought a new sweater",
        "Purchased a phone screen protector",
        "Bought a pair of formal shoes",
        "Ordered a computer accessory",
        "Purchased a clothing bundle",
        "Bought household cleaning tools"
    ],

    "Bills": [
        "Paid monthly electricity charges",
        "Paid home gas bill",
        "Renewed internet broadband payment",
        "Paid mobile network monthly bill",
        "Paid water supply charges",
        "Paid house maintenance bill",
        "Settled electricity dues",
        "Paid monthly WiFi subscription",
        "Paid landline telephone bill",
        "Paid apartment service charges",
        "Paid monthly utility expenses",
        "Renewed home internet package",
        "Paid electricity meter charges",
        "Paid gas connection dues",
        "Settled water bill for home",
        "Paid cable television subscription",
        "Paid monthly phone charges",
        "Paid household utility bill",
        "Renewed mobile data package",
        "Paid building maintenance charges",
        "Paid internet service provider",
        "Settled monthly electricity payment",
        "Paid residential water charges",
        "Paid gas usage bill",
        "Paid telephone service charges",
        "Renewed broadband connection",
        "Paid monthly housing maintenance",
        "Paid utility company invoice",
        "Settled home electricity bill",
        "Paid monthly internet charges",
        "Paid mobile postpaid invoice",
        "Paid water supply invoice",
        "Paid gas utility invoice",
        "Paid building service fee",
        "Renewed television service package"
    ],

    "Education": [
        "Paid semester tuition fee",
        "Purchased university textbooks",
        "Paid online programming course fee",
        "Bought notebooks for classes",
        "Purchased stationery for university",
        "Paid examination registration fee",
        "Bought academic reference books",
        "Paid college admission charges",
        "Purchased study materials",
        "Paid computer science course fee",
        "Bought pens and notebooks",
        "Paid university laboratory charges",
        "Purchased an educational workbook",
        "Paid for online learning classes",
        "Bought mathematics textbooks",
        "Paid school monthly fee",
        "Purchased exam preparation material",
        "Paid certification examination fee",
        "Bought a scientific calculator for study",
        "Paid library membership fee",
        "Purchased educational software license",
        "Paid university registration charges",
        "Bought lecture notes and study guides",
        "Paid for a language learning course",
        "Purchased drawing supplies for class",
        "Paid academic workshop registration",
        "Bought a school uniform for student",
        "Paid tuition academy charges",
        "Purchased computer science books",
        "Paid for professional training",
        "Bought laboratory notebook",
        "Paid online course subscription for learning",
        "Purchased educational reference material",
        "Paid semester examination fee",
        "Bought stationery for school"
    ],

    "Health": [
        "Paid doctor consultation fee",
        "Purchased prescription medicines",
        "Paid hospital examination charges",
        "Bought vitamins from pharmacy",
        "Paid dental checkup fee",
        "Purchased medical bandages",
        "Paid laboratory blood test charges",
        "Bought pain relief medicine",
        "Paid eye specialist appointment",
        "Purchased prescribed tablets",
        "Paid for medical ultrasound",
        "Bought first aid supplies",
        "Paid clinic consultation charges",
        "Purchased cough syrup",
        "Paid physiotherapy session fee",
        "Bought medical thermometer",
        "Paid hospital admission charges",
        "Purchased allergy medication",
        "Paid diagnostic test charges",
        "Bought prescription glasses",
        "Paid dentist treatment bill",
        "Purchased antiseptic solution",
        "Paid medical scan charges",
        "Bought fever medicine",
        "Paid vaccination charges",
        "Purchased healthcare supplies",
        "Paid specialist doctor fee",
        "Bought blood pressure monitor",
        "Paid medical laboratory invoice",
        "Purchased skin treatment cream",
        "Paid eye examination charges",
        "Bought medical supplements prescribed by doctor",
        "Paid emergency clinic bill",
        "Purchased diabetes testing strips",
        "Paid hospital pharmacy bill"
    ],

    "Entertainment": [
        "Purchased cinema movie tickets",
        "Paid monthly Netflix subscription",
        "Bought concert admission ticket",
        "Paid gaming platform subscription",
        "Purchased a video game",
        "Paid for a music streaming subscription",
        "Bought tickets for a comedy show",
        "Paid bowling alley charges",
        "Purchased amusement park tickets",
        "Paid for a theatre performance",
        "Bought a cinema snack combo",
        "Paid online game credits",
        "Purchased a music album",
        "Paid for a live music event",
        "Bought tickets for a sports show",
        "Paid gaming cafe charges",
        "Subscribed to a movie streaming service",
        "Purchased an entertainment app subscription",
        "Paid for a weekend fun activity",
        "Bought tickets for a cultural festival",
        "Paid for karaoke session",
        "Purchased a board game for fun",
        "Paid for a theme park visit",
        "Bought a movie rental online",
        "Paid for a comedy club visit",
        "Purchased gaming accessories for entertainment",
        "Paid for a live concert",
        "Bought tickets for a magic show",
        "Paid for a recreational event",
        "Subscribed to an online gaming service",
        "Purchased a digital movie",
        "Paid for a music concert",
        "Bought a puzzle game",
        "Paid for an arcade visit",
        "Purchased event entry tickets"
    ]
}

additions = []

for category, descriptions in new_examples.items():
    for description in descriptions:
        additions.append({
            "description": description,
            "category": category
        })

new_df = pd.DataFrame(additions)

combined = pd.concat([df, new_df], ignore_index=True)

combined["description"] = combined["description"].astype(str).str.strip()
combined["category"] = combined["category"].astype(str).str.strip()

before = len(combined)
combined = combined.drop_duplicates(
    subset=["description"],
    keep="first"
).reset_index(drop=True)

combined.to_csv(path, index=False)

print("Original examples:", len(df))
print("New examples added:", len(combined) - len(df))
print("Final examples:", len(combined))
print("Duplicate descriptions removed:", before - len(combined))

print("\nFinal category distribution:")
print(combined["category"].value_counts().sort_index())

print("\nDataset saved:", path)
