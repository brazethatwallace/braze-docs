---
nav_title: SmarterSends
article_title: SmarterSends
description: "Cet article de référence présente le partenariat entre Braze et SmarterSends, une interface conviviale conçue pour les non-marketeurs afin de créer, planifier et déployer des campagnes d'e-mails conformes à la marque."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com) favorise la personnalisation grâce à des campagnes marketing que les entreprises peuvent créer, planifier et déployer pour faire respecter la marque et la conformité légale en contrôlant le contenu et les données utilisées.

_Cette intégration est maintenue par SmarterSends._

## À propos de l'intégration {#about-the-integration}

Le partenariat entre Braze et SmarterSends vous permet de combiner la puissance de Braze avec le contenu hyperlocalisé détenu par vos utilisateurs distribués pour renforcer vos campagnes marketing.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte SmarterSends | Un [compte SmarterSends](https://smartersends.com) est nécessaire pour profiter de ce partenariat. |
| Clé REST API de Braze | Une clé REST API de Braze avec les autorisations suivantes : {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. Pour plus de sécurité, ajoutez l'adresse IP de SmarterSends à la liste d'autorisation (disponible dans votre instance). |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| ID de Campaign API Braze | L'[ID de Campaign API Braze]({{site.baseurl}}/api/api_campaigns/) est l'identifiant unique de toutes les Campaigns envoyées par l'intermédiaire de SmarterSends. Celui-ci peut être créé dans le tableau de bord de Braze sous **Messagerie** > **Campaigns**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Grâce à l'intégration de Braze et de SmarterSends, vous pouvez tirer parti du marketing distribué en créant et en exécutant des campagnes marketing sur plusieurs canaux et emplacements. Ces avantages sont les suivants :

1. **Augmentation de la portée :** utilisation de plusieurs canaux et emplacements pour atteindre une audience plus large et cibler les clients dans différentes zones, ce qui se traduit par une exposition accrue de la marque.
2. **Envoi de messages ciblés :** adaptation de l'envoi de messages à travers les canaux et emplacements afin de trouver un écho auprès des audiences locales pour une communication et un engagement plus efficaces avec les clients.
3. **Amélioration de la cohérence de la marque :** alignement des messages et de l'image de votre marque sur tous les canaux et emplacements, ce qui est important pour créer une marque forte et reconnaissable.
4. **Meilleures informations :** collecte de données provenant de différents canaux et emplacements, fournissant des informations précieuses sur le comportement et les préférences des clients, qui peuvent être utilisées pour affiner les stratégies et tactiques marketing aux niveaux local et mondial.
5. **Efficacité accrue :** exploitation des atouts des différents canaux et emplacements, ce qui peut se traduire par une utilisation plus efficace des ressources tout en permettant d'atteindre les objectifs marketing souhaités.

## Intégration {#integration}

### Étape 1 : Créer une clé REST API {#step-1-create-a-rest-api-key}

1. Dans Braze, accédez à **Paramètres** > **Clés API** et cliquez sur **Créer une nouvelle clé API**.
2. Saisissez un nom pour la clé API.
3. Sélectionnez les autorisations suivantes pour cette clé afin de permettre à SmarterSends d'interagir avec votre espace de travail Braze.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Ajoutez l'adresse IP de SmarterSends à la section **Whitelist IPs**.
5. Cliquez sur **Save API Key**.
6. Copiez et collez la clé API avec les autorisations appropriées dans les paramètres du **Braze Email Service Provider** dans SmarterSends.

### Étape 2 : Créer ou copier un ID d'application {#step-2-create-or-copy-an-application-id}

1. Dans votre espace de travail Braze, accédez à **Paramètres** > **Paramètres des applications**.
2. Créez une nouvelle application ou utilisez l'ID d'une application existante dans votre espace de travail. Notez que l'ID de l'application est indiqué comme étant la **clé API**.
3. Copiez et collez cet ID dans le champ **App ID** dans SmarterSends.

### Étape 3 : Créer une Campaign API {#step-3-create-an-api-campaign}

Une Campaign API permet de suivre les indicateurs de tous les envois SmarterSends dans Braze et permet à SmarterSends de déclencher ces Campaigns basées sur l'API.

1. Dans Braze, [créez une Campaign API]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Cliquez sur **Email** sous **Select Message Channel** pour ajouter un canal d'envoi de messages et commencer à suivre les indicateurs.
3. Ensuite, copiez et collez l'ID de la Campaign depuis Braze dans le champ **Campaign ID** dans SmarterSends.
4. Copiez et collez l'ID de la variante de message depuis Braze dans le champ **Message Variant ID** dans SmarterSends. Il s'agit de l'ID de message par défaut utilisé si vous décidez de ne pas créer d'ID de message pour chaque groupe dans SmarterSends.
5. Pour chaque groupe que vous créez dans SmarterSends, ajoutez une variante de message à votre Campaign API dans Braze. Copiez ensuite l'ID de la variante de message dans l'ID de la variante de message du groupe dans SmarterSends.

{% alert tip %}
Créez un ID de variante de message pour chaque groupe que vous créez dans SmarterSends afin d'afficher séparément les indicateurs des envois de chaque groupe dans votre espace de travail Braze. Cela peut être utile pour identifier les tendances entre les groupes lorsque vous créez des rapports dans Braze.
{% endalert %}

## Personnalisation {#customization}

Chaque instance de SmarterSends est entièrement personnalisable avec les couleurs du logo de votre marque et un nom de domaine personnalisé, créant ainsi un environnement familier. De plus, pour une personnalisation plus poussée, vous pouvez définir les attributs et les attributs personnalisés pour cibler les utilisateurs dans les Campaigns en fonction des Segments au sein de votre espace de travail Braze.