---
nav_title: Livrabilité pour les appareils Android chinois
article_title: Livrabilité des notifications push pour les appareils Android chinois
page_order: 10

page_type: reference
description: "Cet article présente les nuances de livrabilité des notifications push à connaître lorsque vous ciblez des utilisateurs sur des appareils Android fabriqués par des OEM chinois."
channel: push

---

# Livrabilité des notifications push pour les appareils Android chinois {#push-deliverability-for-chinese-android-devices}

> Certains appareils Android fabriqués par des fabricants d'équipements d'origine (OEM) chinois, tels que Xiaomi, OPPO, Vivo et Huawei, optimisent l'autonomie de la batterie grâce à une gestion agressive du cycle de vie des applications. Cette optimisation peut avoir pour conséquence involontaire d'interrompre le traitement en arrière-plan des applications, ce qui peut réduire la livrabilité de vos notifications push.<br><br>Pour vous assurer que les performances de communication de votre application fonctionnent comme prévu sur ces appareils, vos équipes marketing et d'ingénierie doivent collaborer et suivre les étapes décrites dans cet article.

## Étapes pour les développeurs {#steps-for-developers}
Ces fabricants (OEM) effectuent leurs optimisations en fermant agressivement les applications en arrière-plan et en les empêchant de se lancer automatiquement pour exécuter des tâches en arrière-plan. En tant que développeur, vous devrez configurer votre application pour demander à l'utilisateur d'assouplir ces restrictions chaque fois que possible.

Pour y parvenir, votre application peut se lancer automatiquement sur l'appareil de l'utilisateur final, ce qui lui donne la permission de s'exécuter en arrière-plan et d'écouter les messages provenant de Braze. Malheureusement, comme il s'agit d'un problème spécifique aux OEM et non d'un problème Android, il n'existe pas d'API documentées pour afficher l'invite de permission de lancement automatique pour chaque OEM.

Pour résoudre ce problème, intégrez une bibliothèque comme [AutoStarter](https://github.com/judemanutd/AutoStarter) dans votre application. AutoStarter prend en charge plusieurs fabricants, ce qui vous offre un moyen simple d'appeler le gestionnaire de permissions de démarrage sur un large éventail d'appareils. Une fois AutoStarter intégré, appelez `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` pour afficher le gestionnaire de permissions de démarrage sur l'appareil de l'utilisateur final. Associez cette action à une invite encourageant l'utilisateur final à activer le « lancement automatique » pour votre application. Votre équipe marketing rédigera ce message — consultez la section suivante !

## Étapes pour les marketeurs {#steps-for-marketers}
Une fois que vos utilisateurs ont accepté de recevoir des notifications push, ils peuvent effectuer des étapes supplémentaires de leur côté pour améliorer la livraison des messages sur ces appareils. Nous vous recommandons de faire suivre votre [message d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) d'un message in-app ciblant les utilisateurs sur les appareils OEM chinois, avec ces étapes supplémentaires :

- Activer le « démarrage automatique » pour l'application
- Désactiver l'optimisation de la batterie pour l'application

### Identifier les utilisateurs sur les appareils OEM chinois {#identifying-users-on-chinese-oem-devices}

Pour cibler votre message in-app vers les utilisateurs sur des appareils OEM chinois spécifiques, utilisez les [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) **Device Model** ou **Device OS** :

- **Device Model :** utilisez ce filtre pour cibler les utilisateurs en fonction du modèle de leur téléphone mobile. Par exemple, pour identifier les appareils Huawei, utilisez une expression régulière contenant `huawei` pour correspondre aux noms de modèles. Pour des instructions de configuration étape par étape, consultez [Créer une expression régulière Device Model pour les appareils Huawei](#build-a-device-model-regex-for-huawei-devices).
- **Device OS :** utilisez ce filtre pour cibler les utilisateurs par système d'exploitation. Certains OEM chinois, comme Huawei, peuvent spécifier explicitement leur version Android personnalisée dans le champ Device OS. Pour les étapes de vérification, consultez [Vérifier les valeurs Device OS avant le ciblage](#verify-device-os-values-before-you-target).

#### Créer une expression régulière Device Model pour les appareils Huawei {#build-a-device-model-regex-for-huawei-devices}

1. Allez dans **Audience** > **Segments**, puis créez ou modifiez un Segment.
2. Ajoutez le filtre **Device Model**.
3. Définissez l'opérateur sur **matches regex**.
4. Saisissez `huawei` pour correspondre aux noms de modèles Huawei.
5. (Facultatif) Si vous souhaitez également inclure les appareils de marque Honor, utilisez `(huawei|honor)`.

Pour plus d'informations sur le comportement des expressions régulières dans Braze et les tests de motifs, consultez [Expressions régulières]({{site.baseurl}}/user_guide/audience/segments/regex).

#### Vérifier les valeurs Device OS avant le ciblage {#verify-device-os-values-before-you-target}

Certaines variantes OEM peuvent signaler des noms de système d'exploitation personnalisés dans les métadonnées de l'appareil. Comme cette valeur peut varier selon le modèle de l'appareil et la distribution Android, vérifiez ce que vos utilisateurs envoient dans Braze avant de créer le Segment :

1. Accédez à **Search Users**, puis ouvrez le profil d'un utilisateur cible connu.
2. Dans l'onglet **Overview**, vérifiez **Recent devices** et examinez la valeur OS affichée pour cet appareil.
3. Copiez la chaîne de caractères OS exacte dans votre filtre de Segment :
   - Utilisez **Device OS** lorsque vous avez besoin d'une correspondance exacte ou basée sur une expression régulière de la chaîne OS.
   - Utilisez **Device OS Version Number** lorsque vous avez besoin de plages de versions numériques.
4. Dans le compositeur de Segments, utilisez **User Lookup** pour confirmer que les utilisateurs test correspondent comme prévu.

Pour plus de détails sur l'emplacement des métadonnées d'appareil dans les profils, consultez [Profils utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Pour plus de détails sur le test de la logique de segmentation, consultez [Créer un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).