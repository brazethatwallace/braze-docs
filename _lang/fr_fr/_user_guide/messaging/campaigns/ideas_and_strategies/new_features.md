---
nav_title: Découverte des fonctionnalités et nouvelle version de l'application
article_title: Découverte des fonctionnalités et nouvelle version de l'application
page_order: 9
page_type: reference
description: "Cet article de référence explique comment tenir vos utilisateurs informés et enthousiastes lors de la publication de nouvelles fonctionnalités ou versions."
tool: Campaigns

---

# Découverte des fonctionnalités et nouvelle version de l'application {#feature-awareness-and-new-app-version}

> Cet article de référence explique comment utiliser la plateforme Braze pour tenir vos clients informés des nouvelles fonctionnalités et versions de votre application.

Vous travaillez sans relâche pour mettre à jour et améliorer votre application, et vous souhaitez que vos utilisateurs profitent de ces nouvelles fonctionnalités et versions. Découvrez comment faire connaître à vos utilisateurs les fonctionnalités qu'ils n'ont pas encore utilisées et les encourager à explorer l'application pour tirer le meilleur parti de ce que vous avez à offrir.

Les campagnes de découverte des fonctionnalités sont un excellent moyen d'encourager vos utilisateurs à rester engagés avec votre application à mesure que vous en améliorez les capacités. Tenir vos utilisateurs informés est un excellent moyen de les garder actifs, d'améliorer les évaluations et de garantir leur engagement.

## Filtrage par versions d'application les plus récentes {#filtering-by-most-recent-app-versions}

Les SDK Braze suivent automatiquement la version d'application la plus récente d'un utilisateur. Ces versions peuvent être utilisées dans les filtres et les Segments pour déterminer quels utilisateurs doivent recevoir un message ou une Campaign.

![Le panneau Options de ciblage dans l'étape Utilisateurs cibles du workflow de création de Campaign. La section Filtres supplémentaires inclut le filtre suivant : « Le numéro de version d'application le plus récent pour Android Stopwatch (Android) est inférieur à 3.7.0 (134.0.0.0) ».]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Le remplissage des versions d'application actuelles peut prendre un certain temps. La version de l'application sur le profil utilisateur est mise à jour lorsque l'information est capturée par le SDK, ce qui dépend du moment où les utilisateurs ouvrent leur application. Si l'utilisateur n'ouvre pas l'application, la version actuelle ne sera pas mise à jour. <br><br> Ces filtres ne s'appliquent pas non plus de manière rétroactive. Il est recommandé d'utiliser « supérieur à » ou « égal à » pour les versions actuelles et futures, mais l'utilisation de filtres sur des versions passées peut entraîner des comportements inattendus.
{% endalert %}

### Numéro de version de l'application {#app-version-number}

Utilisez le filtre **App Version Number** pour segmenter les utilisateurs par la version et le numéro de build de l'application.

Ce filtre prend en charge les comparaisons numériques pour cibler une plage de versions d'application. Par exemple, vous pouvez cibler les utilisateurs dont l'application est « inférieure à », « supérieure à » ou « égale à » la version « 1.2.3 », ce qui peut être utile pour promouvoir une nouvelle fonctionnalité nécessitant une mise à jour de l'application.

Ce filtre peut remplacer l'ancien filtre « App Version Name », qui nécessitait de lister explicitement chaque version antérieure ou d'utiliser une expression régulière.

#### Fonctionnement {#how-it-works}

- Chaque partie de la version `major.minor.patch` envoyée dans la version de votre application est comparée en tant qu'entiers.
- Si les numéros majeurs sont égaux, Braze compare les numéros mineurs. Si les numéros mineurs sont égaux, Braze compare les numéros de correctif.
- Lors de l'utilisation des filtres « inférieur à » ou « inférieur ou égal à », si la version de l'application n'existe pas dans le profil d'un utilisateur, le filtre renvoie `true` et l'utilisateur est considéré comme ayant une version antérieure à la version testée. Pour éviter d'inclure des utilisateurs sans données de version, utilisez plutôt les filtres « supérieur à » ou « égal à ».

#### Considérations importantes {#important-considerations}

