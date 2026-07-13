---
nav_title: Politiques de temporisation
article_title: Politiques de temporisation des e-mails
page_order: 8
page_type: reference
description: "Le présent article couvre les meilleures pratiques en matière de temporisation et décrit les situations dans lesquelles il vaut mieux arrêter d'envoyer des communications à des utilisateurs désengagés."
channel: email

---

# Politiques de temporisation {#sunset-policies}

> Bien sûr, il est parfois tentant d'envoyer des campagnes à autant d'utilisateurs que possible, mais il existe des situations où il vaut vraiment mieux arrêter d'envoyer des messages aux utilisateurs désengagés.

Pour les e-mails, votre adresse IP d'envoi possède un score de réputation qui prend en compte l'engagement, les signalements de courrier indésirable, les mises en liste de blocage, et bien d'autres facteurs. Vous pouvez utiliser des outils comme [Sender Score](https://www.senderscore.org/) ou le [Smart Network Data Service d'Outlook](https://postmaster.live.com/snds/) pour surveiller votre score de réputation. Si votre score de réputation est régulièrement bas, les filtres des ISP et des boîtes aux lettres peuvent automatiquement classer vos e-mails dans le dossier spam ou dans un dossier de faible priorité pour tous les destinataires, y compris ceux qui sont engagés. La création d'une politique de temporisation permet d'envoyer vos e-mails uniquement aux destinataires actifs.

Les filtres de segmentation permettent d'éviter que vos messages n'apparaissent comme du spam en vous permettant de mettre facilement en œuvre des politiques de temporisation pour les e-mails, les notifications push et les notifications in-app. Voici quelques éléments à prendre en compte lors de la création d'une politique de temporisation :

- Comment définit-on un utilisateur « désengagé » ?
- L'engagement est-il défini par les clics, les achats, l'utilisation de l'application, ou une combinaison de ces comportements ?
- Combien de temps l'absence d'engagement doit-elle durer avant que vous cessiez d'envoyer des messages ?
- Enverrez-vous des campagnes spéciales aux utilisateurs avant de les exclure de vos segments ?
- À quels canaux de communication votre politique de temporisation s'appliquera-t-elle ?

Par exemple, si certains de vos utilisateurs ont activé la [protection de la confidentialité dans Mail d'Apple (MPP)]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp), réfléchissez à l'impact que cela peut avoir sur vos campagnes e-mail et vos indicateurs de livrabilité, et déterminez comment structurer au mieux votre politique de temporisation.

Pour intégrer des politiques de temporisation dans vos campagnes, créez un [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#creating-a-segment) qui exclut automatiquement les utilisateurs ayant signalé vos e-mails comme spam ou n'ayant pas interagi avec vos messages pendant une certaine période.

Pour configurer ces segments, choisissez les filtres `Has Marked You As Spam` et `Last Engaged With Message` situés dans la section **Reciblage** du menu déroulant des filtres.

Lorsque vous appliquez le filtre `Last Engaged With Message`, spécifiez le type de message (push, e-mail ou notification in-app) avec lequel l'utilisateur a ou n'a pas interagi, ainsi que le nombre de jours écoulés depuis sa dernière interaction. Après avoir créé un segment, choisissez de cibler ce segment avec n'importe quel [canal de communication]({{site.baseurl}}/user_guide/channels).

![Page de détails du segment avec le filtre « Last Engaged with Message » sélectionné.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Bien que Braze cesse automatiquement d'envoyer des e-mails aux utilisateurs qui vous ont signalé comme spam, le filtre `Has Marked You As Spam` vous permet également d'envoyer à ces utilisateurs des notifications push et des notifications in-app ciblées. Ce filtre est utile pour les [campagnes de reciblage]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#retarget-campaigns). Par exemple, vous pouvez envoyer aux utilisateurs désengagés des messages leur rappelant les fonctionnalités et les offres qu'ils manquent en n'ouvrant pas vos e-mails.

Les politiques de temporisation peuvent être particulièrement utiles dans les campagnes e-mail ciblant les utilisateurs en perte d'engagement. Bien que ces campagnes se concentrent sur des segments n'ayant pas interagi avec votre application pendant un certain temps, elles peuvent mettre en péril la livrabilité de vos e-mails si elles incluent de manière répétée des destinataires désengagés. Les politiques de temporisation vous permettent de cibler les utilisateurs en perte d'engagement sans atterrir dans le dossier spam.