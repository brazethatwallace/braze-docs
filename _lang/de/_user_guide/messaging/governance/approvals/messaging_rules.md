---
nav_title: Messaging-Regeln
article_title: Messaging-Regeln
page_order: 1
page_type: reference
description: "Diese Seite beschreibt, wie Sie Messaging-Regeln im Genehmigungs-Workflow für Campaigns und Canvases mit großem Sendevolumen verwenden."
---

# Messaging-Regeln {#messaging-rules}

> Verwenden Sie Messaging-Regeln in Ihrem Genehmigungs-Workflow, um die Zahl erreichbarer Nutzer:innen zu begrenzen, bevor eine zusätzliche Genehmigung erforderlich ist – so können Sie Ihre Campaigns und Canvases überprüfen, bevor Sie eine größere Zielgruppe ansprechen.

## Voraussetzungen {#prerequisites}

Nur Braze-Administratoren können Messaging-Regeln festlegen, aber jede:r Braze-Nutzer:in kann als Genehmigende:r für Messaging-Regeln fungieren (einschließlich Nutzer:innen ohne allgemeine Genehmigungsberechtigungen).

## Funktionsweise {#how-it-works}

Messaging-Regeln gelten für einen Workspace und bestehen aus einem Nachrichtentyp und einer maximalen Zahl erreichbarer Nutzer:innen.

- **Nachrichtentyp:** Legt fest, auf welchen Nachrichtentyp die Regel angewendet wird: Campaign, Canvas oder sowohl Canvas als auch Campaigns.
- **Maximale erreichbare Nutzer:innen:** Bestimmt, ab welcher Zielgruppengröße eine zusätzliche Genehmigung erforderlich ist.

### Separate Genehmigende {#separate-approvers}

Zwei Regeln können dasselbe Nutzer:innen-Maximum teilen, sodass Sie Ihre Regeln nach Genehmigenden organisieren und trennen können. Beispielsweise erstellen Sie die folgenden zwei Regeln:

- Regel A für Canvas mit einem Maximum von 100.000 Nutzer:innen mit Genehmigenden aus Ihrem Rechts-Team
- Regel B für Canvas mit einem Maximum von 100.000 Nutzer:innen mit Genehmigenden aus Ihrem Marketing-Team

### Keine überlappenden erreichbaren Nutzer:innen {#no-overlapping-reachable-users}

Um Verwirrung zu vermeiden, können Sie keine identischen Regeln mit einer überlappenden Nutzer:innen-Zahl für denselben Nachrichtentyp und dieselben Genehmigenden festlegen. Beispielsweise **kann** die folgende Messaging-Regel **nicht** festgelegt werden:

- Regel C für Canvas mit einem Maximum von 10.000 Nutzer:innen
- Regel D für Canvas mit einem Maximum von 1.000.000 Nutzer:innen

## Messaging-Regel erstellen {#creating-a-messaging-rule}

### 1. Schritt: Regel hinzufügen {#step-1-add-a-rule}

{% alert note %}
Sie können bis zu fünf Messaging-Regeln erstellen.
{% endalert %}

1. Gehen Sie zu **Einstellungen** > **Genehmigungs-Workflow** > **Messaging-Regeln**.
2. Wählen Sie **Regel erstellen** aus.
3. Geben Sie dieser Regel einen Namen (z. B. „Alle Nutzer:innen-Abos“).
4. Wählen Sie unter **Nachrichtentyp** die Option **Campaign**, **Canvas** oder **Sowohl Canvas als auch Campaigns** aus, um die Genehmigungsregel anzuwenden.
5. Geben Sie eine Zahl für **Maximale erreichbare Nutzer:innen** ein. Weitere Informationen finden Sie unter [Zielgruppenstatistiken]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users#audience-statistics).
6. Wählen Sie **Speichern** aus.

![Eine beispielhafte Messaging-Regel „Regel 1“ für Campaigns mit 100.000 Nutzer:innen als Maximum. Es gibt eine:n Nutzer:in, die bzw. der den Canvas und die Campaign zum Starten genehmigen kann.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### 2. Schritt: Starten mit Genehmigung festlegen (optional) {#step-2-determine-launching-with-approval-optional}

Wählen Sie **Starten mit Genehmigung erlauben** aus. Wählen Sie anschließend unter **Mit Genehmigung von** die Genehmigenden aus, die die Berechtigung haben, den Canvas oder die Campaign zu genehmigen, wenn das Maximum erreicht ist.

Beachten Sie die folgenden Details zum Starten von Nachrichten mit Genehmigung:

- Wenn das Maximum erreicht ist und ein:e Genehmigende:r ausgewählt wurde, kann die bzw. der Braze-Nutzer:in mit der Genehmigungsberechtigung im Genehmigungs-Dropdown unter **Zielgruppe** die Option **Genehmigt** auswählen.
- Wenn das Maximum erreicht ist und kein:e Genehmigende:r ausgewählt wurde, wird der Start des Canvas oder der Campaign verhindert.

![Der Schritt „Zusammenfassung“ des Canvas-Workflows, der zeigt, dass Sie eine Genehmigung zum Starten benötigen.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Muss ich meine Berechtigungen neu konfigurieren, um Messaging-Regeln zu verwenden? {#do-i-have-to-reconfigure-my-permissions-to-use-messaging-rules}

Nein. Jede:r Nutzer:in kann unabhängig von den aktuellen Berechtigungen als Genehmigende:r für die Zielpopulation ausgewählt werden.

### Wie hängen Messaging-Regeln mit dem Schritt „Zielgruppe“ zusammen? {#how-do-messaging-rules-relate-to-the-target-audience-step}

Messaging-Regeln berücksichtigen keine Details wie triggernde Ereignisse. Beispielsweise könnte eine Campaign alle Ihre Nutzer:innen ansprechen. Die Campaign wird jedoch durch ein Ereignis getriggert, sodass die tatsächliche Zahl der Empfänger:innen niedriger ist.

### Ändert sich automatisch etwas, wenn Messaging-Regeln aktiviert werden? {#will-anything-automatically-change-when-messaging-rules-are-turned-on}

Nein. Nachdem dieses Feature aktiviert wurde, müssen Sie manuell die maximale Zahl der Nutzer:innen eingeben und Genehmigende auswählen, um das Feature zu nutzen.