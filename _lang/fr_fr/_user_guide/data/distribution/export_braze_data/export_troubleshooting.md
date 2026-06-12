---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes d'exportation
page_order: 6
page_type: reference
description: "Cet article de référence traite des scénarios de résolution des problèmes courants pour les exportations dans les flux de travail CSV et API."
---

# Résolution des problèmes d'exportation {#export-troubleshooting}

> Cette page traite des scénarios de résolution des problèmes courants pour les exportations dans les flux de travail CSV et API.

Utilisez les onglets pour indiquer si vous exportez vers le **compartiment S3 par défaut de Braze** ou vers un **partenaire de stockage cloud**.

{% sdktabs %}
{% sdktab Default export %}

Si aucun partenaire de stockage n'est défini comme destination d'exportation par défaut, Braze utilise son propre compartiment Amazon S3 pour stocker vos fichiers d'exportation. Les fichiers dans cette configuration sont temporaires et expirent après quatre heures.

## Exportations CSV {#csv-exports}
Lorsque vous exportez un fichier CSV depuis le tableau de bord, Braze envoie un lien de téléchargement par e-mail à l'utilisateur connecté. Ce lien renvoie vers un fichier ZIP hébergé dans le compartiment S3 de Braze. Le fichier ZIP contient plusieurs fichiers plus petits qui, ensemble, constituent votre exportation.

Vous devez être connecté au tableau de bord de Braze pour utiliser le lien, et le fichier n'est disponible que pendant quatre heures. Passé ce délai, le lien ne fonctionne plus et les données sont supprimées. Si vous rencontrez des échecs répétés avec des exportations très volumineuses (plus de 500 000 utilisateurs), l'exportation peut échouer. Dans ce cas, essayez de diviser votre exportation en groupes ou champs plus petits, ou envisagez de configurer un partenaire de stockage.

### Erreurs courantes {#common-errors}

- Si vous rencontrez une erreur `AccessDenied`, il est possible que le fichier ait déjà expiré ou que vous ayez tenté de l'ouvrir avant qu'il ne soit prêt. Les rapports volumineux prennent plus de temps à générer ; patientez quelques minutes et réessayez.
- Une erreur `ExpiredToken` indique que le délai de quatre heures est écoulé. Relancez l'exportation afin de générer un nouveau lien.
- Le message `Looks like the file doesn't exist anymore` apparaît généralement lorsque l'e-mail est envoyé, mais que le fichier n'a pas encore fini d'être chargé vers S3. Patienter quelques minutes résout généralement le problème.
- Les apostrophes ajoutées au début de certains champs (tels que `-`, `=`, `+` ou `@`) sont un comportement attendu. Par exemple, `-1943` devient `'-1943` dans le fichier CSV. Braze procède ainsi afin d'éviter que les tableurs n'interprètent incorrectement les données. Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).

## Exportations API {#api-exports}
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
Lorsque vous exportez des données via les API avec un partenaire de stockage connecté, les fichiers exportés sont enregistrés dans votre compartiment. Aucun e-mail n'est envoyé. Les objets sous-jacents résident dans votre espace de stockage et respectent vos paramètres de conservation, même si les URL de téléchargement fournies par Braze peuvent être limitées dans le temps.

Les fichiers apparaissent généralement dans votre compartiment au fur et à mesure de l'exportation, vous n'avez donc pas besoin d'attendre la fin complète du traitement pour accéder aux résultats partiels. Braze charge chaque lot terminé de manière incrémentielle au lieu de tout conserver jusqu'à la fin. Les exportations volumineuses sont divisées en plusieurs fichiers compressés (ZIP ou GZIP), chacun contenant des objets JSON, un par ligne. Cela rend cette méthode plus fiable pour les exportations lourdes.

### Erreurs courantes

- `AccessDenied` survient lorsque Braze ne parvient pas à écrire dans votre compartiment ou lorsque les objets ont été supprimés par la suite. Vérifiez les autorisations et assurez-vous qu'aucun processus externe ne supprime les fichiers.
- `ExpiredToken` signifie que les identifiants d'accès de Braze à votre compartiment sont obsolètes. Actualisez-les dans le tableau de bord.
- Si des fichiers sont manquants ou plus petits que prévu, vérifiez d'abord qu'aucun processus extérieur à Braze ne supprime des objets. Des fichiers de taille réduite sont un comportement attendu.

{% endsdktab %}
{% endsdktabs %}

## Analyses des campagnes et Canvas {#campaign-and-canvas-analytics}

### Le nombre d'utilisateurs dans l'exportation CSV ne correspond pas aux *messages envoyés* ou aux *destinataires uniques* {#number-of-users-in-csv-export-doesnt-match-_messages-sent_-or-_unique-recipients_}

