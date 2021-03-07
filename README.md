# Objetivo: Estudo

# Voos-ANAC
Para essa solução utilizei Python, SSIS, SQL Server e Power BI.
Obs: AS conexões do Power BI foram criadas como Import de Dados, por isso não há a necessidade da base SQL.


SQL Server 2019:
Criei um Data Mart com modelo Star Schema.
Link do arquivo: https://1drv.ms/u/s!AjdRhRYihmCBgRKT0F8e76t9T46k?e=Tn3oC3

SSIS:
Carreguei os registros no Data Mart a partir do arquivo csv.

Python:
Busquei a latitude e logitude das cidades de origem e destino do voos gravei o resultado no Data Mart.

Power BI:
Fiz algumas análises sobre os voos realizados, cancelados e os voos com atraso.
Link do arquivo: https://1drv.ms/u/s!AjdRhRYihmCBgRKT0F8e76t9T46k?e=Tn3oC3

