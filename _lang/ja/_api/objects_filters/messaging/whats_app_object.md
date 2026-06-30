---
nav_title: "WhatsAppオブジェクト"
article_title: WhatsAppメッセージングオブジェクト
page_order: 15
page_type: reference
channel: WhatsApp
description: "この参考記事では、Braze WhatsAppオブジェクトのさまざまなコンポーネントについて説明します。"

---

# WhatsAppオブジェクト {#whatsapp-object}

> `whats_app`オブジェクトを使用すると、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)経由でWhatsAppメッセージを変更または作成できます。

## WhatsAppオブジェクト

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message | list_response_message | flow_response_message),
  "message": (required, object) The message object that must include the required fields based on the selected `message_type`. Below are the specific message structures for each type. Refer to the relevant message type for the required fields and their format.
}
```

- [アプリ識別子]({{site.baseurl}}/api/identifier_types)

### メッセージタイプ {#message-types}

#### template_message

```json
{
  "template_name": (required, string) the WhatsApp template name for the message,
  "template_language_code": (required, string) the language code of the WhatsApp template for the message,
  "header_variables": (optional, header variables object) an object to specify header variable values for specified template_name, required if the header has variables; see object specification below,
  "body_variables": (optional, body variable object) an object to specify body variable values for specified template_name, required if the body has variables; see object specification below,
  "button_variables": (optional, button variables object) an object to specify button variable values for specified template_name, required if buttons have variables; see object specification below,
  "header_media_uri": (optional, string) URI to the header media, if the header is of type IMAGE in specified template_name. Only IMAGE and TEXT header types are supported by the messages/send API.
}
```

{% alert important %}
**メディア送信の制限:** メディア送信（ドキュメント、動画、およびその他のメディアタイプ）は、`messages/send` APIではサポートされていません。APIを介して送信されるテンプレートメッセージでは、TEXTおよびIMAGEヘッダータイプのみがサポートされます。WhatsAppテンプレートがDOCUMENT、VIDEO、またはその他のメディアタイプのヘッダーを使用している場合、`messages/send` APIを使用して送信することはできません。メディアヘッダー付きのテンプレートを送信するには、[Campaigns Triggered API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)またはBrazeダッシュボードを使用してください。
{% endalert %}

##### ヘッダー変数オブジェクト {#header-variables-object}

`header_variables`オブジェクトを使用すると、WhatsAppテンプレートのヘッダー変数の値を指定できます。各キーは、指定された値で置換するWhatsAppテンプレート変数のインデックス（ゼロインデックス）です。

{% alert note %}
`header_variables`は、TEXT型のヘッダーを持つテンプレートでのみ使用できます。IMAGEヘッダーの場合は、代わりに`header_media_uri`を使用してください。DOCUMENT、VIDEO、およびその他のメディアヘッダータイプは、`messages/send` APIではサポートされていません。<br><br>

`header_image_uri`は、テンプレートメッセージではなく、応答メッセージタイプ（`quick_reply_response_message`など）にのみ使用されます。
{% endalert %}

```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
現在、指定できるヘッダー変数は0個または1個のみです。


###### 例 {#example}

```json
{
  "0": "Check it out!"
}
```

##### ボディ変数オブジェクト {#body-variables-object}

`body_variables`オブジェクトを使用すると、WhatsAppテンプレートのボディ変数の値を指定できます。各キーは、指定された値で置換するWhatsAppテンプレート変数のインデックス（ゼロインデックス）です。
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### 例

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### ボタン変数オブジェクト {#button-variables-object}

`button_variables`オブジェクトを使用すると、WhatsAppテンプレートのボタン変数の値を指定できます。各キーは、指定された値で置換するWhatsAppテンプレート変数のインデックス（ゼロインデックス）です。

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

現在、指定できるボタン変数は1つだけで、CTA URLのパスコンポーネントです。変数のインデックスは、テンプレート内のCTA URLボタンのインデックスと一致する必要があります。例えば、CTAボタンがテンプレートの2番目のボタンである場合、変数インデックス「1」を使用します。