L'exportation CSV d'une campagne peut afficher un nombre d'utilisateurs différent de celui des *messages envoyés* et des *destinataires uniques* pour les raisons suivantes :

#### La rééligibilité est activée {#re-eligibility-is-turned-on}

Si les utilisateurs sont (ou ont été à un moment donné) en mesure de recevoir la campagne plus d'une fois, les chiffres d'analyse de la campagne et le nombre de lignes dans l'exportation des données utilisateur ne correspondent pas. *Messages envoyés* comptabilise chaque envoi, y compris lorsque le même utilisateur reçoit le message plusieurs fois. Le téléchargement **Exporter les données utilisateur en CSV** répertorie les utilisateurs uniques — une ligne par profil ayant reçu la campagne — et non une ligne par envoi. Par exemple, si *Messages envoyés* indique 12 et que le fichier CSV contient 10 lignes, ces 12 envois ont été adressés à 10 utilisateurs distincts (certains utilisateurs ont reçu la campagne plus d'une fois).

#### Des utilisateurs ont été supprimés ou fusionnés depuis l'envoi de la campagne ou du Canvas {#users-were-deleted-or-merged-since-the-campaign-or-canvas-sent}

L'exportation CSV fournit un instantané des utilisateurs existants ayant reçu une campagne ou un Canvas donné. Étant donné que des utilisateurs peuvent être supprimés ou fusionnés, le nombre dans l'exportation CSV peut être inférieur au nombre de destinataires uniques. Par exemple, si 1 000 utilisateurs reçoivent une campagne, celle-ci affiche 1 000 destinataires uniques, et l'exportation CSV du même jour indique également 1 000 utilisateurs. Si un mois plus tard, 50 de ces 1 000 utilisateurs sont supprimés, l'exportation CSV contient 950 utilisateurs tandis que le compteur incrémenté de destinataires uniques reste à 1 000.

## E-mails d'exportation de segments depuis le tableau de bord {#dashboard-segment-export-emails}

### « Le segment est trop volumineux » ou l'exportation échoue alors que mon segment semble contenir moins de 500 000 utilisateurs {#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users}

La **taille d'un segment dans le tableau de bord est une estimation**. L'exportation CSV utilise cette estimation pour appliquer la [limite d'exportation de 500 000 utilisateurs]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/#segment-csv-export-details) ; le pipeline d'exportation peut également évaluer la taille différemment de l'interface du générateur de segments. Si les exportations échouent pour un segment proche de ce seuil, utilisez les [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) ou divisez l'audience en segments plus petits, ou utilisez l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) comme décrit dans [Exporter des segments volumineux]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/#exporting-large-segments).

### Pourquoi est-ce que je ne reçois pas les e-mails d'exportation de segments ? {#why-arent-i-receiving-segment-export-emails}

Commencez par vérifier votre dossier de courrier indésirable pour un e-mail provenant de `no-reply@alerts.braze.com`. Si l'e-mail s'y trouve, ajoutez cette adresse à votre liste d'expéditeurs approuvés afin que les futurs messages d'exportation ne soient pas filtrés.

Si l'e-mail ne se trouve pas dans votre dossier de courrier indésirable, vérifiez si un autre membre de votre équipe peut recevoir l'exportation. Si personne ne la reçoit, tenez compte de la taille de votre exportation. Le délai de réception varie en fonction de la taille de l'exportation, mais si l'e-mail n'est pas arrivé au bout d'une heure, contactez l'[Assistance]({{site.baseurl}}/braze_support/).

## Téléchargements de l'API d'exportation de segments {#segment-export-api-downloads}

### Impossible de télécharger un fichier ZIP de segment exporté depuis une URL Braze {#cant-download-an-exported-segment-zip-file-from-a-braze-url}

Si vous obtenez une erreur `403 Forbidden` lors de l'utilisation de l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/), il est possible que le fichier ne soit pas encore prêt. Les exportations volumineuses peuvent prendre du temps à traiter. Patientez jusqu'à une heure avant de réessayer le téléchargement.

Si vous utilisez un script automatisé pour récupérer le fichier, vous pouvez également recevoir une erreur `403 Forbidden` lorsque vous demandez l'URL trop tôt. Si vous exportez régulièrement des données de segments, envisagez de connecter votre propre intégration de compartiment S3 et de transmettre les fichiers à votre propre pipeline ETL (extraire, transformer, charger).

Les exportations prennent du temps, c'est pourquoi un accès immédiat depuis un script échoue souvent. Vous pouvez :

- Interroger l'URL de téléchargement avec des délais exponentiels, ou
- Utiliser le [paramètre `callback_endpoint`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#request-parameters) et le diriger vers un service qui exécute votre script lorsque l'exportation est prête.