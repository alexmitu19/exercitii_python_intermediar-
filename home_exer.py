#Exercitiu -> Adaugare verificari de tip.

# Titlu: Simulator simplu de testare a conexiunii la o baza de date
# creati exceptii customizate pt urmatoarele scenarii:
# 1. NetworkError, 2. AuthenticationError, 3. SQLError, 4. MaxRetriesExceededError
# conditiile de "ridicare" a erorilor este la latitudinea voastra : fie sa aiba o logica, fie sa contina date random
# implementati un mecanism de retry cu maxim 10 incercari
# fiecare incercare de conectare este logata (printata) si se arunca eroarea
# daca totusi conexiunea are loc cu succes, afisati un mesaj de bun venit
# 2 functii : def simulare_conexiune();  def conectare_bazadedate(max_retries=10);