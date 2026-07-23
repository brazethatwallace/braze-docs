1. En el portal de Azure, ve al centro de administración de Microsoft Entra y luego a **App Registrations**.
2. Selecciona **+ New registration** en **Identity > Applications > App registrations**.
3. Introduce un nombre y selecciona `Accounts in this organizational directory only` como tipo de cuenta compatible. Luego, selecciona **Register**.
4. Selecciona la aplicación (entidad de servicio) que acabas de crear y luego ve a **Certificates & secrets > + New client secret**.
5. Introduce una descripción para el secreto y establece un periodo de caducidad para el secreto. Luego, selecciona **Add**.
6. Toma nota del secreto de cliente creado para usarlo en la configuración de Braze.