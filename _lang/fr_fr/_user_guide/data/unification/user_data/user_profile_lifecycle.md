---
nav_title: Cycle de vie du profil utilisateur
article_title: Cycle de vie du profil utilisateur
page_order: 2
page_type: reference
description: "Cet article de référence décrit le cycle de vie du profil utilisateur de Braze et les différentes façons d'identifier et de référencer un profil utilisateur."

---

# Cycle de vie du profil utilisateur {#user-profile-lifecycle}

> Cet article décrit le cycle de vie du profil utilisateur de Braze et les différentes manières d'identifier et de référencer un profil utilisateur. Si vous cherchez à mieux comprendre le cycle de vie de vos clients, consultez plutôt notre cours d'apprentissage Braze sur [le mappage des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles).

Toutes les données persistantes associées à un utilisateur sont stockées dans son profil utilisateur. Après la création d'un profil utilisateur, soit par l'API, soit après la reconnaissance d'un utilisateur par le SDK, vous pouvez attribuer un certain nombre de paramètres à ce profil afin d'identifier et de référencer cet utilisateur.

Ces paramètres comprennent :

* `braze_id` (attribué par Braze)
* `external_id`
* `email`
* `phone`
* Un nombre illimité d'alias d'utilisateur personnalisés que vous définissez

## Profils utilisateurs anonymes {#anonymous-user-profiles}

Tout utilisateur sans `external_id` désigné est appelé un [utilisateur anonyme]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users). Par exemple, il peut s'agir d'utilisateurs qui ont visité votre site web sans s'inscrire, ou d'utilisateurs qui ont téléchargé votre application mobile sans créer de profil.

Au départ, lorsqu'un utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec un `braze_id` associé : un identifiant unique automatiquement attribué par Braze, qui ne peut pas être modifié et qui est spécifique à l'appareil. Cet identifiant peut être utilisé pour mettre à jour le profil utilisateur via l'[API]({{site.baseurl}}/api/endpoints/user_data).

## Profils utilisateurs identifiés {#identified-user-profiles}

Lorsqu'un utilisateur est reconnaissable dans votre application (en fournissant un identifiant utilisateur ou une adresse e-mail), nous vous recommandons d'attribuer un `external_id` au profil de cet utilisateur à l'aide de la méthode `changeUser` ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). Un `external_id` vous permet d'identifier le même profil utilisateur sur plusieurs appareils.

Les avantages supplémentaires de l'utilisation d'un `external_id` sont les suivants :

- Offrir une expérience utilisateur cohérente sur plusieurs appareils et plateformes (par exemple, ne pas envoyer de notifications d'utilisateur inactif sur la tablette Android d'un utilisateur alors qu'il est un utilisateur fidèle de l'application iPhone).
- Améliorer la précision de vos analyses en confirmant que les utilisateurs ne créent pas un nouveau profil utilisateur à chaque fois qu'ils désinstallent et réinstallent l'application, ou qu'ils l'installent sur un autre appareil.
- Permettre l'importation de données utilisateur provenant de sources extérieures à l'application à l'aide des [endpoints de données utilisateur]({{site.baseurl}}/api/endpoints/user_data) et cibler les utilisateurs avec des messages transactionnels via nos [endpoints de messaging]({{site.baseurl}}/api/endpoints/messaging).
- Rechercher des utilisateurs individuels à l'aide de nos [filtres]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) « Testing » dans le segmenteur, et sur la page [**Rechercher des utilisateurs**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

### Considérations relatives aux ID externes {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### Risque d'utiliser un e-mail ou un e-mail haché comme ID externe {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut simplifier la gestion des identités entre vos sources de données ; cependant, il est important de prendre en compte les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.

- **Informations devinables :** les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail d'une autre personne comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.

### Ce qui se passe lorsque vous identifiez des utilisateurs anonymes {#what-happens-when-you-identify-anonymous-users}

L'un des deux scénarios suivants peut se produire lorsque vous identifiez des utilisateurs anonymes :

1) **Un utilisateur anonyme devient un nouvel utilisateur identifié :** <br>Si l'`external_id` n'existe pas encore dans Braze, l'utilisateur anonyme devient un nouvel utilisateur identifié et conserve tous les mêmes attributs et l'historique de l'utilisateur anonyme.

