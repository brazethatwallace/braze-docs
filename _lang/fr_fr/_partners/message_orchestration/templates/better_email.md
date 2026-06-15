---
nav_title: Better Email
article_title: Better Email
alias: /partners/better_email/
description: "Cet article de référence décrit le partenariat entre Braze et Better Email, une plateforme collaborative de création d'e-mails construite autour d'un Email Design System qui vous permet d'exporter des modèles prêts à l'emploi vers Braze."
page_type: partner
search_tag: Partner
---

# Better Email

> [Better Email](https://www.betteremail.dev) est une plateforme collaborative de création d'e-mails construite autour d'un Email Design System. Les équipes peuvent concevoir, gérer et exporter des e-mails prêts à l'emploi à partir d'un système partagé de blocs et de styles, garantissant la cohérence de la marque à grande échelle sans dépendre de développeurs ou d'agences.

_Cette intégration est maintenue par Better Email._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Better Email vous permet de créer et de gérer des modèles d'e-mail dans l'éditeur collaboratif de Better Email et de les exporter directement vers Braze en tant que modèles d'e-mail prêts à l'emploi.

Réexporter un e-mail met à jour le modèle Braze existant au lieu d'en créer un doublon, ce qui permet de garder votre bibliothèque de modèles propre.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Better Email | Un compte Better Email avec un accès administrateur pour créer des intégrations |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations complètes **Templates**.<br><br>Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Utilisez l'hôte REST, et non l'URL du tableau de bord — par exemple, `rest.fra-01.braze.eu`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Cas d'utilisation {#use-cases}

Better Email est conçu pour les équipes marketing qui souhaitent gérer leurs e-mails via un design system et les exporter vers Braze sans travail HTML manuel. Il est idéal pour ceux qui :

- Maintiennent une grande bibliothèque de modèles d'e-mail et ont besoin de cohérence sur l'ensemble de ceux-ci
- Souhaitent appliquer des directives de marque via un Email Design System partagé
- Collaborent entre équipes — designers, marketeurs et développeurs — sur la production d'e-mails
- Utilisent Braze pour l'exécution des campagnes et veulent supprimer le goulot d'étranglement entre la conception et le déploiement

## Intégrer Better Email avec Braze {#integrate-better-email-with-braze}

### Étape 1 : Trouver vos valeurs Braze {#step-1-find-your-braze-values}

Dans votre tableau de bord de Braze, collectez les informations suivantes :

- **URL de l'instance** — Utilisez l'hôte REST, et non l'URL du tableau de bord (par exemple, `rest.fra-01.braze.eu`).
- **Clé API** — Une clé API REST avec les autorisations complètes **Templates**, créée sous **Paramètres** > **Clés API**.

### Étape 2 : Configurer l'intégration dans Better Email {#step-2-set-up-the-integration-in-better-email}

1. Accédez à **Integrations**.
2. Créez une nouvelle intégration.
3. Saisissez un nom pour l'intégration (par exemple, `Braze`).
4. Sélectionnez **Braze** comme type.
5. Facultativement, restreignez l'intégration à des utilisateurs ou groupes spécifiques sous **Access**.
6. Sélectionnez **Save**.
7. Saisissez l'**URL de l'instance** et la **clé API**.
8. Activez l'intégration.
9. Sélectionnez **Save** à nouveau.

### Étape 3 : Exporter vers Braze {#step-3-export-to-braze}

Lorsque l'intégration est active, ouvrez n'importe quel e-mail dans Better Email et sélectionnez **Export** > **Braze**.

Better Email crée ou met à jour le modèle d'e-mail Braze correspondant. Après le premier export, Better Email stocke l'ID du modèle Braze — réexporter le même e-mail met à jour ce modèle au lieu d'en créer un doublon.

### Facultatif : Synchroniser les champs de destinataires depuis Braze {#optional-sync-recipient-fields-from-braze}

Better Email peut synchroniser les attributs personnalisés Braze pour les utiliser comme balises de fusion et champs de segmentation.

1. Ouvrez l'intégration Braze dans Better Email.
2. Activez **Sync recipient fields**.
3. Sélectionnez **Save**.
4. Accédez à **Recipient Fields**.
5. Lancez **Sync from** suivi du nom de votre intégration.

Better Email lit les attributs personnalisés Braze disponibles et les associe aux champs de destinataires.

## Résolution des problèmes {#troubleshooting}

Si un export ou une synchronisation échoue, vérifiez les points suivants :

- L'**URL de l'instance** est bien l'URL REST, et non l'URL du tableau de bord
- La clé API est toujours active et dispose des autorisations **Templates** nécessaires
- L'intégration est activée dans Better Email
- Les utilisateurs ou groupes appropriés ont accès à l'intégration

Pour une assistance supplémentaire, contactez [support@better.email](mailto:support@better.email).

## Utiliser l'intégration {#use-the-integration}

Vous trouverez vos modèles Better Email exportés dans Braze sous **Modèles et médias** > **Modèles d'e-mail**. Utilisez-les dans n'importe quelle campagne ou Canvas Braze.