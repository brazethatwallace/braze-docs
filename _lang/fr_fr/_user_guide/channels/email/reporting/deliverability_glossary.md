---
nav_title: Glossaire de la livrabilité des e-mails
article_title: Glossaire de la livrabilité des e-mails
layout: glossary_page
glossary_top_header: "Glossaire de la livrabilité des e-mails"
glossary_top_text: "Ce glossaire définit les termes courants relatifs à la livrabilité des e-mails et à l'infrastructure e-mail que vous pouvez rencontrer lors de l'envoi d'e-mails via Braze."
page_order: 1
page_type: glossary
description: "Ce glossaire définit les termes courants relatifs à la livrabilité des e-mails et à l'infrastructure e-mail que vous pouvez rencontrer lors de l'envoi d'e-mails via Braze."
channel:
  - email

glossaries:
  - name: Liste d'autorisation
    description: Une liste de contacts que l'utilisateur considère comme acceptables pour recevoir des e-mails et qui ne doivent pas être filtrés ni envoyés dans la corbeille ou le dossier de courrier indésirable.
  - name: Blocage
    description: Un blocage est le résultat d'un e-mail non accepté pour la distribution par le fournisseur de boîte de réception. De nombreux fournisseurs de boîtes de réception bloquent les e-mails provenant d'adresses IP ou de domaines signalés comme envoyant du spam ou des virus, ou dont le contenu enfreint les politiques de messagerie ou les filtres anti-spam. Sendgrid utilise le terme « blocage » pour désigner ce qui est généralement appelé un échec provisoire d'envoi. Chez Sendgrid, un blocage se produit lorsqu'un e-mail n'est pas accepté pour la distribution en raison d'un problème technique ou temporaire.
  - name: Liste de blocage
    description: Listes d'adresses IP signalées et répertoriées comme sources connues de spam. Il existe des listes de blocage publiques et privées. Les listes de blocage publiques sont publiées et mises à la disposition du public, souvent en tant que service gratuit, parfois moyennant des frais.
  - name: Rebond
    description: "Également connu sous le nom d'échec d'envoi définitif, une adresse ayant rebondi est définitivement non distribuable et est supprimée des envois ultérieurs. Pour plus d'informations sur les rebonds dans Braze, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#bounces\">Rebonds</a> dans le glossaire d'analyse des e-mails."
  - name: Dossier de courrier en masse
    description: Également appelé dossier de courrier indésirable ou dossier de spam dans certains clients de messagerie.
  - name: Loi CAN-SPAM
    description: "Loi américaine réglementant les e-mails commerciaux (nom complet : Controlling the Assault of Non-Solicited Pornography and Marketing Act of 2003)."
  - name: Taux de clics
    description: "Le taux auquel les destinataires ont cliqué sur un lien dans le message. Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#unique-clicks\">Clics uniques</a> dans le glossaire d'analyse des e-mails."
  - name: Filtres de contenu
    description: Filtres logiciels qui bloquent les e-mails en fonction du texte, des mots, des expressions ou des informations d'en-tête contenus dans l'e-mail lui-même.
  - name: Différé
    description: Si un message ne peut pas être distribué lors de sa première tentative, ce message est considéré comme différé. La plupart des messages différés finissent par être distribués.
  - name: Livrabilité
    description: Dans la communauté de la livrabilité, ce terme se concentre principalement sur la capacité à atteindre la boîte de réception. Ce taux n'est pas quelque chose que Braze peut suivre directement, vous devez donc utiliser d'autres données disponibles pour faire des déductions sur le placement en boîte de réception.
  - name: Taux de distribution
    description: "Le taux de distributions réussies, indépendamment du placement en boîte de réception ou de l'ouverture du message. Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#deliveries\">Distributions %</a> dans le glossaire d'analyse des e-mails."
  - name: DKIM
    description: DomainKeys Identified Mail permet à une organisation de prendre la responsabilité d'un message pendant son transit. L'organisation est un gestionnaire du message, soit en tant qu'expéditeur d'origine, soit en tant qu'intermédiaire. Sa réputation sert de base pour évaluer si le message peut être considéré comme fiable pour la distribution.
  - name: DMARC
    description: Domain-based Message Authentication, Reporting & Conformance est une spécification technique créée par des organisations pour réduire l'hameçonnage et la fraude par e-mail. Elle est actuellement utilisée par tous les principaux fournisseurs de boîtes de réception, notamment Google, Yahoo et Microsoft.
  - name: Suppression automatique
    description: Sendgrid conserve des listes d'e-mails pour suivre les rebonds, les signalements de courrier indésirable et les désabonnements pour chacun de ses utilisateurs. Si un utilisateur envoie un message à une adresse e-mail figurant sur l'une de ces listes dans son compte, Sendgrid supprime automatiquement le message (c'est-à-dire ne l'envoie pas à cette adresse).
  - name: ESP (fournisseur de services d'e-mailing)
    description: Entreprise qui fournit des capacités d'envoi et de transport d'e-mails aux marketeurs. De nombreuses plateformes actuelles de marketing, de CRM et d'engagement client incluent un composant d'envoi d'e-mails et sont communément appelées fournisseur de services d'e-mailing en référence à leur capacité d'envoi d'e-mails. Parmi les exemples, on trouve ConstantContact, MailChimp, Emarsys, Salesforce Marketing Cloud, Cheetah Digital et Sailthru.
  - name: Boucle de rétroaction (FBL)
    description: Le mécanisme par lequel les expéditeurs sont informés des signalements de courrier indésirable afin de pouvoir calculer un taux de signalement et supprimer l'adresse des envois futurs.
  - name: Échec d'envoi définitif
    description: "Message envoyé à un compte e-mail invalide, fermé ou inexistant. En général, les e-mails ayant subi un échec d'envoi définitif peuvent être identifiés par un code de réponse SMTP de la série 500. Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#hard-bounce\">Échec d'envoi définitif</a> dans le glossaire d'analyse des e-mails."
  - name: IP
    description: Un numéro unique attribué à chaque appareil connecté à Internet.
  - name: FAI (fournisseur de services Internet)
    description: Entreprise qui fournit des services Internet aux consommateurs, comme AT&T, British Telecom, Comcast (Xfinity), Cox, Orange, Sky, Spectrum, Tiscali, TalkTalk et Virgin. Inclut également de manière familière les fournisseurs de boîtes de réception comme Gmail, Yahoo et Microsoft.
  - name: Hygiène de liste
    description: La pratique consistant à maintenir une liste afin que les échecs d'envoi définitifs et les noms désabonnés soient retirés des envois.
  - name: List-Unsubscribe
    description: L'en-tête List-Unsubscribe est un texte que vous pouvez inclure dans la partie en-tête de vos messages, permettant aux destinataires de voir un bouton de désabonnement qu'ils peuvent sélectionner pour arrêter automatiquement les messages futurs.
  - name: Fournisseur de boîte de réception (MBP)
    description: Le fournisseur d'accès à la messagerie pour les destinataires, comme Gmail, Yahoo et Microsoft.
  - name: Enregistrement MX
    description: Un enregistrement MX est un type d'enregistrement de ressource dans le système de noms de domaine (DNS) spécifiant comment les e-mails Internet doivent être acheminés à l'aide du protocole SMTP (Simple Mail Transfer Protocol).
  - name: NDR (rapport de non-distribution)
    description: Retour d'information d'un récepteur d'e-mail lorsqu'il choisit de ne pas accepter un e-mail pour la distribution, sous la forme d'une réponse SMTP. Les NDR sont souvent appelés rebonds.
  - name: Taux d'ouvertures uniques
    description: "Le taux auquel le pixel de suivi d'ouverture a été chargé, en ne comptant que les destinataires uniques (sans doublons). Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#unique-opens\">Ouvertures uniques</a> dans le glossaire d'analyse des e-mails."
  - name: Hameçonnage
    description: Une forme d'usurpation d'identité dans laquelle un escroc utilise un e-mail d'apparence authentique pour inciter les destinataires à divulguer des informations personnelles sensibles, telles que des numéros de carte de crédit ou de compte bancaire, des numéros de sécurité sociale et d'autres données d'identification.
  - name: Campagne de réengagement
    description: "Une campagne d'e-mail envoyée aux utilisateurs inactifs ou non répondants dans le but de les reconquérir et de les réengager avec vos e-mails sous forme d'ouvertures, de clics et de conversions. Une campagne de réengagement peut être envoyée aux inactifs en tant que campagne autonome ou sous forme de série de campagnes."
  - name: DNS inversé (rDNS)
    description: Le processus par lequel une adresse IP est correctement associée à un nom de domaine, au lieu qu'un nom de domaine soit associé à une adresse IP. Si un filtre anti-spam ou un programme ne peut pas associer l'adresse IP au nom de domaine, il peut rejeter l'e-mail.
  - name: Smart Network Data Services (SNDS)
    description: Proposé par Windows en direct Hotmail, SNDS fournit des données aux expéditeurs basées sur les e-mails réellement envoyés aux abonnés Hotmail. Les indicateurs rapportés incluent les plaintes, les résultats du filtre SmartScreen et les détections de pièges à spam.
  - name: Échec provisoire d'envoi
    description: "Tout rebond dû à un problème temporaire ou transitoire comme « boîte de réception pleine », « quota utilisateur dépassé », « e-mail bloqué pour caractéristiques similaires au spam », « message rejeté car il enfreint les politiques de l'organisation » ou « serveur temporairement indisponible ». Sendgrid appelle ces cas des « blocages ».<br><br>La distribution vers tout échec provisoire d'envoi considéré comme un problème temporaire (généralement ceux avec un code SMTP 4xx) est retentée jusqu'à ce que le message soit distribué ou que 72 heures se soient écoulées. Si un message ayant subi un échec provisoire d'envoi ne peut pas être distribué après 72 heures, les tentatives de distribution supplémentaires sont arrêtées et l'échec de distribution du message est comptabilisé comme un rebond. Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#soft-bounce\">Échec provisoire d'envoi</a> dans le glossaire d'analyse des e-mails."
  - name: Spam
    description: "E-mail indésirable. Dans les indicateurs, les utilisateurs doivent marquer ces e-mails comme spam (ce décompte les inclut donc dans les distributions car l'e-mail doit d'abord être distribué). Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#spam\">Spam</a> dans le glossaire d'analyse des e-mails."
  - name: SpamCop
    description: Une liste de blocage et une base de données d'adresses IP, autrefois privée mais désormais intégrée au fournisseur de messagerie Ironport. De nombreux fournisseurs de boîtes de réception vérifient les adresses IP des e-mails entrants par rapport aux enregistrements de SpamCop pour déterminer si l'adresse a été mise sur liste de blocage en raison de plaintes pour spam.
  - name: Taux de spam
    description: "Le taux auquel les destinataires ont marqué un message comme étant du spam lors de sa consultation. Ce taux n'inclut pas les e-mails qui atterrissent dans le dossier de spam. Il n'inclut pas non plus les plaintes des fournisseurs de boîtes de réception qui ne disposent pas de boucle de rétroaction, comme Gmail et iCloud. Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#spam\">Spam</a> dans le glossaire d'analyse des e-mails."
  - name: Piège à spam
    description: "Un e-mail utilisé pour collecter et détecter le spam par les fournisseurs de services Internet et les organisations anti-spam. Également connu sous le nom de spamtrap. Pour plus d'informations, consultez <a href=\"/docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps\">Pièges de livrabilité et pièges à spam</a>."
  - name: Liste de suppression
    description: "Braze ne dispose pas de listes de suppression, cependant, vous pouvez créer une politique de désactivation progressive comme documenté dans <a href=\"/docs/user_guide/channels/email/best_practices/sunset_policies\">Politiques de désactivation progressive</a>. Pour plus d'informations sur la gestion des abonnements e-mail, consultez <a href=\"/docs/user_guide/channels/email/subscriptions\">Abonnements</a>."
  - name: Limitation de débit
    description: La pratique consistant à réguler le nombre de messages e-mail qu'un diffuseur envoie à un fournisseur de boîte de réception ou à un serveur de messagerie à la fois. Certains fournisseurs de boîtes de réception rejettent les e-mails s'ils en reçoivent trop.
  - name: E-mail transactionnel
    description: "Les messages transactionnels sont définis par la loi CAN-SPAM comme tout e-mail « facilitant, complétant ou confirmant une transaction préalablement convenue ». Contrairement aux messages commerciaux, les messages transactionnels ne sont pas tenus d'inclure une adresse postale américaine ni un lien de désabonnement."

---