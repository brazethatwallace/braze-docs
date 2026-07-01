{% comment %}
  識別子フィールドレベル暗号化と個人識別情報（PII）の説明。フィールドレベル暗号化のドキュメントとリリースノートで使用します。
  パラメータ：
  - link（オプション）：設定されている場合、「識別子フィールドレベル暗号化」がこのリンクで囲まれます（例：{{site.baseurl}}/user_guide/analytics/field_level_encryption/）。
{% endcomment %}
{% if include.link %}
[識別子フィールドレベル暗号化]({{ site.baseurl }}/{{ include.link }})を使用すると、AWS Key Management Service（KMS）でメールアドレスをシームレスに暗号化し、Brazeで共有される個人識別情報（PII）を最小限に抑えることができます。暗号化により、機密データは暗号文（読み取ることができない暗号化された情報）に置き換えられます。
{% else %}
識別子フィールドレベル暗号化を使用すると、AWS Key Management Service（KMS）でメールアドレスをシームレスに暗号化し、Brazeで共有される個人識別情報（PII）を最小限に抑えることができます。暗号化により、機密データは暗号文（読み取ることができない暗号化された情報）に置き換えられます。
{% endif %}