---
nav_title: Fuzzy-Abmeldung
article_title: Fuzzy-Abmeldung
description: "Dieser Referenzartikel behandelt die Konfiguration der Fuzzy-Abmeldung, einer Einstellung, die versucht zu erkennen, wenn eine eingehende Nachricht keinem Abmelde-Keyword entspricht."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 4

---

# Fuzzy-Abmeldung {#fuzzy-opt-out}

![iOS-Nachrichtenchat, der ausgehende Abmeldenachrichten als Antwort auf die eingehende Fuzzy-Abmeldung „Please stopppp“ zeigt.]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Nutzer:innen, die SMS, MMS und RCS mit Braze versenden, müssen die geltenden Gesetze, Vorschriften und Branchenstandards einhalten. Für die Abmeldung schreiben Gesetze wie der TCPA vor, dass bei einer Nachricht, die eine angemessene Widerrufung der Einwilligung darstellt (einschließlich anerkannter Abmelde-Keywords wie „STOP“, „STOPALL“, „UNSUBSCRIBE“, „CANCEL“, „END“ oder „QUIT“), alle nachfolgenden Nachrichten im Zusammenhang mit diesem Messaging-Programm eingestellt werden müssen. Braze verarbeitet anerkannte Abmelde-Keywords automatisch und meldet die Nutzer:innen ab.<br><br> Die Fuzzy-Abmeldung erweitert diese Funktion, indem sie versucht, eingehende Nachrichten zu erkennen, die keinem konfigurierten **Abmelde-Keyword** in der Kategorie **Opt-out** der Abo-Gruppe entsprechen (also weder einem [Standard-Abmelde-Keyword]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/) noch einem [benutzerdefinierten Abmelde-Keyword]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/), aber dennoch eine Abmeldeabsicht signalisieren – zum Beispiel eine Nachricht wie „goodbye“ oder „leave me alone“.

Die Fuzzy-Abmeldung ist standardmäßig deaktiviert. Wenn die Fuzzy-Abmeldung aktiviert ist und eine eingehende Nachricht als „fuzzy“ eingestuft wird, können Sie Braze so konfigurieren, dass Nutzer:innen entweder automatisch abgemeldet werden oder eine Nachricht erhalten, die erklärt, wie sie sich manuell abmelden können. Für US-Marken wird die automatische Abmeldung dringend empfohlen, um die TCPA-Anforderungen einzuhalten.

{% alert note %}
Derzeit werden nur Abmelde-Keywords (Standard und benutzerdefiniert) unterstützt, die mit Englisch als [lokaler Sprache]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/#multi-language-support) erstellt wurden.
{% endalert %}

## Was wird als „fuzzy“ eingestuft? {#what-is-deemed-as-fuzzy}

Die Kriterien, damit eine eingehende Antwort als „fuzzy“ eingestuft wird, sind wie folgt (Vergleiche verwenden jedes Keyword in der Kategorie **Opt-out**, einschließlich Standard- und benutzerdefinierter Keywords):
- Wenn das Vertauschen eines Buchstabens mit dem Buchstaben links oder rechts davon auf einer QWERTY-Tastatur ein passendes Abmelde-Keyword ergibt.
- Ein Teilstring der Nachricht einem Abmelde-Keyword entspricht.

Zum Beispiel werden „Stpo“ oder „Please stopppp“ als fuzzy eingestuft, und eine Fuzzy-Abmeldeantwort wird gesendet. Wenn die Nutzer:innen dann mit einem Abmelde-Keyword antworten, wird ein Abmeldeereignis ausgelöst.

## Fuzzy-Abmeldung konfigurieren {#configure-fuzzy-opt-out}

Um die Fuzzy-Abmeldung zu konfigurieren, navigieren Sie zur Keyword-Verwaltungsseite der Abo-Gruppe.

1. Gehen Sie zu **Audience** > **Subscription Group Management** und wählen Sie eine **SMS/MMS/RCS**-Abo-Gruppe aus.
2. Suchen Sie unter **Global Keywords** die Kategorie **Opt-out** und wählen Sie das Stiftsymbol aus.
3. Schalten Sie **Fuzzy Opt-Out** auf **On** um.
4. Wählen Sie Ihre bevorzugte Option für **Fuzzy Opt-Out Logic** aus:
   - **Automatically unsubscribe:** Wenn Nutzer:innen eine Nachricht senden, die einem Abmelde-Keyword ähnelt, werden sie sofort abgemeldet, ohne eine Aufforderung zu erhalten. Die Standard-Abmeldebestätigungsnachricht wird dann gesendet.
   - **Send opt-out instructions:** Wenn Nutzer:innen eine Nachricht senden, die einem Abmelde-Keyword ähnelt, sendet Braze eine benutzerdefinierte Antwort (die **Opt-out instruction message**), die erklärt, wie sie sich abmelden können.
