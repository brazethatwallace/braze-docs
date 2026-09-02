---
nav_title: Himno del futuro
article_title: Himno del futuro
description: "Este artículo de referencia describe la asociación entre Braze y Future Anthem, una plataforma de IA en tiempo real para la personalización de apuestas deportivas e iGaming."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Himno del futuro {#future-anthem}

> La plataforma de IA en tiempo real de [Future Anthem](https://www.futureanthem.com/) impulsa la personalización en deportes, casino, bingo y lotería. Los clientes de Braze pueden enriquecer los perfiles de jugador con atributos específicos del sector, como juego favorito, equipo favorito, puntuación de interacción, recomendación de próxima apuesta, próxima apuesta esperada y mucho más.
>
> Entregados a través de experiencias en tiempo real, audiencias dinámicas y recomendaciones de contenido, todos los atributos se construyen sobre el comportamiento en vivo del jugador, para que los clientes de Braze puedan actuar en el momento.

_Esta integración es mantenida por Future Anthem._

{% alert important %}
Esta característica está actualmente en acceso anticipado. Ponte en contacto con el equipo de éxito del cliente de Future Anthem para empezar.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Future Anthem | Una cuenta de Future Anthem. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permiso para el [punto de conexión `users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Puedes crearla en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | El [punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) de Braze que coincida con tu instancia, como `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Con esta integración, puedes:

- Identificar a los jugadores con altas puntuaciones de interacción y dirigirte a ellos con ofertas personalizadas, como promociones exclusivas o recompensas VIP.
- Sugerir juegos similares basándote en los juegos que un jugador ya disfruta.

## Integración {#integration}

El equipo de éxito del cliente de Future Anthem te ayuda a configurar tu integración. Ponte en contacto con tu contacto de éxito del cliente de Future Anthem y te ayudarán a identificar los atributos más relevantes para enviar a Braze.

| Ejemplo de atributos en Future Anthem | Ejemplo de atributos en Braze |
| ----------------------------------- | --------------------------- |
| ![Dashboard de Future Anthem mostrando atributos de perfil de un jugador.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %}) | ![Perfil de usuario de Braze mostrando atributos de objeto personalizado sincronizados desde Future Anthem.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integración" }

## Atributos personalizados de Braze {#braze-custom-attributes}

Estos son los atributos personalizados de Braze disponibles. Para más información, consulta [Future Anthem: Primeros pasos](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Recomendaciones de apuestas %}

| Subcategoría | Ejemplo (JSON) | Tipo de datos |
| ----------- | ---------------- | --------- |
| Preferencias del usuario | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objeto |
| Recomendaciones de apuestas simples | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objeto |
| Recomendaciones de apuestas acumuladoras (etiquetas de eventos) | `{"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}` | Objeto |
| Recomendaciones de apuestas acumuladoras (cuotas numéricas) | `{"Bet_1": 1.5, "Bet_2": 2}` | Objeto |
| Recomendaciones de constructor de apuestas | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}` | Objeto |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Braze" }

{% endtab %}
{% tab Recomendaciones de bonos %}

| Subcategoría | Ejemplo | Tipo de datos |
| ----------- | ------- | --------- |
| NGR (ingresos netos de juego, de por vida) | 2232 | Número |
| NGR14 (ingresos netos de juego, últimos 14 días de actividad) | 42 | Número |
| Puntuación de rentabilidad del jugador | 130 | Número |
| Puntuación de interacción | 0.78 | Número |
| Puntuación de riesgo de abandono | 0.02 | Número |
| Fecha estimada de la próxima apuesta | 2024-08-29 | Tiempo |
| Recomendación de valor de bono apuesta y consigue | 20 | Número |
| Otras recomendaciones de valor de bono | 0 | Número |
| CLTV futuro | 3126 | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Braze" }

{% endtab %}
{% tab Recomendaciones de juegos %}

| Subcategoría | Ejemplo | Tipo de datos |
| ----------- | ------- | --------- |
| Recomendado para ti | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | Matriz |
| Juegos favoritos | Fishin' Frenzy | Matriz |
| Nuevos juegos recomendados | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | Matriz |
| Jugadores como tú están jugando (filtrado colaborativo) | Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Matriz |
| Porque jugaste (similitud de juegos) | Fluffy Favourites 2, Luck O' the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Matriz |
| A continuación (secuenciación de juegos) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin' Bigger Pots of Gold | Matriz |
| Juegos populares | Temple of Iris, Fishin' Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | Matriz |
| Juegos en tendencia | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Matriz |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Braze" }

{% endtab %}

{% tab Clúster de jugador %}

| Subcategoría | Ejemplo | Tipo de datos |
| ----------- | ------- | --------- |
| Muestra en qué clúster se encuentra el jugador | High Value Game Diverse | Cadena |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Braze" }

{% endtab %}

{% tab Sustain del jugador (riesgo potencial del jugador) %}

| Subcategoría | Ejemplo | Tipo de datos |
| ----------- | ------- | --------- |
| Puntuación de riesgo | 0.5 | Número |
| Jugador arriesgado | True | Booleano |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Braze" }

{% endtab %}
{% endtabs %}