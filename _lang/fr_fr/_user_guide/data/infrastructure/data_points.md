---
nav_title: Points de données
article_title: Points de données
page_order: 3
page_type: reference
description: "Cet article de référence décrit les points de données chez Braze et comment suivre leur utilisation."
search_rank: 6
---

# Points de données {#data-points}

> Chez Braze, les données sont synonymes d'action : chaque élément de donnée qui arrive dans Braze met à jour l'appartenance aux segments, peut déclencher ou annuler des envois de messages, est immédiatement disponible pour la personnalisation des messages, et bien plus encore. Les points de données vous aident à définir les informations les plus pertinentes pour votre entreprise. En réfléchissant soigneusement aux informations à suivre, vous vous assurez de cibler les données ayant le plus fort impact sur l'expérience de vos utilisateurs.

Les points de données reposent sur les informations enregistrées dans les profils utilisateurs. Vous trouverez une répartition plus détaillée de cette définition dans votre contrat Braze. Notre équipe de satisfaction client peut vous recommander les bonnes pratiques en matière de données pour répondre à vos besoins.

## Définition {#definition}

Les « points de donnée » désignent une unité facturable d'utilisation des services Braze, mesurée par un début de session, une fin de session, un événement personnalisé ou un achat enregistré, ainsi que tout attribut défini sur un profil utilisateur final. Pour plus de clarté, chacune des données mentionnées précédemment dans cette section (telles qu'un début de session, une fin de session, un événement personnalisé ou un achat enregistré, ainsi que tout attribut) définie sur le profil d'un utilisateur final à un moment donné compte comme un seul point de donnée.

Les données et événements collectés par défaut par les services Braze, y compris, par exemple, les jetons push, les informations sur l'appareil et tous les événements de suivi d'engagement des Campaigns, tels que les ouvertures d'e-mails et les clics sur les notifications push, ne sont *pas* comptabilisés comme des points de donnée.

