import mysql.connector
from difflib import get_close_matches

def execute_query(cursor, word, is_search = False):
    if is_search:
        query = f"SELECT word FROM dictionary WHERE LENGTH(word) > {len(word)-2} and LENGTH(word) < {len(word)+2}"
    else:
        query = f"SELECT definition FROM dictionary WHERE word LIKE '{word}'"
    cursor.execute(query)
    results = [t[0] for t in cursor.fetchall()]
    return results

def find_definition(cursor):
    input_word = input("Enter word:\n")
    results = execute_query(cursor, input_word)

    if results:
        for result in results:
            print('**', result)
    elif len(get_close_matches(input_word, execute_query(cursor, input_word, True), cutoff=0.8)) > 0:
        close_word = get_close_matches(input_word, execute_query(cursor, input_word, True), cutoff = 0.8)[0]
        answer = input("Did you mean %s? If yes, type Y; if no, type N:\n " % close_word)
        if answer == "Y":
            for result in execute_query(cursor, close_word):
                print('**', result)
        elif answer == "N":
            print("The word doesn't exist. Please double check it.")
        else:
            print("We couldn't figure out what you were trying to say. Please give it another shot.")
    else:
        print("The word doesn't exist. Please double check it.")

con = mysql.connector.connect(user = "root",
                              password = "your_password",
                              host = "localhost",
                              database = "thesaurus")
cursor = con.cursor()
find_definition(cursor)