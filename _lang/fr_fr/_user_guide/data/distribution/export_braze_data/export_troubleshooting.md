---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes d'exportation
page_order: 6
page_type: reference
description: "Cet article de référence traite des scénarios de résolution des problèmes courants pour les exportations dans les flux de travail CSV et API."
---

# Résolution des problèmes d'exportation

> Cette page traite des scénarios de résolution des problèmes courants pour les exportations dans les flux de travail CSV et API.

Utilisez les onglets pour indiquer si vous exportez vers le **compartiment S3 par défaut de Braze** ou vers un **partenaire de stockage cloud**.

{% sdktabs %}
{% sdktab Default export %}

Si aucun partenaire de stockage n'est défini comme destination d'exportation par défaut, Braze utilise son propre compartiment Amazon S3 pour stocker vos fichiers d'exportation. Les fichiers dans cette configuration sont temporaires et expirent après quatre heures.

## Exportations CSV
Lorsque vous exportez un fichier CSV depuis le tableau de bord, Braze envoie un lien de téléchargement par e-mail à l'utilisateur connecté. Ce lien renvoie vers un fichier ZIP hébergé dans le compartiment S3 de Braze. Le fichier ZIP contient plusieurs fichiers plus petits qui, ensemble, constituent votre exportation.

Vous devez être connecté au tableau de bord de Braze pour utiliser le lien, et le fichier n'est disponible que pendant quatre heures. Passé ce délai, le lien ne fonctionne plus et les données sont supprimées. Si vous rencontrez des échecs répétés avec des exportations très volumineuses (plus de 500 000 utilisateurs), l'exportation peut échouer. Dans ce cas, essayez de diviser votre exportation en groupes ou champs plus petits, ou envisagez de configurer un partenaire de stockage.

### Erreurs courantes

- Si vous rencontrez une erreur `AccessDenied`, il est possible que le fichier ait déjà expiré ou que vous ayez tenté de l'ouvrir avant qu'il ne soit prêt. Les rapports volumineux prennent plus de temps à générer ; patientez quelques minutes et réessayez.
- Une erreur `ExpiredToken` indique que le délai de quatre heures est écoulé. Relancez l'exportation afin de générer un nouveau lien.
- Le message `Looks like the file doesn't exist anymore` apparaît généralement lorsque l'e-mail est envoyé, mais que le fichier n'a pas encore fini d'être chargé vers S3. Patienter quelques minutes résout généralement le problème.
- Les apostrophes ajoutées au début de certains champs (tels que `-`, `=`, `+` ou `@`) sont un comportement attendu. Par exemple, `-1943` devient `'-1943` dans le fichier CSV. Braze procède ainsi afin d'éviter que les tableurs n'interprètent incorrectement les données. Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).

## Exportations API
Lorsque vous effectuez une exportation via les API d'exportation sans stockage cloud, Braze enregistre les fichiers dans son compartiment S3. Vous ne recevez pas d'e-mail ; la réponse de l'API inclut à la place une URL de téléchargement temporaire. L'exportation se présente sous la forme d'un fichier ZIP contenant plusieurs fichiers JSON, chacun avec un utilisateur par ligne.

Comme pour les exportations CSV, les liens provenant de l'API expirent au bout de quatre heures. Si vous cliquez sur le lien trop tôt, des erreurs peuvent apparaître car le fichier n'est pas encore prêt. Vous pouvez fournir un `callback_endpoint` dans votre requête si vous souhaitez que Braze vous notifie lorsque le fichier est disponible.

Les exportations API volumineuses peuvent également expirer. Dans ce cas, essayez de réduire la taille de vos requêtes ou connectez un partenaire de stockage pour gérer le volume.

### Erreurs courantes
- `AccessDenied` ou `ExpiredToken` signifie généralement que le lien a expiré ou n'était pas encore prêt. Relancez l'exportation ou patientez un peu plus longtemps.

{% endsdktab %}

{% sdktab Cloud storage connected %}

Lorsque vous connectez un partenaire de stockage (tel qu'Amazon S3, Google Cloud Storage ou Azure Blob) et que vous le désignez comme destination d'exportation par défaut depuis la page **Partenaires technologiques** du tableau de bord, Braze enregistre vos exportations directement dans votre compartiment. Cette configuration est généralement plus fiable pour les exportations volumineuses.

## Exportations CSV
Avec les exportations CSV, Braze vous envoie un lien de téléchargement par e-mail. Ce lien expire après un court délai (généralement environ quatre heures). Lorsqu'un partenaire de stockage est connecté et défini comme destination d'exportation par défaut, Braze envoie également une copie de l'exportation vers votre compartiment connecté. Cette copie réside dans votre propre infrastructure, où l'expiration et la conservation sont régies par vos politiques de stockage.

Dans le stockage cloud, les exportations CSV sont regroupées dans un fichier ZIP. Le fichier ZIP contient plusieurs fichiers CSV de plus petite taille. Les exportations volumineuses sont souvent divisées en lots (par exemple, environ 5 000 utilisateurs chacun), et la taille des lots peut varier. Des fichiers plus petits n'indiquent pas nécessairement des données manquantes. Si le lien envoyé par e-mail ne fonctionne pas mais que la copie dans votre espace de stockage est disponible, vous pouvez toujours récupérer vos données directement depuis votre compartiment.

### Erreurs courantes

- `AccessDenied` signifie que Braze n'a pas pu écrire dans votre compartiment. Vérifiez que vos identifiants et autorisations sont toujours valides.
- `ExpiredToken` apparaît si Braze n'a plus accès à votre compartiment. Mettez à jour vos identifiants dans le tableau de bord de Braze.
- Si certains fichiers semblent plus petits que prévu, c'est un comportement normal. Le processus d'exportation divise intentionnellement les fichiers pour des raisons de stabilité.
- Les apostrophes ajoutées au début de certains champs (tels que `-`, `=`, `+` ou `@`) sont un comportement attendu. Par exemple, `-1943` devient `'-1943` dans le fichier CSV. Braze procède ainsi afin d'éviter que les tableurs n'interprètent incorrectement les données. Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).

## Exportations API
Lorsque vous exportez des données via les API avec un partenaire de stockage connecté, les fichiers exportés sont enregistrés dans votre compartiment. Aucun e-mail n'est envoyé. Les objets sous-jacents résident dans votre espace de stockage et respectent vos paramètres de conservation, même si les URL de téléchargement fournies par Braze peuvent être limitées dans le temps. Chaque fichier ZIP contient des objets JSON, un par ligne. Les exportations volumineuses peuvent être divisées en plusieurs fichiers ZIP au lieu d'un seul, ce qui rend généralement cette méthode plus fiable pour les exportations lourdes.

### Erreurs courantes

- `AccessDenied` survient lorsque Braze ne parvient pas à écrire dans votre compartiment ou lorsque les objets ont été supprimés par la suite. Vérifiez les autorisations et assurez-vous qu'aucun processus externe ne supprime les fichiers.
- `ExpiredToken` signifie que les identifiants d'accès de Braze à votre compartiment sont obsolètes. Actualisez-les dans le tableau de bord.
- Si des fichiers sont manquants ou plus petits que prévu, vérifiez d'abord qu'aucun processus extérieur à Braze ne supprime des objets. Des fichiers de taille réduite sont un comportement attendu.

{% endsdktab %}
{% endsdktabs %}