# RESUMEN INFORME CASO DE ESTUDIO SOBRE RECURSOS HUMANOS 
* DIEGO ALEJANDRO SAAVEDRA VALDIVIESO
* NILSON SUAREZ HERNANDEZ
* DAYAN EDUARDO MARÍN QUINTERO

---------------------------------------------------
<p align="center">
MATERIA: APLICACIONES DE LA ANALÍTICA
<p align="center">
PROFESOR: JUAN CAMILO ESPAÑA LOPERA
<p align="center">
INGENIERÍA INDUSTRIAL
<p align="center">
FACULTAD DE INGENIERÍA 
<p align="center">
UNIVERSIDAD DE ANTIOQUIA
<p align="center">
2023

## Problema de Negocio
El problema de negocio que enfrenta esta empresa se relaciona con la alta tasa de retiros de empleados, que está en torno al 15% anual. Esta situación tiene varias implicaciones negativas y costosas para la empresa.
## Impactos Negativos Actuales
La alta rotación de empleados conlleva costos financieros considerables, retrasos en proyectos, una mayor carga de trabajo en la selección de personal, sobrecarga a los empleados restantes y resulta en la pérdida de conocimiento y experiencia valiosa
## Objetivo Principal
Reducir la tasa de retiros de empleados en la empresa, actualmente se encuentra en un 15% anual, con el fin de mitigar los costos asociados y minimizar las implicaciones negativas en el funcionamiento de la organización.
## Beneficios Esperados 
Reducir la rotación de empleados conlleva ahorros financieros, estabilidad laboral, evita retrasos en proyectos y mejora la satisfacción de clientes y empleados al conservar el conocimiento y la experiencia.
## Métricas de Éxito 
La reducción de la tasa de retiros anual, respaldada por la precisión de las predicciones de nuestro modelo, no solo tiene un impacto positivo en los costos operativos y la eficiencia laboral, sino que también garantiza el mantenimiento de plazos y la calidad en proyectos. Al retener a nuestros empleados clave, estamos fortaleciendo la retención de conocimiento y experiencia dentro de la organización, lo que contribuye significativamente al crecimiento y éxito continuo de la empresa.
## Problema Analítico
Analizar las variables generales que influyen en la deserción de los empleados y tomar acciones correctivas sobre estas variables con el fin de lograr condiciones óptimas en cuanto a la satisfacción de los empleados y mitigar las consecuencias que esto trae sobre la empresa. Así mismo realizar predicciones para ver si el empleado abandonará o no la empresa con el fin de tomar acciones preventivas sobre un empleado puntual que muestre índices de inconformidad. En este caso es de suma importancia realizar dicho proceso con inteligencia artificial dado que se ahorraría mucho tiempo al procesar los más de 4000 registros que al realizarlos de forma manual
## Características más Importantes del Modelo
![Interpretación Librería SHAP](/images/features.png) 
Nota: Nos referimos a “impacto”, cuando la variable arrastra fuertemente la predicción al abandono del empleado (ya que en algunos casos la variable no tuvo tantos registros para quedar en primeros lugares pero los pocos que tuvo impactaron fuertemente, es por eso que no siempre están en los primeros lugares, pero si la cola de color rojo se extiende mostrando su impacto. (si no mencionamos impacto, es porque es un impacto bajo o medio)

En resumen podemos decir que: tiempos altos en la empresa (impacto muy fuerte), pocos años trabajados en su vida (impacto muy fuerte), que haya trabajado en muchas compañías (impacto fuerte), que sea joven, que tenga una satisfacción y un ambiente laboral bajo, que tenga pocos años con su jefe actual, que viva cerca de la empresa (impacto fuerte), que hayan pasado muchos años desde el último ascenso (impacto muy fuerte), que tenga pocos años en la compañía, que sean solteros, que no califique bien su relación trabajo-vida, que viajen con frecuencia, que tenga pocas funciones en la empresa, que tengan un porcentaje de aumento salarial alto, que haya tenido pocas capacitaciones el último año (impacto fuerte) son el perfil de un empleado que abandona la empresa.
## Análisis de Resultados
Tiempos altos en las empresas generan fatiga laboral y conduce al abandono de la empresa, que sean jóvenes se relaciona con otras variables, porque si son jóvenes, llevan pocos años trabajados en su vida, tienen pocos años con su jefe, pocos años en la compañía y posiblemente sean solteros, su explicación puede tener sentido ya que si son jóvenes están iniciando su vida laboral y están buscando experiencia laboral antes de quedarse fijos en una compañía. 

Que haya trabajado en muchas compañías, se explica porque si es un empleado que ha trabajado en muchas compañías es un indicio que no tiene una estabilidad laboral por lo tanto puede tender a renunciar en la empresa actual. El ambiente y satisfacción laboral baja, es muy común que cuando los empleados no están satisfechos tienden a renunciar. 

Posiblemente los empleados no están sintiendo valor en dicha empresa, al no ser ascendidos, asignarles pocas funciones y que obtienen pocas capacitaciones al año, por eso pueden estar buscando otros trabajos
## Diseño Despliegue Modelo
Se tendrá un proceso completamente automatizado en el que se tomará la base de datos de empleados del mes anterior, vigilada por RH y será enviada al modelo alojado en el sitio web corporativo, el cuál solo tendrá acceso un área nueva llamada “RH Analytics”, la cuál consta de un equipo de 5 personas que está conformado por científicos de datos y personal de recursos humanos para juntos crear estrategias y hacer capacitaciones a los empleados. Dicho tablero mostrará indicadores de deserción, además, como se va a ir actualizando mensualmente, se verá el efecto de las estrategias implementadas, logrando no solo un impacto en la deserción sino también un impacto en la empresa de manera global
## Diseño Monitoreo Modelo
Será re-entrenado automáticamente cada semestre y mediante un tablero digital alojado en el mismo sitio web corporativo, podrá tener acceso el área de “ RH Analytics”, pero este tablero entregará información respecto al modelo: curvas de aprendizaje, matrices de confusión y métricas del modelo, para que puedan comprobar y decidir si a ese modelo entrenado se le deben hacer ajustes o si está apto para el despliegue
## Conclusiones:
* Se tiene un modelo con un 96.3 % de confiabilidad con el cuál se crearán estrategias de la mano de recursos humanos para impactar directamente la deserción de empleados
* Al implementar dichas estrategias estamos seguros que se logrará reducir la deserción laboral
* Es de suma importancia re entrenar el modelo semestralmente con el fin de ir monitoreando su desempeño 
## Recomendaciones
* Es importante recordar que las jornadas laborales de los empleados deben ser estables y no exceder un nivel elevado de trabajo
* Crear estrategias para que los jóvenes perduren en la empresa, utilizando incentivos como bonos para postgrado, créditos para vivienda, becas, etc. 
* Evitar contratar personal que ha trabajado en muchas empresas o preguntar cuál fue la causa de su renuncia en sus puestos de trabajo
* Implementar en la empresa encuestas más detalladas y con mayor frecuencia de satisfacción laboral y ambiente laboral para conocer por qué estas están en promedio tan bajas y así evitar la deserción laboral
* Brindar valor a los empleados, asignarle funciones relacionadas con su puesto de trabajo, más capacitaciones al año, esto genera que los empleados se sientan satisfechos
* Revisar que empleados son posibles candidatos a un ascenso y crear una ceremonia con los empleados para motivarlos

## Informe Completo
 https://github.com/diegosaaval/human-resources/blob/main/INFORME_FINAL.pdf 