5. Wenn Sie **Send opt-out instructions** ausgewählt haben, geben Sie Ihren benutzerdefinierten Text im Feld **Opt-out instruction message** ein. Dieses Feld ist für diese Einstellung erforderlich.
6. Wählen Sie **Save** aus.

![Abschnitt zum Bearbeiten von Abmelde-Keywords und zum Bereitstellen einer Abmeldeanweisungsnachricht.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Best Practices für Fuzzy-Abmeldenachrichten {#best-practices-for-fuzzy-opt-out-messages}

Um eine klare, konforme und positive Erfahrung für Ihre Abonnent:innen sicherzustellen, ist es entscheidend, Ihre Fuzzy-Abmeldenachricht sorgfältig zu konfigurieren. Der Hauptzweck der Fuzzy-Abmeldenachricht besteht darin, **Nutzer:innen zu leiten, die eine Nachricht senden, die Ihrem festgelegten Abmelde-Keyword ähnelt, aber nicht genau entspricht**. Die Nachricht weist Nutzer:innen darauf hin, wie sie sich erfolgreich abmelden können.

### Wichtige Überlegungen {#critical-considerations}

{% alert warning %}
Wenn Sie **Send opt-out instructions** ausgewählt haben, konfigurieren Sie Ihre Fuzzy-Abmeldenachricht **nicht** so, dass sie eine Abmeldung bestätigt. Ihre Fuzzy-Abmeldenachricht darf keine Formulierungen enthalten, die implizieren, dass sich Nutzer:innen bereits erfolgreich abgemeldet haben. Verwenden Sie zum Beispiel **nicht** „You have been unsubscribed“, „You will not receive any more messages from this number“ oder „You are now opted out“.
{% endalert %}

Die Fuzzy-Abmeldenachricht wird gesendet, bevor sich die Nutzer:innen erfolgreich abgemeldet haben. Die Verwendung von Bestätigungsformulierungen (wie „You have been unsubscribed“) führt Abonnent:innen in die Irre, da sie glauben, abgemeldet zu sein, obwohl sie es nicht sind. Dies führt zu weiterhin unerwünschten Nachrichten, Frustration bei Abonnent:innen und erheblichen Compliance-Risiken.

Um Nutzer:innen bei einem Fuzzy-Treffer sofort abzumelden, verwenden Sie stattdessen die Einstellung **Automatically unsubscribe**.

{% alert warning %}
Konfigurieren Sie Ihre Fuzzy-Abmeldenachricht **NICHT** so, dass sie identisch oder ähnlich zu Ihrem exakten Abmelde-Keyword ist.
{% endalert %}

Wenn Ihre Fuzzy-Nachricht identisch mit oder zu ähnlich zu Ihrem exakten Abmelde-Keyword ist (zum Beispiel wenn „STOP“ Ihr exaktes Keyword ist und Ihre Fuzzy-Nachricht „Text STOP to unsubscribe“ lautet), kann dies Verwirrung darüber stiften, ob die ursprüngliche Nachricht der Nutzer:innen tatsächlich zu einer Abmeldung geführt hat oder ob eine weitere Aktion erforderlich ist. Die Fuzzy-Nachricht sollte immer klarstellen, welche Aktion die Nutzer:innen ausführen müssen.

### Beispiele für Fuzzy-Abmeldenachrichten {#examples-of-fuzzy-opt-out-messages}

Wenn Sie **Send opt-out instructions** wählen, konzentrieren Sie Ihre Nachricht darauf, die Nutzer:innen anzuleiten. Wenn Ihr Abmelde-Keyword zum Beispiel „STOP“ ist, sind dies gute und schlechte Beispiele für Fuzzy-Abmeldenachrichten, die Sie erstellen könnten:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>„Um sich von allen Nachrichten abzumelden, antworten Sie bitte mit dem Wort STOP.“</td>
      <td>„Sie wurden erfolgreich abgemeldet. Sie erhalten keine weiteren Nachrichten mehr von dieser Nummer. Antworten Sie mit START, um sich erneut anzumelden.“ (Dies ist eine direkte Abmeldebestätigung, die in einem Fuzzy-Abmeldeszenario irreführend ist.)</td>
    </tr>
    <tr>
      <td>„Wir haben Ihre Nachricht erhalten. Wenn Sie keine Textnachrichten mehr erhalten möchten, senden Sie bitte STOP.“</td>
      <td>„STOP.“ (Dies ist nur das exakte Keyword selbst, das die Nutzer:innen nicht anleitet.)</td>
    </tr>
    <tr>
      <td>„Wollten Sie sich abmelden? Antworten Sie mit STOP, um sich von allen zukünftigen Nachrichten abzumelden.“</td>
      <td>„Senden Sie STOP, um sich abzumelden.“ (Wenn „STOP“ auch Ihr exaktes Keyword ist, ist dies redundant und klärt die Aktion nicht, wenn die ursprüngliche Nachricht fuzzy war.)</td>
    </tr>
  </tbody>
</table>