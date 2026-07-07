---
nav_title: Mettre en cache les réponses
article_title: Mettre en cache les réponses du Contenu connecté
page_order: 2.5
description: "Cet article explique comment mettre en cache les réponses du Contenu connecté entre différentes campagnes ou messages dans le même espace de travail afin d'optimiser les vitesses d'envoi."
---

# Mettre en cache les réponses du Contenu connecté {#cache-connected-content-responses}

> Les réponses du Contenu connecté peuvent être mises en cache entre différentes campagnes ou messages (dans le même espace de travail) afin d'optimiser les vitesses d'envoi.

Braze ne journalise ni ne stocke de manière permanente les **corps de réponse** du Contenu connecté. Lors du rendu des messages, les réponses peuvent être conservées temporairement (par exemple, en mémoire et en cache) afin que Braze puisse effectuer le rendu Liquid et envoyer le message.

Pour empêcher la mise en cache, vous pouvez spécifier `:no_cache`, ce qui peut entraîner une augmentation du trafic réseau. Pour faciliter la résolution des problèmes et surveiller l'état du système, Braze journalise les métadonnées des requêtes du Contenu connecté (telles que l'URL de requête entièrement rendue et le code de statut de la réponse) pour les appels réussis et échoués. Ces journaux sont conservés pendant 30 jours maximum.

{% details Rendu du Contenu connecté et traitement des données (avancé) %}
Cette section fournit une vue plus détaillée, de bout en bout, de la façon dont Braze effectue le rendu Liquid et du Contenu connecté, et des endroits où les données peuvent exister temporairement avant l'envoi d'un message. Cela peut être utile pour les examens de confidentialité et de traitement des données.

## Ce qui est et n'est pas stocké {#what-is-and-isnt-stored}

