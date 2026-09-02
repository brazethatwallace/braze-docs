---
nav_title: Assistance technique en matière de protection des données
article_title: Assistance technique en matière de protection des données dans les services de Braze
page_order: 1
description: "Cette page fournit des instructions techniques pour vous permettre de gérer, par le biais des services Braze, les demandes des personnes en ce qui concerne leurs droits en matière de données à caractère personnel."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistance technique en matière de protection des données dans les services de Braze {#data-protection-technical-assistance-in-the-braze-services}

Il existe une gamme de lois sur la protection des données qui régissent ce que les organisations peuvent faire avec les données personnelles (« lois sur la protection des données »), y compris le Règlement général sur la protection des données de l'UE et du Royaume-Uni (« RGPD »), la California Consumer Privacy Act (« CCPA ») et la Health Insurance Portability and Accountability Act (« HIPAA »). Il existe d'autres lois et réglementations sur la protection des données au niveau national, régional et sectoriel qui peuvent s'appliquer à votre entreprise.

Ces lois sur la protection des données accordent aux individus des « droits à la vie privée » sur leurs données personnelles. Les organisations sont tenues de recevoir et de répondre aux demandes des individus qui exercent leurs droits à la vie privée. Les services Braze peuvent vous aider à vous conformer à ces lois sur la protection des données en fournissant des fonctionnalités qui facilitent certaines actions requises par ces lois. Ce document fournit des instructions techniques pour utiliser ces fonctionnalités afin de gérer les demandes relatives aux droits à la vie privée. Il vous appartient de déterminer quelles lois sur la protection des données s'appliquent à votre entreprise et d'agir en conformité avec elles.

## Avis juridique {#legal-disclaimer}

Rien de ce qui suit n'est destiné à constituer, ni ne doit être considéré comme, un conseil juridique de la part de Braze. Il vous est conseillé de consulter votre propre conseiller juridique en ce qui concerne votre situation particulière et la manière dont les lois sur la protection des données s'appliquent à vous et à votre utilisation des services Braze.

## Terminologie {#terminology}

Aux fins du présent document, toute référence aux données personnelles peut également être comprise comme une référence aux informations personnelles ou aux informations permettant d'identifier une personne (« Données personnelles »). Par souci de simplicité, nous nous appuyons généralement sur la terminologie du RGPD lorsque nous abordons les droits des utilisateurs finaux. La terminologie du RGPD est souvent interchangeable ou étroitement alignée avec un terme ou un concept défini par d'autres lois sur la protection des données.

## Les principes fondamentaux {#the-basics}

La plupart des lois sur la protection de la vie privée définissent trois catégories principales de parties prenantes impliquées dans le traitement des données personnelles : les personnes concernées, les contrôleurs des données et les sous-traitants des données. Chaque groupe dispose de droits et de responsabilités différents concernant l'utilisation des données personnelles :

- Une personne concernée est un individu dont les données personnelles sont traitées par le sous-traitant des données ou le contrôleur des données
- Un contrôleur des données est une entité qui détermine les finalités et les moyens du traitement des données personnelles
- Un sous-traitant des données est une entité qui traite les données personnelles pour le compte et selon les instructions du contrôleur des données

En ce qui concerne les services Braze :

- Les personnes concernées sont, par exemple, les utilisateurs finaux de votre application client (par ex., vos clients) ou vos employés qui sont des utilisateurs de l'entreprise dans votre instance des services Braze.
- Vous, le client Braze, êtes le contrôleur des données qui décide comment et pourquoi les données personnelles des personnes concernées seront collectées et traitées au sein des services Braze.
- Braze est un sous-traitant des données qui traite les données personnelles dans les services Braze en votre nom et conformément aux instructions que nous recevons de votre part.

Les termes ci-dessus sont des termes du RGPD, mais à titre d'exemple, les termes comparables dans le cadre du CCPA sont :
- « consommateurs » pour les personnes concernées.
- « entreprises » pour les contrôleurs des données.
- « prestataires de services » pour les sous-traitants des données.

Vous trouverez ci-dessous des informations pertinentes sur les demandes les plus courantes des personnes concernées en matière de droits à la vie privée, y compris la façon dont vous pouvez y répondre grâce aux fonctionnalités techniques des services Braze.

## Le droit d'être informé {#the-right-to-be-informed}

Le droit d'être informé englobe votre obligation de fournir des « informations de traitement équitable », généralement par le biais d'un avis de confidentialité. Il met l'accent sur la nécessité de transparence quant à la manière dont vous utilisez les données personnelles.

### Recommandation de Braze {#braze-recommendation}

La plupart des lois sur la protection des données soulignent la nécessité de transparence quant à la manière dont vous utilisez les données personnelles. Cette responsabilité incombe aux contrôleurs des données, qui maintiennent généralement un avis de confidentialité facilement accessible aux utilisateurs de leurs produits et services, couvrant le traitement effectué par Braze.

## Le droit d'accès {#the-right-of-access}

En vertu des lois sur la protection des données, les personnes concernées peuvent avoir le droit d'obtenir :

- La confirmation que leurs données personnelles font l'objet d'un traitement,
- L'accès à leurs données personnelles, et
- D'autres informations complémentaires telles que déterminées par la loi sur la protection des données applicable.

### Recommandation de Braze

Afin de fournir des données personnelles depuis Braze dans un format lisible par machine en réponse à une demande d'accès d'une personne concernée, vous pouvez exporter son profil d'utilisateur final en effectuant un appel API aux [REST API]({{site.baseurl}}/api/endpoints/export) de Braze avec son identifiant utilisateur (défini par vous comme l'`external_id` fourni à Braze) et/ou son identifiant d'appareil.

