---
nav_title: Opt-in- und Opt-out-Keywords
article_title: SMS-Opt-in- und Opt-out-Keywords
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Braze grundlegende Opt-in- und Opt-out-Keywords für SMS-Messaging verarbeitet."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Opt-in- und Opt-out-Keywords {#opt-in-and-opt-out-keywords}

> Vorschriften verlangen, dass auf alle Opt-in-, Opt-out- und Hilfe-/Info-Keyword-Antworten reagiert wird. Braze verarbeitet automatisch die folgenden _exakten, einzelnen, nicht zwischen Groß- und Kleinschreibung unterscheidenden_ Nachrichten und aktualisiert dabei automatisch den [Abo-Gruppen-Status]({{site.baseurl}}/sms_rcs_subscription_groups) für die Nutzer:in und die zugehörige Telefonnummer bei allen eingehenden Anfragen.

## Standard-Keywords {#default-keywords}

Braze verarbeitet die folgenden Keywords automatisch und aktualisiert den Abo-Gruppen-Status für die Telefonnummer bei allen eingehenden Anfragen. Beachten Sie, dass diese Standard-Keywords und -Antworten auch angepasst werden können und Sie [angepasste Keywords]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling) hinzufügen können.

{% alert tip %}
Möchten Sie Ihre Opt-out-Verarbeitung erweitern? Probieren Sie [Fuzzy-Opt-out]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out) aus – ein Feature, das versucht zu erkennen, wenn eine eingehende Nachricht nicht mit einem Opt-out-Keyword übereinstimmt, aber eine Opt-out-Absicht signalisiert.
{% endalert %}

| Typ | Keyword | Änderung |
|-|-------|---|
| Opt-in | `START`<br> `YES`<br> `UNSTOP` | Jede eingehende Anfrage mit einem dieser `Opt-In`-Keywords führt zu einer Änderung des Abo-Gruppen-Status auf `subscribed`. Darüber hinaus kann der Pool von Absendern, die dieser Abo-Gruppe zugeordnet sind, nun eine SMS-, MMS- oder RCS-Nachricht an diese Kund:in senden (abhängig von der Art des Messagings, die die Absender unterstützen). <br><br>Die Nutzer:in erhält Ihre definierte automatische Opt-in-Antwort. |
| Opt-out | `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Jede eingehende Anfrage mit einem dieser `Opt-Out`-Keywords führt zu einer Änderung des Abo-Gruppen-Status auf `unsubscribed`. Darüber hinaus kann der Pool von Nummern, die dieser Abo-Gruppe zugeordnet sind, keine Nachrichten mehr an diese Kund:in senden.<br><br>Die Nutzer:in erhält Ihre definierte automatische Opt-out-Antwort. |
| Hilfe | `HELP`<br> `INFO` | Die Nutzer:in erhält Ihre definierte automatische Hilfe-Antwort. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Standard-Keywords" }

Nur die **exakte, einzelne Nachricht** wird verarbeitet (ohne Berücksichtigung der Groß-/Kleinschreibung). Keywords wie `STOP PLEASE` werden ignoriert, es sei denn, [Fuzzy-Opt-out]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out) ist aktiviert.

Wenn eine Empfänger:in die Keywords `HELP` oder `INFO` verwendet, wird automatisch eine Antwort getriggert. Die Standardantwort für diese automatischen Antwortnachrichten wird während Ihres [Onboardings]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) und der Beschaffung von Telefonnummern festgelegt. Beachten Sie, dass Sie diese Antworten auch nach der anfänglichen Onboarding-Phase weiterhin aktualisieren können.

{% alert tip %}
Möchten Sie Ihre Opt-out-Verarbeitung erweitern? Probieren Sie [Fuzzy-Opt-out]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out) aus – ein Feature, das versucht zu erkennen, wenn eine eingehende Nachricht nicht mit einem Opt-out-Keyword übereinstimmt, aber eine Opt-out-Absicht signalisiert.
{% endalert %}

## Natürlichsprachliche Opt-outs verarbeiten {#handle-natural-language-opt-outs}

Sie können einen [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents) erstellen, der Sentimentanalyse nutzt, um Opt-out-Absichten zu erfassen, die außerhalb von Standard- oder angepassten Keywords liegen (z. B. „Bitte schreiben Sie mir nicht mehr“). Weitere Informationen finden Sie unter [Natürlichsprachliche Opt-outs in der Agentenkonsole verarbeiten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#handle-natural-language-opt-outs-in-the-agent-console).