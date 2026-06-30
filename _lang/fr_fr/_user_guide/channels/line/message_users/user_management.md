---
nav_title: Gestion des utilisateurs
article_title: Gestion des utilisateurs LINE
page_order: 0
description: "Cet article couvre l'ID utilisateur LINE et comment le configurer."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# Gestion des utilisateurs LINE {#line-user-management}

> L'ID utilisateur LINE est stocké dans l'attribut de profil utilisateur appelé `native_line_id`, qui est utilisé pour envoyer des messages à un utilisateur sur le canal LINE. Cet article explique comment configurer et trouver l'attribut `native_line_id`.

Les données utilisateur client sont représentées dans un [profil utilisateur Braze]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle). Un profil utilisateur stocke des informations et des attributs sur les utilisateurs d'une entreprise, tels que les prénoms et les adresses e-mail.

Lorsque vous envoyez des messages LINE via Braze, Braze utilise l'attribut `native_line_id` pour identifier les utilisateurs auxquels envoyer le message. Lorsque LINE envoie des événements webhook à Braze, par exemple lorsqu'un utilisateur suit un canal ou répond à un message, le `native_line_id` est utilisé pour rechercher le profil utilisateur correspondant.

{% alert note %}
Les ID utilisateur LINE sont distincts par fournisseur LINE. Un utilisateur spécifique aura des ID utilisateur LINE différents pour chaque fournisseur qu'il suit. Il est peu probable que les utilisateurs connaissent leur ID LINE (contrairement à leur adresse e-mail ou leur numéro de téléphone), car il change pour chaque marque qu'ils suivent.
{% endalert %}

## Configurer l'attribut `native_line_id` {#setting-the-native_line_id-attribute}

Il existe plusieurs scénarios dans lesquels `native_line_id` est défini sur le profil utilisateur, décrits ci-dessous.

| Scénario | Existence d'un profil utilisateur avec `native_line_id` | Résultat |
| --- | --- | --- |
| Un utilisateur suit un canal LINE | Non | Un profil utilisateur anonyme est créé (une fusion sera nécessaire) :<br> - `native_line_id` est défini sur l'ID LINE de l'utilisateur <br>- L'alias d'utilisateur `line_id` est défini sur l'ID LINE de l'utilisateur<br>- L'utilisateur est abonné au groupe d'abonnement Braze du canal |
| Un utilisateur suit un canal LINE | Oui | Tous les profils utilisateur avec le `native_line_id` :<br>- Sont abonnés au groupe d'abonnement Braze du canal |
| L'entreprise utilise l'import CSV d'utilisateurs avec une colonne `native_line_id` | Non | Si aucun profil utilisateur n'existe pour l'`external_id` ou l'alias d'utilisateur spécifié :<br>- `native_line_id` est défini sur la valeur spécifiée<br> - Tous les autres attributs spécifiés dans le CSV sont définis sur le profil utilisateur |
| L'entreprise utilise l'import CSV d'utilisateurs avec une colonne `native_line_id` | Oui | Si un profil utilisateur existe pour l'`external_id` ou l'alias d'utilisateur spécifié :<br>- `native_line_id` est défini sur la valeur spécifiée<br>- Tous les autres attributs spécifiés dans le CSV sont définis sur le profil utilisateur<br>- Plusieurs profils ont le même `native_line_id` |
| L'entreprise utilise l'endpoint `/users/track` et spécifie l'attribut `native_line_id` | Non | Si aucun profil utilisateur n'existe pour l'utilisateur spécifié ([spécifié par `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)) :<br>- `native_line_id` est défini sur la valeur spécifiée<br>- Tous les autres attributs spécifiés dans la requête sont définis sur le profil utilisateur |
| L'entreprise utilise l'endpoint `/users/track` et spécifie l'attribut `native_line_id` | Oui | Si un profil utilisateur existe pour l'utilisateur spécifié ([spécifié par `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)) :<br>- `native_line_id` est défini sur la valeur spécifiée<br>- Tous les autres attributs spécifiés dans la requête sont définis sur le profil utilisateur<br>- Plusieurs profils ont le même `native_line_id` |
| L'entreprise demande à Braze d'exécuter le synchroniseur de statut d'abonnement | Non | Si un ID utilisateur LINE est renvoyé par LINE sans profil utilisateur correspondant dans Braze, un profil utilisateur anonyme est créé :<br>- `native_line_id` est défini sur l'ID LINE de l'utilisateur<br>- L'alias d'utilisateur `line_id` est défini sur l'ID LINE de l'utilisateur<br>- L'utilisateur est abonné au groupe d'abonnement Braze du canal<br><br>Notez que si un utilisateur avec le même ID LINE est créé ultérieurement, il y aura des utilisateurs en double, mais les deux auront le bon statut d'abonnement LINE. La fusion d'utilisateurs peut nettoyer votre base d'utilisateurs dans ces cas. |
| L'entreprise demande à Braze d'exécuter le synchroniseur de statut d'abonnement | Oui | Si un ID utilisateur LINE est renvoyé par LINE avec un profil utilisateur correspondant dans Braze :<br>- L'utilisateur est abonné au groupe d'abonnement Braze du canal |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurer l'attribut nativelineid" }

## Trouver le `native_line_id` {#finding-the-native_line_id}

Lorsque vous consultez un profil utilisateur dans le tableau de bord de Braze, vous pouvez vérifier si l'attribut `native_line_id` est défini en accédant à l'onglet **Engagement** > section **Contact Settings** > section **LINE**.

Si le `native_line_id` a été défini, il sera affiché sous **LINE User ID**. Sinon, il n'apparaîtra pas.

![Paramètres de contact LINE dans l'onglet Engagement.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}