###### 例

```json
{
  "1": "/marketing/promotion123"
}
```

### 応答メッセージ {#response-messages}

#### text_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "preview_url": (optional, boolean) whether WhatsApp should render a preview of links included in body
}
```

##### 例

```json
{
  "body": "Check out our new deals at https://braze.com",
  "preview_url": true
}
```

#### text_image_response_message

```json
{
  "image_uri": (required, string) the uri of the image to send,
  "caption": (optional, string) the caption for the image being sent
}
```

##### 例

```json
{
  "image_uri": "https://braze.com/promotion.jpg",
  "caption": "This won't last for long, check it out!"
}
```

#### quick_reply_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "header_image_uri": (optional, string) the URI of the image to send as the message header (only valid if header_text not present),
  "header_text": (optional, string) the text to send as the message header (only valid if header_image_uri not present),
  "footer": (optional, string) the footer of the message to send,
  "buttons": (required, array) array of Button objects. Will render in message based on order in array.
}
```

##### ボタンオブジェクト {#button-object}

```json
{
  "text": (required, string) the text of the button
}
```

###### 例

```json
{
  "body": "Want to keep hearing from us?",
  "buttons": [
    {
      "text": "Yes!"
    },
    {
      "text": "No thanks"
    }
  ]
}
```

#### list_response_message

`list_response_message`タイプを使用すると、WhatsAppでリストベースのメッセージを送信できます。このメッセージタイプには、受信者が操作できる項目のリストが含まれます。

```json
{
  "header": (optional, string) the header of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "list": (required, object) the list object that contains:
    "list_button_text": (required, string) the text that will appear on the list button,
    "list_sections": (required, array) an array of List Section Objects
}
```

#### リストセクションオブジェクト {#list-section-object}

```json
{
  "section_title": (required, string) The title of the section,
  "list_rows": (required, array) An array of List Row Objects
}
```

#### リスト行オブジェクト {#list-row-object}

```json
{
  "row_title": (required, string) The title of the row,
  "row_description": (optional, string) The description for the row
}
```

##### 制約 {#constraints}

- **list_sections**: 少なくとも1つのセクションが必要です。
- **list_rows**: すべてのセクションで最大10行まで含めることができます。
- **row_description**: 各行でオプションです。

##### 例

```json
{
  "body": "Here is a list of options to choose from:",
  "list": {
    "list_button_text": "Choose an option",
    "list_sections": [
      {
        "section_title": "Section 1",
        "list_rows": [
          {
            "row_title": "Option 1"
          },
          {
            "row_title": "Option 2",
            "row_description": "Description for Option 2"
          }
        ]
      },
      {
        "section_title": "Section 2",
        "list_rows": [
          {
            "row_title": "Option 3"
          },
          {
            "row_title": "Option 4"
          },
          {
            "row_title": "Option 5"
          }
        ]
      }
    ]
  }
}
```

#### flow_response_message

`flow_response_message`タイプを使用すると、WhatsAppでフローベースのメッセージを送信できます。このメッセージタイプには、受信者が完了できるインタラクティブなフローが含まれます。

```json
{
  "header_text": (optional, string) the header text of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "flow_button": (required, object) the flow button object that contains:
    "caption": (required, string) the text that will appear on the flow button,
    "flow_id": (required, string) the unique identifier of the WhatsApp Flow,
  "generate_custom_attribute": (optional, boolean) whether to save flow response on the user profile and generate a custom attribute upon responding to this flow message
}
```

##### フローボタンオブジェクト {#flow-button-object}

```json
{
  "caption": (required, string) The text displayed on the button,
  "flow_id": (required, string) The ID of the flow
}
```

##### 制約

- **flow_button**: captionと`flow_id`の両方を含める必要があります。
- **caption**: 最大20文字です。
- **flow_id**: 公開済みの有効なフローIDである必要があります。

##### 例

```json
{
  "body": "Please complete your order details",
  "flow_button": {
    "caption": "Start Order",
    "flow_id": "594425479261596"
  },
  "generate_custom_attribute": true
}
```
