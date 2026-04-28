---
nav_title: Diferencia entre bloquear y eliminar
article_title: Diferencia entre bloquear y eliminar
page_order: 2

page_type: solution
description: "Este artículo de ayuda te explica la diferencia entre el bloqueo y la eliminación de atributos."
---

# Diferencia entre bloquear y eliminar {#difference-between-blocklisting-and-deleting}

Para entender la diferencia entre bloquear y eliminar datos personalizados en Braze, revisa los resultados de cada acción:

- **Bloqueo:** Si se bloquean atributos personalizados, eventos o compras, permanecerán en los perfiles de usuario, pero Braze dejará de procesar datos nuevos para esos objetos.
- **Eliminación:** Si se eliminan atributos personalizados, eventos o compras, Braze eliminará esos datos de los perfiles de usuario. Los atributos personalizados y eventos eliminados pasan al estado `Trashed` durante siete días, periodo en el que puedes restaurarlos. Después de siete días, Braze los elimina de forma permanente. La eliminación tampoco impide la entrada de datos nuevos, así que asegúrate de que los datos ya no se estén enviando a través de tu SDK, API o importaciones CSV antes de eliminarlos.

## ¿Qué debo hacer? {#which-should-i-do}

Para llevar a cabo el bloqueo, Braze tendrá que enviar la información de bloqueo al dispositivo de cada usuario, y será una operación que consumirá muchos datos, algo que idealmente intentamos evitar. Además, si la lista es demasiado grande (> 100 atributos, eventos o compras), tu aplicación puede empezar a ralentizarse.

Si ya no piensas enviar atributos a Braze, la eliminación sería la solución recomendada.

Independientemente de la opción que elijas, los atributos personalizados, eventos y compras que elimines ya no aparecerán en la página **Manage Workspace**, lo que los quita como filtros de segmento. Si eliminas datos personalizados, Braze eliminará esos datos a nivel de usuario de los perfiles.