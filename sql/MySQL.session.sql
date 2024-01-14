SELECT *
FROM balotage.balotage;


-- Total votos por departamento

SELECT 
Departamento
,SUM(b.Total_Habilitados) AS Total_Habilitados
,SUM(b.Total_Habilitados) - SUM(b.Total_Votos_Observados) - SUM(b.Total_Anulados) - SUM(B.Total_EN_Blanco) AS Total_Validos
,ROUND((SUM(b.Total_Habilitados) - SUM(b.Total_Votos_Observados) - SUM(b.Total_Anulados) - SUM(B.Total_EN_Blanco))/ (SELECT SUM(Total_Habilitados) FROM balotage AS b2),2) AS procentaje_total_valido
FROM balotage.balotage AS b
GROUP BY Departamento
ORDER BY Total_Habilitados DESC;


-- Total Votos Candidatos por departamento

SELECT 
Departamento
,SUM(b.Total_Martinez_Villar) AS Total_Martinez_Villar
,ROUND(SUM(b.Total_Martinez_Villar)/ (SUM(b.Total_Martinez_Villar)+SUM(b.Total_Lacalle_Pou_Argimon)),2) AS porcentaje_martinez_villar
,SUM(b.Total_Lacalle_Pou_Argimon) AS Total_Lacalle_Pou_Argimon
,ROUND(SUM(b.Total_Lacalle_Pou_Argimon)/ (SUM(b.Total_Martinez_Villar)+SUM(b.Total_Lacalle_Pou_Argimon)),2) AS porcentaje_lacalle_argimon
FROM balotage.balotage AS b
GROUP BY Departamento;


-- Total Votos Candidatos 


SELECT 
SUM(b.Total_Martinez_Villar) AS Total_Martinez_Villar
,ROUND(SUM(b.Total_Martinez_Villar)/ (SUM(b.Total_Martinez_Villar)+SUM(b.Total_Lacalle_Pou_Argimon)),2) AS porcentaje_martinez_villar
,SUM(b.Total_Lacalle_Pou_Argimon) AS Total_Lacalle_Pou_Argimon
,ROUND(SUM(b.Total_Lacalle_Pou_Argimon)/ (SUM(b.Total_Martinez_Villar)+SUM(b.Total_Lacalle_Pou_Argimon)),2) AS porcentaje_lacalle_argimon
FROM balotage.balotage AS b;