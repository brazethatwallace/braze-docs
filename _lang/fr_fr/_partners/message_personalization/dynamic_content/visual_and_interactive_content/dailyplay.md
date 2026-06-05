---
nav_title: DailyPlay
article_title: DailyPlay
description: "Découvrez comment connecter les jeux de marque et les récompenses DailyPlay à Braze pour synchroniser les données de jeu, segmenter les audiences et déclencher des campagnes personnalisées."
alias: /partners/dailyplay/
page_type: partner
search_tag: Partner
---

# DailyPlay

> [DailyPlay](https://dailyplay.ai/) est une plateforme de gamification. Utilisez-la pour lancer des jeux de marque personnalisés et des systèmes de récompenses intégrés qui renforcent l'engagement et améliorent la rétention.

*Cette intégration est maintenue par DailyPlay.*

## À propos de cette intégration {#about-this-integration}

L'intégration de Braze et DailyPlay vous permet de déployer et de suivre les performances des jeux et des récompenses à travers les segments d'audience. Les jeux et systèmes de récompenses de DailyPlay fonctionnent avec le moteur d'orchestration de Braze afin que vous puissiez transformer des audiences passives en participants actifs.

Vous pouvez envoyer des jalons de jeu, des échanges de récompenses et des indicateurs d'engagement à Braze pour créer des segments d'audience et déclencher des messages automatisés cross-canal basés sur le comportement en jeu. Avec cette intégration, vous pouvez :

- **Enrichir les profils utilisateur :** Transmettre des indicateurs de jeu, des scores et des statuts de récompenses aux profils utilisateur dans Braze.
- **Débloquer une segmentation avancée :** Créer des segments d'audience basés sur le comportement en jeu, comme les meilleurs scores, les gagnants récents ou les utilisateurs proches de débloquer une récompense.
- **Automatiser des campagnes en temps réel :** Déclencher des messages cross-canal personnalisés (push, e-mail, in-app) basés sur les interactions de jeu pour favoriser le jeu répété, la fidélité à la marque et une valeur vie client plus élevée.

## Cas d'utilisation {#use-cases}

- **Réengager les clients inactifs :** Envoyer un lien vers un jeu avec une chance de gagner une récompense de réduction pour les clients inactifs.
- **Activité autour des produits et tendances :** Créer des jeux personnalisés qui mettent en avant un nouveau produit ou une saison de fêtes, une tendance ou un événement.
- **Déployer des jeux ciblés :** Combiner la segmentation et le ciblage de Braze avec la personnalisation de DailyPlay pour créer du contenu de jeu engageant pour différents objectifs et résultats.
- **Onboarding et activation :** Intégrer un lien vers un jeu DailyPlay de type grattage ou révélation instantanée dans votre série de bienvenue Braze pour inciter à un premier achat ou à la complétion du profil.
- **Rétention et fidélité :** Lorsqu'un consommateur atteint un jalon de fidélité ou effectue une action clé suivie dans Braze, déclencher un jeu DailyPlay personnalisé qui célèbre sa réussite et débloque des récompenses spécifiques à son niveau.
- **Prévention de l'attrition et reconquête :** Identifier les utilisateurs qui se désengagent dans Braze, puis proposer un jeu DailyPlay à faible friction pour recapter leur attention et les ramener vers votre application ou site.

## Conditions préalables {#prerequisites}


| Condition | Description |
| --- | --- |
| Compte DailyPlay | Un compte DailyPlay est requis pour utiliser cette intégration. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. Créez cette clé dans Braze sous **Settings** > **APIs and Identifiers** > **API Keys**. Pour plus d'informations, consultez [Clés API]({{site.baseurl}}/api/api_key/). |
| Endpoint REST Braze | L'URL de l'endpoint REST pour [votre instance Braze]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

### Étape 1 : Créer une connexion {#step-1-create-a-connection}

1. Dans le [tableau de bord DailyPlay](https://app.dailyplay.ai/connections), accédez à la page **Connections** et sélectionnez **Add Connection**.

![Page Connections de DailyPlay listant les connexions Braze actives et les statistiques de déclencheurs.]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. Sous **Provider**, choisissez **Braze**. Saisissez un nom, votre clé API REST Braze, l'App ID et l'endpoint REST, puis sélectionnez **Create Connection**.

![Fenêtre modale Add Connection de DailyPlay avec Braze sélectionné et les champs d'identification pour la clé API, l'App ID et l'endpoint REST.]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### Étape 2 : Créer un stream {#step-2-create-a-stream}

Accédez à la page **Streams** et créez un nouveau stream.

1. Ajoutez la connexion Braze que vous avez créée à l'étape 1 au nouveau stream.
2. Configurez les événements déclencheurs à suivre, tels que **Stream Access**, **Play Start**, **Play Complete** et **Prize Redemption**.
3. Créez et ajoutez des jeux au stream.
4. Copiez le code d'intégration Braze pour le stream.

![Fenêtre modale Manage Connections de DailyPlay affichant les événements déclencheurs Braze et le code d'intégration pour les modèles d'e-mail Braze.]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### Étape 3 : Créer une campagne dans Braze {#step-3-create-a-campaign-in-braze}

Collez le code de l'étape 2 dans votre campagne dans Braze.

Lorsque les utilisateurs jouent à des jeux dans le stream, DailyPlay déclenche un événement et l'envoie à Braze via votre endpoint REST Braze.

### Étape 4 : Inspecter les actions et élargir votre entonnoir {#step-4-inspect-actions-and-expand-your-funnel}

Les utilisateurs qui effectuent des actions dans les streams DailyPlay reçoivent des attributs personnalisés et des événements personnalisés sur leur profil Braze.

Créez une [campagne]({{site.baseurl}}/user_guide/messaging/campaigns/) ou un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) avec un déclencheur [basé sur une action]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) qui utilise les événements personnalisés ou attributs personnalisés DailyPlay requis pour votre cas d'utilisation.

## Utiliser DailyPlay avec Braze {#use-dailyplay-with-braze}

Pour engager un segment de clients spécifique, suivez ces étapes après avoir terminé la configuration de l'intégration.

### Étape 1 : Configurer DailyPlay {#step-1-set-up-your-dailyplay-configuration}

Suivez les étapes d'intégration ci-dessus pour configurer votre connexion Braze et votre stream DailyPlay. Copiez le code d'intégration.

### Étape 2 : Créer une campagne ou un Canvas Braze {#step-2-create-a-braze-campaign-or-canvas}

Créez une campagne ou un Canvas en utilisant un déclencheur basé sur une action. Sélectionnez les événements personnalisés ou attributs personnalisés DailyPlay requis pour votre cas d'utilisation.

Vous pouvez utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour référencer les propriétés envoyées par DailyPlay dans le contenu de votre message.

**Exemple d'attribut personnalisé :**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**Exemple d'événement personnalisé :**

Utilisez la notation par points pour référencer les propriétés de l'événement déclencheur :

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## Résolution des problèmes {#troubleshooting}

Pour des conseils de configuration supplémentaires et une FAQ, consultez la [documentation d'intégration Braze de DailyPlay](https://docs.dailyplay.ai/connections/braze/).