Consultez la section [Décompte de la consommation](#consumption-count) de cet article pour comprendre quelles données sont prises en compte dans votre allocation de points de donnée.

## Consulter l'utilisation des points de donnée {#viewing-data-point-usage}

Pour consulter votre utilisation des points de donnée, accédez à **Paramètres** > **Facturation** et sélectionnez l'onglet **Total Data Points Usage**.

### Calendrier d'actualisation des points de donnée {#data-point-refresh-schedule}

L'utilisation des points de donnée est mise en cache (et non en temps réel) toutes les 24 heures, aux alentours de 2 h (heure de l'Est). Tant que le cache n'est pas actualisé, différents utilisateurs du tableau de bord peuvent voir les mêmes totaux, même s'ils ouvrent l'onglet à des moments différents le même jour. Pour le même comportement de mise en cache sur d'autres vues de facturation, consultez [Tableau de bord du total des points de donnée]({{site.baseurl}}/user_guide/administer/global/billing#total-data-points-dashboard).

Pour plus d'informations sur les composants du tableau de bord des points de donnée, consultez [Facturation]({{site.baseurl}}/user_guide/administer/global/billing).

{% alert tip %}
**Ne gaspillez pas vos points de donnée. Ne mettez à jour que les données qui changent !**<br><br>
Pour minimiser l'utilisation des points de donnée, nous vous recommandons de mettre en place un programme qui évite d'envoyer les mêmes données inchangées et qui ne transmet que les données nouvelles et pertinentes à Braze. Braze travaillera avec vous pour établir cette bonne pratique lors de l'onboarding.
{% endalert %}

## Nombre de consommations {#consumption-count}

En résumé, les points de donnée sont accumulés lorsque les données du profil d'un utilisateur sont mises à jour ou lorsqu'il effectue des actions spécifiques. Essentiellement, les points de donnée correspondent au nombre de `session starts`, `session ends`, `events` et `purchases` de chacun de vos utilisateurs.

Vous trouverez dans les sections suivantes un détail de la manière dont Braze accumule les points de donnée. Si vous avez des questions sur les subtilités des points de donnée Braze, votre gestionnaire de compte Braze pourra y répondre.

Pour l'ingestion par API, chaque mise à jour facturable effectuée via [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) suit les mêmes règles que les autres mises à jour de profil : par exemple, chaque **événement personnalisé** enregistré compte comme un point de donnée, et les **attributs personnalisés** comptent généralement par attribut mis à jour dans cette requête (consultez les tableaux de facturation dans la section suivante et les [Circonstances particulières](#special-circumstances)).

Les actions suivantes n'enregistrent pas de points de donnée :
- Supprimer des utilisateurs de Braze
- Utiliser le contenu connecté dans les communications
- Modifier l'état d'abonnement de manière globale ou au niveau des groupes d'abonnement
- Renommer les ID externes de vos utilisateurs via des [appels API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)
- Bloquer des événements, des attributs ou des propriétés d'événement

### Circonstances particulières {#special-circumstances}

#### Tableaux (arrays) {#arrays}

Un tableau (array) est une collection ordonnée d'éléments stockés dans un attribut personnalisé. La mise à jour d'un tableau coûte un point de donnée par appel API, même si le tableau ne change pas réellement. Par exemple, envoyer une opération `remove` pour une valeur qui n'existe pas dans le tableau consomme tout de même un point de donnée. De la même manière, définir un attribut personnalisé à `null` pour le supprimer du profil consomme un point de donnée. Si vous ajoutez des valeurs à un tableau de manière incrémentale, cela comptera comme un point de donnée par valeur.

{% alert tip %}
Pour les tableaux simples, si vous définissez l'ensemble du tableau en une seule fois, cela comptera comme un seul point de donnée. Les tableaux sont donc un excellent outil pour maintenir les profils utilisateurs à jour avec des informations pertinentes tout en réduisant les coûts. <br><br> Les tableaux d'objets consomment un point de donnée pour chaque clé mise à jour. Réduisez la consommation inutile de points de donnée en ne transmettant que les mises à jour à Braze.
{% endalert %}

#### Attributs personnalisés imbriqués {#nested-custom-attributes}

Les attributs personnalisés imbriqués font référence à un objet qui définit un ensemble d'attributs en tant que propriété d'un autre attribut. Chaque clé de l'objet compte comme un point de donnée.

{% alert note %}
Mettre à jour un objet d'attribut personnalisé à `null` consomme également un point de donnée.
{% endalert %}

#### CSV

Les attributs personnalisés importés via un fichier CSV sont comptabilisés dans vos points de donnée. Cependant, les imports CSV à des fins de segmentation (imports effectués avec `external_id`, `braze_id` ou `user_alias_name` comme seul champ) n'enregistrent pas de points de donnée.

De plus, comme les changements d'état d'abonnement n'enregistrent pas de points de donnée, la mise à jour des champs `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` dans votre fichier CSV n'entraîne pas de frais.

## Points de donnée

{% alert note %}
Les tableaux suivants sont fournis à titre indicatif. Pour connaître les conventions de nommage exactes, la casse et les valeurs acceptées pour certains champs, consultez la documentation correspondante à votre méthode d'ingestion.
{% endalert %}

{% tabs %}
{% tab Non facturables %}

### Points de donnée non facturables (par défaut) {#non-billable-data-points-default}

<div class="small_table"></div>

| Type de donnée | Point de donnée |
| --------- | ---------- |
| Données de profil | Pays |
| Données de profil | Langue |
| Données de profil | ID utilisateur |
| Données de profil | Alias d'utilisateur |
| Appareils récents | Nombre d'appareils |
| Appareils récents | Montre la plus récente |
| Appareils récents | Version de l'application |
| Appareils récents | Appareil |
| Appareils récents | OS de l'appareil |
| Paramètres de contact | Abonné aux e-mails |
| Paramètres de contact | Abonné aux notifications push |
| Paramètres de contact | Applications enregistrées pour les notifications push |
| Paramètres de contact | Groupe d'abonnement |
| Campaigns reçues | Adresse e-mail |
| Attribution d'installation | Source d'installation |
| Attribution d'installation | Campaign |
| Attribution d'installation | Groupe d'annonces |
| Attribution d'installation | Annonce |
| Divers | Numéro de compartiment aléatoire |
| Messages Canvas reçus | Messages Canvas reçus |
| Engagement par message | Tous les événements d'engagement (tels que les ouvertures, clics, impressions et rejets) |
| Twitter | Abonnés |
| Twitter | Abonnements |
| Twitter | Nombre de tweets |
| Facebook | Mentions J'aime |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Points de donnée non facturables (par défaut)" }

{% endtab %}
{% tab Facturables %}

### Points de donnée facturables {#billable-data-points}

{% alert important %}
L'ajout, la suppression ou la mise à jour des types de données suivants entraîne un point de donnée facturable.
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

| Type de donnée | Point de donnée | Notes |
| --------- | ---------- | ----- |
| Données de profil | Prénom | |
| Données de profil | Nom | |
| Données de profil | Adresse e-mail | |
| Données de profil | Genre | |
| Données de profil | Tranche d'âge | |
| Données de profil | Pays | Lorsqu'il est collecté manuellement. N'est pas comptabilisé dans la consommation lorsqu'il est collecté automatiquement. |
| Données de profil | Ville | |
| Données de profil | Langue | Lorsqu'elle est collectée manuellement. N'est pas comptabilisée dans la consommation lorsqu'elle est collectée automatiquement. |
| Données de profil | Paramètres régionaux de l'appareil le plus récent | |
| Données de profil | Fuseau horaire | |
| Données de profil | Date de naissance | |
| Données de profil | Biographie | |
| Données de profil | Numéro de téléphone | |
| Données d'utilisation de l'application | Début de session | |
| Données d'utilisation de l'application | Fin de session | |
| Attributs personnalisés | Tous les attributs personnalisés | |
| Événements personnalisés | Tous les événements personnalisés | |
| Propriétés d'événement personnalisé | Toutes les propriétés d'événement personnalisé | Les propriétés d'événement personnalisé activées pour la segmentation avec les filtres `X Custom Event Property in Y Days` ou `X Purchase Property in Y Days` sont toutes comptabilisées comme des points de donnée distincts, en plus du point de donnée comptabilisé par l'événement personnalisé lui-même. |
| Achats | Tous les achats | |
| Propriétés d'achat | Toutes les propriétés d'achat | |
| Affectation de cohorte Amplitude | Toutes les affectations | |
| Affectation de cohorte Mixpanel | Toutes les affectations | |
| Affectation de cohorte Hightouch | Toutes les affectations | |
| Affectation de cohorte Appsflyer | Toutes les affectations | |
| Emplacement le plus récent | Tous les emplacements les plus récents | L'entrée ou la sortie de géorepérages ne consomme pas de points de donnée, car les données de géorepérage ne sont pas stockées dans le profil utilisateur. Les géorepérages sont surveillés par les services de localisation Apple et Google ; Braze est uniquement notifié lorsqu'un utilisateur déclenche un géorepérage. |
| Twitter | Nom d'utilisateur | |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Points de donnée facturables" }

{% endtab %}
{% endtabs %}