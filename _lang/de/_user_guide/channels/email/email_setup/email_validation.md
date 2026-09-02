---
nav_title: E-Mail-Validierung
article_title: E-Mail-Validierung
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt die Validierungsregeln für den lokalen und den Host-Teil von E-Mail-Adressen."
channel: email

---

# E-Mail-Validierung {#email-validation}

> Dieser Referenzartikel behandelt die Validierungsregeln für den lokalen und den Host-Teil von E-Mail-Adressen. Die Validierung wird für Dashboard-E-Mail-Adressen, Endnutzer:innen-E-Mail-Adressen (Ihre Kund:innen) sowie für Absender- und Antwortadressen einer E-Mail-Nachricht verwendet.

## Funktionsweise {#how-it-works}

Braze validiert eine E-Mail-Adresse, wenn sie aktualisiert, per API importiert, per CSV hochgeladen, über das SDK or Software-Development-Kit übermittelt oder im Dashboard geändert wird. E-Mail-Adressen dürfen keine Leerzeichen enthalten. Wenn Sie die API verwenden, gibt ein Leerzeichen einen `400`-Fehler zurück.

Braze lehnt bestimmte Zeichen ab und markiert die Adresse als ungültig. Wenn eine E-Mail einen Bounce verursacht, markiert Braze die Adresse als ungültig und ändert den Abo-Status nicht. Wenn der E-Mail-Text nicht standardmäßige [ASCII](https://en.wikipedia.org/wiki/ASCII)-Zeichen enthält, sendet Braze die E-Mail nicht.

{% details Akzeptierte Zeichen %}
- Buchstaben (A–Z)
- Ziffern (0–9)
- Symbole
	- -
	- &#94;
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- `
	- |
	- ~
	- !
	- ?
	- . (nur zwischen Buchstaben oder anderen Zeichen)
{% enddetails %}

{% details Nicht akzeptierte Zeichen %}
- Leerzeichen (ASCII und Unicode)
{% enddetails %}

Diese Validierung ist eine Syntaxprüfung, kein Validierungsdienst. Ein Ziel dieses Prozesses ist die Unterstützung internationaler Zeichen (wie UTF-8) im lokalen Teil der E-Mail-Adresse.

Braze validiert die Syntax sowohl für den lokalen als auch für den Host-Teil einer E-Mail-Adresse. Der lokale Teil ist alles vor dem At-Zeichen (@); der Host-Teil ist alles danach. Der lokale Teil darf mit jedem zulässigen Zeichen beginnen und enden, außer mit einem Punkt (.). Dieser Prozess prüft nicht, ob die Domain einen gültigen MX-Server hat oder ob ein:e Nutzer:in auf dieser Domain existiert.

{% alert important %}
Wenn der Domain-Teil nicht standardmäßige ASCII-Zeichen enthält, muss er [Punycode-kodiert](https://www.punycoder.com/) werden, bevor er an Braze übermittelt wird.
{% endalert %}

Wenn Braze eine Anfrage erhält, ein:e Nutzer:in mit einer ungültigen E-Mail-Adresse hinzuzufügen, gibt die API einen Fehler zurück. Bei einem CSV-Upload erstellt Braze die/den Nutzer:in, lässt aber die ungültige E-Mail-Adresse weg.

## Validierungsregeln für den lokalen Teil {#local-part-validation-rules}

### Allgemeine E-Mail-Validierung {#general-email-validation}

Für die meisten Domains muss der lokale Teil folgende Parameter erfüllen:
- Kann beliebige Buchstaben und Ziffern enthalten, einschließlich Unicode-Buchstaben und -Ziffern, sowie die folgenden Zeichen: (+) (&) (#) (_) (-) (^) oder (/)
- Kann das folgende Zeichen enthalten, darf aber nicht damit beginnen oder enden: (.)
- Darf keine doppelten Anführungszeichen (") enthalten
- Muss zwischen 1 und 64 Zeichen lang sein

Der folgende reguläre Ausdruck kann verwendet werden, um zu prüfen, ob eine E-Mail-Adresse als gültig betrachtet wird:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Gmail-Adressen {#gmail-addresses}

Wenn der Domain-Teil Gmail ist, muss der lokale Teil mindestens zwei Zeichen lang sein und der oben aufgeführten Validierung mit regulärem Ausdruck entsprechen.

### Microsoft-Domains {#microsoft-domains}

Wenn die Host-Domain „msn“, „hotmail“, „outlook“ oder „live“ enthält, verwendet Braze den folgenden regulären Ausdruck zur Validierung des lokalen Teils: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

Der lokale Teil der Microsoft-Adresse muss folgende Parameter erfüllen:

- Kann mit einem Buchstaben (a–z), einem Unterstrich (_) oder einer Zahl (0–9) beginnen.
- Kann beliebige alphanumerische Zeichen (a–z oder 0–9) oder einen Unterstrich (_) enthalten
- Kann die folgenden Zeichen enthalten: (.) oder (-)
- Darf nicht mit einem Punkt (.) beginnen
- Darf nicht zwei oder mehr aufeinanderfolgende Punkte (.) enthalten
- Darf nicht mit einem Punkt (.) enden

Der Validierungstest prüft, ob der lokale Teil vor dem „+“ dem regulären Ausdruck entspricht.

## Validierungsregeln für den Host-Teil {#host-part-validation-rules}

Der Host-Teil darf keine IPv4- oder IPv6-Adresse sein. Die Top-Level-Domain (wie .com, .org, .net) darf nicht vollständig numerisch sein.

Der folgende reguläre Ausdruck wird zur Validierung der Domain verwendet:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

Der Domainname muss folgende Parameter erfüllen:

- Besteht aus zwei oder mehr durch Punkte getrennten Labels
	- Jeder Teil eines Domainnamens wird als „Label“ bezeichnet. Zum Beispiel besteht der Domainname „example.com“ aus dem Label „example“ und dem Label „com“.
- Muss mindestens einen Punkt (.) enthalten
- Darf nicht zwei oder mehr aufeinanderfolgende Punkte enthalten
- Jedes durch Punkte getrennte Label muss:
	- Nur alphanumerische Zeichen (a–z oder 0–9) und den Bindestrich (-) enthalten
	- Mit einem alphanumerischen Zeichen (a–z oder 0–9) beginnen
	- Mit einem alphanumerischen Zeichen (a–z oder 0–9) enden
	- 1 bis 63 Zeichen enthalten

### Zusätzliche erforderliche Validierung {#additional-validation-required}

Das letzte Label der Domain muss eine gültige Top-Level-Domain (TLD) sein, die durch alles nach dem letzten Punkt bestimmt wird. Diese TLD sollte in der [TLD-Liste der ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) erscheinen. Der Braze-Validator prüft nur die Syntax. Er erkennt keine Tippfehler oder nicht existierende Adressen.

{% alert important %}
Unicode wird nur für den lokalen Teil der E-Mail-Adresse akzeptiert. Unicode wird für den Domain-Teil nicht akzeptiert, kann aber Punycode-kodiert werden.
{% endalert %}