albopretoriopa
==============

L'*Albo Pretorio* è "il **luogo** e lo spazio dove vengono affissi tutti quegli atti per i quali la legge impone la pubblicazione in quanto debbono essere portati a **conoscenza del pubblico**, come condizione necessaria per acquisire **efficacia** e quindi **produrre gli effetti previsti**" (vedi [Qualita PA](http://qualitapa.gov.it/relazioni-con-i-cittadini/open-government/strumenti-della-pa-digitale/albo-pretorio-on-line/)).

Nell'albo pretorio del Comune di Palermo:
* non posso inviare a un mio amico l'indirizzo della pagina web di una gara molto interessante, perché **non esiste un indirizzo univoco** per i singoli elementi dell'albo;
* non è prevista un'**iscrizione** ad una determinata categoria dell'albo e ricevere (ad esempio) per email un avviso automatico per ogni nuova pubblicazione;
* non potrò scoprire casualmente qualcosa di interessante pubblicato sull'albo, perché **non è indicizzato dai motori di ricerca** (credo che ci siano ragioni sensate legate al [diritto all'oblio](https://it.wikipedia.org/wiki/Diritto_all'oblio));
* non c'è un **canale social** in cui sono pubblicati i nuovi avvisi, e non si amplia la diffusione degli stessi;
* i contenuti dell'albo non sono pubblicati nella sezione **open data**.

Ho preso la cassetta degli attrezzi e ho costruito al momento, **per i soli  Avvisi di Gara**,  le seguenti cose:

* il **[canale twitter](https://twitter.com/albopretoriopa)** che pubblica ogni aggiornamento;
* il **[feed RSS](http://pipes.yahoo.com/pipes/pipe.run?_id=cf98396256f62f6364df2be5bf5b74e1&_render=rss&urlinput1=http%3A%2F%2Falbopretorio.comune.palermo.it%2Falbopretorio%2Fjsp%2Fhome.jsp%3Fmodo%3Dinfo%26info%3Dscelta_tipo_documento.jsp%26AP%3DAP%26TD%3D60%26ARECOD%3D70)** degli avvisi;
* una [ricetta IFTTT](https://ifttt.com/recipes/202623-inviami-un-email-per-ogni-avviso-di-gara-dell-albo-pretorio-del-comune-di-palermo) per ricevere un'**email** per ogni nuova pubblicazione;
* un **[file CSV](http://bit.ly/albopretoriopa_avvisi)** con gli ultimi avvisi di gara pubblicati (al momento non archivierò tutta la serie).

C'è un limite in tutto questo: non esistendo un indirizzo web - un URL - per il singolo avviso, non è possibile creare un link che porti in modo diretto all'elemento di interesse. Ho forzato pertanto il link ad una [sezione](http://albopretorio.comune.palermo.it/albopretorio/jsp/home.jsp?modo=info&info=scelta_tipo_documento.jsp&AP=AP&TD=60&ARECOD=70) dell'albo e starà poi ad ognuno entrare nella sottosezione "Avviso di Gara", e cercare per "Numero di Protocollo" o "Oggetto".