- **Corps de réponse du Contenu connecté :** Non stocké de manière permanente par Braze. Il peut être conservé temporairement en mémoire et, lorsque la mise en cache est activée, stocké en cache avec une durée de vie (TTL).
- **Métadonnées des requêtes du Contenu connecté :** Les métadonnées des requêtes, telles que l'URL entièrement rendue, le code de statut HTTP et la durée de la réponse, sont journalisées à des fins de résolution des problèmes et de surveillance. Ces journaux sont conservés pendant 30 jours maximum.
- **Message final rendu :** Existe en mémoire pendant le rendu. Il peut également être stocké ailleurs selon votre configuration et votre canal (par exemple, l'Archivage des messages ou les Content Cards).

## Flux de rendu (vue d'ensemble) {#rendering-flow-high-level}

Le flux suivant décrit comment Braze effectue le rendu et envoie les messages pour les canaux basés sur un fournisseur, tels que l'e-mail, le SMS et les notifications push. Les canaux délivrés par le SDK, comme les Content Cards, utilisent le même rendu Liquid et Contenu connecté sous-jacent, mais diffèrent dans le moment où le contenu est généré et la façon dont il est délivré.

1. Un processus en arrière-plan effectue le rendu du modèle Liquid pour un message lorsque celui-ci est préparé pour être délivré.
2. Les balises du Contenu connecté sont évaluées pendant le rendu Liquid.
3. Pour chaque balise du Contenu connecté, Braze vérifie un cache multi-niveaux. Si aucune valeur en cache n'existe (ou si la mise en cache est désactivée), Braze appelle votre endpoint et reçoit la réponse.
4. La réponse est injectée dans le modèle Liquid et le message est entièrement rendu.
5. Pour les canaux basés sur un fournisseur, le message rendu est envoyé au fournisseur du canal, puis à l'utilisateur. Pour les canaux délivrés par le SDK, tels que les Content Cards, le contenu rendu est synchronisé avec le SDK Braze et peut être généré à la première impression ou au moment de l'affichage, moment auquel il est présenté à l'utilisateur.

## Où les réponses du Contenu connecté peuvent résider temporairement {#where-connected-content-responses-can-live-temporarily}

Braze utilise un cache multi-niveaux pour les réponses du Contenu connecté avec des TTL compris entre cinq minutes et quatre heures, selon votre utilisation de `:cache_max_age` et d'autres règles de mise en cache :

- **Cache mémoire en cours de processus :** Cache transitoire au sein du processus de travail. Les données ne peuvent exister que pendant la durée de la tâche (jusqu'à environ 11 minutes selon le délai d'expiration du processus).
- **Cache machine locale :** Un cache par processus de travail, tel qu'une instance Memcached locale.
- **Cache à l'échelle du cluster :** Un cache distribué partagé entre les processus de travail, tel qu'un cluster Memcached.

Ces couches de cache sont volatiles et peuvent évincer les données avant le TTL configuré.

## Ce qui change lorsque vous utilisez `:no_cache` {#what-changes-when-you-use-no_cache}

Pour les endpoints qui ne sont pas hébergés dans l'infrastructure Braze, l'utilisation de `:no_cache` empêche le corps de réponse du Contenu connecté d'être stocké dans Memcached. Dans ces cas, la réponse ne réside que dans la mémoire du processus de travail pendant la durée de la tâche de rendu (jusqu'à environ 11 minutes). Pour les endpoints qui résolvent vers des hôtes internes à Braze, les réponses peuvent toujours être mises en cache comme décrit dans [Invalidation du cache](#cache-busting).

## Où le résultat final rendu peut résider {#where-the-final-rendered-output-can-live}

- **Archivage des messages :** Si l'Archivage des messages est activé, Braze peut écrire le message final rendu dans votre compartiment de stockage cloud configuré. Si votre réponse du Contenu connecté est incluse dans le message rendu, elle sera incluse dans la copie archivée.
- **Appareils des utilisateurs :** Après la délivrance, le contenu du message entièrement rendu peut persister sur les appareils des utilisateurs pendant une durée indéterminée.
- **Content Cards :** Le contenu rendu pour les Content Cards est stocké dans une base de données Braze jusqu'à l'expiration de la carte.
{% enddetails %}

## Paramètres de cache par défaut {#default-cache-settings}

La durée du cache est de cinq minutes maximum (300 secondes). Vous pouvez la modifier en ajoutant le paramètre `:cache_max_age` à l'appel du Contenu connecté. Voici un exemple :

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Les requêtes GET sont mises en cache par défaut. Vous pouvez désactiver la mise en cache en ajoutant le paramètre `:no_cache` à l'appel du Contenu connecté.

Les requêtes POST ne sont pas mises en cache par défaut, mais vous pouvez activer la mise en cache en ajoutant le paramètre `:cache_max_age` à l'appel du Contenu connecté. La durée minimale du cache est de 5 minutes et la durée maximale est de 4 heures.

{% alert note %}
Les paramètres de cache ne sont pas garantis. La mise en cache peut réduire les appels vers vos endpoints, c'est pourquoi nous recommandons d'utiliser plusieurs appels par endpoint dans la durée du cache plutôt que de dépendre excessivement de la mise en cache.
{% endalert %}

### Limite de taille du cache {#cache-size-limit}

Le corps de réponse du Contenu connecté peut atteindre 1&nbsp;Mo maximum. Si le corps de réponse dépasse 1&nbsp;Mo, il ne sera pas mis en cache.

## Durée du cache {#cache-time}

Le Contenu connecté met en cache la valeur renvoyée par les endpoints GET pendant un minimum de cinq minutes. Si aucune durée de cache n'est spécifiée, la durée par défaut est de cinq minutes.

La durée du cache du Contenu connecté peut être allongée avec `:cache_max_age`, comme illustré dans l'exemple suivant. La durée minimale du cache est de cinq minutes et la durée maximale est de quatre heures. Les données du Contenu connecté sont mises en cache en mémoire à l'aide d'un système de cache volatile, tel que Memcached.

Par conséquent, quelle que soit la durée de cache spécifiée, les données du Contenu connecté peuvent être évincées du cache en mémoire de Braze plus tôt que prévu. Cela signifie que les durées de cache sont indicatives et ne représentent pas nécessairement la durée pendant laquelle Braze conserve effectivement les données en cache. Vous pourriez donc observer plus de requêtes de Contenu connecté que prévu pour une durée de cache donnée.

### Cache pour un nombre de secondes spécifié {#cache-for-specified-seconds}

Cet exemple met en cache pendant 900 secondes (soit 15 minutes).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Invalidation du cache {#cache-busting}

Pour empêcher le Contenu connecté de mettre en cache la valeur renvoyée par une requête GET, vous pouvez utiliser la configuration `:no_cache`. Cependant, les réponses provenant d'hôtes internes à Braze seront toujours mises en cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Assurez-vous que l'endpoint du Contenu connecté fourni peut gérer de fortes rafales de trafic avant d'utiliser cette option, sinon vous constaterez probablement une latence d'envoi accrue (délais plus importants ou intervalles de temps plus larges entre la requête et la réponse) car Braze effectuera des requêtes de Contenu connecté pour chaque message individuel.
{% endalert %}

Avec une requête POST, il n'est pas nécessaire d'invalider le cache, car les requêtes POST ne sont pas mises en cache par défaut. Pour mettre en cache une réponse POST, ajoutez `:cache_max_age` ; pour éviter la mise en cache d'une requête POST, omettez `:cache_max_age`.

## Bon à savoir {#things-to-know}

{% raw %}
- La mise en cache peut aider à réduire les appels de Contenu connecté en double. Cependant, il n'est pas garanti qu'elle aboutisse toujours à un seul appel de Contenu connecté par utilisateur.
- La mise en cache du Contenu connecté est basée sur l'espace de travail, l'URL de la requête, le type de contenu de la requête et le corps de la requête. Si l'appel du Contenu connecté utilise une URL identique, il peut être mis en cache entre les Campaigns et les Canvas.
- Le cache est basé sur une combinaison unique d'URL, de type de contenu et de corps de requête, et non sur un ID utilisateur ou une Campaign. Cela signifie que la version mise en cache d'un appel de Contenu connecté peut être utilisée par plusieurs utilisateurs et Campaigns dans un espace de travail si l'URL, le type de contenu et le corps de la requête sont identiques.
- La mise en cache du Contenu connecté peut être ignorée si le balisage de la balise contient l'un des extraits de code à haute cardinalité suivants :
    - `{{${user_id}}}`
    - `{{${braze_id}}}`
    - `{{${email}}}`
    - `{{${email_address}}}`
    - `{{${phone_number}}}`
    - `{{${date_of_birth}}}`
{% endraw %}