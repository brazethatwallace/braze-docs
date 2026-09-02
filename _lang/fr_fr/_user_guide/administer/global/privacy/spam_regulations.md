---
nav_title: Réglementations relatives aux courriers indésirables
article_title: Réglementations relatives aux courriers indésirables
page_order: 0
page_type: reference
description: "Le présent article fournit des résumés et des ressources sur diverses réglementations des spams susceptibles de vous concerner, vous ou vos utilisateurs."
channel:
- email
- push
- SMS

---

# Réglementations relatives aux courriers indésirables {#spam-regulations}

> Il existe un certain nombre de lois qui réglementent les expéditeurs de communications électroniques, y compris les e-mails, les notifications push et les SMS. Vous devez toujours être au courant des [réglementations locales](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country) qui peuvent vous concerner ou concerner vos utilisateurs.

Braze fournit des informations pertinentes sur la base de ses propres recherches, mais vous devez également consulter le texte intégral de ces lois pour obtenir des détails complets et actualisés.

- [CAN-SPAM](#can-spam)
- [Loi canadienne anti-spam](#casl)

## CAN-SPAM {#can-spam}

La loi CAN-SPAM de 2003 réglemente les expéditeurs d'e-mails aux États-Unis envoyant « tout message électronique dont l'objet principal est la publicité commerciale ou la promotion d'un produit ou d'un service commercial ». Pour plus d'informations, consultez le site officiel de la [Federal Trade Commission](http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business).

Il existe sept exigences clés pour CAN-SPAM :

1. N'utilisez pas d'informations d'en-tête fausses ou trompeuses (telles que « From », « To » et « Reply-To »)
2. N'utilisez pas de lignes d'objet trompeuses
3. Identifiez le message en tant que publicité
4. Indiquez aux destinataires votre emplacement (adresse physique par exemple)
5. Indiquez aux destinataires comment se désabonner de vos futurs e-mails
6. Honorez rapidement les demandes de désabonnement
7. Surveillez ce que d'autres font en votre nom

Les e-mails transactionnels sont exemptés de ces règles, à l'exception de la règle n° 1.

## Loi canadienne anti-spam (CASL) {#casl}

Le 1er juillet 2014, la loi canadienne anti-spam (CASL) est entrée en vigueur pour les e-mails envoyés aux résidents canadiens. Vous pouvez lire le texte intégral de la loi sur le site [Lois du ministère de la Justice](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) du gouvernement du Canada. La loi stipule essentiellement que les destinataires canadiens d'e-mails et de notifications push doivent fournir un consentement « exprès ou tacite » pour que vous puissiez communiquer avec eux.

### CASL versus CAN-SPAM {#casl-versus-can-spam}

Il existe quelques différences clés entre la CASL et la CAN-SPAM, notamment :

- La CASL s'applique en fonction du lieu de réception du message, ce qui signifie que les expéditeurs situés en dehors du Canada sont également concernés
- Les destinataires des messages doivent donner leur consentement explicite (opt-in), au lieu de simplement pouvoir se désabonner (opt-out)

### Responsabilité {#liability}

Bien que la CASL prévoie une période de transition de trois ans, se terminant le 1er juillet 2017, le Conseil de la radiodiffusion et des télécommunications canadiennes (CRTC), le Bureau de la concurrence et le Commissariat à la protection de la vie privée du Canada peuvent engager des enquêtes et des poursuites pendant cette période. À la fin de la période de transition, les particuliers peuvent également intenter des poursuites contre les entités qu'ils soupçonnent d'envoyer des courriers indésirables.

### Messages exemptés {#exempt-messages}

Les types de messages suivants sont exemptés des exigences de la CASL :

- Les messages ouverts en dehors du Canada
- Les messages adressés à des membres de la famille ou à d'autres relations personnelles
- Les messages adressés à des personnes associées à votre entreprise, y compris les employé or salariés ou les sous-traitants
- Les messages fournissant des informations de garantie, des informations de rappel de produit ou des informations de sécurité concernant un produit ou un service que le destinataire a utilisé ou acheté
- Les messages fournissant une notification d'informations factuelles concernant un abonnement, une adhésion ou un compte
- Les messages livrant un produit ou un service, y compris les mises à jour ou les mises à niveau de produit

{% alert note %}
Ceci n'est pas la liste complète des exemptions. Consultez le [texte intégral de la loi](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) pour plus de détails.
{% endalert %}

### Consentement aux messages {#message-consent}

Braze exige un consentement explicite pour tous les e-mails et messages SMS/MMS.

#### Consentement tacite {#implied-consent}

Le consentement tacite peut être légalement autorisé dans certaines juridictions, mais il n'est pas suffisant pour envoyer des e-mails via Braze. Notre politique d'utilisation acceptable va au-delà des exigences légales.

#### Consentement exprès {#express-consent}

Le consentement exprès est une confirmation écrite ou orale du destinataire du message et n'est valide que si le message comprend une description claire et simple :

- De la raison pour laquelle le consentement est demandé
- De la personne ou de l'organisation qui demande le consentement

## Filtres anti-spam {#spam-filters}

Le fait que vos e-mails aient été envoyés avec succès ne signifie pas nécessairement qu'ils ont été vus. Il n'existe pas de solution miracle pour éviter tous les filtres anti-spam, car chaque filtre est unique dans sa manière d'évaluer le « score de spam » d'un e-mail. Voici cependant quelques conseils pour éviter que vos e-mails soient classés comme « spam ».

### Obtenez la permission {#get-permission}

Un processus de double opt-in consiste à envoyer un e-mail de suivi avec un lien de confirmation après un premier opt-in. Cela permet de valider que les destinataires souhaitent bien recevoir votre contenu. Vous pouvez même aller plus loin en demandant aux utilisateurs de vous ajouter à leur carnet d'adresses. Veillez également à développer vos listes d'e-mails de manière organique&#8212;les listes achetées ont tendance à être obsolètes !


### Construisez votre réputation {#build-your-reputation}

Assurez-vous de définir les attentes lorsque les utilisateurs s'inscrivent pour recevoir vos e-mails. Soyez explicite sur ce que vous enverrez et à quelle fréquence. Ensuite, encouragez les utilisateurs à interagir avec vos campagnes par e-mail en leur proposant du contenu de qualité. Un contenu personnalisé et pertinent réduit la probabilité que vos destinataires marquent les messages comme spam.

### Maintenez votre réputation {#maintain-your-reputation}

Restez en contact régulier avec vos utilisateurs pour éviter que vos listes d'e-mails ne deviennent obsolètes. Attendre trop longtemps avant d'envoyer un message peut amener le destinataire à vous oublier et à vous signaler comme spam. Maintenez vos listes d'e-mails à jour en mettant en place une politique de suppression progressive pour retirer les adresses e-mail qui génèrent des rebonds. Les taux de rebond sont un facteur clé utilisé par les ISP pour évaluer la réputation d'un expéditeur.

### Vérifiez et testez {#check-and-test}

Assurez-vous que votre message ne contient rien qui puisse déclencher les filtres anti-spam. Cela inclut les balises superflues provenant d'éditeurs de texte externes comme Microsoft Word, le formatage de texte anormal, l'utilisation excessive de points d'exclamation (!) et de points d'interrogation (?) comme ponctuation, l'écriture en MAJUSCULES et les mots déclencheurs de spam. Envoyez des e-mails avec des contenus variés en utilisant les fonctionnalités de test multivarié pour vous assurer que vos e-mails ne finissent pas dans les spams.

## Canal de communication {#messaging-channel}

### E-mail {#spam-email}

La qualité de votre liste d'e-mails est particulièrement importante. Une poignée de mauvaises adresses e-mail dans votre liste peut ruiner la distribution pour un million d'utilisateurs valides. Collecter une liste de mauvaises adresses e-mail génère des rebonds, des mises en liste de blocage, des pièges à spam et fait chuter vos taux de réponse. Supprimer les e-mails sans activité de manière régulière et retirer les rebonds évidents constituent la première étape. Que vous mettiez en place un opt-in (cocher la case), un opt-out (décocher la case), un opt-in de confirmation (un e-mail qui remercie pour l'inscription et fournit un lien de désabonnement) ou un double opt-in (un e-mail qui nécessite un clic pour confirmer), ce qui compte avant tout, c'est la qualité de la liste.

### iOS {#spam-ios-windows}

Sur iOS, vos utilisateurs ont toujours été invités à donner leur consentement pour les notifications push. La boîte de dialogue iOS apparaît simplement à l'ouverture de l'application et demande à l'utilisateur d'accepter les notifications pour votre application. L'utilisateur voit le même message pop-up dès qu'il ouvre l'application pour la première fois, de sorte que tous les utilisateurs figurant sur votre liste iOS pour les notifications push ont, par définition, donné leur consentement.

### Android {#spam-android}

Sur Android, vos utilisateurs peuvent être considérés comme ayant donné leur consentement par le biais du consentement tacite mentionné dans votre politique de confidentialité ou votre contrat de licence utilisateur final. Vous pouvez envisager de mettre en place un processus de consentement exprès, par exemple sur un écran initial dès que l'utilisateur lance l'application pour la première fois. Consultez l'article sur les [bonnes pratiques pour les notifications push]({{site.baseurl}}/user_guide/channels/push/best_practices) pour plus de détails. Vous pouvez également informer l'utilisateur des types de notifications push qu'il recevra, augmentant ainsi le taux d'opt-in.