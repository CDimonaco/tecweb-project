# A.N.D.R.A. - Backend 

Parte del progetto per l'esame di Tecnologie web,
Troviamo un servizio REST realizzato usando `Python 3`, `Flask`, `Flask-Restful`.

Per la persistenza dei dati mi sono affidato a mongodb, usato nell'api tramite il driver `pymongo`

## Cos'è A.N.D.R.A ?

A.N.D.R.A. è una dashboard per la gestione e il monitoraggio di un pool di sensori.

I sensori sono divisi in progetti, ogni utente ha diritto a 25 progetti.

Ogni sensore associato, avrà una propria api-key che potrà utilizzare per inviare le proprie rilevazioni al sistema,
con una semplice chiamata POST infatti, sarà possibile aggiungere una rilevazione effettuata in tempo reale.

Per ogni sensore sarà possibile consultare lo storico delle rilevazioni e avere dei grafici sulle rilevazioni dello stesso.

Tutto il codice è documentato in italiano.

E' inclusa una gestione di utenti e ruoli, con autenticazione JWT.

Tutte le dipendenze sono nel file `requirements.txt`

L'API è stata hostata su amazon AWS in un istanza EC2, è stato usato Gunicorn unito a nginx come reverse proxy.

Sulla stessa istanza è hostata anche l'app react, responsabile della parte frontend del sistema.


Carmine Di Monaco
Matricola 0124001236
