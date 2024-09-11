<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recoger datos del formulario
    $username = $_POST['registerUser'];
    $password = $_POST['registerPassword'];
    $role = $_POST['role'] ?? 'u'; // Asignar 'u' por defecto si no se especifica rol

    // Validar datos
    if (empty($username) || empty($password)) {
        echo "Todos los campos son requeridos.";
        exit();
    }

    // Cifrar la contraseña
   // $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
   $hashedPassword = $password;

    // Ruta al archivo CSV
    $csvFile = 'usuarios.csv';

    // Abrir archivo CSV para agregar el nuevo usuario
    if (($handle = fopen($csvFile, "a")) !== FALSE) {
        fputcsv($handle, [$username, $hashedPassword, $role]);
        fclose($handle);
        echo "Registro exitoso. Puedes iniciar sesión ahora.";
    } else {
        echo "Error al abrir el archivo.";
    }
}
?>