#### BrazeAI Decisioning Studio™

Pour répondre à une demande de droit d'accès relative aux données personnelles dans BrazeAI Decisioning Studio™, contactez votre gestionnaire de compte avec le(s) customer_id et/ou e-mail(s) concerné(s).

## Le droit de rectification {#the-right-to-rectification}

Les personnes concernées ont le droit de faire corriger leurs données personnelles si celles-ci sont inexactes ou incomplètes. Si vous avez divulgué les données personnelles en question à des tiers, vous pouvez envisager la nécessité de les informer de la rectification dans la mesure du possible.

### Recommandation de Braze

Dans le cas où une personne concernée vous demande de rectifier des inexactitudes dans les données personnelles traitées par vous ou par Braze en votre nom, vous pouvez utiliser les SDK Braze ou les [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze pour corriger ces données personnelles.

## Le droit à l'effacement {#the-right-to-erasure}

Le droit à l'effacement est également connu sous le nom de « droit à l'oubli » ou « droit à la suppression ».

### Recommandation de Braze

#### Suppression standard {#standard-deletion}

Une fois que vous avez arrêté la collecte de données, vous pouvez utiliser l'[endpoint REST API de suppression d'utilisateur de Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) pour supprimer un utilisateur final, ce qui supprimera tous les enregistrements de cet utilisateur final des services Braze :

- Pour les utilisateurs finaux disposant d'un external_id dans les services Braze, vous pouvez utiliser cet ID pour supprimer les données de cet utilisateur final.
- Pour les utilisateurs finaux anonymes qui ne disposent pas d'un external_id dans les services Braze, vous pouvez récupérer l'identifiant d'appareil de cet utilisateur final à l'aide du SDK Braze et utiliser cet identifiant d'appareil pour trouver le profil utilisateur final associé à cet appareil. Vous pouvez ensuite utiliser l'API de suppression d'utilisateur pour supprimer le profil associé à cet utilisateur final.

La suppression d'un utilisateur final des services Braze supprimera définitivement le profil utilisateur centralisé de Braze pour cet utilisateur final, tel que défini par l'`external_id` fourni. Cela inclut les informations de profil structurées que Braze a collectées par défaut ou que vous avez configuré les services Braze pour collecter, telles que les informations sur l'appareil, le pays, la langue et l'adresse e-mail.

Notez que l'adresse e-mail ou le numéro de téléphone associé au profil de l'utilisateur final pourrait encore être stocké par Braze, car ils pourraient être associés au profil d'un autre utilisateur final. Les adresses e-mail et les numéros de téléphone ne sont pas uniques dans les services Braze. Cela signifie que votre équipe pourrait avoir configuré Braze pour stocker la même adresse e-mail ou le même numéro de téléphone sur plusieurs profils utilisateur. Si votre équipe a configuré Braze de cette manière, sachez que vous pourriez avoir besoin de supprimer tous les profils utilisateur représentant une personne concernée donnée afin de vous conformer à une demande de suppression de cette personne concernée, et votre équipe devrait effectuer plusieurs appels API pour supprimer tous les profils utilisateur faisant référence à une personne concernée particulière.

#### BrazeAI Decisioning Studio™

Pour répondre à une demande de droit à l'effacement concernant des données personnelles dans BrazeAI Decisioning Studio™, contactez votre gestionnaire de compte avec le ou les customer_id et/ou e-mail(s) concernés. Votre gestionnaire de compte peut organiser la suppression de toutes les données personnelles associées trouvées dans l'entrepôt de données.

