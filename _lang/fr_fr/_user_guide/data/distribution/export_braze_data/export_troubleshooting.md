---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes d'exportation
page_order: 6
page_type: reference
description: "Diagnostiquez les échecs d'exportation CSV et API à l'aide d'un index de symptômes, d'un parcours d'investigation standard et de conseils spécifiques à chaque destination de stockage."
---

# Résolution des problèmes d'exportation {#export-troubleshooting}

> Utilisez cette page pour diagnostiquer les problèmes d'exportation CSV et API dans le tableau de bord et les API d'exportation. Pour les flux de travail et les limites d'exportation, consultez [Exporter les données de segment au format CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) et [API d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_apis).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

Trouvez le comportement que vous observez dans le tableau, puis accédez à la section correspondante pour des vérifications ciblées.

| Symptôme | Accéder à |
| --- | --- |
| Le lien de téléchargement CSV renvoie `AccessDenied`, `ExpiredToken` ou « le fichier n'existe pas » | [Exportation par défaut : erreurs CSV](#defaultexport_csv-exports) ou [Stockage cloud : erreurs CSV](#csv-exports-1) |
| L'URL de téléchargement d'exportation API renvoie `403 Forbidden` | [Impossible de télécharger un ZIP de Segment exporté](#cant-download-an-exported-segment-zip-from-a-braze-url) |
| L'exportation de Segment échoue ou indique que le Segment est trop volumineux | [Le Segment est trop volumineux](#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users) |
| Aucun e-mail d'exportation de Segment reçu | [Pas d'e-mail d'exportation de Segment](#not-receiving-segment-export-emails) |
| Le nombre de lignes du CSV ne correspond pas aux analyses de la campagne | [Écart entre les analyses de Campaign et de Canvas](#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients) |
| Des colonnes attendues sont absentes du fichier d'exportation | [Colonnes manquantes](#expected-columns-are-missing-from-a-segment-export-file) |
| L'exportation vers le stockage cloud affiche `AccessDenied` ou `ExpiredToken` | [Stockage cloud connecté : erreurs API](#common-errors-1) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme d'exportation" }

## Processus d'investigation standard {#standard-investigation-path}

Utilisez ce workflow pour chaque incident d'exportation. Commencez à l'étape 1.

1. Confirmez si vous exportez vers le compartiment S3 Braze par défaut ou un partenaire de stockage cloud connecté. L'expiration des liens et le comportement de relance diffèrent entre les deux.
2. Pour les exportations CSV depuis le tableau de bord, confirmez que vous êtes connecté à Braze lorsque vous ouvrez le lien de téléchargement. Les liens du compartiment par défaut nécessitent une session active sur le tableau de bord.
3. Vérifiez depuis combien de temps l'exportation est terminée. Les liens de téléchargement envoyés par e-mail depuis le tableau de bord expirent au bout de quatre heures, que vous utilisiez le compartiment Braze par défaut ou un partenaire de stockage connecté. Lorsqu'un partenaire de stockage est connecté, Braze envoie également une copie dans votre compartiment ; cette copie suit vos politiques de conservation et peut rester disponible après l'expiration du lien envoyé par e-mail.
4. Pour les exportations de Segments volumineux, confirmez que l'audience est inférieure à la limite de 500 000 utilisateurs pour l'exportation CSV depuis le tableau de bord. Les estimations du générateur de Segments peuvent différer de l'évaluation du pipeline d'exportation.
5. Pour les exportations via l'API, attendez la fin du traitement avant de télécharger. Utilisez `callback_endpoint` sur [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) ou interrogez avec des délais exponentiels au lieu de demander l'URL immédiatement.
6. Si vous êtes toujours bloqué, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) en indiquant le type d'exportation (CSV ou API), l'identifiant du Segment ou de la Campaign, l'horodatage (avec le fuseau horaire) et le message d'erreur exact.

## Destinations de stockage {#cloud-storage-connected}

Utilisez les onglets pour indiquer si vous exportez vers le compartiment S3 par défaut de Braze ou vers un partenaire de stockage cloud. Pour les instructions relatives au stockage cloud, ouvrez l'onglet **Stockage cloud connecté** et consultez les sections CSV et API.

{% sdktabs %}
{% sdktab Default export %}

Si aucun partenaire de stockage n'est défini comme destination d'exportation par défaut, Braze utilise son propre compartiment Amazon S3 pour stocker vos fichiers d'exportation. Les fichiers dans cette configuration sont temporaires et expirent après quatre heures.

### Exportations CSV {#csv-exports}

Symptôme : un e-mail d'exportation CSV depuis le tableau de bord arrive, mais le lien de téléchargement échoue, ou l'exportation ne se termine jamais.


Lorsque vous exportez un fichier CSV depuis le tableau de bord, Braze envoie un lien de téléchargement par e-mail à l'utilisateur connecté. Ce lien renvoie vers un fichier ZIP hébergé dans le compartiment S3 de Braze. Le fichier ZIP contient plusieurs fichiers plus petits qui, ensemble, constituent votre exportation.

Vous devez être connecté au tableau de bord de Braze pour utiliser le lien, et le fichier n'est disponible que pendant quatre heures. Passé ce délai, le lien ne fonctionne plus et les données sont supprimées. Si vous rencontrez des échecs répétés avec des exportations très volumineuses (plus de 500 000 utilisateurs), l'exportation peut échouer. Dans ce cas, essayez de diviser votre exportation en groupes ou champs plus petits, ou envisagez de configurer un partenaire de stockage.

#### Erreurs courantes {#common-errors}

- Si vous rencontrez une erreur `AccessDenied`, il est possible que le fichier ait déjà expiré ou que vous ayez tenté de l'ouvrir avant qu'il ne soit prêt. Les rapports volumineux prennent plus de temps à générer ; patientez quelques minutes et réessayez.
- Une erreur `ExpiredToken` indique que le délai de quatre heures est écoulé. Relancez l'exportation afin de générer un nouveau lien.
- Le message `Looks like the file doesn't exist anymore` apparaît généralement lorsque l'e-mail est envoyé, mais que le fichier n'a pas encore fini d'être chargé vers S3. Patienter quelques minutes résout généralement le problème.
- Les apostrophes ajoutées au début de certains champs (tels que `-`, `=`, `+` ou `@`) sont un comportement attendu. Par exemple, `-1943` devient `'-1943` dans le fichier CSV. Braze procède ainsi afin d'éviter que les tableurs n'interprètent incorrectement les données. Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Exportations API {#api-exports}

Symptôme : un appel à l'API d'exportation réussit, mais l'URL de téléchargement échoue ou renvoie des données vides.


Lorsque vous effectuez une exportation via les API d'exportation sans stockage cloud, Braze enregistre les fichiers dans son compartiment S3. Vous ne recevez pas d'e-mail ; la réponse de l'API inclut à la place une URL de téléchargement temporaire. L'exportation se présente sous la forme d'un fichier ZIP contenant plusieurs fichiers JSON, chacun avec un utilisateur par ligne.

Comme pour les exportations CSV, les liens provenant de l'API expirent au bout de quatre heures. Si vous cliquez sur le lien trop tôt, des erreurs peuvent apparaître car le fichier n'est pas encore prêt. Vous pouvez fournir un `callback_endpoint` dans votre requête si vous souhaitez que Braze vous notifie lorsque le fichier est disponible.

Les exportations API volumineuses peuvent également expirer. Dans ce cas, essayez de réduire la taille de vos requêtes ou connectez un partenaire de stockage pour gérer le volume.

#### Erreurs courantes

- `AccessDenied` ou `ExpiredToken` signifie généralement que le lien a expiré ou n'était pas encore prêt. Relancez l'exportation ou patientez un peu plus longtemps.

{% endsdktab %}

{% sdktab Cloud storage connected %}

Lorsque vous connectez un partenaire de stockage (tel qu'Amazon S3, Google Cloud Storage ou Azure Blob) et que vous le désignez comme destination d'exportation par défaut depuis la page **Partenaires technologiques** du tableau de bord, Braze enregistre vos exportations directement dans votre compartiment. Cette configuration est généralement plus fiable pour les exportations volumineuses.

### Exportations CSV {#csv-exports-1}

Symptôme : le lien CSV envoyé par e-mail échoue, mais les fichiers apparaissent (ou n'apparaissent pas) dans votre compartiment connecté.


Avec les exportations CSV, Braze vous envoie un lien de téléchargement par e-mail. Ce lien expire après un court délai (généralement environ quatre heures). Lorsqu'un partenaire de stockage est connecté et défini comme destination d'exportation par défaut, Braze envoie également une copie de l'exportation vers votre compartiment connecté. Cette copie réside dans votre propre infrastructure, où l'expiration et la conservation sont régies par vos politiques de stockage.

Dans le stockage cloud, les exportations CSV sont regroupées dans un fichier ZIP. Le fichier ZIP contient plusieurs fichiers CSV de plus petite taille. Les exportations volumineuses sont souvent divisées en lots (par exemple, environ 5 000 utilisateurs chacun), et la taille des lots peut varier. Des fichiers plus petits n'indiquent pas nécessairement des données manquantes. Si le lien envoyé par e-mail ne fonctionne pas mais que la copie dans votre espace de stockage est disponible, vous pouvez toujours récupérer vos données directement depuis votre compartiment.

#### Erreurs courantes

- `AccessDenied` signifie que Braze n'a pas pu écrire dans votre compartiment. Vérifiez que vos identifiants et autorisations sont toujours valides.
- `ExpiredToken` apparaît si Braze n'a plus accès à votre compartiment. Mettez à jour vos identifiants dans le tableau de bord de Braze.
- Si certains fichiers semblent plus petits que prévu, c'est un comportement normal. Le processus d'exportation divise intentionnellement les fichiers pour des raisons de stabilité.
- Les apostrophes ajoutées au début de certains champs (tels que `-`, `=`, `+` ou `@`) sont un comportement attendu. Par exemple, `-1943` devient `'-1943` dans le fichier CSV. Braze procède ainsi afin d'éviter que les tableurs n'interprètent incorrectement les données. Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Exportations API

Symptôme : les exportations API n'apparaissent pas dans votre compartiment ou les fichiers sont incomplets.


Lorsque vous exportez des données via les API avec un partenaire de stockage connecté, les fichiers exportés sont enregistrés dans votre compartiment. Aucun e-mail n'est envoyé. Les objets sous-jacents résident dans votre espace de stockage et respectent vos paramètres de conservation, même si les URL de téléchargement fournies par Braze peuvent être limitées dans le temps.

Les fichiers apparaissent généralement dans votre compartiment au fur et à mesure de l'exportation, vous n'avez donc pas besoin d'attendre la fin de l'ensemble du traitement pour accéder aux résultats partiels. Braze charge chaque lot terminé de manière incrémentielle au lieu de tout conserver jusqu'à la fin. Les exportations volumineuses sont divisées en plusieurs fichiers compressés (ZIP ou GZIP), chacun contenant des objets JSON, un par ligne. Cela rend cette méthode plus fiable pour les exportations lourdes.

#### Erreurs courantes {#common-errors-1}

- `AccessDenied` survient lorsque Braze ne parvient pas à écrire dans votre compartiment ou lorsque les objets ont été supprimés par la suite. Vérifiez les autorisations et assurez-vous qu'aucun processus externe ne supprime les fichiers.
- `ExpiredToken` signifie que les identifiants d'accès de Braze à votre compartiment sont obsolètes. Actualisez-les dans le tableau de bord.
- Si des fichiers sont manquants ou plus petits que prévu, vérifiez d'abord qu'aucun processus extérieur à Braze ne supprime des objets. Des fichiers de taille réduite sont un comportement attendu.

{% endsdktab %}
{% endsdktabs %}

## Analyse de Campaign et Canvas {#campaign-and-canvas-analytics}

### Le nombre d'utilisateurs dans l'export CSV ne correspond pas aux *Messages envoyés* ou aux *Destinataires uniques* {#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients}

Symptôme : l'export CSV d'une Campaign affiche un nombre d'utilisateurs différent de celui des *Messages envoyés* ou des *Destinataires uniques* sur la page d'analyse.


L'export CSV d'une Campaign peut afficher un nombre d'utilisateurs différent de celui des *Messages envoyés* et des *Destinataires uniques* pour les raisons suivantes :

#### La rééligibilité est activée {#re-eligibility-is-turned-on}

Si les utilisateurs peuvent (ou pouvaient à un moment donné) recevoir la Campaign plus d'une fois, les chiffres d'analyse de la Campaign et le nombre de lignes dans l'export de données utilisateur ne correspondent pas. *Messages envoyés* comptabilise chaque envoi, y compris lorsque le même utilisateur reçoit le message plusieurs fois. Le téléchargement **Export CSV des données utilisateur** répertorie les utilisateurs uniques — une ligne par profil ayant reçu la Campaign — et non une ligne par envoi. Par exemple, si *Messages envoyés* indique 12 et que le fichier CSV contient 10 lignes, ces 12 envois ont été adressés à 10 utilisateurs distincts (certains utilisateurs ont reçu la Campaign plus d'une fois).

#### Des utilisateurs ont été supprimés ou fusionnés depuis l'envoi de la Campaign ou du Canvas {#users-were-deleted-or-merged-since-the-campaign-or-canvas-sent}

L'export CSV fournit un instantané des utilisateurs existants ayant reçu une Campaign ou un Canvas donné. Étant donné que des utilisateurs peuvent être supprimés ou fusionnés, le nombre dans l'export CSV peut être inférieur au nombre de destinataires uniques. Par exemple, si 1 000 utilisateurs reçoivent une Campaign, celle-ci affiche 1 000 destinataires uniques, et l'export CSV du même jour affiche également 1 000 utilisateurs. Si un mois plus tard, 50 de ces 1 000 utilisateurs sont supprimés, l'export CSV contient 950 utilisateurs alors que le nombre incrémenté de destinataires uniques reste à 1 000.

## E-mails d'exportation de Segments depuis le tableau de bord {#dashboard-segment-export-emails}

### Le Segment est trop volumineux ou l'exportation échoue alors que mon Segment semble contenir moins de 500 000 utilisateurs {#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users}

Symptôme : l'exportation de Segment depuis le tableau de bord échoue ou affiche une erreur de taille, même si l'estimation du Segment semble acceptable.


La **taille d'un Segment dans le tableau de bord est une estimation**. L'exportation CSV utilise cette estimation pour appliquer la [limite d'exportation de 500 000 utilisateurs]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details) ; le pipeline d'exportation peut également évaluer la taille différemment de l'interface du générateur de Segments. Si les exportations échouent pour un Segment proche de ce seuil, utilisez les [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) ou divisez l'audience en Segments plus petits, ou bien utilisez l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) comme décrit dans [Exporter des Segments volumineux]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#exporting-large-segments).

### Pourquoi est-ce que je ne reçois pas les e-mails d'exportation de Segments ? {#not-receiving-segment-export-emails}

Symptôme : une exportation CSV de Segment a été déclenchée mais aucun e-mail n'est arrivé.


Commencez par vérifier votre dossier de courrier indésirable pour un e-mail provenant de `no-reply@alerts.braze.com`. Si l'e-mail s'y trouve, ajoutez cette adresse à votre liste d'expéditeurs autorisés afin que les futurs messages d'exportation ne soient pas filtrés.

Si l'e-mail ne se trouve pas dans votre dossier de courrier indésirable, vérifiez si un autre membre de votre équipe peut recevoir l'exportation. Si personne ne la reçoit, examinez la taille de votre exportation. Le délai de réception varie en fonction de la taille de l'exportation, mais si l'e-mail n'est toujours pas arrivé au bout d'une heure, contactez le [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Téléchargements de l'API d'exportation de Segments {#segment-export-api-downloads}

### Impossible de télécharger un fichier ZIP de Segment exporté depuis une URL Braze {#cant-download-an-exported-segment-zip-from-a-braze-url}

Symptôme : une erreur `403 Forbidden` lors du téléchargement depuis l'URL de réponse de `/users/export/segment`.


Si vous obtenez une erreur `403 Forbidden` en utilisant l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), le fichier n'est peut-être pas encore prêt. Les exportations volumineuses peuvent prendre un certain temps à traiter. Attendez jusqu'à une heure avant de relancer le téléchargement.

Si vous utilisez un script automatisé pour récupérer le fichier, vous pouvez également recevoir une erreur `403 Forbidden` lorsque vous demandez l'URL trop tôt. Si vous exportez régulièrement des données de Segments, envisagez de connecter votre propre intégration de compartiment S3 et de transmettre les fichiers vers votre propre pipeline ETL (ETL or extraire, transformer, charger).

Les exportations nécessitent du temps pour se terminer, c'est pourquoi un accès immédiat depuis un script échoue souvent. Vous pouvez :

- Interroger l'URL de téléchargement avec des délais exponentiels, ou
- Utiliser le [paramètre `callback_endpoint`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#request-parameters) et le diriger vers un service qui exécute votre script lorsque l'exportation est prête.

## Champs de l'API d'exportation de Segments et d'utilisateurs {#segment-and-user-export-api-fields}

### Des colonnes attendues sont absentes d'un fichier d'exportation de Segment {#expected-columns-are-missing-from-a-segment-export-file}

Symptôme : Une exportation via l'API ou le tableau de bord ne contient pas les champs attendus.


L'option **CSV Export User Data** du tableau de bord pour un Segment utilise un ensemble fixe de colonnes (voir [Exporter les données d'un Segment au format CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#data-included-in-export)). Elle n'inclut pas de colonne ou de paramètre `fields_to_export`.

Pour les exportations de Segments via l'API, vous devez transmettre `fields_to_export` dans le corps de la requête. Certains champs récupèrent automatiquement des données associées — par exemple, demander `canvases_received` nécessite également les données de résumé de parcours dans le profil utilisateur. Consultez la référence de l'endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) pour connaître les noms de champs valides et les conditions requises.

Si des colonnes sont absentes d'un fichier ZIP d'exportation via l'API, vérifiez que le tableau `fields_to_export` de votre requête inclut bien tous les champs dont vous avez besoin et que votre espace de travail dispose des autorisations d'exportation requises.

## Quand contacter le support {#when-to-contact-support}

Contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) si vous avez suivi le [parcours d'investigation standard](#standard-investigation-path) et que vous avez toujours besoin d'aide. Incluez le type d'exportation, l'ID du Segment ou de la Campaign, l'horodatage (avec le fuseau horaire), ainsi que le message d'erreur exact ou le code de statut HTTP.