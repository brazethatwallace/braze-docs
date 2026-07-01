---
nav_title: テンプレートの管理
article_title: テンプレートの管理
page_order: 1

page_type: reference
description: "このリファレンス記事では、Brazeダッシュボードのテンプレートセクションでテンプレートを複製およびアーカイブする方法について説明します。"
tool:
  - Templates
  - Media

---

# テンプレートの管理 {#manage-templates}

> テンプレートをアーカイブまたは複製することで、テンプレートをより効率的に整理・管理できます。このリファレンス記事では、Brazeダッシュボードの**テンプレート**セクションでテンプレートをアーカイブおよび複製する方法について説明します。

## テンプレートの複製 {#duplicating-templates}

{% tabs %}
{% tab 個別のテンプレート %}

![複製オプションを含むドロップダウンメニュー。]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

個別のテンプレートを複製するには、テンプレートの<i class="fas fa-ellipsis-v"></i> **その他のオプション**を選択し、ドロップダウンメニューから**複製**を選択します。
<br><br>

{% alert note %}
[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)テンプレートの場合、下書きコピーが作成されます。その他のすべてのテンプレートでは、新しい複製コピーが自動的に作成されます。
{% endalert %}

{% endtab %}
{% tab 複数のテンプレート %}

{% raw %}

複数のテンプレートを複製するには、テンプレート名の横にあるチェックボックスを選択します。まずテンプレートを選択し、次に**複製**を選択します。

複製されたテンプレートは、**最終編集日時**列でソートすると見つけることができます。デフォルトでは、新しいテンプレートの名前は`Copy of ORIGINAL_TEMPLATE_NAME`となります。

{% endraw %}

![テンプレートの最終編集日時でソートされた3つのテンプレート。コピーされたテンプレートがリストの一番上に表示されています。]({% image_buster /assets/img/duplicate_multiple_template.gif %})

{% endtab %}
{% endtabs %}

## テンプレートのアーカイブ {#archiving-templates}

![展開された設定ドロップダウンメニュー。「アーカイブ」、「複製」、「ワークスペースにコピー」の3つのオプションが表示され、「アーカイブ」オプションがハイライトされています。]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

個別のテンプレートをアーカイブするには、テンプレートグリッド画面で<i class="fas fa-ellipsis-v"></i> **その他のオプション**を選択し、**アーカイブ**を選択します。テンプレートがアーカイブされた場合、以下の点に注意してください。

- アクティブなキャンペーンは、中断なくアーカイブされたテンプレートを引き続き使用します。
- 下書きのキャンペーンは、アーカイブされたテンプレートのコンテンツを保持し、編集および起動できます。
- アーカイブされたテンプレートを編集するには、まずアーカイブを解除する必要があります。同様に、アーカイブされたテンプレートをキャンペーンに使用するには、まずテンプレートのアーカイブを解除する必要があります。

複数のテンプレートをアーカイブするには、アーカイブしたい各テンプレートの横にあるチェックボックスを選択します。複数のテンプレートを選択したら、**アーカイブ**を選択します。アーカイブされたテンプレートは、テンプレートグリッドの**表示**の下にある**アーカイブ済み**を選択すると見つけることができます。

![保存済みのドラッグ＆ドロップメールテンプレートセクション。2つのテンプレートが選択され、ツールバーにアーカイブオプションが表示されています。]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
アーカイブは現在、[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-templates)では利用できません。
{% endalert %}