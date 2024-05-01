import spacy
import mysql.connector
import spacy_transformers
import re
# Load the spaCy model
nlp = spacy.load("model/model_trf_3")


def extract_batches(input_string):
    # Define regular expression pattern to match year formats (e.g., 2023, '23)
    year_pattern = r'(\b20\d{2}\b|\b\d{2}\b)'    
    matches = re.findall(year_pattern, input_string)
    batches = set()
    for match in matches:
        # Ensure the year is in four-digit format
        if len(match) == 2:
            match = '20' + match
        batches.add(match)
    return batches

# Connect to MySQL database
def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="ttt"
    )
    return mydb

# Function to extract entities from text
# def extract_entities(text):
#     doc = nlp(text)
#     entities = {"MESSAGE": text}
#     entities['BATCHES'] = extract_batches(text)
#     extracted_types = set()  # Keep track of extracted entity types
#     for ent in doc.ents:
#         # Check if entity type has already been extracted
#         if ent.label_ not in extracted_types:
#             entities[ent.label_] = entities.get(ent.label_, []) + [ent.text]
#             extracted_types.add(ent.label_)  # Add entity type to set
#     return entities

def extract_entities(text):
    # Placeholder for extracted entities
    entities = {"MESSAGE": text}
    
    # Use the spaCy model to process the text
    doc = nlp(text)
    
    # Extract named entities and add the first occurrence of each entity type to the entities dictionary
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = ent.text
    return entities


# Function to create entities table if not exists
def create_entities_table(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS entities (
            id INT AUTO_INCREMENT PRIMARY KEY,
            MESSAGE TEXT,
            COMPANY VARCHAR(255),
            ROLE VARCHAR(255),
            BATCH VARCHAR(255),
            `APPLY LINK` TEXT
        )
    """)
    mydb.commit()
    mycursor.close()

# Function to insert entities into MySQL database
def insert_entities(entities, mydb):
    mycursor = mydb.cursor()
    sql = "INSERT INTO alldata (batch, apply_link, company_name, roles, discription,un) VALUES (%s, %s, %s, %s, %s,%s)"
    # Prepare a list to hold the values to be inserted
    values = [
        entities.get("BATCH", "N/A"),
        entities.get("APPLY LINK", "N/A"),
        entities.get("COMPANY", "N/A"),  # Take the first value if exists, otherwise 'N/A'
        entities.get("ROLE", "N/A"),
        entities.get("MESSAGE", "N/A")
    ]
    values.append(values[0]+values[1])
    values = tuple(values)
    mycursor.execute(sql, values)
    mydb.commit()
    mycursor.close()














