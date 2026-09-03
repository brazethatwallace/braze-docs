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

Pour les e-mails, la réputation de votre adresse IP d'envoi et de votre domaine prend en compte l'engagement, les signalements de courrier indésirable, les mises en liste de blocage, et bien d'autres facteurs. Si votre réputation reste basse, les fournisseurs de services Internet et les filtres de boîtes aux lettres peuvent automatiquement classer vos e-mails dans le dossier spam ou dans un dossier de faible priorité pour tous les destinataires, pas seulement les inactifs. Les politiques de temporisation limitent les envois continus aux utilisateurs désengagés, ce qui contribue à protéger votre réputation ; associez-les à une surveillance régulière pour détecter les problèmes au plus tôt.

## Surveiller la santé de l'IP et du domaine {#monitor-ip-and-domain-health}

Utilisez le [Centre de livrabilité]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) pour suivre la façon dont les fournisseurs de messagerie perçoivent vos envois :

- **Google Postmaster Tools** (après avoir connecté votre compte) : réputation de l'IP, réputation du domaine, erreurs de distribution, authentification (SPF, DKIM, DMARC) et indicateurs de chiffrement pour la visibilité liée à Gmail.
- **Microsoft Smart Network Data Services (SNDS)** (lorsque configuré pour vos IP) : santé de l'IP pour les boîtes aux lettres Outlook et Microsoft, y compris les résultats de filtrage, les taux de plaintes et les pièges à spam détectés.

Pour une hygiène d'envoi plus large, consultez [Améliorer la livrabilité des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) et [Pièges de livrabilité et pièges à spam]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

Vous pouvez également tirer parti d'outils externes tels que [Sender Score](https://www.senderscore.org/) ou le [Smart Network Data Services d'Outlook](https://postmaster.live.com/snds/) en dehors de Braze pour obtenir des signaux supplémentaires.

## Utiliser les listes de suppression {#use-suppression-lists}

Les [listes de suppression]({{site.baseurl}}/user_guide/audience/suppression_lists) sont des groupes d'utilisateurs définis à l'aide de filtres de segment qui ne reçoivent pas de Campaigns ni de Canvas par défaut, même lorsqu'ils apparaissent dans le segment cible. Pour les destinataires inactifs ou désengagés, une liste de suppression agit comme un garde-fou à l'échelle de l'espace de travail. Lorsque les utilisateurs remplissent vos critères d'inactivité, ils cessent de recevoir la plupart des messages sans que vous ayez à modifier chaque segment ou Campaign.

Pour l'aligner sur une politique de temporisation, construisez la liste de suppression avec des filtres qui capturent les utilisateurs ne devant plus recevoir d'e-mails promotionnels réguliers (par exemple, `Last Engaged With Message` ou d'autres filtres sous **Reciblage**) en utilisant la même fenêtre de rétrospection et les mêmes choix de canaux que ceux définis comme « désengagés » dans votre politique. L'appartenance est dynamique : les utilisateurs entrent dans la liste lorsqu'ils remplissent les critères et en sortent lorsqu'ils interagissent à nouveau.

Si vous souhaitez tout de même que certains envois atteignent les utilisateurs inactifs, comme une dernière tentative de reconquête ou des parcours transactionnels approuvés, configurez des tags d'exception sur la liste de suppression afin que les Campaigns ou Canvas portant ces tags soient tout de même distribués lorsque les utilisateurs font partie de l'audience cible. Les listes de suppression fonctionnent conjointement avec la segmentation, qui définit les utilisateurs inclus dans un envoi. Pour les étapes de configuration, les autorisations et les limites, consultez [Configurer les listes de suppression]({{site.baseurl}}/user_guide/audience/suppression_lists#setup).

## Utiliser les filtres de segmentation {#use-segmentation-filters}

Les filtres de segmentation permettent d'éviter que vos messages n'apparaissent comme du spam en vous permettant de mettre facilement en œuvre des politiques de temporisation pour les e-mails, les notifications push et les notifications in-app. Voici quelques éléments à prendre en compte lors de la création d'une politique de temporisation :

- Comment définit-on un utilisateur « désengagé » ?
- L'engagement est-il défini par les clics, les achats, l'utilisation de l'application, ou une combinaison de ces comportements ?
- Combien de temps l'absence d'engagement doit-elle durer avant que vous cessiez d'envoyer des messages ?
- Enverrez-vous des campagnes spéciales aux utilisateurs avant de les exclure de vos segments ?
- À quels canaux de communication votre politique de temporisation s'appliquera-t-elle ?

Par exemple, si certains de vos utilisateurs ont activé la [protection de la confidentialité dans Mail d'Apple (MPP)]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp), réfléchissez à l'impact que cela peut avoir sur vos campagnes e-mail et vos indicateurs de livrabilité, et déterminez comment structurer au mieux votre politique de temporisation.

Pour intégrer des politiques de temporisation dans vos campagnes, créez un [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) qui exclut automatiquement les utilisateurs ayant signalé vos e-mails comme spam ou n'ayant pas interagi avec vos messages pendant une certaine période.

Pour configurer ces segments, choisissez les filtres `Has Marked You As Spam` et `Last Engaged With Message` situés dans la section **Reciblage** du menu déroulant des filtres.

Lorsque vous appliquez le filtre `Last Engaged With Message`, spécifiez le type de message (notification push, e-mail ou notification in-app) avec lequel l'utilisateur a ou n'a pas interagi, ainsi que le nombre de jours écoulés depuis sa dernière interaction. Après avoir créé un segment, choisissez de cibler ce segment avec n'importe quel [canal de communication]({{site.baseurl}}/user_guide/channels).

![Page de détails du segment avec le filtre « Last Engaged with Message » sélectionné.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Bien que Braze cesse automatiquement d'envoyer des e-mails aux utilisateurs qui vous ont signalé comme spam, le filtre `Has Marked You As Spam` vous permet également d'envoyer à ces utilisateurs des notifications push et des notifications in-app ciblées. Ce filtre est utile pour les [campagnes de reciblage]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns). Par exemple, vous pouvez envoyer aux utilisateurs désengagés des messages leur rappelant les fonctionnalités et les offres qu'ils manquent en n'ouvrant pas vos e-mails.

Les politiques de temporisation peuvent être particulièrement utiles dans les campagnes e-mail ciblant les utilisateurs en perte d'engagement. Bien que ces campagnes se concentrent sur des segments n'ayant pas interagi avec votre application pendant un certain temps, elles peuvent mettre en péril la livrabilité de vos e-mails si elles incluent de manière répétée des destinataires désengagés. Les politiques de temporisation vous permettent de cibler les utilisateurs en perte d'engagement sans atterrir dans le dossier spam.