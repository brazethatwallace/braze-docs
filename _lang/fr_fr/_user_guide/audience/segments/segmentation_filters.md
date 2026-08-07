---
page_order: 3
nav_title: Filtres de segmentation
article_title: Filtres de segmentation
layout: glossary_page
glossary_top_header: "Filtres de segmentation"
glossary_top_text: "Le SDK Braze vous fournit un puissant arsenal de filtres pour segmenter et cibler vos utilisateurs en fonction de fonctionnalités et d'attributs spécifiques. Vous pouvez rechercher ou affiner ces filtres par catégorie de filtre.<br><br>Pour en savoir plus sur les différents types de données d'attributs personnalisés que vous pouvez utiliser pour segmenter les utilisateurs, consultez <a href=\"/docs/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types\">Types de données d'attributs personnalisés</a>."

page_type: glossary
tool: Segments
description: "Ce glossaire répertorie les filtres disponibles pour segmenter et cibler vos utilisateurs."
search_rank: 2
glossary_tag_name: Catégorie de filtre
glossary_filter_text: "Sélectionnez une catégorie pour affiner le glossaire :"

glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    description: "Vous permet de filtrer en fonction de l'appartenance à un segment partout où les filtres sont utilisés (comme les segments, les campagnes, etc.) et de cibler plusieurs segments différents au sein d'une même campagne. <br><br>Pour capturer l'appartenance à un segment à un moment précis, exportez les utilisateurs du segment dans le tableau de bord ou appelez l'endpoint <a href=\"/docs/api/endpoints/export/user_data/post_users_segment/\"><code>/users/export/segment</code></a> avant d'envoyer une campagne ou un Canvas. Braze ne stocke pas l'historique de segmentation par utilisateur, vous ne pouvez donc pas vérifier rétroactivement si un utilisateur faisait partie d'un segment à un moment passé. Pour plus d'informations, consultez <a href=\"/docs/user_guide/data/distribution/export_braze_data/segment_data_to_csv/\">Exporter les données de segment au format CSV</a>.<br><br>Notez que les segments utilisant déjà ce filtre ne peuvent pas être davantage inclus ou imbriqués dans d'autres segments, car cela pourrait créer un cycle où le segment A inclut le segment B, qui tente ensuite d'inclure le segment A. Si cela se produisait, le segment se référencerait en permanence, rendant impossible le calcul des utilisateurs qui en font réellement partie. De plus, l'imbrication de segments ajoute de la complexité et peut ralentir les performances. Recréez plutôt le segment que vous essayez d'inclure en utilisant les mêmes filtres.<br><br>Si un segment n'apparaît pas dans le menu déroulant du filtre <strong>Segment Membership</strong>, recréez-le avec les mêmes filtres et sélectionnez le nouveau segment, ou vérifiez qu'il ne dépend pas déjà de cette audience d'une manière qui créerait un cycle."
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: "Après avoir créé une extension de segment dans le tableau de bord de Braze, vous pouvez choisir d'inclure ou d'exclure ces extensions dans votre segment."
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: "Segmente vos utilisateurs selon qu'ils faisaient partie ou non d'un import CSV. Braze ne conserve que les 100 imports CSV les plus récents par profil utilisateur à des fins de segmentation. Si un utilisateur apparaît dans plus de 100 imports CSV sélectionnés pour le reciblage, seuls les 100 plus récents sont disponibles pour ce filtre. Les imports plus anciens ne correspondent plus à cet utilisateur."
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: "Détermine si un utilisateur correspond ou non à une valeur d'attribut personnalisé enregistrée. La période de rétrospection maximale est de 100 ans pour les comparaisons de dates et d'intervalles de temps.<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Custom attribute
  - name: Created At
    description: "Segmente les utilisateurs en fonction de la date de création de leur profil utilisateur. Si un utilisateur a été ajouté par CSV ou API, ce filtre reflète la date à laquelle il a été ajouté. Si l'utilisateur n'a pas été ajouté par CSV ou API et que sa première session est suivie par le SDK, ce filtre reflète la date de cette première session. La période de rétrospection maximale est de 100 ans."
    tags:
      - Other Filters
  - name: Created From
    description: "Segmente les utilisateurs en fonction de l'origine de création de leur profil utilisateur.<br><br>Les valeurs suivantes sont prises en charge :<br>- SDK (<code>sdk</code>) : profil utilisateur créé via le SDK Braze.<br>- REST API (<code>rest</code>) : profil utilisateur créé via la REST API Braze.<br>- Import de jeton push (<code>pti</code>) : profil utilisateur créé via l'import de jetons push.<br>- CSV (<code>csv</code>) : profil utilisateur créé via un import CSV.<br>- Démo (<code>demo</code>) : profil utilisateur créé via des données de démonstration.<br>- SMS (<code>sms</code>) : profil utilisateur créé via SMS.<br>- Shopify (<code>shopify</code>) : profil utilisateur créé via Shopify.<br>- WhatsApp (<code>whats_app</code>) : profil utilisateur créé via WhatsApp.<br>- Événement fournisseur (<code>provider_event</code>) : profil utilisateur créé via un événement fournisseur.<br>- Synchronisation fournisseur (<code>provider_sync</code>) : profil utilisateur créé via une synchronisation fournisseur.<br>- Page de destination (<code>landing_page</code>) : profil utilisateur créé via une page de destination."
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: "Attributs qui sont les propriétés d'attributs personnalisés.<br><br>Lors du filtrage d'un attribut personnalisé imbriqué de type date, vous pouvez choisir de filtrer par « Jour de l'année » ou « Heure ». « Jour de l'année » compare uniquement le mois et le jour. « Heure » compare l'horodatage complet, y compris l'année. La période de rétrospection maximale est de 100 ans pour les comparaisons d'intervalles de temps. La même logique s'applique lors du filtrage sur les variables de contexte dans les parcours d'audience Canvas ; consultez <a href=\"/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#day-of-year-and-time-filters-for-date-context-variables\">Filtres Jour de l'année et Heure pour les variables de contexte de type date</a> pour plus de détails."
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: "Ce filtre examine le mois et le jour d'un attribut personnalisé de type « date », mais ne prend pas en compte l'année. Ce filtre est utile pour les événements annuels.<br><br>Fuseau horaire&#58;<br>Ce filtre s'ajuste au fuseau horaire de l'utilisateur, à condition que le message soit envoyé avec l'option de planification en heure locale ; sinon, ce filtre utilise le fuseau horaire de votre entreprise."
    tags:
      - Custom attribute
  - name: Custom Event
    description: "Détermine si un utilisateur a effectué ou non un événement spécialement enregistré.<br><br>Exemple :<br>Activité terminée avec la propriété activity_name.<br><br>Fuseau horaire :<br>UTC - Jour calendaire = 1 jour calendaire examine 24 à 48 heures d'historique utilisateur"
    tags:
      - Custom events
  - name: First Did Custom Event
    description: "Détermine la première fois qu'un utilisateur a effectué un événement spécialement enregistré. La période de rétrospection maximale est de 100 ans. (période de 24 heures) <br><br>Exemple :<br> Premier panier abandonné il y a moins d'1 jour<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Custom events
  - name: Last Did Custom Event
    description: "Détermine la dernière fois qu'un utilisateur a effectué un événement spécialement enregistré. Ce filtre prend en charge les décimales, comme 0,25 heure. La période de rétrospection maximale est de 100 ans. (période de 24 heures) <br><br>Exemple :<br> Dernier panier abandonné il y a moins d'1 jour<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré entre 0 et 50 fois au cours du nombre spécifié de jours calendaires entre 1 et 30. (Jour calendaire = 1 jour calendaire examine 24 à 48 heures d'historique utilisateur)<br> <a href=\"/docs/x-in-y-behavior\"> En savoir plus sur le comportement X-en-Y ici.</a> <br><br>Exemple :<br>Panier abandonné exactement 0 fois au cours du dernier jour calendaire<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, 1 jour calendaire examine 24 à 48 heures d'historique utilisateur, selon l'heure à laquelle le segment est évalué ; pour 2 jours calendaires, examine 48 à 72 heures d'historique utilisateur, et ainsi de suite."
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré en relation avec une propriété spécifique entre 0 et 50 fois au cours du nombre spécifié de jours calendaires entre 1 et 30. (Jour calendaire = 1 jour calendaire examine 24 à 48 heures d'historique utilisateur)<br><a href=\"/docs/x-in-y-behavior\">En savoir plus sur le comportement X-en-Y ici.</a> <br><br>Exemple :<br> Ajouté aux favoris avec la propriété « event_name » exactement 0 fois au cours du dernier jour calendaire<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, 1 jour calendaire examine 24 à 48 heures d'historique utilisateur, selon l'heure à laquelle le segment est évalué ; pour 2 jours calendaires, examine 48 à 72 heures d'historique utilisateur, et ainsi de suite."
    tags:
      - Custom events
  - name: Email Address
    description: "Vous permet de désigner les destinataires de votre campagne par adresses e-mail individuelles à des fins de test. Cela peut également être utilisé pour envoyer des e-mails transactionnels à tous vos utilisateurs (y compris les désabonnés) en utilisant le spécificateur « L'adresse e-mail n'est pas vide » dans le filtre, afin de maximiser la distribution des e-mails quel que soit le statut d'abonnement. <br><br>Ce filtre vérifie uniquement si les profils utilisateur possèdent une adresse e-mail, tandis que le filtre <a href=\"/docs/user_guide/audience/segments/segmentation_filters#email-available\">E-mail disponible</a> vérifie des critères supplémentaires."
    tags:
      - Other Filters
  - name: External User ID
    description: "Vous permet de désigner les destinataires de votre campagne par identifiants utilisateur individuels à des fins de test."
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: "Segmente vos utilisateurs par un nombre attribué aléatoirement (de 0 à 9999 inclus). Il permet la création de segments uniformément distribués d'utilisateurs véritablement aléatoires pour les tests A/B et multivariés."
    tags:
      - Other Filters
  - name: Session Count
    description: "Segmente vos utilisateurs par le nombre de sessions qu'ils ont eues dans l'une de vos applications au sein de votre espace de travail."
    tags:
      - Sessions
  - name: Session Count For App
    description: "Segmente vos utilisateurs par le nombre de sessions qu'ils ont eues dans une application spécifique désignée."
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: "Segmente vos utilisateurs par le nombre de sessions (entre 0 et 50) qu'ils ont eues dans votre application au cours du nombre spécifié de jours calendaires entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior\">En savoir plus sur le comportement X-en-Y ici.</a>"
    tags:
      - Sessions
  - name: First Used App
    description: "Segmente vos utilisateurs par la première date enregistrée à laquelle ils ont ouvert votre application. <em>Cela capture la première session qu'ils ont eue en utilisant une version de votre application avec le SDK Braze intégré.</em> La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: First Used Specific App
    description: "Segmente vos utilisateurs par la première date enregistrée à laquelle ils ont ouvert l'une de vos applications au sein de votre espace de travail. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: Last Used App
    description: "Segmente vos utilisateurs par la date la plus récente à laquelle ils ont ouvert votre application. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: Last Used Specific App
    description: "Segmente vos utilisateurs par la date la plus récente à laquelle ils ont ouvert une application spécifique désignée. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: Median Session Duration
    description: "Segmente vos utilisateurs par la durée médiane de leurs sessions dans votre application."
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne spécifique. <br><br>Pour les Content Cards, les bannières et les messages in-app, cela correspond au moment où un utilisateur enregistre une impression, et non au moment où la carte ou le message in-app est envoyé.<br><br> Pour les notifications push et les webhooks, cela correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, cela correspond au moment où la dernière requête API de message est envoyée à WhatsApp, et non au moment où le message est distribué sur l'appareil de l'utilisateur.<br><br> Pour les e-mails, le profil utilisateur ciblé correspond à ce filtre lorsqu'une requête d'e-mail est envoyée au fournisseur de services d'e-mailing (qu'il soit effectivement distribué ou non).<br><br> Pour les SMS et RCS, les utilisateurs sont considérés comme ayant « reçu » un message au moment de l'envoi. Même si le message n'atteint pas l'appareil de l'utilisateur, celui-ci correspond toujours à ce filtre.<br><br> Lorsqu'un message est distribué, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal (par exemple, e-mail ou numéro de téléphone), de sorte que les utilisateurs partageant un identifiant avec quelqu'un qui a reçu le message peuvent correspondre à ce filtre même si leur profil n'a pas directement reçu la campagne."
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: "Segmente vos utilisateurs selon la variante d'une campagne multivariée qu'ils ont reçue.<br><br>Ce filtre s'applique aux campagnes multivariées et aux campagnes push rapides multivariées. Les campagnes API, les campagnes multicanales standard et les campagnes d'expérimentation de feature flags n'apparaissent pas dans le sélecteur de campagne. Les campagnes uniquement webhook n'apparaissent pas dans le sélecteur de campagne.<br><br>Pour les Content Cards, les bannières et les messages in-app, cela correspond au moment où un utilisateur enregistre une impression, et non au moment où la carte ou le message in-app est envoyé.<br><br> Pour les notifications push et les webhooks, cela correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, cela correspond au moment où la dernière requête API de message est envoyée à WhatsApp, et non au moment où le message est distribué sur l'appareil de l'utilisateur.<br><br> Pour les e-mails, le profil utilisateur ciblé correspond à ce filtre lorsqu'une requête d'e-mail est envoyée au fournisseur de services d'e-mailing (qu'il soit effectivement distribué ou non).<br><br> Pour les SMS et RCS, les utilisateurs sont considérés comme ayant « reçu » un message au moment de l'envoi. Même si le message n'atteint pas l'appareil de l'utilisateur, celui-ci correspond toujours à ce filtre.<br><br> Lorsqu'un message est distribué, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal (par exemple, e-mail ou numéro de téléphone), de sorte que les utilisateurs partageant un identifiant avec quelqu'un qui a reçu le message peuvent correspondre à ce filtre même si leur profil n'a pas directement reçu la campagne."
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non un composant Canvas spécifique.<br><br>Pour les Content Cards et les messages in-app, cela correspond au moment où un utilisateur enregistre une impression, et non au moment où la carte ou le message in-app est envoyé.<br><br> Pour les notifications push et les webhooks, cela correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, cela correspond au moment où la dernière requête API de message est envoyée à WhatsApp, et non au moment où le message est distribué sur l'appareil de l'utilisateur.<br><br> Pour les e-mails, le profil utilisateur ciblé correspond à ce filtre lorsqu'une requête d'e-mail est envoyée au fournisseur de services d'e-mailing (qu'il soit effectivement distribué ou non).<br><br> Pour les SMS et RCS, les utilisateurs sont considérés comme ayant « reçu » un message au moment de l'envoi. Même si le message n'atteint pas l'appareil de l'utilisateur, celui-ci correspond toujours à ce filtre.<br><br> Lorsqu'un message est distribué, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal (par exemple, e-mail ou numéro de téléphone), de sorte que les utilisateurs partageant un identifiant avec quelqu'un qui a reçu le message peuvent correspondre à ce filtre même si leur profil n'a pas directement reçu la campagne."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: "Segmente vos utilisateurs en fonction du moment où ils ont reçu un composant Canvas spécifique. La période de rétrospection maximale est de 100 ans.<br><br> Étant donné que les données sont mises à jour pour tous les profils partageant le même identifiant de canal (par exemple, e-mail ou téléphone) lorsqu'une distribution, une ouverture ou un clic se produit, un utilisateur partageant un identifiant avec quelqu'un qui a reçu un message peut correspondre à ce filtre même s'il n'a jamais reçu explicitement le message. Utilisez « Entered Canvas Variation » pour isoler les profils utilisateur des doublons.<br><br> Ce filtre ne prend pas en compte le moment où les utilisateurs ont reçu d'autres composants Canvas."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne spécifique. La période de rétrospection maximale est de 100 ans.<br><br> Étant donné que les données sont mises à jour pour tous les profils partageant le même identifiant de canal (par exemple, e-mail ou téléphone) lorsqu'une distribution, une ouverture ou un clic se produit, un utilisateur partageant un identifiant avec quelqu'un qui a reçu un message peut correspondre à ce filtre même s'il n'a jamais reçu explicitement le message.<br><br> Ce filtre ne prend pas en compte le moment où les utilisateurs ont reçu d'autres campagnes."
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne ou un Canvas spécifique avec une étiquette spécifique.<br><br>Braze n'évalue que les 200 dernières campagnes et Canvas envoyés utilisant l'étiquette sélectionnée lorsque ce filtre est exécuté.<br><br> Pour les Content Cards, les bannières (Campaigns uniquement) et les messages in-app, cela correspond au moment où un utilisateur enregistre une impression, et non au moment où la carte ou le message in-app est envoyé.<br><br> Pour les notifications push et les webhooks, cela correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, cela correspond au moment où la dernière requête API de message est envoyée à WhatsApp, et non au moment où le message est distribué sur l'appareil de l'utilisateur.<br><br> Pour les e-mails, le profil utilisateur ciblé correspond à ce filtre lorsqu'une requête d'e-mail est envoyée au fournisseur de services d'e-mailing (qu'il soit effectivement distribué ou non).<br><br> Pour les SMS et RCS, les utilisateurs sont considérés comme ayant « reçu » un message au moment de l'envoi. Même si le message n'atteint pas l'appareil de l'utilisateur, celui-ci correspond toujours à ce filtre.<br><br> Lorsqu'un message est distribué, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal (par exemple, e-mail ou numéro de téléphone), de sorte que les utilisateurs partageant un identifiant avec quelqu'un qui a reçu le message peuvent correspondre à ce filtre même si leur profil n'a pas directement reçu la campagne."
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: "Segmente vos utilisateurs en fonction du moment où ils ont reçu une campagne ou un Canvas spécifique avec une étiquette spécifique. Ce filtre ne prend pas en compte le moment où les utilisateurs ont reçu d'autres campagnes ou Canvas. La période de rétrospection maximale est de 100 ans. (période de 24 heures)"
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne ou un composant Canvas."
    tags:
      - Retargeting
  - name: Last Received Email
    description: "Segmente vos utilisateurs par la dernière fois qu'ils ont reçu l'un de vos e-mails. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Last Received Push
    description: "Segmente vos utilisateurs par la dernière fois qu'ils ont reçu l'une de vos notifications push. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: "Segmente vos utilisateurs par la dernière fois qu'ils ont vu un message in-app. La période de rétrospection maximale est de 100 ans."
    tags:
      - Retargeting
  - name: Last Received SMS
    description: "Segmente vos utilisateurs par le moment où le dernier SMS, MMS ou message RCS a été distribué au fournisseur SMS ou RCS. Cela ne garantit pas que le message a été distribué sur l'appareil de l'utilisateur. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: "Segmente vos utilisateurs par la dernière fois que Braze a envoyé un webhook pour cet utilisateur. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: "Segmente vos utilisateurs par la dernière fois qu'ils ont reçu un message WhatsApp. Cela correspond au moment où la dernière requête API de message est envoyée à WhatsApp, et non au moment où le message est distribué sur l'appareil de l'utilisateur. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: "Segmente vos utilisateurs selon qu'ils sont enregistrés pour démarrer une activité en direct via les notifications push iOS pour une application spécifique."
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: "Filtre par interaction avec une campagne spécifique. Pour les messages in-app, les clics sur les messages in-app incluent les clics sur le corps et les boutons. Les actions de fermeture ou la fermeture du message avec le X ne sont pas comptabilisées.<br><br>Pour les e-mails, l'événement d'ouverture inclut à la fois les ouvertures automatiques et les ouvertures non automatiques. Ce filtre inclut également l'option de filtrer par « a ouvert un e-mail (ouvertures automatiques) » et « a ouvert un e-mail (autres ouvertures) ». Les clics sur les liens de désabonnement et les centres de préférences ne sont pas comptabilisés dans ce filtre. Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur d'origine change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants ayant cette adresse e-mail au lieu de l'utilisateur d'origine.<br><br>Pour les SMS et RCS, une interaction est définie comme :<br>- L'utilisateur a envoyé en dernier un SMS ou RCS de réponse correspondant à une catégorie de mot-clé donnée. Cela est attribué à la campagne la plus récente reçue par tous les utilisateurs ayant ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures.<br>- L'utilisateur a sélectionné en dernier un lien raccourci dans un SMS ou un message RCS dont le suivi des clics utilisateur est activé, provenant d'une campagne donnée."
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: "Filtre par interaction avec une campagne spécifique ayant une étiquette spécifique. Pour les messages in-app, les clics sur les messages in-app incluent les clics sur le corps et les boutons. Les actions de fermeture ou la fermeture du message avec le X ne sont pas comptabilisées.<br><br>Pour les e-mails, l'événement d'ouverture inclut à la fois les ouvertures automatiques et les ouvertures non automatiques. Ce filtre inclut également l'option de filtrer par « a ouvert un e-mail (ouvertures automatiques) » et « a ouvert un e-mail (autres ouvertures) ». Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur d'origine change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants ayant cette adresse e-mail au lieu de l'utilisateur d'origine.<br><br>Pour les SMS et RCS, une interaction est définie comme :<br>- L'utilisateur a envoyé en dernier un SMS ou RCS de réponse correspondant à une catégorie de mot-clé donnée. Cela est attribué à la campagne la plus récente reçue par tous les utilisateurs ayant ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures.<br>- L'utilisateur a sélectionné en dernier un lien raccourci dans un SMS ou un message RCS dont le suivi des clics utilisateur est activé, provenant d'une campagne ou d'une étape Canvas donnée avec une étiquette."
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: "Filtre par interaction avec un composant Canvas spécifique. Pour les messages in-app, les clics sur les messages in-app incluent également les clics sur le corps et les boutons. Les actions de fermeture ou la fermeture du message avec le X ne sont pas comptabilisées.<br><br>Pour les e-mails, l'événement d'ouverture inclut à la fois les ouvertures automatiques et les ouvertures non automatiques. Ce filtre inclut également l'option de filtrer par « a ouvert un e-mail (ouvertures automatiques) » et « a ouvert un e-mail (autres ouvertures) ».<br><br>Pour les SMS et RCS, une interaction est définie comme :<br>- L'utilisateur a envoyé en dernier un SMS ou RCS de réponse correspondant à une catégorie de mot-clé donnée. Cela est attribué à la campagne la plus récente reçue par tous les utilisateurs ayant ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures. <br>- L'utilisateur a sélectionné en dernier un lien raccourci dans un SMS ou un message RCS dont le suivi des clics utilisateur est activé, provenant d'une étape Canvas donnée."
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: "Filtre vos utilisateurs selon qu'ils ont cliqué sur un alias spécifique dans une campagne spécifique. Cela s'applique uniquement aux e-mails. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur d'origine change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants ayant cette adresse e-mail au lieu de l'utilisateur d'origine."
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: "Filtre vos utilisateurs selon qu'ils ont cliqué sur un alias spécifique dans un Canvas spécifique. Cela s'applique uniquement aux e-mails. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur d'origine change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants ayant cette adresse e-mail au lieu de l'utilisateur d'origine."
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: "Filtre vos utilisateurs selon qu'ils ont cliqué sur un alias spécifique dans n'importe quelle campagne ou Canvas. Cela s'applique uniquement aux e-mails. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur d'origine change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants ayant cette adresse e-mail au lieu de l'utilisateur d'origine."
    tags:
      - Retargeting
  - name: Hard Bounced
    description: "Segmente vos utilisateurs selon que leur adresse e-mail a subi un échec d'envoi définitif (par exemple, l'adresse e-mail est invalide). Pour exporter les utilisateurs ayant des e-mails invalides, appelez l'endpoint <a href=\"/docs/api/endpoints/email/get_list_hard_bounces/\"><code>/email/hard_bounces</code></a> ou créez un segment avec des filtres tels que l'adresse e-mail n'est pas vide, l'e-mail n'est pas disponible et le statut d'abonnement e-mail n'est pas désabonné."
    tags:
      - Retargeting
  - name: Soft Bounced
    description: "Segmente vos utilisateurs selon qu'ils ont subi un échec provisoire d'envoi X fois en Y jours. Les filtres de segment ne peuvent remonter que sur 30 jours, mais vous pouvez remonter plus loin avec les extensions de segments.<br><br>Ce filtre fonctionne différemment d'un événement d'échec provisoire d'envoi dans Currents. Le filtre de segment Échec provisoire d'envoi comptabilise un échec provisoire si aucune distribution réussie n'a eu lieu pendant la période de nouvelle tentative de 72 heures. Dans Currents, chaque tentative infructueuse est envoyée comme un événement d'échec provisoire d'envoi."
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: "Segmente vos utilisateurs selon qu'ils ont marqué vos messages comme spam."
    tags:
      - Retargeting
  - name: Invalid Phone Number
    description: "Segmente vos utilisateurs selon que leur numéro de téléphone est invalide."
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: "Segmente vos utilisateurs en fonction du moment où ils ont envoyé en dernier un SMS, MMS ou RCS à un groupe d'abonnement spécifique dans une catégorie de mot-clé spécifique. La période de rétrospection maximale est de 100 ans."
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: "Segmente vos utilisateurs selon qu'ils ont converti sur une campagne spécifique. Ce filtre n'inclut pas les utilisateurs du groupe de contrôle."
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: "Segmente vos utilisateurs selon qu'ils ont converti sur un Canvas spécifique. Ce filtre n'inclut pas les utilisateurs du groupe de contrôle."
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: "Segmente vos utilisateurs selon qu'ils faisaient partie du groupe de contrôle d'une campagne multivariée spécifique."
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: "Segmente vos utilisateurs selon qu'ils faisaient partie du groupe de contrôle d'un Canvas spécifique. Ce filtre n'évalue que les utilisateurs qui sont entrés dans le Canvas, de sorte que les utilisateurs qui n'y sont jamais entrés sont entièrement exclus des résultats.<br><br>Par exemple, si vous filtrez les utilisateurs qui ne sont pas dans le groupe de contrôle d'un Canvas, vous n'obtenez que les utilisateurs qui sont entrés dans le Canvas et ont été affectés à une variante non-contrôle — les utilisateurs qui ne sont jamais entrés dans le Canvas ne sont pas inclus. Pour inclure tous les utilisateurs indépendamment de l'entrée dans le Canvas, utilisez plutôt le filtre <code>Entered Canvas Variation</code>."
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: "Segmente vos utilisateurs par la dernière fois qu'ils ont été placés dans le groupe de contrôle d'une campagne. La période de rétrospection maximale est de 100 ans. <br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: "Segmente vos utilisateurs selon qu'ils sont entrés dans un chemin de variante d'un Canvas spécifique. Ce filtre évalue tous les utilisateurs.<br><br>Par exemple, si vous filtrez les utilisateurs qui ne sont pas entrés dans un groupe de contrôle de variante Canvas, vous obtenez tous les utilisateurs qui ne sont pas dans le groupe de contrôle, qu'ils soient entrés ou non dans le Canvas."
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: "Segmente vos utilisateurs en déterminant le dernier message reçu. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Pour les Content Cards, les bannières et les messages in-app, cela correspond au moment où un utilisateur a enregistré une impression pour la dernière fois, et non au moment où la carte ou le message in-app a été envoyé.<br><br>Pour les notifications push et les webhooks, cela correspond au moment où un message a été envoyé à l'utilisateur.<br><br> Pour WhatsApp, cela correspond au moment où la dernière requête API de message a été envoyée à WhatsApp, et non au moment où le message a été distribué sur l'appareil de l'utilisateur.<br><br> Pour les e-mails, le profil utilisateur ciblé correspond à ce filtre lorsqu'une requête d'e-mail est envoyée au fournisseur de services d'e-mailing (qu'il soit effectivement distribué ou non).<br><br> Pour les SMS et RCS, les utilisateurs sont considérés comme ayant « reçu » un message au moment de l'envoi. Même si le message n'atteint pas l'appareil de l'utilisateur, celui-ci correspond toujours à ce filtre.<br><br> Lorsqu'un message est distribué, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal (par exemple, e-mail ou numéro de téléphone), de sorte que les utilisateurs partageant un identifiant avec quelqu'un qui a reçu le message peuvent correspondre à ce filtre même si leur profil n'a pas directement reçu la campagne.<br><br>Exemple :<br>Dernier message reçu il y a moins d'1 jour = il y a moins de 24 heures<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: "Segmente vos utilisateurs par la dernière fois qu'ils ont cliqué ou ouvert l'un de vos canaux de communication (bannières, Content Cards, e-mail, in-app, SMS, RCS, push, WhatsApp).<br><br>Pour les Content Cards, les bannières et les messages in-app, cela correspond au moment où un utilisateur enregistre une impression, et non au moment où la carte ou le message in-app est envoyé.<br><br> Pour les notifications push et les webhooks, cela correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, cela correspond au moment où la dernière requête API de message est envoyée à WhatsApp, et non au moment où le message est distribué sur l'appareil de l'utilisateur.<br><br> Pour les e-mails, l'événement d'ouverture inclut à la fois les ouvertures automatiques et les ouvertures non automatiques. La période de rétrospection maximale est de 100 ans. (période de 24 heures)<br><br>Pour les e-mails, le profil utilisateur ciblé correspond à ce filtre lorsqu'une requête d'e-mail est envoyée au fournisseur de services d'e-mailing (qu'il soit effectivement distribué ou non). Cela inclut également l'option de filtrer par « a ouvert un e-mail (ouvertures automatiques) » et « a ouvert un e-mail (autres ouvertures) ».<br><br> Pour les SMS et RCS, cela correspond au moment où l'utilisateur a sélectionné en dernier un lien raccourci dans un message dont le suivi des clics utilisateur est activé.<br><br> Lorsqu'un message est distribué, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal (par exemple, e-mail ou numéro de téléphone), de sorte que les utilisateurs partageant un identifiant avec quelqu'un qui a reçu le message peuvent correspondre à ce filtre même si leur profil n'a pas directement reçu la campagne.<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Clicked card
    description: "Segmente vos utilisateurs selon qu'ils ont cliqué sur une Content Card spécifique. Ce filtre est disponible en tant que sous-filtre de « A cliqué/ouvert une campagne », « A cliqué/ouvert une campagne ou un Canvas avec une étiquette » et « A cliqué/ouvert une étape »."
    tags:
      - Retargeting
  - name: Feature Flags
    description: "Le segment de vos utilisateurs pour lesquels un <a href=\"/docs/developer_guide/feature_flags\">feature flag</a> particulier est actuellement activé."
    tags:
      - Retargeting
  - name: Subscription Group
    description: "Segmente vos utilisateurs par leur groupe d'abonnement pour les e-mails, SMS, MMS, RCS ou WhatsApp. Les groupes archivés n'apparaissent pas et ne peuvent pas être utilisés."
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: "Segmente vos utilisateurs selon qu'ils possèdent une adresse e-mail valide et qu'ils sont abonnés ou ont opté pour les e-mails. Ce filtre vérifie trois critères&#58; si l'utilisateur s'est désabonné des e-mails, si Braze a reçu un échec d'envoi définitif et si l'e-mail a été marqué comme spam. Si l'un de ces critères est rempli, ou si aucune adresse e-mail n'existe pour un utilisateur, l'utilisateur n'est pas inclus.<br><br>Les utilisateurs dont l'e-mail disponible est <code>false</code> sont exclus de l'audience de la campagne et ne reçoivent pas l'e-mail, même si vos paramètres d'envoi sont configurés pour envoyer à tous les utilisateurs (y compris les utilisateurs désabonnés).<br><br>Pour les e-mails où le statut d'abonnement est important, utilisez E-mail disponible au lieu de <a href=\"/docs/user_guide/audience/segments/segmentation_filters#email-address\">Adresse e-mail</a>. Les critères supplémentaires vous aident à cibler les utilisateurs éligibles à la réception d'e-mails."
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: "Segmente vos utilisateurs par la date à laquelle ils se sont abonnés aux e-mails. La période de rétrospection maximale est de 100 ans."
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: "Segmente vos utilisateurs par leur statut d'abonnement aux e-mails."
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    description: "Segmente vos utilisateurs par la date à laquelle ils se sont désabonnés des futurs e-mails. La période de rétrospection maximale est de 100 ans."
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    description: "Segmente vos utilisateurs qui ont une autorisation push provisoire ou qui sont activés pour les notifications push au premier plan. Plus précisément, ce décompte inclut :<br>1. Les utilisateurs iOS qui sont provisoirement autorisés pour les notifications push. <br>2. Les utilisateurs qui sont activés pour les notifications push au premier plan et dont le statut d'abonnement push n'est pas désabonné, pour l'une de vos applications. Pour ces utilisateurs, ce décompte inclut uniquement les notifications push au premier plan.<br><br>Notifications push au premier plan activées n'inclut pas les utilisateurs qui se sont désabonnés. <br><br>Après avoir segmenté avec ce filtre, vous pouvez voir une répartition des utilisateurs de ce segment pour Android, iOS et web dans le panneau inférieur, appelé <em>Utilisateurs joignables</em>."
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: "Segmente selon que les utilisateurs ont les notifications push activées pour votre application sur leur appareil. Utilisateurs pour lesquels les notifications push au premier plan sont activées pour une application. Cela ne prend pas en compte le statut d'abonnement push. Ce décompte inclut les utilisateurs qui ont provisoirement autorisé les jetons push au premier plan et en arrière-plan."
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: "Segmente selon que les utilisateurs possèdent un jeton push et ne se sont pas désabonnés. Utilisateurs pour lesquels les notifications push en arrière-plan ou au premier plan sont activées pour l'une de vos applications."
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: "Segmente vos utilisateurs par la date à laquelle ils se sont abonnés aux notifications push. La période de rétrospection maximale est de 100 ans."
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: "Segmente vos utilisateurs par leur <a href=\"/docs/user_guide/channels/push/push_setup/push_subscription_states\">statut d'abonnement</a> aux notifications push."
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: "Segmente vos utilisateurs par la date à laquelle ils se sont désabonnés des futures notifications push. La période de rétrospection maximale est de 100 ans."
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: "Segmente vos utilisateurs par les produits achetés dans votre application."
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: "Segmente vos utilisateurs par le nombre d'achats qu'ils ont effectués dans votre application."
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: "Filtre les utilisateurs par le nombre de fois qu'un produit spécifique a été acheté."
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: "Segmente vos utilisateurs par le nombre de fois (entre 0 et 50) qu'ils ont effectué un achat au cours du nombre spécifié de jours calendaires entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior\">En savoir plus sur le comportement X-en-Y ici.</a>"
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: "Segmente vos utilisateurs par le nombre de fois qu'un achat a été effectué en relation avec une certaine propriété d'achat au cours du nombre spécifié de jours calendaires entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior\">En savoir plus sur le comportement X-en-Y ici.</a>"
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: "Segmente vos utilisateurs par la première fois qu'un utilisateur a effectué un achat dans votre application. La période de rétrospection maximale est de 100 ans."
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: "Segmente vos utilisateurs par la première fois qu'un utilisateur a effectué un achat depuis votre application. La période de rétrospection maximale est de 100 ans."
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    description: "Filtre les utilisateurs par la dernière fois qu'ils ont effectué un achat. La période de rétrospection maximale est de 100 ans."
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: "Filtre les utilisateurs par la dernière fois qu'ils ont acheté un produit spécifique. La période de rétrospection maximale est de 100 ans."
    tags:
      - Purchase behavior
  - name: Money Spent
    description: "Segmente vos utilisateurs par le montant qu'ils ont dépensé dans votre application."
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: "Segmente vos utilisateurs par le montant qu'ils ont dépensé dans votre application au cours du nombre spécifié de jours calendaires entre 1 et 30. Ce montant inclut uniquement la somme des 50 derniers achats. <br> <a href=\"/docs/x-in-y-behavior\">En savoir plus sur le comportement X-en-Y ici.</a>"
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: "Segmente vos utilisateurs en fonction du moment où ils ont passé leur dernière commande, basé sur l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes passées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour, et la fenêtre de rétrospection maximale est de 2 ans.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: "Segmente vos utilisateurs par le nombre total de commandes d'un utilisateur au cours des 2 dernières années, basé sur l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes passées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Ce décompte exclut les commandes annulées, qui doivent être suivies à l'aide de l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes annulées. Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total orders count
    description: "Segmente vos utilisateurs par le nombre total de commandes d'un utilisateur sur toute sa durée de vie, basé sur l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes passées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Ce décompte exclut les commandes annulées, qui doivent être suivies à l'aide de l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes annulées. Les utilisateurs sont évalués pour ce filtre en temps réel.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: "Segmente vos utilisateurs par le nombre total de commandes annulées par un utilisateur au cours des 2 dernières années, basé sur l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes passées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: "Segmente vos utilisateurs par le chiffre d'affaires total qu'un utilisateur est censé générer sur l'ensemble de son historique d'achat avec votre marque. Le calcul prend en compte les 730 derniers jours et utilise la valeur moyenne de commande (AOV), la multiplie par le nombre total de commandes passées, puis prend en compte la durée d'achat active de l'utilisateur (la période entre sa première et sa plus récente commande). Ce filtre utilise les données suivies dans les <a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événements eCommerce recommandés</a> (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: "Segmente vos utilisateurs par la valeur des remboursements accordés à un utilisateur au cours des 2 dernières années, basé sur l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes remboursées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total refund value
    description: "Segmente vos utilisateurs par la valeur totale des remboursements accordés à un utilisateur sur toute sa durée de vie, basé sur l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes remboursées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre en temps réel.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: "Segmente vos utilisateurs par le chiffre d'affaires total généré par les commandes d'un utilisateur au cours des 2 dernières années, calculé en soustrayant le chiffre d'affaires associé à l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes remboursées du chiffre d'affaires associé à l'événement eCommerce pour les commandes passées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total revenue
    description: "Segmente vos utilisateurs par le chiffre d'affaires total généré par les commandes d'un utilisateur sur toute sa durée de vie, calculé en soustrayant le chiffre d'affaires associé à l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes remboursées du chiffre d'affaires associé à l'événement eCommerce pour les commandes passées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre en temps réel.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: "Segmente vos utilisateurs par la valeur moyenne (arithmétique) des commandes d'un utilisateur au cours des 2 dernières années, basé sur l'<a href=\"/docs/user_guide/data/activation/events/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour les commandes passées (les espaces de travail ne suivant pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Country
    description: "Segmente vos utilisateurs par leur dernière localisation de pays indiquée."
    tags:
      - Demographic attributes
  - name: City
    description: "Segmente vos utilisateurs par leur dernière localisation de ville indiquée."
    tags:
      - Demographic attributes
  - name: Language
    description: "Segmente vos utilisateurs par leur langue préférée."
    tags:
      - Demographic attributes
  - name: Age
    description: "Segmente vos utilisateurs par leur âge, tel qu'ils l'ont indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: Birthday
    description: "Segmente vos utilisateurs par leur date de naissance, telle qu'ils l'ont indiquée dans votre application. <br> Les utilisateurs nés le 29 février sont inclus dans les segments incluant le 1er mars.<br><br>Pour cibler les anniversaires de décembre ou janvier, insérez uniquement la logique de filtre dans la période de 12 mois de l'année que vous ciblez. En d'autres termes, n'insérez pas de logique qui remonte au mois de décembre de l'année civile précédente ou qui avance au mois de janvier de l'année suivante. Par exemple, pour cibler les anniversaires de décembre, vous pouvez filtrer par « le 31 décembre », « avant le 31 décembre » ou « après le 30 novembre »."
    tags:
      - Demographic attributes
  - name: Gender
    description: "Segmente vos utilisateurs par genre, tel qu'ils l'ont indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: "Segmente vos utilisateurs par leur numéro de téléphone non formaté. N'inclut pas les parenthèses, tirets ou autres symboles."
    tags:
      - Demographic attributes
  - name: First Name
    description: "Segmente vos utilisateurs par leur prénom, tel qu'ils l'ont indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: Last Name
    description: "Segmente vos utilisateurs par leur nom de famille, tel qu'ils l'ont indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: Has App
    description: "Segmente selon qu'un utilisateur a déjà installé votre application. Cela inclut les utilisateurs qui ont actuellement votre application installée et ceux qui l'ont désinstallée par le passé. Cela nécessite généralement que les utilisateurs ouvrent l'application (démarrent une session) pour être inclus dans ce filtre. Cependant, il existe quelques exceptions, par exemple si un utilisateur a été importé dans Braze et associé manuellement à votre application."
    tags:
      - App
  - name: Most Recent App Version Name
    description: "Segmente par le nom le plus récent de la version de l'application de l'utilisateur.<br><br>Lors de l'utilisation de « inférieur à » ou « inférieur ou égal à », si la version principale de l'application n'existe pas, ce filtre renvoie <code>true</code> car l'utilisateur est plus ancien que la version de l'application. Cela signifie que si la dernière version principale de l'application de l'utilisateur n'existe pas, il correspond automatiquement au filtre."
    tags:
      - App
  - name: Most Recent App Version Number
    description: "Segmente par le numéro de version le plus récent de l'application de l'utilisateur. Le numéro de version entre parenthèses est utilisé pour le filtrage, tandis que le numéro qui le précède est fourni à titre de référence — par exemple, dans « 3.7.0(134.0.0.0) », « 134.0.0.0 » est le numéro de version filtré.<br><br>Lors de l'utilisation de « inférieur à » ou « inférieur ou égal à », si la version principale de l'application n'existe pas, ce filtre renvoie <code>true</code> car l'utilisateur est plus ancien que la version de l'application. Cela signifie que si la dernière version principale de l'application de l'utilisateur n'existe pas, il correspond automatiquement au filtre.<br><br>Il peut falloir un certain temps pour que les versions actuelles de l'application soient renseignées. La version de l'application sur le profil utilisateur est mise à jour lorsque l'information est capturée par le SDK, ce qui dépend du moment où les utilisateurs ouvrent leurs applications. Si l'utilisateur n'ouvre pas l'application, la version actuelle ne sera pas mise à jour. Ces filtres ne s'appliquent pas non plus rétroactivement. Il est recommandé d'utiliser « supérieur à » ou « égal à » pour les versions actuelles et futures, mais l'utilisation de filtres sur des versions passées peut entraîner des comportements inattendus."
    tags:
      - App
  - name: Uninstalled
    description: "Segmente vos utilisateurs selon qu'ils sont actuellement marqués comme ayant désinstallé l'application en back-end. Les utilisateurs qui ont désinstallé puis réinstallé l'application ne sont pas inclus. Ce filtre reflète l'état de désinstallation actuel, et non un historique de chaque événement de désinstallation. La période de rétrospection maximale est de 100 ans."
    tags:
      - Uninstall
  - name: Device Carrier
    description: "Segmente vos utilisateurs par leur opérateur d'appareil."
    tags:
      - Devices
  - name: Device Count
    description: "Segmente vos utilisateurs par le nombre d'appareils sur lesquels ils ont utilisé votre application."
    tags:
      - Devices
  - name: Device Model
    description: "Segmente vos utilisateurs par la version du modèle de leur téléphone mobile."
    tags:
      - Devices
  - name: Device OS
    description: "Segmente vos utilisateurs qui possèdent un ou plusieurs appareils avec le système d'exploitation spécifié. Pour segmenter les utilisateurs par une plage de systèmes d'exploitation, utilisez le filtre <a href=\"/docs/user_guide/audience/segments/segmentation_filters#device-os-version-number\">Numéro de version du système d'exploitation de l'appareil</a>."
    tags:
      - Devices
  - name: Device OS Version Number
    description: "Segmente vos utilisateurs qui possèdent un ou plusieurs appareils avec une version de système d'exploitation dans une plage spécifiée. Par exemple, vous pouvez cibler les utilisateurs qui ont un système d'exploitation iOS dont la version est supérieure ou égale à 26.0."
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: "Segmente vos utilisateurs par les <a href=\"/docs/user_guide/messaging/messaging_fundamentals/localization\">informations de paramètres régionaux</a> de l'appareil le plus récemment utilisé."
    tags:
      - Devices
  - name: Most Recent Watch Model
    description: "Segmente vos utilisateurs par leur modèle de montre connectée le plus récent."
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    description: "Vous permet de trouver les utilisateurs qui sont provisoirement autorisés sur iOS 12 pour une application donnée."
    tags:
      - Devices
  - name: Web Browser
    description: "Segmente vos utilisateurs par le navigateur web qu'ils utilisent pour accéder à votre site web. Ce filtre correspond à n'importe quel navigateur dans l'historique des appareils de l'utilisateur, pas uniquement au navigateur le plus récemment utilisé."
    tags:
      - Devices
  - name: Device IDFA
    description: "Vous permet de désigner les destinataires de votre campagne par IDFA à des fins de test."
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: "Vous permet de désigner les destinataires de votre campagne par IDFV à des fins de test."
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: "Segmente vos utilisateurs par l'identifiant publicitaire Google."
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: "Segmente vos utilisateurs par l'identifiant publicitaire Roku."
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: "Segmente vos utilisateurs par l'identifiant publicitaire Windows."
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    description: "Vous permet de filtrer selon que vos utilisateurs ont opté pour le suivi publicitaire. Le suivi publicitaire est lié à l'IDFA ou « identifiant pour les annonceurs » attribué à tous les appareils iOS par Apple, qui peut être défini par les SDK. Cet identifiant permet aux annonceurs de suivre les utilisateurs et de leur diffuser des publicités ciblées."
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: "Segmente vos utilisateurs par le dernier emplacement enregistré où ils ont utilisé votre application."
    tags:
      - Location
  - name: Location Available
    description: "Segmente vos utilisateurs selon qu'ils ont signalé leur emplacement. Pour utiliser ce filtre, votre application doit avoir le <a href=\"/docs/search?query=location%20tracking\">suivi de localisation intégré.</a>"
    tags:
      - Location
  - name: Amplitude Cohorts
    description: "Les clients qui utilisent Amplitude peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Amplitude."
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: "Les clients qui utilisent Census peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Census."
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: "Les clients qui utilisent Heap peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Heap."
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: "Les clients qui utilisent Hightouch peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Hightouch."
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: "Les clients qui utilisent Kubit peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Kubit."
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: "Les clients qui utilisent Mixpanel peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Mixpanel."
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: "Les clients qui utilisent Segment peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Segment."
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: "Les clients qui utilisent Tinyclues peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Tinyclues."
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: "Segmente vos utilisateurs par la publicité à laquelle leur installation a été attribuée."
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: "Segmente vos utilisateurs par le groupe publicitaire auquel leur installation a été attribuée."
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    description: "Segmente vos utilisateurs par la campagne publicitaire à laquelle leur installation a été attribuée."
    tags:
      - Install attribution
  - name: Install Attribution Source
    description: "Segmente vos utilisateurs par la source à laquelle leur installation a été attribuée."
    tags:
      - Install attribution
  - name: Churn Risk Category
    description: "Segmente vos utilisateurs par catégorie de risque d'attrition selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: "Segmente vos utilisateurs par score de risque d'attrition selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: "Segmente vos utilisateurs par probabilité d'effectuer un événement selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: "Segmente vos utilisateurs par score de probabilité d'effectuer un événement selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: "Segmente vos utilisateurs par leur canal le plus actif au cours des trois derniers mois."
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    description: "Filtre vos utilisateurs en fonction de leur <a href=\"/docs/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels\">probabilité d'ouvrir un message sur un canal spécifié</a> sur une échelle de 0 à 100 %. Les utilisateurs sans données suffisantes pour mesurer une probabilité pour un canal peuvent être sélectionnés en utilisant « est vide ».<br><br>Pour les e-mails, les ouvertures automatiques sont exclues du calcul de probabilité."
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: "Segmente vos utilisateurs par le nombre d'amis Facebook qu'ils ont et qui utilisent la même application."
    tags:
      - Social activity
  - name: Connected Facebook
    description: "Segmente vos utilisateurs selon qu'ils ont connecté votre application à Facebook."
    tags:
      - Social activity
  - name: Connected Twitter
    description: "Segmente vos utilisateurs selon qu'ils ont connecté votre application à X (anciennement Twitter)."
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: "Segmente vos utilisateurs par le nombre d'abonnés X (anciennement Twitter) qu'ils ont."
    tags:
      - Social activity
  - name: Phone Number
    description: "Segmente vos utilisateurs par le champ de numéro de téléphone au format E.164.<br><br> Lorsqu'un numéro de téléphone est envoyé à Braze, Braze tente de le convertir au <a href=\"/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#import-phone-numbers\">format E.164</a> utilisé pour l'envoi sur les canaux SMS, RCS et WhatsApp. Le processus de conversion peut échouer si le numéro n'est pas correctement formaté, ce qui fait que le profil utilisateur possède un numéro de téléphone non formaté mais pas de numéro de téléphone d'envoi. Ce filtre de segment renvoie les utilisateurs par leur numéro de téléphone au format E.164 (lorsqu'il est disponible).<br><br>Cas d'usage :<br> - Utilisez ce filtre pour comprendre la taille d'audience cible la plus précise lors de l'envoi de messages SMS, RCS ou WhatsApp.<br>- Utilisez les expressions régulières (regex) avec ce filtre pour segmenter par numéros de téléphone avec un indicatif de pays spécifique. <br>- Utilisez ce filtre pour segmenter les utilisateurs dont les numéros de téléphone n'ont pas réussi le processus de conversion E.164."
    tags:
      - Other Filters
---