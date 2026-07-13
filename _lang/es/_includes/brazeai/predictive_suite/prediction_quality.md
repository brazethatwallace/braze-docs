Para medir la precisión de tu modelo, la métrica _Calidad de predicción_ te mostrará la eficacia que parece tener este modelo de aprendizaje automático concreto cuando se prueba con datos históricos. Braze extrae los datos según los grupos que hayas especificado en la página de creación del modelo. El modelo se entrena con un conjunto de datos (el conjunto de "entrenamiento") y luego se prueba con un conjunto de datos nuevo e independiente (el conjunto de "prueba").

La predicción se volverá a entrenar cada dos semanas y se actualizará junto con la métrica _Calidad de predicción_ para mantener tus predicciones al día con los patrones de comportamiento más recientes de los usuarios. Además, cada vez que esto ocurra, las predicciones de las dos últimas semanas se contrastarán con los resultados reales de los usuarios. La _Calidad de predicción_ se calculará entonces a partir de estos resultados reales (en lugar de estimaciones). Se trata de un backtest automático (es decir, probar un modelo predictivo con datos históricos) para garantizar que la predicción es precisa en escenarios reales. La última vez que se produjo este reentrenamiento y backtesting se mostrará en la página **Predictions** y en la página de análisis de una predicción individual. Incluso una predicción en vista previa realizará este backtest una vez después de su creación. De este modo, puedes estar seguro de la precisión de tu predicción personalizada, incluso con la versión gratuita de la característica.

{% details Ejemplo de calidad de predicción %}

Por ejemplo, si el 20 % de tus usuarios suelen abandonar de media, y eliges un subconjunto aleatorio del 20 % de tus usuarios y los etiquetas como usuarios que abandonan al azar (lo sean realmente o no), esperarías identificar correctamente solo al 20 % de los usuarios que realmente abandonan. Eso es adivinación aleatoria. Si el modelo solo lo hiciera así de bien, el lift sería 1 para este caso.

Si, por el contrario, el modelo te permitiera enviar mensajes al 20 % de los usuarios y, al hacerlo, captar a todos los "verdaderos" usuarios que abandonan y a nadie más, el lift sería 100 % / 20 % = 5. Si graficas esta relación para cada proporción de los usuarios con mayor probabilidad de abandono a los que podrías enviar mensajes, obtendrás la [curva de lift](https://en.wikipedia.org/wiki/Lift_(data_mining)).

Otra forma de entender la calidad del lift (y también la _Calidad de predicción_) es cuánto avanza la curva de lift de la predicción entre la adivinación aleatoria (0 %) y la perfección (100 %) a la hora de identificar a los usuarios que abandonan en el conjunto de prueba. Para consultar el artículo original sobre la calidad del lift, consulta [Measuring lift quality in database marketing](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}

### Cómo se mide {#how-its-measured}

Nuestra medida de la _Calidad de predicción_ es la [calidad del lift](https://dl.acm.org/doi/10.1145/380995.381018). En general, "lift" se refiere al aumento de la tasa o porcentaje de un resultado exitoso, como una conversión. En este caso, el resultado exitoso es identificar correctamente a un usuario que habría abandonado. La calidad del lift es el lift medio que proporciona la predicción en todos los tamaños de audiencia posibles para el envío de mensajes al conjunto de prueba. Este enfoque mide cuánto mejor es el modelo en comparación con la adivinación aleatoria. Con esta medida, 0 % significa que el modelo no es mejor que adivinar al azar quién abandonará, y 100 % indica un conocimiento perfecto de quién abandonará.

### Rangos recomendados {#recommended-ranges}

Esto es lo que recomendamos para distintos rangos de _Calidad de predicción_:

| Rango de calidad de predicción (%) | Recomendación |
| ---------------------- | -------------- |
| 60 - 100 | Excelente. Precisión de primer nivel. Es poco probable que cambiar las definiciones de audiencia ofrezca beneficios adicionales. |
| 40 - 60 | Bueno. Este modelo producirá predicciones precisas, pero probar una configuración de audiencia diferente podría dar mejores resultados. |
| 20 - 40 | Aceptable. Este modelo puede ofrecer precisión y valor, pero considera probar otras definiciones de audiencia para ver si aumentan el rendimiento. |
| 0 - 20 | Deficiente. Te recomendamos que cambies las definiciones de audiencia y vuelvas a intentarlo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rangos recomendados" }