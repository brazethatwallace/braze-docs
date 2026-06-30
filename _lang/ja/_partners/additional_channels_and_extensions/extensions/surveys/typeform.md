---
nav_title: Typeform
article_title: Typeform
description: "この記事では、データやフィードバックなどを収集するための使いやすいツールであるBrazeとTypeformのパートナーシップについて説明します。"
alias: /partners/typeform/
page_type: partner
search_tag: Partner
---

# Typeform

> [Typeform](https://www.typeform.com/)は、データやフィードバックなどを収集するための使いやすいツールです。

BrazeとTypeformを統合することで、以下のことが可能になります。

- Typeformの回答から収集したデータでBrazeのユーザープロファイルを更新する
- ユーザーのTypeformへのエンゲージメントに基づいてBrazeでメッセージングをトリガーする
- ユーザーのTypeformの回答に基づいてBrazeのメッセージをパーソナライズする

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Typeformアカウント | このパートナーシップを利用するには、webhookにアクセスできるTypeformアカウントが必要です。 |
| Brazeデータ変換 | Typeformからデータを受信するには、[データ変換URL]({{site.baseurl}}/data_transformation)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1: TypeformのWebhookを受け入れるようにBrazeデータ変換を設定する {#step-1}

{% multi_lang_include data_activation/create_transformation.md location="typeform" %}

### ステップ2: TypeformのWebhookを設定する {#step-2-set-up-typeform-webhooks}

[TypeformのWebhookドキュメント](https://www.typeform.com/help/a/webhooks-360029573471/)の手順に従ってWebhookを設定します。

ステップ4で、**Destination URL**としてデータ変換のWebhook URLを追加します。

![送信先URLフィールドが表示されたTypeformのWebhook設定画面。]({% image_buster /assets/img/typeform/typeform_add_webhook.png %}){: style="max-width:50%" }

**View deliveries**をクリックし、次に**Send test request**をクリックして、データ変換にテストイベントを送信します。

![「Send test request」が選択されたTypeformのView deliveriesページ。]({% image_buster /assets/img/typeform/typeform_test_request.png %})

### ステップ3: 選択したTypeformイベントを受け入れる変換コードを書く {#step-3-write-transformation-code-to-accept-your-chosen-typeform-events}

このステップでは、Typeformから送信されるWebhookペイロードをJavaScriptオブジェクトの戻り値に変換します。

1. データ変換を更新し、**Webhook Details**にTypeformのテストペイロードが表示されていることを確認します。
2. 選択したTypeformイベントをサポートするようにデータ変換コードを更新します。
3. **Validate**をクリックして、コード出力のプレビューを返し、受け入れ可能な`/users/track`リクエストであるかどうかを確認します。
4. データ変換を保存して有効化します。

![Typeformのテストペイロード検証が成功したことを示すデータ変換プレビュー。]({% image_buster /assets/img/typeform/typeform_test_result.png %})

#### リクエスト本文の形式 {#request-body-format}

この戻り値は、Brazeの`/users/track`リクエスト本文の形式に準拠する必要があります。

- 変換コードはJavaScriptプログラミング言語で記述します。if/elseロジックなど、標準的なJavaScript制御フローがすべてサポートされています。
- 変換コードは、payload変数を通じてWebhookリクエスト本文にアクセスします。この変数は、リクエスト本文のJSONを解析して生成されたオブジェクトです。
- `/users/track`エンドポイントでサポートされるすべての機能がサポートされています。以下が含まれます。
    - ユーザー属性オブジェクト、イベントオブジェクト、購入オブジェクト
    - ネストされた属性とネストされたカスタムイベントプロパティ
    - サブスクリプショングループの更新
    - 識別子としてのメールアドレス

## TypeformのWebhookペイロードの例 {#example-typeform-webhook-payload}

```http
Content-Type: application/json

{
  "event_id": "01HC3PTZN05GJWT0QDXXB2QV8F",
  "event_type": "form_response",
  "form_response": {
    "form_id": "uaIA4a7Y",
    "token": "7pctqdoqxg41to97pctqdibhqn6hqvto",
    "landed_at": "2023-10-06T23:57:52Z",
    "submitted_at": "2023-10-06T23:58:18Z",
    "hidden": {
		"user_id": "hidden_value"
    },
    "definition": {
      "id": "uaIA4a7Y",
      "title": "Project Feedback Survey",
      "fields": [
        {
          "id": "G0IbXtfvsfjV",
          "ref": "814b9fc2-e6d2-4672-accf-22f754b84f20",
          "type": "email",
          "title": "Please provide your email",
          "properties": {}
        },
        {
          "id": "lg82q3t0rK03",
          "ref": "e1503b62-0241-4269-9902-5c539abf305e",
          "type": "short_text",
          "title": "What was your role in the project?",
          "properties": {}
        },
        {
          "id": "UXftY0tSmuDV",
          "ref": "5b839dbb-566b-47de-a47e-b0914d9ccf7c",
          "type": "opinion_scale",
          "title": "How would you rate the overall performance of the team?",
          "properties": {}
        },
        {
          "id": "fE17bXVUEB4E",
          "ref": "fd6be99d-1ed1-4a4d-b811-f6ecdd8fa9b6",
          "type": "yes_no",
          "title": "Did the project meet its intended outcomes?",
          "properties": {}
        },
        {
          "id": "NmVOQFuI0vv9",
          "ref": "cd2b4176-db9a-49bb-a918-4463720bbc79",
          "type": "multiple_choice",
          "title": "Which area of the project do you think went well?",
          "properties": {},
          "choices": [
            {
              "id": "RvV3LaMEQ2eK",
              "ref": "2d5e0913-afe9-491c-b31c-0648dd397d56",
              "label": "Communication"
            },
            {
              "id": "7iXmfpPMeQvz",
              "ref": "7a7749d2-5cd6-4bf7-9726-65c7ab11ec83",
              "label": "Planning"
            },
            {
              "id": "1No85DZlvP6f",
              "ref": "d7b7304a-776b-4630-8bee-7dc7ef9c9404",
              "label": "Execution"
            },
            {
              "id": "ruMnsZWjyalW",
              "ref": "41dc926a-85af-4625-8a61-725fda35afda",
              "label": "Problem Solving"
            },
            {
              "id": "CexnFN3roprG",
              "ref": "cfdd2da4-8c57-4ff1-b4c0-1a5262e2ff84",
              "label": "Other"
            }
          ]
        },
        {
          "id": "ZJop9pvoObzk",
          "ref": "ce903cda-7e27-4b4c-9fa8-0623c47c61b4",
          "type": "multiple_choice",
          "title": "Which area of the project do you think could be improved?",
          "properties": {},
          "choices": [
            {
              "id": "YQLArFf0Wks5",
              "ref": "09fa30c7-7bdc-4753-971e-0d922638d023",
              "label": "Communication"
            },
            {
              "id": "iGjaELgfnChw",
              "ref": "61820c89-3426-464d-b031-c06de5125fd5",
              "label": "Planning"
            },
            {
              "id": "2EyI5tozFxro",
              "ref": "c35f71b2-2a6d-4488-a1ba-87c2e711ce19",
              "label": "Execution"
            },
            {
              "id": "VGtsIHBLAhME",
              "ref": "6c171a9a-9324-4f7d-adb9-290bd701efe9",
              "label": "Problem Solving"
            },
            {
              "id": "lVdV7MIL1anS",
              "ref": "faba551f-4e6b-4377-9f74-11ca4fcc8ed5",
              "label": "Other"
            }
          ]
        },
        {
          "id": "hcCNsLUHGXgv",
          "ref": "d1ae8537-0d5a-4ca8-bb6b-f8057f04d7e2",
          "type": "opinion_scale",
          "title": "How satisfied were you with the level of communication during the project?",
          "properties": {}
        },
        {
          "id": "dBqPlgeKejN2",
          "ref": "e2c884c1-0d92-4f18-9833-79dff0b3eef2",
          "type": "nps",
          "title": "How likely are you to recommend Braze for customer engagement services?",
          "properties": {}
        },
        {
          "id": "vLdpFmCmulF5",
          "ref": "a86e48ec-6d10-49fc-ac03-4ac1aad4bfec",
          "type": "dropdown",
          "title": "In which country was the project executed?",
          "properties": {}
        }
      ],
      "endings": [
        {
          "id": "LUpVm67y72vb",
          "ref": "30c03bdf-80b3-45f5-8307-df8ca49046b1",
          "title": "Thank you for taking the time to complete our survey!",
          "type": "thankyou_screen",
          "properties": {
            "button_text": "Create a typeform",
            "show_button": true,
            "share_icons": true,
            "button_mode": "default_redirect"
          }
        }
      ]
    },
    "answers": [
      {
        "type": "email",
        "email": "typeformintegration@example.com",
        "field": {
          "id": "G0IbXtfvsfjV",
          "type": "email",
          "ref": "814b9fc2-e6d2-4672-accf-22f754b84f20"
        }
      },
      {
        "type": "text",
        "text": "Project",
        "field": {
          "id": "lg82q3t0rK03",
          "type": "short_text",
          "ref": "e1503b62-0241-4269-9902-5c539abf305e"
        }
      },
      {
        "type": "number",
        "number": 9,
        "field": {
          "id": "UXftY0tSmuDV",
          "type": "opinion_scale",
          "ref": "5b839dbb-566b-47de-a47e-b0914d9ccf7c"
        }
      },
      {
        "type": "boolean",
        "boolean": true,
        "field": {
          "id": "fE17bXVUEB4E",
          "type": "yes_no",
          "ref": "fd6be99d-1ed1-4a4d-b811-f6ecdd8fa9b6"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "ruMnsZWjyalW",
          "label": "Problem Solving",
          "ref": "41dc926a-85af-4625-8a61-725fda35afda"
        },
        "field": {
          "id": "NmVOQFuI0vv9",
          "type": "multiple_choice",
          "ref": "cd2b4176-db9a-49bb-a918-4463720bbc79"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "lVdV7MIL1anS",
          "label": "Other",
          "ref": "faba551f-4e6b-4377-9f74-11ca4fcc8ed5"
        },
        "field": {
          "id": "ZJop9pvoObzk",
          "type": "multiple_choice",
          "ref": "ce903cda-7e27-4b4c-9fa8-0623c47c61b4"
        }
      },
      {
        "type": "number",
        "number": 8,
        "field": {
          "id": "hcCNsLUHGXgv",
          "type": "opinion_scale",
          "ref": "d1ae8537-0d5a-4ca8-bb6b-f8057f04d7e2"
        }
      },
      {
        "type": "number",
        "number": 6,
        "field": {
          "id": "dBqPlgeKejN2",
          "type": "nps",
          "ref": "e2c884c1-0d92-4f18-9833-79dff0b3eef2"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "KESjdqLseWmC",
          "label": "Brazil",
          "ref": "250210d9-33f6-4734-8ec6-06005a8ef66d"
        },
        "field": {
          "id": "vLdpFmCmulF5",
          "type": "dropdown",
          "ref": "a86e48ec-6d10-49fc-ac03-4ac1aad4bfec"
        }
      }
    ],
    "ending": {
      "id": "LUpVm67y72vb",
      "ref": "30c03bdf-80b3-45f5-8307-df8ca49046b1"
    }
  }
}
```

## データ変換のユースケース {#data-transformation-use-cases}

以下は、[TypeformのWebhookペイロードの例](#example-typeform-webhook-payload)を使用して作成したテンプレートの例です。これらのテンプレートは出発点として使用できます。ゼロから作成するか、必要に応じて特定のコンポーネントを削除することができます。

これらのテンプレート例では、Brazeプロファイルにカスタムイベントを記録しています。Typeformのタイトルがカスタムイベント名として渡され、Typeformの結果がイベントプロパティとして渡されます。これらのテンプレート例では、TypeformのCalendly、File Upload、Paymentの質問タイプは考慮されていません。

### ユースケース: 識別子としてのメール {#use-case-email-as-identifier}

このテンプレート例では、メールアドレス（Typeform内のメールアドレスの質問から取得）を識別子として使用しています。

{% alert note %}
メールアドレスを識別子として使用する場合は、`/users/track`エンドポイントの[よくある質問]({{site.baseurl}}/api/endpoints/user_data/post_user_track#frequently-asked-questions)を参照して、期待される動作の詳細を確認してください。
{% endalert %}

{% tabs local %}
{% tab Input %}

```javascript
/* In the Typeform webhook payload each question is stored as a “title” within each object of the “fields” array. Our code defines a “title” variable where we store the value of each field title. */
const titles = payload.form_response.definition.fields.map(field => field.title);

/* The answers array is saved to a “tfAnswers” variable so this can be iterated through */
const tfAnswers = payload.form_response.answers;

/* The value of a response will change based on the type of question, to account for this we have created a function that iterates through the answers, determines what the answer type is and then, based on the type, adds the associated response to an extractedValues array. */
const extractValues = (tfAnswers) => {
	const extractedValues = [];

	tfAnswers.forEach((tfAnswer) => {
		let result = null;

		if (tfAnswer.type === 'choices') {
			if (tfAnswer.choices) {
				// Multiple choices
				let labels = tfAnswer.choices.labels || [];
				if (tfAnswer.choices.other) {
					labels.push(tfAnswer.choices.other);
				}
				result = labels;
			}
		} else if (tfAnswer.type === 'choice' && Object.keys(tfAnswer.choice).length > 1) {
			// Single choice
			result = tfAnswer.choice && tfAnswer.choice.other ?
				tfAnswer.choice.other.toString() :
				tfAnswer.choice.label.toString();
		} else if (tfAnswer.type === 'dropdown') {
			// Dropdown
			result = tfAnswer.text;
		} else {
			// For other types, use the type-specific value
			result = tfAnswer[tfAnswer.type];
		}

		extractedValues.push(result);
	});

	return extractedValues;
};

/* We use the above defined function, passing it the “tfAnswers” variable that holds the answers portion of the Typeform webhook payload and save the output to a ”values” variable */
const values = extractValues(tfAnswers);

/* Finally, the values within the previously assigned “titles” variable and “values” variable are paired together in an object as the values to a “question” key and “answer” key in a “responses” array of objects variable. */
const results = titles.map((title, index) => {
	return {
		question: title,
		answer: values[index],
	};
});

/* The code defines a variable, "brazecall", to build a /users/track request. Within the request, the typeform title is populated as the event name, and our “results” variable (where all of our question/answer pairs are stored), is assigned as the event’s properties. */
let brazecall = {
	"events": [{
		"email": payload.form_response.answers.find(answer => answer.type === 'email').email,
		"name": payload.form_response.definition.title,
		"time": new Date().toISOString(),
		"properties": {
			"responses": results
		}
	}]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return “brazecall” to create an output
return brazecall;
```

{% endtab %}
{% tab Output %}

```json
{
  "events": [
    {
      "email": "an_account@example.com",
      "name": "Project Feedback Survey",
      "time": "2023-10-17T18:21:39.527Z",
      "properties": {
        "responses": [
          {
            "question": "Please provide your email",
            "answer": "an_account@example.com"
          },
          {
            "question": "What was your role in the project?",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "How would you rate the overall performance of the team?",
            "answer": 5
          },
          {
            "question": "Did the project meet its intended outcomes?",
            "answer": true
          },
          {
            "question": "If you answered \"No\" to the previous question, please explain why. If you answered \"Yes\", skip this question.",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "Which area of the project do you think went well?",
            "answer": "Communication"
          },
          {
            "question": "Which area of the project do you think could be improved?",
            "answer": "Communication"
          },
          {
            "question": "How satisfied were you with the level of communication during the project?",
            "answer": 5
          },
          {
            "question": "How likely are you to recommend Braze for customer engagement services?",
            "answer": 5
          },
          {
            "question": "In which country was the project executed?",
            "answer": "United States"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### ユースケース: 隠しフィールドで渡された識別子を使用する {#use-case-using-identifier-passed-in-hidden-fields}

Typeformの隠しフィールドを使用して、Typeformの回答でこの情報を渡すことなく、TypeformのWebhookペイロードにユーザーのIDなどのデータを含めることができます。

このテンプレート例では、「user_id」隠しフィールドを使用し、これを`/users/track`リクエストペイロードに`external_id`として渡しています。ここでは「user_id」を使用していますが、必要に応じてフィールドを変更できます。

{% tabs local %}
{% tab Input %}

```javascript
/* In the Typeform webhook payload each question is stored as a “title” within each object of the “fields” array. Our code defines a “title” variable where we store the value of each field title. */
const titles = payload.form_response.definition.fields.map(field => field.title);

/* The answers array is saved to a “tfAnswers” variable so this can be iterated through */
const tfAnswers = payload.form_response.answers;

/* The value of a response will change based on the type of question, to account for this we have created a function that iterates through the answers, determines what the answer type is and then, based on the type, adds the associated response to an extractedValues array. */
const extractValues = (tfAnswers) => {
	const extractedValues = [];

	tfAnswers.forEach((tfAnswer) => {
		let result = null;

		if (tfAnswer.type === 'choices') {
			if (tfAnswer.choices) {
				// Multiple choices
				let labels = tfAnswer.choices.labels || [];
				if (tfAnswer.choices.other) {
					labels.push(tfAnswer.choices.other);
				}
				result = labels;
			}
		} else if (tfAnswer.type === 'choice' && Object.keys(tfAnswer.choice).length > 1) {
			// Single choice
			result = tfAnswer.choice && tfAnswer.choice.other ?
				tfAnswer.choice.other.toString() :
				tfAnswer.choice.label.toString();
		} else if (tfAnswer.type === 'dropdown') {
			// Dropdown
			result = tfAnswer.text;
		} else {
			// For other types, use the type-specific value
			result = tfAnswer[tfAnswer.type];
		}

		extractedValues.push(result);
	});

	return extractedValues;
};

/* We use the above defined function, passing it the “tfAnswers” variable that holds the answers portion of the Typeform webhook payload and save the output to a ”values” variable */
const values = extractValues(tfAnswers);

/* Finally, the values within the previously assigned “titles” variable and “values” variable are paired together in an object as the values to a “question” key and “answer” key in a “responses” array of objects variable. */
const results = titles.map((title, index) => {
	return {
		question: title,
		answer: values[index],
	};
});

/* The code defines a variable, "brazecall", to build a /users/track request. Within the request, the typeform title is populated as the event name, and our “results” variable (where all of our question/answer pairs are stored), is assigned as the event’s properties. */
let brazecall = {
	"events": [{
		"external_id": payload.form_response.hidden.user_id,
		"name": payload.form_response.definition.title,
		"time": new Date().toISOString(),
		"properties": {
			"responses": results
		}
	}]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return “brazecall” to create an output
return brazecall;
```

{% endtab %}
{% tab Output %}

```json
{
  "events": [
    {
      "external_id": "hidden_value",
      "name": "Project Feedback Survey",
      "time": "2023-10-17T18:27:22.209Z",
      "properties": {
        "responses": [
          {
            "question": "Please provide your email",
            "answer": "an_account@example.com"
          },
          {
            "question": "What was your role in the project?",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "How would you rate the overall performance of the team?",
            "answer": 5
          },
          {
            "question": "Did the project meet its intended outcomes?",
            "answer": true
          },
          {
            "question": "If you answered \"No\" to the previous question, please explain why. If you answered \"Yes\", skip this question.",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "Which area of the project do you think went well?",
            "answer": "Communication"
          },
          {
            "question": "Which area of the project do you think could be improved?",
            "answer": "Communication"
          },
          {
            "question": "How satisfied were you with the level of communication during the project?",
            "answer": 5
          },
          {
            "question": "How likely are you to recommend Braze for customer engagement services?",
            "answer": 5
          },
          {
            "question": "In which country was the project executed?",
            "answer": "United States"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### ステップ4: TypeformのWebhookを公開する {#step-4-publish-your-typeform-webhook}

データ変換の作成が完了したら、**Validate**をクリックしてデータ変換コードが正しくフォーマットされており、期待通りに動作することを確認します。その後、データ変換を保存してアクティブ化します。

アクティブ化すると、ユーザーがフォームへの入力を完了した際にカスタムイベントデータがユーザーのプロファイルに記録されます。

![Typeformの送信後にカスタムイベントが記録されたユーザープロファイル。]({% image_buster /assets/img/typeform/typeform_custom_event.png %})

## モニタリングとトラブルシューティング {#monitoring-and-troubleshooting}

変換のモニタリングとトラブルシューティングの詳細については、「[変換のモニタリング]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-5-monitor-your-transformation)」セクションを参照してください。