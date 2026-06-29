---
nav_title: "Configurer le suivi"
article_title: "Suivi"
page_order: 2
description: "Cet article de référence explique comment configurer le suivi en temps réel pour les campagnes d'e-mails transactionnels."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Suivre les e-mails transactionnels {#track-transactional-emails}

> Cette page décrit comment configurer le suivi en temps réel pour les [campagnes d'e-mails transactionnels]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/). Pour plus d'informations sur l'endpoint lui-même, consultez [Envoyer des e-mails transactionnels via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

Lorsque vous envoyez des e-mails transactionnels, comme des confirmations de commande ou des réinitialisations de mot de passe, il est essentiel de savoir s'ils parviennent à vos clients. Grâce aux postbacks d'événements HTTP transactionnels de Braze, vous obtenez des informations en temps réel sur l'état de chaque e-mail transactionnel, ce qui vous permet d'agir rapidement en cas de problème.

Utilisez cette fonctionnalité pour :

- **Surveiller vos e-mails en temps réel :** voir immédiatement si les messages sont envoyés, traités, distribués ou s'ils rencontrent des problèmes.
- **Réagir de manière proactive :** renvoyer les messages, basculer vers un autre canal comme le SMS, ou utiliser des systèmes de secours pour vous assurer que vos communications sont bien distribuées.

## Suivi de vos e-mails transactionnels {#tracking-your-transactional-emails}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}