---
nav_title: Wie Braze Currents verwendet
article_title: Wie Braze Currents verwendet
page_order: 6
page_type: tutorial
description: "Dieser Currents-Artikel führt Sie durch die grundlegenden Schritte zur Einrichtung der richtigen Dateneingabe für Ereignisdaten sowie zur Übertragung dieser Daten in eine Datenbank und ein Business-Intelligence (BI)-Tool."
tool: Currents

---

# Wie Braze Currents verwendet

> Braze verwendet Currents intern mit ausgewählten [Partnern]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/).

Wir filtern unsere Daten aus E-Mail- und Push-Campaigns in ein Business-Insights-Tool, Looker, aber der Weg dorthin ist etwas anders. Wir verwenden eine umgekehrte Version der Extract, Transform, Load (ETL)-Methode – wir ändern die Reihenfolge in Extract, Load, Transform (ELT).

## 1. Schritt: Event-Daten eingeben und aggregieren

Nachdem wir Campaigns mit einem unserer Engagement-Tools (wie Campaigns oder Canvas) gestartet haben, verfolgen wir die Ereignisdaten mit unserem eigenen System sowie teilweise mit denen unserer E-Mail-Partner. Einige dieser Daten werden im Dashboard zusammengefasst und angezeigt, aber wir möchten tiefer eintauchen!

## 2. Schritt: Event-Daten an einen Partner für die Datenspeicherung senden

Wir haben Currents eingerichtet, um Braze-Ereignisdaten zur Speicherung und Extraktion an Amazon S3 zu senden. Wir wissen, dass Sie [Athena](https://aws.amazon.com/athena/) verwenden können, um auf S3 aufzusetzen und Abfragen durchzuführen. Das ist eine großartige kurzfristige Lösung. Aber wir wollten eine langfristige Lösung mit einer relationalen Datenbank und einem Business-Intelligence/Analytics-Tool. (Das empfehlen wir auch für Sie.)

S3 bietet flexible Speicher- und Routing-Optionen zum Verschieben, Pivotieren und Analysieren von Daten. Wir transformieren die Daten nicht in S3, da wir eine bestimmte Struktur dafür beibehalten.

## 3. Schritt: Event-Daten mit einer relationalen Datenbank transformieren

Von S3 aus wählen wir ein Warehouse ([Snowflake Datenfreigabe](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) oder Snowflake Reader Accounts, in unserem Fall). Dort transformieren wir die Daten und verschieben sie dann nach Looker, wo wir Blöcke eingerichtet haben, die unsere Daten strukturieren und organisieren.

Snowflake ist nicht die einzige Warehouse-Option. Weitere Optionen sind [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) und mehr!

### Snowflake Reader Accounts

Snowflake Reader Accounts bieten Nutzer:innen Zugriff auf dieselben Daten und Funktionen wie die [Snowflake Datenfreigabe]({{site.baseurl}}/partners/snowflake/), ohne dass ein Snowflake-Konto oder eine Kundenbeziehung mit Snowflake erforderlich ist. Mit Reader Accounts erstellt und teilt Braze Ihre Daten in einem Konto und stellt Ihnen Zugangsdaten zur Verfügung, um sich anzumelden und auf Ihre Daten zuzugreifen. Dadurch werden alle Datenfreigabe- und Nutzungskosten vollständig von Braze übernommen.

Um mehr zu erfahren, kontaktieren Sie Ihren Customer-Success-Manager.

#### Zusätzliche Ressourcen
Hilfreiche Ressourcen zur Nutzungsüberwachung finden Sie in den Snowflake-Artikeln zu [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html) und [Viewing Warehouse Credit Usage](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## 4. Schritt: Ein Business-Intelligence (BI)-Tool zur Datenbearbeitung verwenden

Schließlich verwenden wir ein BI-Tool, um unsere Daten zu analysieren, sie in Charts und andere visuelle Werkzeuge umzuwandeln und mehr – mit [Looker und Looker Blocks](https://www.marketplace.looker.com/), sodass wir nicht jedes Mal ETL oder ELT durchführen müssen, wenn Daten aus Currents verschoben werden.

Inspiriert, dasselbe zu tun? Sehen Sie sich die folgenden Dokumente an, um weitere Informationen darüber zu erhalten, wie Sie diese nutzen können, um Ihre Datenbank aufzubauen!

- [User Behavior Block](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Message Engagement Block](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)