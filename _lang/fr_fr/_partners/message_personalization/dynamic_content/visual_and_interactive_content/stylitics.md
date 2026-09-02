---
nav_title: Stylitics
article_title: Stylitics
description: "Cet article de référence décrit le partenariat entre Braze et Stylitics, une plateforme SaaS basée sur le cloud qui vous permet d'améliorer vos campagnes d'e-mail existantes avec un contenu groupé engageant et pertinent, créant une expérience client personnalisée."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) est une plateforme SaaS basée sur le cloud destinée aux retailers, permettant d'automatiser et de distribuer du contenu visuel à grande échelle. Les offres groupées de Stylitics inspirent en contextualisant les produits, en renforçant la confiance dans les achats et en augmentant l'engagement, ce qui conduit à une valeur moyenne de commande et à des taux de conversion plus élevés.

_Cette intégration est maintenue par Stylitics._

## À propos de l'intégration {#about-the-integration}

Votre intégration Braze et Stylitics vous permet d'améliorer vos campagnes d'e-mail existantes avec un contenu groupé attrayant et pertinent, créant une expérience client personnalisée.

![Exemple de contenu groupé Stylitics intégré dans une expérience e-mail Braze.]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Stylitics | Un compte [Stylitics](https://stylitics.com/) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'usage {#use-cases}

La liste suivante présente quelques exemples courants de programmes d'e-mails déclenchés :
- E-mails de panier abandonné
- E-mails de navigation abandonnée
- E-mails de confirmation d'expédition
- E-mails post-achat

## Intégration {#integration}

Stylitics fournit les données de bundle pour cette intégration. Votre fournisseur de services d'e-mail marketing peut créer ou mettre à jour le modèle d'e-mail pour inclure les bundles Stylitics. Stylitics ne peut pas modifier la mise en page ou le design des e-mails.

1. Intégrez le bundle dans l'e-mail. L'fournisseur de services d'e-mailing détermine la position et la personnalisation.
2. L'fournisseur de services d'e-mailing met à jour le code de l'e-mail déclenché pour inclure le contenu Stylitics.
3. L'fournisseur de services d'e-mailing testera, prévisualisera et lancera la série déclenchée mise à jour.

Stylitics ne fournira que les données de bundle pour les articles. Entre vous et votre fournisseur de services d'e-mailing, vous disposerez des données utilisateurs et pourrez intégrer les données de bundle Stylitics pour les envoyer aux utilisateurs.

## Échange de données {#data-exchange}

Les trois approches suivantes vous permettent d'inclure des bundles Stylitics dans vos e-mails déclenchés.

### 1. Approche API (recommandée) {#1-api-approach-recommended}

Vous ou votre fournisseur de services d'e-mailing pouvez effectuer un appel API par article pour alimenter les données de bundle dans votre e-mail. Stylitics recommande d'utiliser leur API pour effectuer des appels API, car elle est prête à l'emploi immédiatement.

{% alert note %}
Si vous exécutez un test A/B géré par Stylitics, les paramètres `styliticsCID` et `styliticsoverride` doivent être ajoutés aux URL PDP des articles Stylitics sur lesquels l'utilisateur clique dans l'e-mail.
<br><br>
Par exemple, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2. Approche par fichier plat {#2-flat-file-approach}

Vous ou votre fournisseur de services d'e-mailing pouvez référencer les données de bundle d'un article dans un fichier plat pour alimenter votre e-mail avec les données de bundle. Stylitics peut aplatir les données de bundle au format CSV, TXT ou XML et vous les envoyer quotidiennement. Ils peuvent également ajuster le format du fichier selon les besoins de votre fournisseur de services d'e-mailing. Notez que la création de ce fichier prend 2 à 3 semaines.

#### Exigences : {#requirements}
- **Emplacement** : Stylitics peut déposer le fichier sur le SFTP Stylitics pour que vous puissiez le récupérer quotidiennement, ou vous pouvez leur envoyer vos identifiants SFTP pour qu'ils déposent le fichier.
- **Horaire** : Stylitics déposera le fichier chaque matin. Faites-leur savoir si vous avez besoin du fichier à une heure précise.
- **Clé de fichier** : vous et Stylitics devez vous mettre d'accord sur la chaîne de caractères des données de l'article à utiliser comme clé du fichier afin que votre fournisseur de services d'e-mailing puisse référencer les données. L'unité de gestion des stocks, `item_group_id` ou `item_number` sont couramment utilisés.

### 3. Approche par extraction de données du site web {#3-website-data-extraction-approach}

Les fournisseurs peuvent extraire le contenu Stylitics depuis l'interface de votre site et insérer les données de bundle dans les e-mails. Aucun travail supplémentaire de la part de Stylitics n'est requis.

## Bonnes pratiques pour les modèles d'e-mail {#email-template-best-practices}

Vous et votre fournisseur de services d'e-mailing créerez un modèle d'e-mail HTML pour insérer les données et bundles Stylitics. Voici quelques bonnes pratiques et recommandations :
- Afficher 2 à 4 bundles dans l'e-mail pour l'article le plus cher ou le premier article à plein tarif que l'utilisateur a acheté ou avec lequel il a interagi
- Appeler plusieurs `item_numbers` et afficher les premières réponses de bundle
- Prévoir une option de repli s'il n'y a pas de bundles disponibles pour l'article
	- Masquer la section où se trouvent les bundles Stylitics
	- Afficher les bundles pour le prochain article consulté par l'utilisateur
- Afficher les images de bundle ainsi qu'une liste de titres de produits et de vignettes pour garantir un parcours de clic clair pour l'utilisateur

{% alert note %}
Le widget JavaScript de Stylitics ne peut pas être inséré dans les e-mails, car les e-mails ne prennent pas en charge JavaScript.
{% endalert %}

## Analyses {#analytics}

Stylitics fournit les données de bundle pour ce type de programme d'e-mail. Par conséquent, nous demandons un partage de données ouvert entre vous, votre fournisseur de services d'e-mailing et Stylitics. Si possible, nous souhaitons recevoir les indicateurs suivants de votre part afin de comprendre l'impact et d'améliorer le programme :
- E-mails envoyés
- E-mails ouverts
- Vues et engagements
- Taux de clics
- Ajouts au panier
- Achats

## Prochaines étapes {#next-steps}

Contactez votre gestionnaire de compte Stylitics pour coordonner les prochaines étapes et le calendrier du programme d'e-mail. Voici quelques prochaines étapes :
- Décider quels e-mails vous souhaitez utiliser
- Connecter Stylitics avec votre fournisseur de services d'e-mailing pour discuter de l'échange de données et choisir entre l'option API ou l'option fichier plat
- Créer des maquettes avec votre fournisseur de services d'e-mailing
- S'aligner sur les analyses
- S'aligner sur le calendrier de lancement