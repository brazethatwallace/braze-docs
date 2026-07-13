---
nav_title: Authentification par e-mail
article_title: Authentification par e-mail
page_order: 2
page_type: reference
description: "Cet article de référence couvre l'authentification par e-mail, un ensemble de techniques visant à équiper vos e-mails d'informations vérifiables sur leur origine."
channel: email

---

# Authentification par e-mail {#email-authentication}

> L'authentification par e-mail est un ensemble de techniques visant à équiper vos e-mails d'informations vérifiables sur leur origine.<br><br>Une authentification correcte est primordiale pour que les fournisseurs de services Internet (ISP) reconnaissent votre qualité d'expéditeur d'e-mails légitimes et les distribuent immédiatement. Sans authentification, vos communications sont présumées frauduleuses.

{% alert note %}
Aucune coordination particulière avec Braze n'est nécessaire pour **BIMI** (Brand Indicators for Message Identification). Les enregistrements DNS et les certificats requis sont gérés de votre côté.
{% endalert %}

## Méthodes d'authentification {#methods-of-authentication}

### Sender Policy Framework (SPF) {#spf}

Cette méthode confirme que votre adresse IP d'envoi d'e-mail Braze est autorisée à envoyer du courrier en votre nom. SPF est votre authentification de base et est réalisée en publiant les enregistrements de texte dans les paramètres DNS. Le serveur de réception vérifie les enregistrements DNS et détermine s'ils sont authentiques ou non. Cette méthode est conçue pour valider l'expéditeur de l'e-mail.

Braze configure votre enregistrement SPF lorsque nous configurons vos adresses IP et vos domaines. En dehors de l'ajout des enregistrements DNS que nous fournissons, aucune autre action n'est requise de votre part.

### Domain Keys Identified Mail (DKIM) {#dkim}

Cette méthode confirme que votre domaine d'envoi d'e-mail Braze est autorisé à envoyer du courrier en votre nom. Cette méthode permet de valider l'authenticité de l'expéditeur et de s'assurer que l'intégrité du message est préservée. Elle utilise également des signatures numériques cryptographiques individuelles afin que les fournisseurs de services Internet puissent s'assurer que le courrier qu'ils distribuent est bien celui que vous avez envoyé.

Braze signe le courrier avec votre clé privée secrète. Les fournisseurs de services Internet vérifient la signature à l'aide de votre clé publique, stockée dans votre enregistrement DNS personnalisé. Aucune signature n'est exactement identique à une autre, et seule votre clé publique peut vérifier avec succès la signature de votre clé privée.

Braze configure votre enregistrement DKIM lorsque nous configurons vos adresses IP et vos domaines. En dehors de l'ajout des enregistrements DNS que nous fournissons, aucune autre action n'est requise de votre part.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC) {#dmarc}

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) est un protocole d'authentification des e-mails permettant aux expéditeurs de prouver la légitimité de leur courrier, ce qui renforce la confiance des destinataires et favorise l'acceptation des messages. DMARC permet aux expéditeurs d'e-mails de spécifier comment traiter les e-mails qui n'ont pas été authentifiés via Sender Policy Framework (SPF) ou Domain Keys Identified Mail (DKIM). Pour cela, le protocole vérifie que les contrôles SPF et DKIM sont tous deux réussis.

Les expéditeurs indiquent aux fournisseurs de messagerie comment traiter le courrier qui échoue aux vérifications de signature ou d'authentification. Les échecs peuvent indiquer une usurpation d'identité. Vous pouvez demander aux fournisseurs de rejeter ou de mettre en quarantaine le courrier en échec et d'envoyer des rapports automatisés. Cela aide les fournisseurs à identifier les expéditeurs de courrier indésirable, à bloquer les e-mails malveillants, à minimiser les faux positifs et à améliorer la transparence des rapports d'authentification.

#### Fonctionnement {#how-it-works}

Pour déployer DMARC, vous devez publier un enregistrement DMARC dans votre système de noms de domaine (DNS). Il s'agit d'un enregistrement TXT qui exprime publiquement la politique de votre domaine e-mail après vérification de l'état SPF et DKIM. DMARC authentifie le message si SPF ou DKIM, ou les deux, réussissent. C'est ce qu'on appelle l'alignement DMARC.

