---
nav_title: Configuration des expéditeurs
article_title: Expéditeurs SMS, MMS et RCS
page_order: 2
description: "Cet article fournit un aperçu des codes et des expéditeurs disponibles pour l'envoi de messages SMS, MMS et RCS."
page_type: reference
alias: /sending_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

{% multi_lang_include channels/sms/short_and_long_codes.md %}

## Exigences spécifiques au MMS {#mms-specific-requirements}

### Exigences relatives à l'expéditeur MMS {#mms-sender-requirements}

> Le MMS et le SMS sont tous deux liés au canal SMS de Braze. Pour accéder au MMS sur votre compte, il est nécessaire d'acheter le SMS pour ceux qui n'ont pas encore acheté cet accès. Les clients SMS existants peuvent accéder au MMS après l'avoir acheté.

Le MMS est actuellement pris en charge pour les codes courts américains (numéros à 5-6 chiffres), les codes longs américains et canadiens (numéros à 10 chiffres) et les numéros clients américains et canadiens. Le MMS est pris en charge pour les numéros gratuits par certains fournisseurs de services.

L'envoi de MMS vers des numéros en dehors des États-Unis et du Canada est possible, mais les messages MMS sont convertis en message SMS avec un lien vers la ressource multimédia.

### Codes courts MMS {#mms-short-codes}

Certains utilisateurs peuvent ne pas implémenter ou utiliser de codes courts MMS, mais ils sont disponibles si nécessaire ultérieurement.

Pour les utilisateurs qui ont obtenu leurs codes courts avant que Braze ne prenne en charge le MMS, tous les clients existants disposant de codes courts américains sont éligibles pour activer instantanément le MMS. Contactez votre gestionnaire du succès des clients si cette situation s'applique à vous et que vous souhaitez activer le MMS.

{% alert important %}
Lors de l'activation du MMS pour des codes courts qui n'avaient pas le MMS activé auparavant, les codes courts peuvent nécessiter une nouvelle approbation dans le cadre d'un processus qui peut prendre des semaines. Il est important de tenir compte de ce délai lorsque vous décidez d'activer le MMS.
{% endalert %}

#### Bonnes pratiques pour les codes courts MMS {#mms-short-code-best-practices}

- Chez Braze, nous recommandons fortement de séparer les messages transactionnels et promotionnels, chacun avec des codes courts différents. Étant donné que le MMS est lié au canal SMS, et que le canal SMS est fortement réglementé, les clients peuvent être tenus de payer une pénalité financière en cas de mauvaise utilisation du canal et voir leur code court suspendu (ce qui est irréversible). Séparer les messages transactionnels et promotionnels sur des codes courts différents protège leurs messages transactionnels.
- Si les clients disposent déjà d'un code court dédié aux messages promotionnels et qu'il est compatible MMS, ils n'ont pas besoin d'un code court distinct pour le MMS.

### Codes longs MMS {#mms-long-codes}

Les clients peuvent envoyer des MMS avec des codes longs. Pour ce faire, vous devez vous assurer que vos codes longs sont compatibles MMS. Cela peut être fait initialement lors de la configuration, ou ultérieurement depuis votre compte.

Les messages MMS ne peuvent pas être envoyés avec un identifiant d'expéditeur alphanumérique.

### Limites et débit des messages MMS {#mms-message-limits-and-throughput}

Le débit MMS est d'un segment par seconde via un code long.

Les opérateurs imposent leurs propres limites de taille de fichier, qui déterminent le succès des envois MMS. Ces limites peuvent varier selon la zone géographique et l'opérateur, c'est pourquoi Braze recommande de ne pas dépasser 600&nbsp;Ko pour votre ressource multimédia tout en incluant un corps de message. Dans le composeur SMS ou MMS de Braze, les téléchargements supérieurs à 1&nbsp;Mo sont bloqués. Le message d'erreur recommande de télécharger un fichier de 600&nbsp;Ko ou moins. Nous recommandons également de tester pour confirmer que votre média peut être livré chez les opérateurs de vos utilisateurs.

#### Limites de taille de fichier par opérateur {#carrier-file-size-limits}

| Taille&nbsp;du&nbsp;fichier | Traitement par l'opérateur |
| --- | --- |
| 300&nbsp;Ko | Tous les opérateurs devraient gérer de manière fiable les messages MMS de cette taille. |
| 600&nbsp;Ko | Il s'agit de la taille de fichier maximale standard pour le MMS chez la plupart des opérateurs. |
| 1&nbsp;Mo | La plupart des opérateurs américains et canadiens peuvent gérer les messages MMS de cette taille, bien que cela puisse varier selon l'opérateur. Certains opérateurs peuvent autoriser des tailles de fichier supérieures. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de taille de fichier par opérateur" }

#### Types de fichiers acceptés {#accepted-file-types}

Braze accepte les fichiers JPEG, GIF, PNG et VCF et vous permet de joindre une seule ressource multimédia à votre message MMS.