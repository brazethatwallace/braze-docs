---
nav_title: FAQ
article_title: FAQ sur les exportations
page_order: 7
page_type: FAQ
description: "Cet article répond à certaines questions fréquemment posées sur les exportations API et CSV."

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page fournit des réponses à certaines questions fréquemment posées sur les exportations API et CSV.

## Est-il possible de faire apparaître certaines exportations dans votre compartiment S3 et pas d'autres ? {#can-you-make-certain-exports-appear-in-your-s3-bucket-and-others-not}

Non. Si vous avez fourni des identifiants S3, toutes vos exportations apparaîtront dans votre compartiment S3 ; sinon, si aucun identifiant n'est fourni, toutes les exportations apparaîtront dans un compartiment S3 appartenant à Braze.

## Dois-je ajouter des identifiants S3 à Braze pour exporter des données ? {#do-i-have-to-add-s3-credentials-to-braze-to-export-data}

Non. Si vous n'ajoutez pas d'identifiants S3, vos exportations apparaîtront dans un compartiment S3 appartenant à Braze.

## Que se passe-t-il si vous configurez des identifiants S3 dans le tableau de bord mais que vous ne sélectionnez pas « Make this the default data export destination » ? {#what-happens-if-you-set-up-s3-credentials-in-the-dashboard-but-dont-select-make-this-the-default-data-export-destination}

La case à cocher **Make this the default data export destination** détermine si les exportations sont envoyées vers S3 ou Azure, en supposant que vous ayez ajouté des identifiants pour les deux.

## La destination d'exportation de données par défaut affecte-t-elle Braze Currents ? {#does-the-default-data-export-destination-affect-braze-currents}

Non. Currents utilise ses propres paramètres de connecteur et de stockage. Le choix d'une destination d'exportation par défaut pour les exportations CSV et pilotées par API ne modifie pas l'emplacement où les données Currents sont écrites.

## Pourquoi ai-je reçu plusieurs fichiers lors de l'exportation de profils utilisateurs vers S3 ? {#why-did-i-receive-multiple-files-when-exporting-user-profiles-to-s3}

C'est le comportement attendu pour les espaces de travail avec beaucoup d'utilisateurs. Braze divise votre exportation en plusieurs fichiers en fonction du nombre d'utilisateurs dans votre espace de travail. En général, un fichier est généré tous les 5 000 utilisateurs. Notez que si vous exportez un petit segment dans un grand espace de travail, vous pouvez tout de même recevoir plusieurs fichiers.

## Pourquoi y a-t-il des doublons lorsque j'exporte des utilisateurs par segment via la REST API ? {#why-do-i-see-duplicates-when-i-export-users-by-segment-through-rest-api}

Il s'agit d'un cas très rare, dû à l'architecture sous-jacente du fournisseur de base de données. Les doublons sont nettoyés toutes les semaines ; cependant, la plupart du temps, aucun doublon n'est supprimé.

## Comment ouvrir des rapports CSV dans Excel ? {#how-do-i-open-csv-reports-in-excel}

Bien que les fichiers CSV soient généralement ouverts automatiquement dans Excel par défaut, ce n'est pas toujours le cas. Consultez les articles de résolution des problèmes pour [Windows](https://support.microsoft.com/en-us/windows/change-which-programs-windows-7-uses-by-default-62fd162f-8c82-0436-806f-c60d69dcf495) et [Apple](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac) afin de définir Excel comme programme par défaut.

Pour convertir un fichier CSV en XLSX ou XLS, ou pour supprimer la virgule entre les valeurs de données, consultez [ce guide sur l'importation de fichiers CSV dans Excel](https://www.ablebits.com/office-addins-blog/convert-csv-excel/#import-csv-wizard).

Si vous constatez que les zéros en début de chaîne sont supprimés des ID utilisateur dans votre exportation CSV, cela est dû au fait qu'Excel traite les nombres d'un fichier CSV comme des données numériques plutôt que du texte. Pour résoudre ce problème, utilisez l'[assistant d'importation de texte d'Excel](https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros).