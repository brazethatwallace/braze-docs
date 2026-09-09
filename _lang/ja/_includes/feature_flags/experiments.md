# フィーチャーフラグ実験 {#feature-flag-experiments}

> フィーチャーフラグ実験では、コンバージョン率を最適化するためにアプリケーションの変更をA/Bテストできます。マーケターはフィーチャーフラグを使って、新機能がコンバージョン率にプラスまたはマイナスの影響を与えるかどうか、あるいはどのフィーチャーフラグプロパティのセットが最適かを判断できます。

## 前提条件 {#prerequisites}

実験でユーザーデータを追跡するには、ユーザーがフィーチャーフラグを操作したときにアプリが記録する必要があります。これはフィーチャーフラグインプレッションと呼ばれます。テスト対象の機能をユーザーが見た、または見た可能性がある場合は、コントロールグループに属している場合であっても、必ずフィーチャーフラグインプレッションを記録してください。

フィーチャーフラグインプレッションの記録について詳しくは、「[フィーチャーフラグの作成]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions)」を参照してください。

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## フィーチャーフラグ実験の作成 {#creating-a-feature-flag-experiment}

### ステップ1：実験を作成する {#step-1-create-an-experiment}

1. **メッセージング** > **キャンペーン**に移動し、**+ キャンペーンを作成**を選択します。
2. **フィーチャーフラグ実験**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。

### ステップ2：実験バリアントを追加する {#step-2-add-experiment-variants}

次に、バリエーションを作成します。各バリアントについて、有効化または無効化するフィーチャーフラグを選択し、割り当てられたプロパティを確認します。

フィーチャーの影響をテストするには、バリアントを使用してトラフィックを2つ以上のグループに分割します。1つのグループに「My control group」と名前を付け、そのフィーチャーフラグを無効にします。

フィーチャーフラグ実験は、合計9つのグループ（1つのコントロールグループと最大8つのバリアント）をサポートしています。

### ステップ3：プロパティを上書きする（任意） {#step-3-overwrite-properties-optional}

特定のキャンペーンバリアントを受け取るユーザー向けに最初に設定したデフォルトプロパティを上書きすることができます。

追加のデフォルトプロパティを編集、追加、または削除するには、**メッセージング** > **フィーチャーフラグ**からフィーチャーフラグ自体を編集します。バリアントが無効な場合、SDKは指定されたフィーチャーフラグに対して空のプロパティオブジェクトを返します。

![「実験バリアント」セクションで、変数キー「link」が「/sales」で上書きされている画面。]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### ステップ4：ターゲットユーザーを選択する {#step-4-choose-users-to-target}

セグメントまたはフィルターを使用して、[ターゲットユーザー]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)を選択します。たとえば、**Received Feature Flag Variant** フィルターを使用して、すでにA/Bテストを受け取ったユーザーをリターゲティングすることができます。

![フィーチャーフラグ実験の「ターゲット」ページで、フィルターグループの検索バーに「Received Feature Flag Variant」がハイライトされている画面。]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
セグメントメンバーシップは、指定されたユーザーのフィーチャーフラグが更新されたときに計算されます。変更は、アプリがフィーチャーフラグを更新した後、または新しいセッションが開始されたときに利用可能になります。
{% endalert %}

### ステップ5：バリアントを配分する {#step-5-distribute-variants}

実験のパーセンテージ配分を選択します。ベストプラクティスとして、実験を開始した後は配分を変更しないでください。

### ステップ6：コンバージョンを割り当てる {#step-6-assign-conversions}

Brazeでは、キャンペーンを受け取った後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間のウィンドウを指定します。

### ステップ7：確認して開始する {#step-7-review-and-launch}

実験の最後の構築が完了したら、その詳細を確認し、**Launch Experiment** を選択します。

## 結果の確認 {#reviewing-the-results}

フィーチャーフラグ実験が完了したら、実験のインプレッションデータを確認できます。**メッセージング** > **キャンペーン**に移動し、フィーチャーフラグ実験を含むキャンペーンを選択します。

### キャンペーン分析 {#campaign-analytics}

**キャンペーン分析**では、実験のパフォーマンスの概要を確認できます。たとえば以下のような情報があります。

- インプレッションの合計数
- ユニークインプレッションの数
- 1次コンバージョン率
- メッセージによって生成された合計収益
- 推定オーディエンス

また、配信、オーディエンス、コンバージョンに関する実験の設定も確認できます。

### フィーチャーフラグ実験のパフォーマンス {#feature-flag-experiment-performance}

**フィーチャーフラグ実験のパフォーマンス**では、さまざまなディメンションにわたってメッセージがどの程度パフォーマンスを発揮したかを確認できます。表示される具体的な指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかによって異なります。各バリアントに関連付けられたフィーチャーフラグの値を確認するには、**プレビュー**を選択します。