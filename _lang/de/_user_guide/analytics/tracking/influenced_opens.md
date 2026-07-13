---
nav_title: Beeinflusste Öffnungen
article_title: Beeinflusste Öffnungen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erklärt beeinflusste Öffnungen und wie Sie diese tracken können, um detailliertere Einblicke in Ihre Push-Campaigns zu erhalten."
channel: push

---

# Beeinflusste Öffnungen {#influenced-opens}

> Wenn Nutzer:innen eine Push-Benachrichtigung auswählen und zu Ihrer App weitergeleitet werden, protokolliert Braze dies als direkte Öffnung. Wenn Nutzer:innen die Benachrichtigung nicht auswählen, aber dennoch von der Push-Benachrichtigung beeinflusst werden könnten, protokolliert Braze dies als beeinflusste Öffnung. Dies bietet einen detaillierteren Einblick in die Wirkung Ihrer Push-Campaigns.

## Funktionsweise {#how-it-works}

Beeinflusste Öffnungen messen im Grunde die Anzahl der Nutzer:innen, die die App nach dem Erhalt einer Benachrichtigung öffnen, ohne die Benachrichtigung auszuwählen. Da es keine direkte Aktion gibt, die die Benachrichtigung mit der App-Öffnung verknüpft, wird eine beeinflusste Öffnung protokolliert, wenn Nutzer:innen die App weniger als dreißig Minuten nach Erhalt der Push-Benachrichtigung oder innerhalb der Hälfte der durchschnittlichen Zeit seit der letzten Sitzung dieser Nutzer:innen öffnen.

Nehmen wir beispielsweise an, Sie senden eine Push-Benachrichtigung an die Nutzer:innen Ihrer App. Wenn Nutzer:innen, die die App normalerweise 30 Mal am Tag öffnen, Ihre App sechs Stunden nach Erhalt des Push öffnen, hat der Push wenig bis gar keinen Einfluss auf die Öffnung. Wenn jedoch Nutzer:innen, die die App normalerweise einmal im Monat nutzen, die App sechs Stunden nach Erhalt des Push öffnen, ist die Chance wesentlich größer, dass die Öffnung als beeinflusste Öffnung gezählt wird.

Dies unterscheidet sich von der Einstellung von App-Öffnungen als Konversions-Event für eine Push-Campaign. Bei Conversions werden alle Öffnungen innerhalb des Conversion-Fensters der Campaign zugeschrieben. Beeinflusste Öffnungen legen ein Zeitfenster und eine Attribution auf der Grundlage des individuellen Verhaltens einzelner Nutzer:innen fest.

## Beeinflusste Öffnungen einer Campaign anzeigen {#viewing-a-campaigns-influenced-opens}

Beeinflusste Öffnungen werden zu den direkten Öffnungen einer Campaign addiert, um die Gesamtzahl der Öffnungen zu ermitteln. Dies wird auf der Seite **Campaign Analytics** einer Push-Campaign angezeigt. Die Gesamtzahl der Öffnungen und die direkten Öffnungen werden in den Abschnitten zur Nachrichten-Performance und **Historical Performance** angezeigt. Beeinflusste Öffnungen sind die Differenz zwischen den beiden Kennzahlen.

![Statistiken zu beeinflussten Öffnungen auf der Seite „Campaign-Details“ für eine Campaign]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Weitere Informationen zum Tracking von Öffnungen finden Sie im Abschnitt zum Conversion-Tracking in unseren [Best Practices für Push]({{site.baseurl}}/user_guide/channels/push/best_practices).