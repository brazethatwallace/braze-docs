---
nav_title: Points de données
article_title: Aperçu des points de données
page_order: 3
page_type: reference
description: "Cet article de référence décrit les points de données chez Braze et comment suivre leur utilisation."
search_rank: 6
---

# Points de données {#data-points}

> Chez Braze, les données sont synonymes d'action : chaque élément de donnée qui arrive dans Braze met à jour l'appartenance aux segments, peut déclencher ou annuler des envois de messages, est immédiatement disponible pour la personnalisation des messages, et bien plus encore. Les points de données vous aident à définir les informations les plus pertinentes pour votre entreprise. En réfléchissant soigneusement aux informations à suivre, vous vous assurez de cibler les données ayant le plus fort impact sur l'expérience de vos utilisateurs.

Les points de données reposent sur les informations enregistrées dans les profils utilisateurs. Vous trouverez une répartition plus détaillée de cette définition dans votre contrat Braze. Notre équipe de satisfaction client peut vous recommander les bonnes pratiques en matière de données pour répondre à vos besoins.

## Définition {#definition}

Les « Points de données » désignent une unité facturable d'utilisation des Services Braze, mesurée par un début de session, une fin de session, un événement personnalisé ou un achat enregistré, ainsi que tout attribut défini sur un profil d'utilisateur final. Pour plus de clarté, chacune des données mentionnées ci-dessus (telles que le début de session, la fin de session, l'événement personnalisé ou l'achat enregistré, ainsi que tout attribut) définies dans le profil d'un utilisateur final à un moment donné sera comptée comme un seul point de donnée.

Les données et les événements collectés par défaut par les services Braze, y compris, par exemple, les jetons de notification push, les informations sur les appareils et tous les événements de suivi de l'engagement des Campaigns, tels que les ouvertures d'e-mails et les clics sur les notifications push, ne sont *pas* comptés comme des points de données.