2) **Un utilisateur anonyme est identifié comme un utilisateur déjà existant :** <br>Si l'`external_id` existe déjà dans Braze, cet utilisateur a été précédemment identifié comme utilisateur dans le système d'une autre manière, par exemple via un autre appareil (comme une tablette) ou des données utilisateur importées.

En d'autres termes, vous disposez déjà d'un profil utilisateur pour cet utilisateur. Dans ce cas, Braze effectuera les opérations suivantes :
1. Rendre orphelin l'utilisateur anonyme
2. Fusionner les [champs spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) qui n'existent pas encore sur le profil utilisateur identifié à partir du profil anonyme
3. Supprimer le profil anonyme de votre base d'utilisateurs afin que le nombre d'utilisateurs ne soit pas artificiellement gonflé

Si l'utilisateur anonyme et l'utilisateur connu ont tous deux un prénom, le prénom de l'utilisateur connu est conservé. Si l'utilisateur connu a une valeur nulle et que l'utilisateur anonyme a une valeur, la valeur de l'utilisateur anonyme est fusionnée dans le profil de l'utilisateur connu si la valeur fait partie de ces [champs spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

{% alert important %}
Toutes les données ne sont pas fusionnées à partir du profil anonyme. Les jetons de notification push et l'historique de messaging sont transférés, et les attributs personnalisés, les événements personnalisés et l'historique d'achats du profil anonyme sont fusionnés dans l'utilisateur identifié uniquement lorsque ces champs n'existent pas déjà sur le profil utilisateur identifié. En cas de données conflictuelles, les valeurs de l'utilisateur identifié sont conservées. Consultez le [comportement de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) pour la liste complète des champs qui sont et ne sont pas transférés.
{% endalert %}

Pour savoir comment définir un `external_id` sur un profil utilisateur, consultez notre documentation ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)).

{% alert note %}
Les utilisateurs orphelins ne sont pas éligibles à la réception de messages.
{% endalert %}

### Fusionner les utilisateurs en double {#merging-duplicate-users}

Lorsque vous identifiez des profils utilisateurs en double dans votre espace de travail, vous pouvez les fusionner à l'aide de la REST API. Pour plus d'informations sur la fusion des utilisateurs et les méthodes disponibles, consultez [Fusionner les utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

## Alias d'utilisateurs {#user-aliases}

Pour faire référence aux utilisateurs par des identifiants autres que l'`external_id` de Braze, définissez des alias d'utilisateurs sur un profil utilisateur. Tout alias défini sur un profil utilisateur fonctionnera en complément du `braze_id` ou de l'`external_id` de l'utilisateur, et non en remplacement. Il n'y a pas de limite au nombre d'alias que vous pouvez définir sur un profil utilisateur.

Chaque alias fonctionne comme une paire clé-valeur composée de deux parties : un `alias_label`, qui définit la clé de l'alias, et un `alias_name`, qui définit la valeur. Un `alias_name` pour un libellé donné doit être unique dans l'ensemble de votre base d'utilisateurs (tout comme l'`external_id`). Si vous essayez de mettre à jour un second profil utilisateur avec une combinaison de libellé et de nom déjà existante, le profil utilisateur ne sera pas mis à jour.

### Mise à jour des alias d'utilisateurs {#updating-user-aliases}

Un alias peut être mis à jour avec un nouveau nom pour un libellé donné après sa création, soit en utilisant nos [endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint), soit en transmettant un nouveau nom via le SDK. L'alias d'utilisateur sera alors visible lors de l'exportation des données de cet utilisateur.