#### Considérations supplémentaires relatives à la suppression {#additional-deletion-considerations}

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
  <caption>Considérations supplémentaires relatives à la suppression</caption>
<tbody>
  <tr>
    <td>
        <p>Les clients peuvent créer des champs personnalisés pour les propriétés d'événement et les extras de message. Ces champs ne sont pas destinés aux données personnelles, et par conséquent, ils ne sont pas inclus dans le processus de suppression par défaut décrit ci-dessus. Toutefois, si vous utilisez Braze pour saisir ou collecter des données personnelles via les propriétés d'événement et les extras de message, vous pouvez configurer le processus de suppression déclenché par l'endpoint REST API de suppression d'utilisateur pour inclure également ces champs, de sorte que les données contenues dans ces champs soient également supprimées.</p>
        <p>Les paramètres par défaut sont appliqués au niveau de l'entreprise, mais vous pouvez choisir de supprimer les champs suivants lors de l'exécution du processus de suppression, au niveau du groupe d'applications/espace de travail :</p>
    <ul>
        <li>PROPERTIES pour USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES pour USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS pour :
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Futurs événements d'envoi de messages</li>
            </ul>
        </li>
    </ul>
    <p>Les paramètres correspondants sont accessibles via <b>Paramètres de l'entreprise</b> > <b>Paramètres d'administration</b> > <b>Paramètres de sécurité</b>. Les préférences de suppression des données sont définies par type d'événement ou catégorie. Seul un utilisateur disposant des autorisations d'administrateur peut modifier ces paramètres. Un administrateur peut également déléguer ces autorisations à un autre utilisateur.</p>
    <p>Si un type d'événement ou un extra de message est configuré pour être inclus dans le processus de suppression, les données de ce champ seront supprimées à l'avenir pour les utilisateurs pour lesquels vous exécutez l'endpoint REST API de suppression d'utilisateur. De plus, lorsque vous sélectionnez cette préférence de suppression, lors de la prochaine tâche de suppression planifiée, les données de ces champs seront supprimées de tous les ensembles de données anonymisées existants contenant ces champs. La restauration des champs de données supprimés ne sera pas possible.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analyse {#analytics}

Afin de maintenir l'intégrité des analyses d'utilisation des Campaign et des applications, les données agrégées anonymes ne seront pas modifiées lorsqu'un utilisateur final est supprimé. Par exemple, Braze ne décrémentera pas le nombre total de sessions d'une application lorsqu'un utilisateur final est supprimé. La ou les sessions au cours desquelles cet utilisateur final a visité l'application seront toujours incluses dans le nombre total de visites de cette application, mais ces données ne seront en aucun cas liées au profil de l'utilisateur final oublié, garantissant ainsi que ces données anonymisées et agrégées ne puissent pas être rattachées à un utilisateur final individuel.

Les analyses au sein des services Braze sont liées à l'identifiant d'utilisateur final Braze. Une fois le profil de l'utilisateur final supprimé, l'identifiant d'utilisateur Braze devient effectivement un identifiant entièrement anonymisé, car Braze est dans l'incapacité de le relier à un utilisateur final individuel.

#### Une fois la suppression effectuée {#once-deletion-has-happened}

Vous êtes généralement tenu de faire des efforts raisonnables pour informer les personnes concernées lorsque vous avez donné suite à leur demande d'effacement de leurs données personnelles. Un utilisateur final supprimé peut se réinscrire ou réinteragir avec votre application ou service ultérieurement, et Braze ne sera pas en mesure de l'identifier comme l'utilisateur supprimé ou oublié. Les services Braze ne sont pas en mesure de créer des listes d'identifiants d'utilisateurs supprimés ou d'adresses e-mail en votre nom.

## Le droit à la limitation du traitement {#the-right-to-restriction-of-processing}

Les personnes concernées peuvent avoir le droit de « bloquer » ou de supprimer le traitement de leurs données personnelles dans certaines circonstances. Limiter le traitement signifie ne pas effectuer de traitement auquel une personne concernée s'est opposée.

### Recommandation de Braze

Les services Braze ne prennent pas en charge la limitation du traitement de catégories individuelles de données personnelles. Si une personne concernée vous a demandé de limiter le traitement de certains sous-ensembles de ses données personnelles, vous devez utiliser les [API de Braze]({{site.baseurl}}/api/home) pour exporter l'intégralité du ou des profils de cet utilisateur final, puis le [supprimer]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze. Les API de Braze peuvent être utilisées pour réimporter ces données dans le cas où l'utilisateur final vous autoriserait par la suite à traiter ces sous-ensembles particuliers de ses données personnelles. De plus, vous devriez recommander à votre utilisateur final de désinstaller ou de se déconnecter de toutes vos applications qui utilisent le SDK Braze afin de cesser de collecter toute donnée supplémentaire sur la personne concernée.

Pour les clients qui utilisent uniquement BrazeAI Decisioning Studio™, vous ne devriez plus envoyer de données à Decisioning Studio.

## Le droit à la portabilité des données {#the-right-to-data-portability}

Le droit à la portabilité des données permet aux personnes concernées d'obtenir et de réutiliser leurs données personnelles à leurs propres fins dans le cadre de différents services. Les données personnelles doivent être fournies dans un format structuré, lisible par machine et couramment utilisé.

### Recommandation de Braze

Comme pour le droit d'accès, vous pouvez utiliser la [REST API]({{site.baseurl}}/api/endpoints/export) de Braze pour exporter les données personnelles d'un utilisateur final et les transmettre à la personne concernée conformément à sa demande. De plus, contactez votre gestionnaire de compte en fournissant le(s) customer_id et/ou e-mail(s) pertinents pour demander une copie de toute donnée personnelle détenue dans BrazeAI Decisioning Studio.

## Le droit d'opposition {#the-right-to-object}

Les individus peuvent avoir le droit de s'opposer aux traitements suivants :

- le traitement fondé sur des intérêts légitimes ou l'exécution d'une mission d'intérêt public/l'exercice de l'autorité officielle (y compris le profilage) ;
- le marketing direct (y compris le profilage) ; et
- le traitement à des fins de recherche scientifique/historique et de statistiques.

### Recommandation de Braze

Braze offre la possibilité de marquer un profil utilisateur comme étant désabonné des SMS, des e-mails ou des notifications push via nos [REST API]({{site.baseurl}}/api/home) et via les SDK [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes) et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes). Si vous recevez des objections de la part de personnes concernées relatives à la réception de tels messages, vous pouvez utiliser les API de Braze pour désabonner ces utilisateurs finaux.

