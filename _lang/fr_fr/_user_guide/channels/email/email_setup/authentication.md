---
nav_title: Authentification des e-mails
article_title: Authentification des e-mails
page_order: 2
page_type: reference
description: "Cet article de référence traite de l'authentification des e-mails, un ensemble de techniques visant à doter vos e-mails d'informations vérifiables sur leur origine."
channel: email

---

# Authentification des e-mails

> L'authentification des e-mails est un ensemble de techniques qui dotent vos e-mails d'informations vérifiables sur leur origine.<br><br>Une authentification correcte est essentielle pour que les fournisseurs de services Internet (ISP) vous reconnaissent comme expéditeur d'e-mails légitimes et distribuent votre courrier immédiatement. Sans authentification, vos communications sont présumées frauduleuses.

{% alert note %}
Aucune coordination particulière avec Braze n'est nécessaire pour **BIMI** (Brand Indicators for Message Identification). Les enregistrements DNS et les certificats requis sont gérés de votre côté.
{% endalert %}

## Méthodes d'authentification

### Sender Policy Framework (SPF)

Cette méthode confirme que l'adresse IP d'envoi d'e-mails de Braze est autorisée à envoyer du courrier en votre nom. SPF constitue votre authentification de base et s'effectue en publiant des enregistrements texte dans les paramètres DNS. Le serveur de réception vérifie les enregistrements DNS et détermine s'ils sont authentiques. Cette méthode est conçue pour valider l'expéditeur de l'e-mail.

Braze configure votre enregistrement SPF lors de la mise en place de vos adresses IP et domaines. En dehors de l'ajout des enregistrements DNS que nous fournissons, aucune action supplémentaire n'est requise de votre part.

### Domain Keys Identified Mail (DKIM)

Cette méthode confirme que votre domaine d'envoi d'e-mails Braze est autorisé à envoyer du courrier en votre nom. Elle est conçue pour valider l'authenticité de l'expéditeur et garantir que l'intégrité du message est préservée. Elle utilise également des signatures numériques cryptographiques individuelles afin que les ISP puissent s'assurer que le courrier qu'ils distribuent est bien celui que vous avez envoyé.

Braze signe le courrier avec votre clé privée secrète. Les ISP vérifient la signature à l'aide de votre clé publique, stockée dans votre enregistrement DNS personnalisé. Aucune signature n'est exactement identique à une autre, et seule votre clé publique peut vérifier avec succès la signature de votre clé privée.

Braze configure votre enregistrement DKIM lors de la mise en place de vos adresses IP et domaines. En dehors de l'ajout des enregistrements DNS que nous fournissons, aucune action supplémentaire n'est requise de votre part.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC)

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) est un protocole d'authentification des e-mails permettant aux expéditeurs de prouver la légitimité de leur courrier, ce qui renforce la confiance des destinataires et favorise l'acceptation des messages. DMARC permet aux expéditeurs d'e-mails de spécifier comment traiter les e-mails qui n'ont pas été authentifiés via Sender Policy Framework (SPF) ou Domain Keys Identified Mail (DKIM). Pour cela, le protocole vérifie que les contrôles SPF et DKIM sont tous deux réussis.

Les expéditeurs indiquent aux fournisseurs de messagerie comment traiter le courrier qui échoue aux vérifications de signature ou d'authentification. Les échecs peuvent indiquer une usurpation d'identité. Vous pouvez demander aux fournisseurs de rejeter ou de mettre en quarantaine le courrier en échec et d'envoyer des rapports automatisés. Cela aide les fournisseurs à identifier les expéditeurs de courrier indésirable, à bloquer les e-mails malveillants, à minimiser les faux positifs et à améliorer la transparence des rapports d'authentification.

#### Fonctionnement

Pour déployer DMARC, vous devez publier un enregistrement DMARC dans votre système de noms de domaine (DNS). Il s'agit d'un enregistrement TXT qui exprime publiquement la politique de votre domaine e-mail après vérification de l'état SPF et DKIM. DMARC authentifie le message si SPF ou DKIM, ou les deux, réussissent. C'est ce qu'on appelle l'alignement DMARC.

Un enregistrement DMARC indique également aux serveurs de messagerie d'envoyer des rapports XML à l'adresse e-mail de rapport spécifiée dans l'enregistrement DMARC. Ces rapports fournissent des informations sur la façon dont vos e-mails circulent dans l'écosystème et vous permettent d'identifier tout ce qui tente d'utiliser votre domaine e-mail pour envoyer des communications par e-mail.

Définissez une politique DMARC sur le domaine racine afin qu'elle s'applique à tous les sous-domaines. Cela évite une configuration supplémentaire sur les sous-domaines actuels et futurs. Vous pouvez définir l'une des politiques suivantes :

| Politique | Impact |
| --- | --- |
| None | Indique au fournisseur de messagerie de ne prendre aucune mesure contre les messages en échec. |
| Quarantine | Indique au fournisseur de messagerie d'envoyer les messages en échec dans le dossier spam. |
| Reject | Indique au fournisseur de messagerie que les messages en échec iront dans le dossier spam et doivent être bloqués. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Comment vérifier l'authentification DMARC de votre domaine

Il existe deux options pour vérifier l'authentification DMARC de votre domaine :

- **Option 1 :** Vous pouvez saisir votre domaine parent ou sous-domaine dans n'importe quel vérificateur DMARC tiers, tel que [MXToolbox](https://mxtoolbox.com/dmarc.aspx), pour vérifier si vous avez une politique DMARC en place et à quoi elle est configurée.
    - **MXToolbox** : si vous avez défini votre DMARC au niveau du domaine racine, saisissez-le dans MXToolbox. Si vous avez défini le DMARC au niveau du sous-domaine, saisissez le sous-domaine dans MXToolbox. Sachez que MXToolbox ne « remonte ni ne descend » lors des recherches. Cela signifie que si vous définissez le DMARC au niveau du domaine racine et saisissez le sous-domaine, MXToolbox affichera un échec car il ne sait pas que le DMARC a été défini au niveau du domaine racine.
- **Option 2 :** Ouvrez un e-mail provenant de votre domaine ou sous-domaine dans votre boîte de réception, puis recherchez le message original pour vérifier si DMARC réussit l'authentification sur cet e-mail.

Par exemple, si vous utilisez Gmail, suivez ces étapes :

1. Cliquez sur **Plus** <i class="fa-solid fa-ellipsis"></i> dans un message e-mail.
2. Sélectionnez **Afficher l'original**.
3. Vérifiez que vous avez un état « PASS » pour **DMARC**.

![Un e-mail dont la valeur DMARC est « PASS ».]({% image_buster /assets/img_archive/dmarc_example.png %})