![Deux profils utilisateurs différents pour des utilisateurs distincts avec le même libellé d'alias d'utilisateur mais des noms d'alias différents]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Étiquetage des utilisateurs anonymes {#tagging-anonymous-users}

Les alias d'utilisateurs vous permettent également d'étiqueter les utilisateurs anonymes avec un identifiant. Par exemple, si un utilisateur fournit son adresse e-mail à votre site eCommerce mais ne s'est pas encore inscrit, l'adresse e-mail peut être utilisée comme alias pour cet utilisateur anonyme. Ces utilisateurs peuvent ensuite être exportés à l'aide de leurs alias ou référencés par l'API.

### Comportement des alias sur les profils utilisateurs anonymes {#behavior-of-aliases-on-anonymous-user-profiles}

Si un profil utilisateur anonyme possédant un alias est ultérieurement reconnu avec un `external_id`, il sera traité comme un profil utilisateur identifié normal, mais conservera son alias existant et pourra toujours être référencé par cet alias.

### Recherche d'un alias d'utilisateur {#searching-for-a-user-alias}

Si vous connaissez le nom et le libellé de l'alias d'un utilisateur, vous pouvez trouver l'utilisateur dans **Search Users** avec le format `alias_label:alias_name`. Par exemple, si vous avez un profil avec alias uniquement dont le nom est `alias_name: bobby_alias` et le libellé `alias_label: m4pzOndtA-CnO0u`, vous pouvez trouver cet utilisateur en saisissant `m4pzOndtA-CnO0u:bobby_alias`.

Si vous ne disposez pas de ces informations, vous pouvez appeler l'[endpoint `Export user profile by identifier`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) et trouver l'alias d'utilisateur dans la réponse de l'API.

### Définition d'alias sur des profils utilisateurs connus {#setting-aliases-on-known-user-profiles}

Un alias d'utilisateur peut également être défini sur un profil utilisateur connu pour référencer un utilisateur connu par un autre ID externe connu. Par exemple, un utilisateur peut avoir un ID d'outil d'aide à la décision (comme un ID Amplitude) que vous souhaitez référencer dans Braze.

Pour plus d'informations sur la définition d'un alias d'utilisateur, consultez notre documentation pour chaque plateforme ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#aliasing-users)).

![Organigramme du cycle de vie d'un profil utilisateur dans Braze. Lorsque changeUser() est appelé pour un utilisateur anonyme, cet utilisateur devient un utilisateur identifié et les données sont migrées vers son profil utilisateur identifié. L'utilisateur identifié possède un ID Braze et un ID externe. À ce stade, si un second utilisateur anonyme fait l'objet d'un appel changeUser(), les champs de données utilisateur qui n'existent pas déjà sur l'utilisateur identifié seront fusionnés. Si l'utilisateur identifié se voit ajouter un alias à son profil utilisateur existant, aucune donnée ne sera affectée mais il deviendra un utilisateur identifié avec alias. Si un troisième utilisateur anonyme possédant le même libellé d'alias que l'utilisateur identifié mais un nom d'alias différent fait ensuite l'objet d'un appel changeUser(), tous les champs qui n'existent pas sur l'utilisateur identifié seront fusionnés et le libellé d'alias du profil utilisateur identifié sera conservé.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Vous avez du mal à visualiser comment cela peut se présenter pour le cycle de vie du profil utilisateur de vos clients ? Consultez les [bonnes pratiques]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices) pour découvrir les meilleures pratiques de collecte de données utilisateur.
{% endalert %}

## Cas d'usage avancé {#advanced-use-case}

Vous pouvez définir un nouvel alias d'utilisateur pour des profils utilisateurs identifiés existants via notre SDK et notre API en utilisant les [endpoints User Data]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint). Cependant, les alias d'utilisateurs ne peuvent pas être définis via l'API pour un profil utilisateur inconnu existant.

Les alias d'utilisateurs sont également fusionnés au cours du processus. Toutefois, si l'utilisateur à orpheliner et l'utilisateur cible possèdent tous deux un alias avec le même libellé, seul l'alias de l'utilisateur cible est conservé.

La désinstallation et la réinstallation d'une application génèrent un nouveau `braze_id` anonyme pour cet utilisateur.

### Résolution des problèmes avec les ID utilisateur {#troubleshooting-with-user-ids}

Tous les ID utilisateur peuvent être utilisés pour rechercher et identifier des utilisateurs dans votre tableau de bord à des fins de test. Pour trouver votre utilisateur dans le tableau de bord de Braze, consultez la section [Ajout d'utilisateurs test]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).

{% alert important %}
Braze bloque les profils utilisateurs dont la taille augmente de manière anormale (« utilisateurs factices »), car ces profils sont généralement le résultat d'une mauvaise intégration. Un profil est bloqué lorsqu'il dépasse l'un des seuils suivants :

- Plus de 5 000 000 de sessions
- Plus de 20 000 noms d'événements personnalisés distincts
- Plus de 20 000 noms de produits distincts dans les achats

Après le blocage d'un profil, Braze cesse d'ingérer toutes les données entrantes pour ce profil, provenant aussi bien des SDK que de la REST API. Si vous constatez que cela est arrivé à un utilisateur légitime, contactez votre gestionnaire de compte Braze. Pour en savoir plus, consultez la section [Blocage du spam]({{site.baseurl}}/user_archival).
{% endalert %}