Si cela n'est pas suffisant, afin d'éviter le traitement des données personnelles de l'utilisateur final par Braze, le profil de l'utilisateur final doit être supprimé de la même manière que celle spécifiée dans la section « Droit à l'effacement ».

## Droits liés à la prise de décision automatisée et au profilage {#rights-related-to-automated-decision-making-and-profiling}

Certaines lois sur la protection des données interdisent, ou permettent aux personnes concernées de s'opposer à, la prise de décision automatisée ou le profilage dans certaines circonstances, en particulier pour les décisions qui « produisent un effet juridique ou un effet significatif similaire sur l'individu ».

### Recommandation de Braze

Braze n'effectue aucune action de profilage automatisé ou de prise de décision ayant des ramifications juridiques ou équivalentes pour les personnes concernées. Si vous estimez que votre propre utilisation des services Braze aura des impacts juridiques ou équivalents et que vous avez reçu une objection à ce sujet, vous pouvez choisir de supprimer le profil utilisateur de la même manière que dans le cadre du « droit à l'effacement ».

## Publicité ciblée {#targeting-advertising}

En vertu de certaines lois américaines sur la protection de la vie privée, les personnes concernées peuvent s'opposer à l'utilisation de leurs données personnelles à des fins de publicité ciblée.

### Recommandation de Braze

Lorsque vous créez des audiences dans le but de cibler des publicités vers vos personnes concernées, vous devez vous assurer d'avoir exclu toute personne ayant exprimé son opposition à la publicité ciblée, par exemple les consommateurs californiens ayant exercé leur droit de refus de vente ou de partage (« Do Not Sell or Share ») en vertu du CCPA.

Pour plus d'informations sur la création d'audiences à synchroniser avec des plateformes tierces, consultez la section [Audience sync]({{site.baseurl}}/partners/canvas_audience_sync).

## Le droit à la non-discrimination {#the-right-to-non-discrimination}

Les personnes concernées ont le droit d'exercer leurs droits en matière de vie privée sans discrimination.

### Recommandation de Braze

Dans le cadre de leur utilisation des services Braze, les clients doivent s'assurer qu'ils ne pratiquent aucune discrimination à l'encontre des personnes concernées ayant exercé leurs droits en matière de vie privée. Par exemple, nous recommandons que les personnes concernées ayant exercé leurs droits en matière de vie privée ne soient pas segmentées en audiences ni ciblées d'une manière qui pourrait constituer une discrimination à leur égard.