import random
import re

elenco_studenti = [
    {"nome": "Marco", "cognome": "Arlotti"},
    {"nome": "Angelo", "cognome": "Berlini"},
    {"nome": "Luca", "cognome": "Bernardini"},
    {"nome": "Alberto", "cognome": "Bruscolini"},
    {"nome": "Francesco", "cognome": "Cervesi"},
    {"nome": "Marco", "cognome": "Clementi"},
    {"nome": "Romeo", "cognome": "D'Angelosante"},
    {"nome": "Alessandro", "cognome": "Del Baldo"},
    {"nome": "Ibragimov", "cognome": "Kamil"},
    {"nome": "Amin", "cognome": "Kriouech"},
    {"nome": "Simon", "cognome": "Kola"},
    {"nome": "Matteo", "cognome": "Massa"},
    {"nome": "Cristian", "cognome": "Monticelli"},
    {"nome": "Eldar", "cognome": "Nedria"},
    {"nome": "Lorenzo", "cognome": "Pezzolesi"},
    {"nome": "Luca", "cognome": "Pontellini"},
    {"nome": "Nicolo", "cognome": "Romagna"},
    {"nome": "Alessandro", "cognome": "Sanchi"},
    {"nome": "Luca", "cognome": "Santini"},
    {"nome": "Diego", "cognome": "Torsani"},
]


def estrai_3_studenti(elenco, pattern=".*"):
    """
    Estrae 3 studenti a caso dall'elenco usando un'espressione regolare.
    Il pattern di default ".*" matcha tutti gli studenti.
    """
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Filtra gli studenti che matchano il pattern
    studenti_filtrati = []
    for studente in elenco:
        nome_cognome = f"{studente['nome']} {studente['cognome']}"
        if regex.search(nome_cognome):
            studenti_filtrati.append(studente)
    
    # Se ci sono meno di 3 studenti filtrati, ritorna quelli trovati
    # Se ce ne sono 3 o più, estrae 3 a caso
    if len(studenti_filtrati) <= 3:
        studenti_selezionati = studenti_filtrati
    else:
        studenti_selezionati = random.sample(studenti_filtrati, 3)
    
    return studenti_selezionati


if __name__ == "__main__":
    print("SISTEMA DI ESTRAZIONE 3 NOMINATIVI PER INTERROGAZIONE")
    print("=" * 60)
    
    # Estrae 3 studenti usando un'espressione regolare
    # Esempi di pattern:
    # ".*" - matcha tutti gli studenti
    # "L" - matcha studenti con "L" nel nome o cognome
    # "^[A-M]" - matcha studenti che iniziano con A-M
    
    pattern = "(.*)"  # Pattern 
    
    studenti = estrai_3_studenti(elenco_studenti, pattern)
    
    print(f"\nPattern regex: '{pattern}'")
    print(f"Studenti selezionati per l'interrogazione ({len(studenti)}):")
    for idx, studente in enumerate(studenti, 1):
        print(f"  {idx}. {studente['nome']} {studente['cognome']}")

    

















