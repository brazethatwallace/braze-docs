---
nav_title: Future Anthem
article_title: Future Anthem
description: "Cet article de référence décrit le partenariat entre Braze et Future Anthem, une plateforme d'intelligence artificielle en temps réel pour la personnalisation des paris sportifs et de l'iGaming."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> La plateforme d'intelligence artificielle en temps réel de [Future Anthem](https://www.futureanthem.com/) permet la personnalisation dans les domaines du sport, du casino, du bingo et de la loterie. Les clients de Braze peuvent enrichir les profils des joueurs avec des attributs spécifiques au secteur, notamment le jeu préféré, l'équipe préférée, le score d'engagement, la recommandation du prochain pari, le prochain pari attendu, et bien plus encore.
>
> Fournis via les expériences en temps réel, les audiences dynamiques et les recommandations de contenu, chaque attribut repose sur le comportement en direct or en ligne/en production/instantané des joueurs, ce qui permet aux clients de Braze d'agir au bon moment.

_Cette intégration est maintenue par Future Anthem._

{% alert important %}
Cette fonctionnalité est actuellement en accès anticipé. Contactez l'équipe Customer Success de Future Anthem pour commencer.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Future Anthem | Un compte Future Anthem. |
| Clé API REST Braze | Une clé API REST Braze avec la permission pour l'[endpoint `users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Vous pouvez la créer dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | L'[endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) de Braze qui correspond à votre instance, par exemple `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Grâce à cette intégration, vous pouvez :

- Identifier les joueurs ayant un score d'engagement élevé et les cibler avec des offres personnalisées, telles que des promotions exclusives ou des récompenses VIP.
- Suggérer des jeux similaires en fonction des jeux qu'un joueur apprécie déjà.

## Intégration {#integration}

L'équipe Customer Success de Future Anthem vous aide à mettre en place votre intégration. Contactez votre interlocuteur Customer Success chez Future Anthem, qui vous aidera à identifier les attributs les plus pertinents à envoyer à Braze.

| Exemples d'attributs dans Future Anthem | Exemples d'attributs dans Braze |
| ----------------------------------- | --------------------------- |
| ![Tableau de bord Future Anthem affichant les attributs de profil d'un joueur.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %}) | ![Profil utilisateur Braze affichant les attributs d'objet personnalisé synchronisés depuis Future Anthem.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Intégration" }

## Attributs personnalisés Braze {#braze-custom-attributes}

Voici les attributs personnalisés Braze disponibles. Pour plus d'informations, consultez [Future Anthem : Mise en route](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Bet Recommendations %}

| Sous-catégorie | Exemple (JSON) | Type de données |
| ----------- | ---------------- | --------- |
| Préférences de l'utilisateur | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objet |
| Recommandations de paris simples | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objet |
| Recommandations de paris accumulateurs (libellés d'événements) | `{"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}` | Objet |
| Recommandations de paris accumulateurs (cotes numériques) | `{"Bet_1": 1.5, "Bet_2": 2}` | Objet |
| Recommandations de paris Bet Builder | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}` | Objet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés Braze" }

{% endtab %}
{% tab Bonus Recommendations %}

| Sous-catégorie | Exemple | Type de données |
| ----------- | ------- | --------- |
| NGR (chiffre d'affaires net des jeux, durée de vie) | 2232 | Nombre |
| NGR14 (chiffre d'affaires net des jeux, 14 derniers jours d'activité) | 42 | Nombre |
| Score de rentabilité du joueur | 130 | Nombre |
| Score d'engagement | 0.78 | Nombre |
| Score de risque d'attrition | 0.02 | Nombre |
| Date estimée du prochain pari | 2024-08-29 | Date |
| Recommandation de valeur du bonus Bet and Get | 20 | Nombre |
| Autres recommandations de valeur de bonus | 0 | Nombre |
| CLTV futur | 3126 | Nombre |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés Braze" }

{% endtab %}
{% tab Game Recommendations %}

| Sous-catégorie | Exemple | Type de données |
| ----------- | ------- | --------- |
| Recommandé pour vous | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | Tableau |
| Jeux préférés | Fishin' Frenzy | Tableau |
| Nouveaux jeux recommandés | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | Tableau |
| Des joueurs comme vous jouent (filtrage collaboratif) | Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Tableau |
| Parce que vous avez joué (similarité de jeu) | Fluffy Favourites 2, Luck O' the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Tableau |
| À suivre (séquençage de jeux) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin' Bigger Pots of Gold | Tableau |
| Jeux populaires | Temple of Iris, Fishin' Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | Tableau |
| Jeux en vogue | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Tableau |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés Braze" }

{% endtab %}

{% tab Player Cluster %}

| Sous-catégorie | Exemple | Type de données |
| ----------- | ------- | --------- |
| Cluster auquel appartient le joueur | High Value Game Diverse | Chaîne de caractères |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés Braze" }

{% endtab %}

{% tab Player Sustain (risque potentiel du joueur) %}

| Sous-catégorie | Exemple | Type de données |
| ----------- | ------- | --------- |
| Score de risque | 0.5 | Nombre |
| Joueur à risque | True | Valeur booléenne |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés Braze" }

{% endtab %}
{% endtabs %}