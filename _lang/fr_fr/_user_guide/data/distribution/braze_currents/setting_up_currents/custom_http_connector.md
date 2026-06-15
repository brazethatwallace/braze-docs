---
nav_title: Connecteur HTTP personnalisé
article_title: Connecteur HTTP personnalisé
alias: /currents/custom_http_connector/
page_order: 3
page_type: reference
tool: Currents
description: "Cet article de référence explique comment configurer un connecteur HTTP personnalisé pour diffuser les données d'événements Braze Currents directement vers votre propre endpoint HTTP en temps réel."
---

# Connecteur HTTP personnalisé {#custom-http-connector}

> Découvrez comment intégrer un connecteur Currents personnalisé afin de recevoir les données d'événements de Braze en temps réel, pour des analyses, des rapports et une automatisation plus personnalisés.

## Conditions préalables {#prerequisites}

Pour intégrer un connecteur Currents personnalisé dans Braze, vous devrez fournir une URL d'endpoint et un [jeton d'authentification facultatif](#authentication).

De plus, si vous avez plusieurs groupes d'applications dans Braze, vous devrez configurer un connecteur Currents personnalisé pour chaque groupe. Cependant, vous pouvez diriger tous les groupes d'applications vers le même endpoint, ou vers un endpoint avec un paramètre `GET` supplémentaire, tel que `your_app_group_key="Brand A"`.

## Intégration {#integration}

### Étape 1 : Configurer votre endpoint {#step-1-set-up-your-endpoint}

Vous aurez besoin d'une URL d'endpoint pour configurer cette intégration. Votre endpoint doit être capable de recevoir des requêtes HTTP POST et de renvoyer un code de statut `2XX` pour confirmer la bonne réception des événements. Si vous souhaitez authentifier les requêtes provenant de Braze, vous aurez également besoin d'un jeton bearer.

### Étape 2 : Configurer Braze Currents {#step-2-configure-braze-currents}

Dans Braze, accédez à **Partner Integrations** > **Data Export**, cliquez sur **Create New Current** et sélectionnez **Custom Currents Export**.

Donnez un nom à votre export ainsi qu'un e-mail de contact, puis passez à la page **Current Details**. Sur cette page, saisissez l'URL de votre endpoint et le jeton bearer facultatif.

Après avoir configuré vos identifiants, cochez tous les événements d'engagement de messages, de comportement client et d'utilisateur que vous souhaitez exporter, puis cliquez sur **Launch Current**.

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation des données suivantes vers votre connecteur HTTP personnalisé :

- [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

Pour la structure du payload de chaque événement, sélectionnez l'onglet **Custom HTTP Connector** dans le glossaire des événements.

## Prévention de la perte de données {#preventing-data-loss}

### Surveillance des erreurs {#error-monitoring}

Pour éviter la perte de données et les interruptions de service, il est essentiel de surveiller vos endpoints en permanence et de traiter rapidement toute erreur ou temps d'arrêt.

Pour la plupart des types d'erreurs (telles que les erreurs serveur et les erreurs de connexion réseau), Braze réessaiera activement la transmission des événements. Si le problème persiste pendant plus de 5 jours, l'intégration sera automatiquement désactivée. Les nouveaux événements entrants seront abandonnés et définitivement perdus.

### Résilience aux changements {#change-resilience}

Il arrive que nous apportions des modifications non disruptives aux schémas de Braze Currents. Les modifications non disruptives sont de nouvelles colonnes nullables ou de nouveaux types d'événements.

Nous donnons généralement un préavis de deux semaines pour ces changements, mais ce n'est pas toujours possible. Il est essentiel que vous conceviez votre intégration pour gérer les champs ou types d'événements non reconnus, sinon cela entraînera probablement une perte de données.

{% alert tip %}
Pour la liste complète des schémas d'événements Currents, consultez [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) et [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).
{% endalert %}

## Mise en lots et sérialisation {#batching-and-serialization}

Le format de données cible est JSON via HTTPS. Par défaut, les événements sont envoyés à votre endpoint par lots de 100 événements maximum.

Les événements sont envoyés à l'endpoint sous forme de tableau JSON contenant tous les événements, dans le format suivant :

```json
{"events": [event1, event2, event3, etc...]}
```

Il y aura un objet JSON de niveau supérieur avec la clé `"events"` qui correspond à un tableau d'autres objets JSON, chacun représentant un événement unique. Chaque événement contient deux sous-objets :

| Nom | Description |
|----|-----------|
| `"user"` | Contient les propriétés de l'utilisateur telles que `user_id`, `external_user_id`, `device_id` et `timezone`. |
| `"properties"` | Contient les attributs d'un événement, tels que l'`app/campaign/canvas/platform` auquel il s'applique. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si un endpoint en aval reçoit un payload avec zéro événement ou un corps de requête vide, le résultat doit être considéré comme un no-op, ce qui signifie qu'aucun effet en aval ne doit résulter de cet appel. Cependant, vous devez toujours vérifier l'en-tête `Authorization` (comme vous le feriez pour un appel API normal) et renvoyer une réponse HTTP appropriée pour les [identifiants invalides](#authentication), telle que `401` ou `403`. Cela permet à Braze de savoir que les identifiants du connecteur sont valides.

## Authentification {#authentication}

Les jetons d'authentification dans votre payload sont facultatifs. Ils peuvent être transmis via un en-tête HTTP `Authorization` en utilisant le schéma d'autorisation `Bearer`, tel que spécifié dans la [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Bien que facultatif, si un jeton d'authentification est transmis, Braze le validera toujours en premier&#8212;même si aucun événement ne figure dans le payload.

Conformément à la RFC 6750, les jetons doivent être des valeurs encodées en Base64 comportant au moins un caractère. Gardez à l'esprit que la RFC 6750 autorise les jetons à contenir les caractères suivants en plus des caractères Base64 normaux : `-`, `.`, `_` et `~`. Vous pouvez choisir d'inclure ou non ces caractères dans votre jeton&#8212;cependant, il doit être au format Base64.

De plus, si l'en-tête `Authorization` est présent, il sera construit selon le format suivant :

```plaintext
"Authorization: Bearer " + <token>
```

Par exemple, si votre jeton d'authentification est `0p3n5354m3==`, votre en-tête `Authorization` devrait ressembler à ceci :

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
À l'avenir, nous pourrions utiliser les en-têtes `Authorization` pour implémenter un schéma d'autorisation personnalisé, basé sur des paires clé-valeur, propre à Braze. Cela respecterait la spécification [RFC 7235](https://tools.ietf.org/html/rfc7235), qui est la manière dont certaines entreprises implémentent leurs schémas d'authentification, comme Amazon Web Services (AWS).
{% endalert %}

## Versionnage {#versioning}

Toutes les requêtes provenant de notre intégration de connecteur HTTP seront envoyées avec un en-tête personnalisé indiquant la version de la requête Currents effectuée :

```plaintext
Braze-Currents-Version: 1
```

La version sera toujours `1`, car nous ne prévoyons pas d'incrémenter ce numéro très souvent, voire jamais.

Tout comme nos [schémas de stockage d'entrepôt de données]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), chaque champ d'événement dans un événement individuel est garanti rétrocompatible avec les versions précédentes du payload d'événement, selon la définition de rétrocompatibilité d'[Apache Avro](https://avro.apache.org/) :

1. Les champs d'événement spécifiques sont garantis de toujours avoir le même type de données au fil du temps.
2. Tout nouveau champ ajouté au payload au fil du temps doit être considéré comme facultatif par toutes les parties.
3. Les champs requis ne seront jamais supprimés.

## Gestion des erreurs et mécanisme de réessai {#error-handling-and-retry-mechanism}

Si une erreur survient, Braze mettra en file d'attente et réessaiera la requête en fonction du code de retour HTTP reçu. Si le problème persiste pendant plus de 5 jours, l'intégration sera automatiquement désactivée : les nouveaux événements entrants seront abandonnés et définitivement perdus, et les événements déjà en file d'attente seront définitivement supprimés après une rétention de 7 jours. Si des données sont bloquées pendant plus de 24 heures, nos ingénieurs d'astreinte seront automatiquement alertés. Pour un détail complet de la gestion de chaque code de statut, consultez le tableau ci-dessous.

Si votre intégration Currents renvoie des erreurs d'authentification, Braze vous enverra automatiquement un e-mail de notification.

Tout code d'erreur HTTP non répertorié ci-dessous sera traité comme une erreur HTTP `5XX`.

{% alert warning %}
Si le problème persiste pendant plus de 5 jours, l'intégration sera désactivée. Les nouveaux événements entrants seront abandonnés et définitivement perdus, et les événements déjà en file d'attente seront définitivement supprimés après une rétention de 7 jours.
{% endalert %}

Les codes de statut HTTP suivants seront reconnus par notre client connecteur :

<table aria-label="Gestion des erreurs et mécanisme de réessai">
  <thead>
    <tr>
      <th>Code de statut</th>
      <th>Réponse</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Réussi</td>
      <td>Les données d'événement ne seront pas renvoyées.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Erreur côté serveur</td>
      <td>Les données d'événement seront renvoyées selon un schéma de délais exponentiels avec gigue. Si le problème persiste pendant plus de 5 jours, l'intégration sera désactivée, et les événements déjà en file d'attente seront conservés pendant 7 jours.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Erreur côté client</td>
      <td>Le connecteur a envoyé au moins un événement mal formé. Les données d'événement seront divisées en lots de taille 1 et renvoyées. Tout événement dans ces lots de taille 1 qui reçoit une autre réponse <code>400</code> sera définitivement supprimé.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Non autorisé</td>
      <td>Le connecteur a été configuré avec des identifiants invalides. Les événements échoués ne seront pas renvoyés. Corrigez vos identifiants et réactivez l'intégration pour reprendre. Si le problème persiste pendant plus de 5 jours, l'intégration sera désactivée, et les événements déjà en file d'attente seront conservés pendant 7 jours.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Interdit</td>
      <td>Le connecteur a été configuré avec des identifiants invalides. Les événements échoués ne seront pas renvoyés. Corrigez vos identifiants et réactivez l'intégration pour reprendre. Si le problème persiste pendant plus de 5 jours, l'intégration sera désactivée, et les événements déjà en file d'attente seront conservés pendant 7 jours.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Non trouvé</td>
      <td>Le connecteur a été configuré avec une URL d'endpoint incorrecte ou des identifiants invalides. Vérifiez que l'URL de votre endpoint est correcte et accessible. Corrigez votre configuration et réactivez l'intégration pour reprendre. Si le problème persiste pendant plus de 5 jours, l'intégration sera désactivée, et les événements déjà en file d'attente seront conservés pendant 7 jours.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Payload trop volumineux</td>
      <td>Les données d'événement seront divisées en lots plus petits et renvoyées.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Trop de requêtes</td>
      <td>Indique une limitation de débit. Les données d'événement seront renvoyées selon un schéma de délais exponentiels avec gigue. Si le problème persiste pendant plus de 5 jours, l'intégration sera désactivée, et les événements déjà en file d'attente seront conservés pendant 7 jours.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }