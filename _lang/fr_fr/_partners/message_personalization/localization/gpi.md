---
nav_title: GPI
article_title: Globalization Partners International
date_published: "2026-09-09"
description: "Cet article de référence présente le partenariat entre Braze et Globalization Partners International (GPI), un fournisseur de services de traduction. Le connecteur GPI Translation Services extrait le contenu de Braze pour traduction et réimporte les traductions terminées via l'API Translation de Braze."
alias: /partners/gpi/
page_type: partner
search_tag: Partner
---

# Globalization Partners International

> [Globalization Partners International](https://www.globalizationpartners.com/) (GPI) fournit le connecteur GPI Translation Services pour Braze. Ce connecteur extrait le contenu des Campaigns, Canvas, modèles d'e-mail et Content Blocks pour traduction, puis réimporte les traductions terminées dans Braze via l'API Translation. GPI prend en charge la traduction humaine, la traduction par IA et la traduction par IA avec post-édition par des experts, dans plus de 200 langues.

_Cette intégration est maintenue par Globalization Partners International._

## À propos de l'intégration {#about-the-integration}

Le connecteur GPI Translation Services s'intègre au modèle multilingue natif de Braze et à l'API Translation. Vous extrayez le contenu traduisible depuis le portail de traduction GPI, l'envoyez à GPI pour traduction, puis réimportez les traductions terminées dans Braze sans copier-coller manuellement. GPI préserve les balises Liquid et la personnalisation tout au long du processus.

## Cas d'usage {#use-cases}

### Lancement de campagne internationale {#global-campaign-launch}

Sélectionnez des Campaigns, Canvas ou modèles d'e-mail dans Braze, définissez les langues source et cible, puis soumettez le contenu à GPI pour une traduction humaine professionnelle. GPI gère la localisation et l'assurance qualité via des aperçus de brouillon avant le lancement.

### Localisation urgente ou à volume élevé {#time-sensitive-or-high-volume-localization}

Envoyez des ventes flash, des messages de cycle de vie urgents ou de grands lots de Content Blocks via le connecteur pour recevoir les traductions réimportées automatiquement dans Braze. Le délai de livraison dépend du flux de travail choisi et peut varier de quelques semaines à quelques minutes.

### Prise en charge de l'internationalisation {#internationalization-support}

GPI fournit des conseils sur le formatage et les bonnes pratiques pour la localisation dans Braze, y compris pour les langues s'écrivant de droite à gauche (RTL) comme l'arabe, l'hébreu et le persan.

### Localisation continue à grande échelle {#ongoing-localization-at-scale}

GPI utilise la mémoire de traduction pour réutiliser les traductions précédentes, garantir la cohérence terminologique et stylistique, et réduire les coûts sur les correspondances exactes, répétées et approximatives. Mettez à jour vos Campaigns en langue source dans Braze et envoyez le contenu révisé à GPI pour actualiser les traductions correspondantes.

## Prérequis {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Prérequis | Description |
| --- | --- |
| Un compte Globalization Partners International | Un compte GPI est nécessaire pour utiliser cette intégration. |
| Une clé API REST Braze | Une clé API REST Braze avec les autorisations suivantes :<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br>- `content_blocks.list`<br>- `content_blocks.info`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.list`<br>- `templates.email.info`<br>- `templates.email.translations.get`<br>- `templates.email.translations.update`<br><br>Créez cette clé dans le tableau de bord de Braze depuis **Paramètres** > **API et identifiants** > **Clés API**. Pour en savoir plus, consultez [Création de clés API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Un endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
| Paramètres multilingues Braze | Les locales cibles doivent être configurées dans Braze sous **Paramètres** > **Paramètres de localisation**. Pour en savoir plus, consultez [Paramètres multilingues]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Créer une clé API REST Braze {#step-1-create-a-braze-rest-api-key}

1. Dans Braze, accédez à **Paramètres** > **API et identifiants** > **Clés API**.
2. Créez une clé API REST avec les autorisations listées dans [Prérequis](#prerequisites).
3. Copiez la clé API et notez l'endpoint REST de votre instance.

### Étape 2 : Envoyer les paramètres à GPI {#step-2-send-settings-to-gpi}

1. Transmettez votre clé API et votre endpoint REST à votre gestionnaire de compte GPI.
2. Envoyez la liste des utilisateurs devant accéder au connecteur afin que GPI puisse l'activer pour eux.
3. GPI configure le connecteur avec vos identifiants et valide la connexion.

### Étape 3 : Configurer les paramètres de localisation dans Braze {#step-3-configure-localization-settings-in-braze}

1. Dans Braze, accédez à **Paramètres** > **Paramètres de localisation** et confirmez que vos locales cibles sont activées.
2. Vérifiez que le contenu envoyé pour traduction dispose des locales requises activées. Le contenu sans locales activées ne peut pas recevoir de traductions importées.
3. Ajoutez des [balises Liquid de traduction]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) autour du contenu à traduire.
4. Pour les langues RTL, ajoutez des balises Liquid pour gérer la direction du contenu en fonction de la langue. Évitez les directives de style d'alignement, sauf si vous confirmez qu'elles n'affectent pas le rendu RTL.

## Utiliser GPI avec Braze {#use-gpi-with-braze}

Seul le contenu en brouillon ou en état de brouillon post-lancement peut être traduit dans Braze.

### Étape 1 : Exporter le contenu à traduire {#step-1-export-content-for-translation}

1. Dans le [portail de traduction GPI](https://www.translationportal.com), ouvrez le connecteur **Braze** et sélectionnez **New Request**.
2. Complétez l'onglet **Information**, puis ouvrez l'onglet **Content**. Depuis **Categories**, sélectionnez **Campaign**, **Canvas**, **Email Template** ou **Content Block**, puis choisissez les éléments à exporter.
3. Sélectionnez **Submit** pour envoyer une demande de devis à GPI. Votre gestionnaire de compte GPI vous contactera lorsque le devis sera prêt pour examen et approbation.

### Étape 2 : Importer les traductions dans Braze {#step-2-import-translations-into-braze}

1. Dans le connecteur **Braze**, localisez le projet que vous souhaitez importer.
2. Sélectionnez l'icône **Import** dans la colonne **Actions**.
3. Attendez le message de confirmation d'importation. Vérifiez le statut de la tâche d'importation sur la page **Jobs**.

### Étape 3 : Vérifier le statut de la demande de traduction {#step-3-check-translation-request-status}

1. Accédez au [portail de traduction GPI](https://www.translationportal.com).
2. Sélectionnez **Sign In** et saisissez vos identifiants.
3. Dans la navigation du portail de traduction GPI, sélectionnez **Braze** pour ouvrir le tableau de bord du connecteur. Consultez les tableaux **Quotes** et **Projects** pour connaître le statut des demandes et des projets.

### Étape 4 : Prévisualiser les traductions dans Braze {#step-4-preview-translations-in-braze}

Après avoir importé les traductions, prévisualisez-les dans Braze :

1. Ouvrez l'écran **Modifier** pour la campagne ou le message que vous avez traduit.
2. Dans le **compositeur de messages**, accédez à l'onglet **Aperçu et test** ou **Test**.
3. Sous **Prévisualiser le message en tant qu'utilisateur**, sélectionnez **Utilisateur multilingue**, puis choisissez la locale que vous souhaitez consulter.
4. Confirmez l'aperçu dans la langue cible. Pour partager avec des réviseurs externes, générez un lien d'aperçu.

## Remarques {#considerations}

- Le connecteur GPI Translation Services pour Braze est distribué gratuitement.

## Résolution des problèmes {#troubleshooting}

Pour obtenir de l'aide concernant le connecteur GPI Translation Services pour Braze ou tout projet de traduction GPI, contactez votre chef de projet GPI, appelez le +1-866-272-5874 ou envoyez un e-mail à [support@globalizationpartners.com](mailto:support@globalizationpartners.com).