Consultez la section [Décompte de la consommation](#consumption-count) de cet article pour comprendre quelles données comptent dans votre allocation de points de données.

## Visualisation de l'utilisation des points de données {#viewing-data-point-usage}

Pour consulter votre utilisation des points de données, allez dans **Paramètres** > **Facturation** et sélectionnez l'onglet **Utilisation totale des points de données**.

### Calendrier d'actualisation des points de données {#data-point-refresh-schedule}

L'utilisation des points de données est mise en cache (et non en temps réel) toutes les 24 heures, aux alentours de 2 h (heure de l'Est). Tant que le cache n'est pas actualisé, différents utilisateurs du tableau de bord peuvent voir les mêmes totaux, même s'ils ouvrent l'onglet à des moments différents le même jour. Pour le même comportement de mise en cache sur d'autres vues de facturation, consultez [Tableau de bord de l'utilisation totale des points de données]({{site.baseurl}}/user_guide/administer/global/billing#total-data-points-dashboard).

Pour plus d'informations sur les composants du tableau de bord des points de données, consultez [Facturation]({{site.baseurl}}/user_guide/administer/global/billing).

{% alert tip %}
**Ne gaspillez pas de points de données. Ne mettez à jour que les données modifiées !**<br><br>
Pour minimiser l'utilisation des points de données, nous vous recommandons de mettre en place un programme empêchant l'envoi des mêmes données immuables et de ne transmettre à Braze que des données nouvelles et pertinentes. Braze travaillera avec vous pour établir cette bonne pratique pendant l'onboarding.
{% endalert %}

## Décompte de la consommation {#consumption-count}

En résumé, les points de données s'accumulent lorsque les données de profil d'un utilisateur sont mises à jour ou lorsqu'il effectue des actions spécifiques. Concrètement, les points de données correspondent aux décomptes des `session starts`, `session ends`, `events` et `purchases` de chacun de vos utilisateurs.

Vous trouverez une décomposition de la façon dont Braze accumule les points de données dans les sections suivantes. Si vous avez des questions sur les subtilités des points de données Braze, votre gestionnaire de compte Braze pourra y répondre.

Pour l'ingestion via l'API, chaque mise à jour facturable effectuée via [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) suit les mêmes règles que les autres mises à jour de profil : par exemple, chaque **événement personnalisé** enregistré compte comme un point de donnée, et les **attributs personnalisés** comptent généralement par attribut mis à jour dans cette requête (voir les tableaux facturables ci-dessous et les [Circonstances particulières](#special-circumstances)).

Les actions suivantes n'enregistrent pas de points de données :
- Supprimer des utilisateurs de Braze
- Utiliser du contenu connecté lors de l'envoi de messages
- Les changements d'état d'abonnement à l'échelle globale et au niveau des groupes d'abonnement
- Renommer les ID externes de vos utilisateurs via des [appels d'API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)
- Bloquer des événements, des attributs ou des propriétés d'événement

### Circonstances particulières {#special-circumstances}

#### Tableaux {#arrays}

Un tableau est une collection ordonnée d'éléments stockés dans un attribut personnalisé. La mise à jour d'un tableau coûte un point de donnée par appel API, même si le tableau ne change pas réellement. Par exemple, envoyer une opération `remove` pour une valeur qui n'existe pas dans le tableau consomme tout de même un point de donnée. De même, définir un attribut personnalisé sur `null` pour le supprimer du profil consomme un point de donnée. Si vous ajoutez des valeurs à un tableau de manière incrémentale, cela comptera comme un point de donnée par valeur.

{% alert tip %}
Pour les tableaux simples, si vous définissez l'ensemble du tableau en une seule fois, cela comptera comme un seul point de donnée. De ce fait, les tableaux constituent un excellent outil pour maintenir les profils utilisateurs à jour avec les informations pertinentes tout en réduisant les coûts. <br><br> Les tableaux d'objets consomment un point de donnée pour chaque clé mise à jour. Réduisez la consommation inutile de points de données en ne transmettant que les mises à jour à Braze.
{% endalert %}

#### Attributs personnalisés imbriqués {#nested-custom-attributes}

Les attributs personnalisés imbriqués font référence à un objet qui définit un ensemble d'attributs en tant que propriété d'un autre attribut. Chaque clé de l'objet est comptée comme un point de donnée.

{% alert note %}
La mise à jour d'un objet d'attribut personnalisé vers `null` consomme également un point de donnée.
{% endalert %}

#### CSV

Les attributs personnalisés importés via un fichier CSV comptent dans vos points de données. Toutefois, les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id` ou `user_alias_name` comme seul champ) n'enregistrent pas de points de données.

En outre, comme les changements d'état d'abonnement n'enregistrent pas de points de données, la mise à jour des champs `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` dans votre fichier CSV n'entraînera pas de frais.

## Points de données

{% alert note %}
Les tableaux suivants sont donnés à titre d'exemple. Pour connaître les conventions d'appellation exactes, les majuscules et les valeurs acceptées pour certains champs, reportez-vous à la documentation relative à votre méthode d'ingestion.
{% endalert %}

{% tabs %}
{% tab Non facturables %}

### Points de données non facturables (par défaut) {#non-billable-data-points-default}

<div class="small_table"></div>

| Type de données | Point de donnée |
| --------- | ---------- |
| Données de profil | Pays |
| Données de profil | Langue |
| Données de profil | ID utilisateur |
| Données de profil | Alias d'utilisateur |
| Appareils récents | Nombre d'appareils |
| Appareils récents | Montre la plus récente |
| Appareils récents | Version de l'application |
| Appareils récents | Appareil |
| Appareils récents | Système d'exploitation de l'appareil |
| Paramètres de contact | Abonnement aux e-mails |
| Paramètres de contact | Abonnement aux notifications push |
| Paramètres de contact | Applications enregistrées pour les notifications push |
| Paramètres de contact | Groupe d'abonnement |
| Campaigns reçues | Adresse e-mail |
| Attribution d'installation | Source d'installation |
| Attribution d'installation | Campaign |
| Attribution d'installation | Groupe publicitaire |
| Attribution d'installation | Publicité |
| Divers | Numéro de compartiment aléatoire |
| Messages Canvas reçus | Messages Canvas reçus |
| Engagement des messages | Tous les événements d'engagement (tels que les ouvertures, les clics, les impressions et les fermetures) |
| Twitter | Abonnés |
| Twitter | Abonnements |
| Twitter | Nombre de tweets |
| Facebook | Mentions J'aime |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Points de données non facturables (par défaut)" }

{% endtab %}
{% tab Facturables %}

### Points de données facturables {#billable-data-points}

{% alert important %}
L'ajout, la suppression ou la mise à jour des types de données suivants donne lieu à un point de donnée facturable.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Type de données | Point de donnée | Remarques |
| --------- | ---------- | ----- |
| Données de profil | Prénom | |
| Données de profil | Nom | |
| Données de profil | Adresse e-mail | |
| Données de profil | Genre | |
| Données de profil | Tranche d'âge | |
| Données de profil | Pays | Lorsqu'il est collecté manuellement. Ne compte pas pour la consommation lorsqu'il est collecté automatiquement. |
| Données de profil | Ville | |
| Données de profil | Langue | Lorsqu'elle est collectée manuellement. Ne compte pas pour la consommation lorsqu'elle est collectée automatiquement. |
| Données de profil | Paramètres régionaux les plus récents de l'appareil | |
| Données de profil | Fuseau horaire | |
| Données de profil | Date de naissance (DDN) | |
| Données de profil | Bio | |
| Données de profil | Numéro de téléphone | |
| Données d'utilisation des applications | Début de session | |
| Données d'utilisation des applications | Fin de session | |
| Attributs personnalisés | Tous les attributs personnalisés | |
| Événements personnalisés | Tous les événements personnalisés | |
| Propriétés d'événement personnalisé | Toutes les propriétés d'événement personnalisé | Les propriétés d'événement personnalisé activées pour la segmentation avec les filtres `X Custom Event Property in Y Days` ou `X Purchase Property in Y Days` sont toutes comptées comme des points de données séparés, en plus du point de donnée comptabilisé par l'événement personnalisé lui-même.
| Achats | Tous les achats | |
| Propriétés d'achat | Toutes les propriétés d'achat | |
| Affectation de cohorte Amplitude | Toutes les affectations | |
| Affectation de cohorte Mixpanel | Toutes les affectations | |
| Affectation de cohorte Hightouch | Toutes les affectations | |
| Affectation de cohorte Appsflyer | Toutes les affectations | |
| Localisation la plus récente | Toutes les localisations les plus récentes | Entrer ou sortir d'un géorepérage n'enregistre pas de points de données, car les données de géorepérage ne sont pas stockées dans le profil utilisateur. Les géorepérages sont surveillés par les services de localisation d'Apple et de Google ; Braze n'est notifié que lorsqu'un utilisateur déclenche un géorepérage. |
| Twitter | Nom d'utilisateur | |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Points de données facturables" }

{% endtab %}
{% endtabs %}