- Les applications Android disposent à la fois d'un [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) lisible par l'utilisateur et d'un [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) interne. Le filtre App Version Number utilise `versionCode` car il est garanti d'être incrémenté à chaque publication sur la boutique d'applications.
- Cela peut prêter à confusion lorsque le `versionName` et le `versionCode` de votre application ne sont plus synchronisés, d'autant plus que les deux champs sont visibles depuis le tableau de bord de Braze. En bonne pratique, vérifiez que le `versionName` et le `versionCode` de votre application sont incrémentés ensemble.
- Si vous devez filtrer par le champ `versionName` lisible par l'utilisateur (cas peu fréquent), utilisez le filtre App Version Name.

#### Prérequis SDK {#sdk-requirements}

Les valeurs de ce filtre sont collectées à partir du SDK Braze pour Android v3.6.0+ et du SDK iOS v3.21.0+. Même si ce filtre a des prérequis SDK, vous pouvez toujours cibler les utilisateurs qui utilisent des versions inférieures (plus anciennes) de votre application grâce à cette fonctionnalité.

Pour Android, ce numéro de version est basé sur le [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) de l'application.

Pour iOS, ce numéro de version est basé sur le [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de l'application.

{% alert tip %}
Ce filtre ne renseigne les valeurs qu'après que les utilisateurs ont mis à jour leurs applications vers les versions du SDK Braze prises en charge. Jusque-là, le filtre n'affiche aucune version lorsqu'il est sélectionné.
{% endalert %}

#### Cas d'usage {#use-case}

Dans le scénario suivant, supposons que vous avez d'abord effectué la mise à niveau vers les SDK Braze prenant en charge ce filtre dans la version `2.0.0` de votre application.

Une fois que Braze reçoit des données de la version 2.0.0 de votre application, vous pouvez cibler les utilisateurs avec des versions antérieures ou ultérieures.

| Filtre | Version de l'application de l'utilisateur | Résultat |
| :------------- | :----------- | :--------- |
| Inférieur à 2.0.0 | 1.0.0 | L'utilisateur fait partie du Segment, même si son SDK Braze ne prenait pas en charge le filtre « App Version Number ». |
| Supérieur à 2.0.0 | 2.5.1 | L'utilisateur et toutes les futures installations font partie du Segment. |
| Supérieur à 2.0.0 | 1.9.9 | L'utilisateur ne fait pas partie du Segment. |
| Inférieur ou égal à 2.0.0 | 3.0.1 | L'utilisateur ne fait pas partie du Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cas d'usage" }

### Nom de version de l'application {#app-version-name}

Utilisez le filtre « App Version Name » pour segmenter les utilisateurs par le « nom de build » visible par l'utilisateur de l'application.

Ce filtre prend en charge la correspondance avec « est », « n'est pas » et les expressions régulières. Par exemple, vous pouvez cibler les utilisateurs dont l'application n'est pas la version « 1.2.3-test-build ».

Pour Android, ce nom de version est basé sur le [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) de l'application. Pour iOS, ce nom de version est basé sur le [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de l'application.

### Fonctionnalité non utilisée {#have-not-used-feature}

Lorsque vous publiez une nouvelle version de votre application et introduisez de nouvelles fonctionnalités, les utilisateurs peuvent ne pas remarquer le nouveau contenu. Lancer une campagne de sensibilisation aux fonctionnalités est un excellent moyen d'informer les utilisateurs sur les nouvelles fonctionnalités ou celles qu'ils n'ont jamais utilisées. Pour ce faire, vous devez créer un [attribut personnalisé]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) qui est attribué aux utilisateurs n'ayant jamais effectué une certaine action dans votre application, ou utiliser un [événement personnalisé]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) pour suivre une action particulière. Vous pouvez utiliser cet attribut (ou événement) pour segmenter les utilisateurs auxquels vous souhaitez envoyer la Campaign.

{% alert tip %}
Vous souhaitez recibler une portion spécifique de votre audience ? Consultez [Reciblage de Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns) pour apprendre à recibler des Campaigns en exploitant les actions précédentes de vos utilisateurs.
{% endalert %}