Un enregistrement DMARC indique également aux serveurs de messagerie d'envoyer des rapports XML à l'adresse e-mail de rapport spécifiée dans l'enregistrement DMARC. Ces rapports fournissent des informations sur la façon dont vos e-mails circulent dans l'écosystème et vous permettent d'identifier tout ce qui tente d'utiliser votre domaine e-mail pour envoyer des communications par e-mail.

Définissez une politique DMARC sur le domaine racine afin qu'elle s'applique à tous les sous-domaines. Cela évite une configuration supplémentaire sur les sous-domaines actuels et futurs. Vous pouvez définir l'une des politiques suivantes :

| Politique | Impact |
| --- | --- |
| None | Indique au fournisseur de messagerie de ne prendre aucune mesure contre les messages en échec. |
| Quarantine | Indique au fournisseur de messagerie d'envoyer les messages en échec dans le dossier spam. |
| Reject | Indique au fournisseur de messagerie que les messages en échec iront dans le dossier spam et doivent être bloqués. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnement" }

#### Comment vérifier l'authentification DMARC de votre domaine {#how-to-check-your-domains-dmarc-authentication}

Il existe deux options pour vérifier l'authentification DMARC de votre domaine :

- **Option 1 :** Vous pouvez saisir votre domaine parent ou sous-domaine dans n'importe quel vérificateur DMARC tiers, tel que [MXToolbox](https://mxtoolbox.com/dmarc.aspx), pour vérifier si vous avez une politique DMARC en place et à quoi elle est configurée.
    - **MXToolbox** : si vous avez défini votre DMARC au niveau du domaine racine, saisissez-le dans MXToolbox. Si vous avez défini le DMARC au niveau du sous-domaine, saisissez le sous-domaine dans MXToolbox. Sachez que MXToolbox ne « remonte ni ne descend » lors des recherches. Cela signifie que si vous définissez le DMARC au niveau du domaine racine et saisissez le sous-domaine, MXToolbox affichera un échec car il ne sait pas que le DMARC a été défini au niveau du domaine racine.
- **Option 2 :** Ouvrez un e-mail provenant de votre domaine ou sous-domaine dans votre boîte de réception, puis recherchez le message original pour vérifier si DMARC réussit l'authentification sur cet e-mail.

Les étapes varient selon le client de messagerie :

{% tabs %}
{% tab Gmail %}

1. Sélectionnez **Plus** <i class="fa-solid fa-ellipsis"></i> dans un message e-mail.
2. Sélectionnez **Afficher l'original**.
3. Vérifiez que vous avez un état « PASS » pour **DMARC**.

![Un e-mail dont la valeur DMARC est « PASS ».]({% image_buster /assets/img_archive/dmarc_example.png %})

{% endtab %}
{% tab Outlook %}

1. Ouvrez l'e-mail.
2. Sélectionnez la flèche à côté de **Répondre**.
3. Sélectionnez **Afficher la source du message**.
4. Vérifiez que vous avez un état « PASS » pour **DMARC**.

{% endtab %}
{% tab Apple Mail %}

1. Ouvrez l'e-mail.
2. Sélectionnez **Présentation** dans la barre de menus.
3. Sélectionnez **Message** > **Source brute**.
4. Vérifiez que vous avez un état « PASS » pour **DMARC**.

{% endtab %}
{% endtabs %}

#### Résoudre les échecs DMARC {#troubleshoot-dmarc-failures}

Si DMARC affiche **FAIL** pour les messages envoyés via Braze :

1. Ouvrez les en-têtes bruts ou les résultats d'authentification d'un message récent et vérifiez si **SPF** et **DKIM** réussissent ou échouent.
2. **Alignement :** DMARC réussit lorsque *soit* SPF, *soit* DKIM est aligné avec le domaine **From**. L'alignement signifie que le domaine **From** correspond au domaine ayant réussi SPF (souvent le domaine **Return-Path** / enveloppe) *ou* au domaine figurant dans la signature DKIM **d=**.
3. Si SPF réussit mais que DMARC échoue, le domaine Return-Path peut ne pas être aligné avec votre domaine **From** — vérifiez que vos [domaines d'envoi et de suivi en marque blanche]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains) correspondent aux domaines pour lesquels vous publiez SPF et DKIM.
4. Si DKIM échoue, vérifiez que les enregistrements DNS DKIM fournis par Braze sont présents et inchangés.

Les vérificateurs tiers (par exemple, [MXToolbox](https://mxtoolbox.com/dmarc.aspx)) permettent de confirmer les enregistrements publiés ; validez toujours également avec un message réel envoyé depuis Braze.