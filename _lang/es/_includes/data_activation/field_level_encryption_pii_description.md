{% comment %}
  Descripción del cifrado a nivel de campo del identificador y la PII. Se usa en el documento de cifrado a nivel de campo y en las notas de lanzamiento.
  Parámetros:
  - link (opcional): Si se establece, "cifrado a nivel de campo del identificador" se incluirá en este enlace (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Mediante el [cifrado a nivel de campo del identificador]({{ site.baseurl }}/{{ include.link }}), puedes cifrar fácilmente las direcciones de correo electrónico con AWS Key Management Service (KMS) para minimizar la información de identificación personal (PII) compartida en Braze. El cifrado sustituye los datos sensibles por texto cifrado, que es información cifrada ilegible.
{% else %}
Mediante el cifrado a nivel de campo del identificador, puedes cifrar fácilmente las direcciones de correo electrónico con AWS Key Management Service (KMS) para minimizar la información de identificación personal (PII) compartida en Braze. El cifrado sustituye los datos sensibles por texto cifrado, que es información cifrada ilegible.
{% endif %}