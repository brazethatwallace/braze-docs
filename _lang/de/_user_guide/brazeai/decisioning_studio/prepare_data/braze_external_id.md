---
nav_title: Braze externe ID verwenden
article_title: Braze externe ID verwenden
page_order: 5
page_type: reference
description: "Dieser Referenzartikel erklärt, warum Decisioning Studio die Braze externe ID als Einheit der Kundenidentität verwendet und was passiert, wenn eine andere Bezeichnerstruktur genutzt wird."
---

# Braze externe ID verwenden {#use-braze-external-id}

> Decisioning Studio erfordert einen einzelnen, stabilen Kundenbezeichner, der über alle Datenbestände hinweg konsistent ist. Die Empfehlung ist, die Braze externe ID als diesen Bezeichner zu verwenden. Dieser Artikel erklärt, warum das so ist und welche Risiken entstehen, wenn stattdessen andere Bezeichnerstrukturen verwendet werden.

## Warum die Braze externe ID verwenden? {#why-use-braze-external-id}

Decisioning Studio arbeitet ausschließlich mit der Braze externen ID als Einheit der Kundenidentität. Alle Datenbestände (Kundenprofile, Features, Aktivierungen, Engagements, Conversions) sollten die Braze externe ID als primären Kundenbezeichner referenzieren.

Über die Erfüllung einer technischen Anforderung hinaus ist die Verwendung der Braze externen ID eine bewusste Designentscheidung, die die Zuverlässigkeit des Modelltrainings und der Empfehlungen schützt.

### Herausforderungen anderer Bezeichner {#challenges-of-other-identifiers}

Viele Organisationen pflegen zwei verschiedene Kundenbezeichnersysteme:

- **Eine Warehouse- oder System-of-Record-ID** (manchmal als „kanonische ID“ oder „physische ID“ bezeichnet): die maßgebliche Quelle für Metriken wie Lifetime-Value, Retouren und Loyalität. Sie befindet sich in Ihrem Data Warehouse oder ERP.
- **Eine Plattform-ID:** der Bezeichner, der von Tools wie Braze verwendet wird und typischerweise an eine E-Mail-Adresse, ein Geräte-Token oder einen ähnlichen Aktivierungskanal gebunden ist.

Die Versuchung besteht darin, die Warehouse-ID für den Aufbau von Kunden-Features zu verwenden (da dort die Daten liegen) und die Braze-ID für die Aktivierung (da Braze diese nutzt). Dies erfordert jedoch eine Übersetzungsschicht zwischen den beiden Systemen, und diese Übersetzungsschicht führt zu Fragilität.

#### Identitätsdrift {#identity-drift}

Selbst wenn die Zuordnung zwischen Ihrer Warehouse-ID und Ihrer Braze-ID derzeit eins-zu-viele ist (eine physische geschäftskunden wird mehreren Braze-Profilen zugeordnet), kann sich diese Zuordnung im Laufe der Zeit zu einer Viele-zu-viele-Beziehung destabilisieren. Wenn eine einzelne Warehouse-ID im Laufe der Zeit verschiedenen Kund:innen zugewiesen wird oder wenn dasselbe Braze-Profil mit mehreren Warehouse-IDs verknüpft wird, entsteht **Identitätsdrift**.

Identitätsdrift verursacht:

- **Fehler beim Modelltraining:** Wenn die geschäftskunden, für die das Modell eine Empfehlung generieren wollte, tatsächlich eine andere Person ist, wird das Trainingssignal verfälscht.
- **Ungenauigkeiten in der Berichterstattung:** Metriken werden bedeutungslos, wenn die zugrunde liegende Identitätszuordnung instabil ist.
- **Attributionsfehler:** Conversions werden den falschen Empfehlungen zugeordnet.

### Wie die Braze externe ID diese Risiken adressiert {#how-braze-external-id-addresses-these-risks}

#### Aktivierungsbereit durch Design {#activation-ready-by-design}

Empfehlungen, die auf Basis einer Braze externen ID generiert werden, können direkt über Liquid oder Connected-Content in Nachrichten eingespeist werden – ohne einen ID-Übersetzungsschritt. Das Entfernen der Übersetzungsschicht beseitigt eine erhebliche Quelle operativer Komplexität und Fehleranfälligkeit.

#### Isoliert von Upstream-Änderungen {#isolated-from-upstream-changes}

Durch die Arbeit mit der Braze externen ID ist Decisioning Studio von Änderungen in Ihren vorgelagerten Systemen isoliert. Wenn sich Ihre interne Warehouse-ID aufgrund einer Systemmigration, einer Datenqualitätskorrektur oder eines ERP-Updates ändert, bleibt die Braze externe ID – und alles, was damit verknüpft ist – stabil.

#### Saubere Kanaltrennung {#clean-channel-separation}

In Braze entspricht ein Nutzerprofil einem erreichbaren Kommunikationskanal. Wenn eine geschäftskunden zwei E-Mail-Adressen registriert, hat sie zwei separate Braze-Profile mit zwei separaten Braze externen IDs. Decisioning Studio behandelt diese als zwei getrennte Entitäten, was bedeutet, dass Empfehlungen und Ereignisverlauf für eine E-Mail-Adresse nicht durch Aktivitäten der anderen kontaminiert werden.

Dies verhindert, was man als „Kontextschleichen“ bezeichnen könnte. Das Empfehlungssystem würde beispielsweise nicht arbeitsbezogenes Kaufverhalten in Empfehlungen einfließen lassen, die an ein persönliches E-Mail-Konto gesendet werden.

## Überlegungen zu mehreren Entitäten {#multi-entity-considerations}

### Multi-Store- oder hierarchische Unternehmen {#multi-store-or-hierarchical-businesses}

Für Unternehmen, die mehrere Filialen oder Untermarken betreiben (zum Beispiel ein Franchisegeber mit vielen Franchisenehmern), kann das Konzept „geschäftskunden“ mehrdeutig sein. Eine geschäftskunden, die an mehreren Standorten einkauft, kann an jedem Standort separate Datensätze haben, sollte aber für Empfehlungszwecke als eine Person behandelt werden.

Wenn Ihr Unternehmen diese Struktur aufweist, besprechen Sie mit Ihrem Decisioning-Studio-Team, wie die Kundenhierarchie modelliert werden soll, bevor Sie Ihre Bezeichnerstrategie finalisieren.

### B2C-Identitätsfragmentierung {#b2c-identity-fragmentation}

Eine einzelne physische Person kann im Laufe der Zeit mehrere Braze-Profile ansammeln, beispielsweise durch die Registrierung mit verschiedenen E-Mail-Adressen oder das Einloggen auf verschiedenen Geräten vor einer Kontozusammenführung. Decisioning Studio behandelt jede Braze externe ID als eigenständige geschäftskunden.

Dies ist beabsichtigt: Jedes Profil repräsentiert einen eigenständigen Aktivierungskanal. Es bedeutet jedoch auch, dass die Qualität Ihrer Empfehlungen von der Qualität Ihrer Braze-Identitätsauflösung abhängt. Wenn Ihre Braze-Implementierung doppelte Profile nicht zuverlässig zusammenführt, erhalten einige Kund:innen möglicherweise eine weniger hochwertige Personalisierung, da ihr Verlauf über mehrere Profile fragmentiert ist.