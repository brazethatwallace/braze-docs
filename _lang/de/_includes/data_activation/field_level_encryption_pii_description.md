{% comment %}
  Beschreibung der Verschlüsselung auf Bezeichnerfeld-Ebene und PII. Verwendung in der Dokumentation zur Verschlüsselung auf Feldebene und in den Versionshinweisen.
  Parameter:
  - link (optional): Wenn gesetzt, wird „Verschlüsselung auf Bezeichnerfeld-Ebene“ in diesen Link eingebunden (z. B. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Mit der [Verschlüsselung auf Bezeichnerfeld-Ebene]({{ site.baseurl }}/{{ include.link }}) können Sie E-Mail-Adressen nahtlos mit dem AWS Key Management Service (KMS) verschlüsseln, um die in Braze weitergegebenen personenbezogenen Daten (PII) zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d. h. durch unlesbare verschlüsselte Informationen.
{% else %}
Mit der Verschlüsselung auf Bezeichnerfeld-Ebene können Sie E-Mail-Adressen nahtlos mit dem AWS Key Management Service (KMS) verschlüsseln, um die in Braze weitergegebenen personenbezogenen Daten (PII) zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d. h. durch unlesbare verschlüsselte Informationen.
{% endif %}