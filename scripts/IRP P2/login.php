<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recoger datos del formulario
    $username = $_POST['loginUser'];
    $password = $_POST['loginPassword'];
    $rol1 = "a";
    $rol2 = "u";
    $con =10;



    // Ruta al archivo CSV
    $csvFile = 'usuarios.csv';
    
    // Leer el archivo CSV
    if (($handle = fopen($csvFile, "r")) !== FALSE) {
        $isValidUser = false;
        
        // Leer línea por línea
        while (($data = fgetcsv($handle)) !== FALSE) {
            // Si el nombre de usuario y la contraseña coinciden
            if ($data[0] == $username && $data[1] == $password && $data[2] == $rol1) {
                $isValidUser = true;
                $con = 1;
                break;

            }else  if($data[0] == $username && $data[1] == $password && $data[2] == $rol2) {
                $isValidUser = true;
                $con = 0;
                break;
              
            }
        }
        fclose($handle);
        
        // Verificar si el usuario es válido
        if ($isValidUser) {
            if($con == 1){

            
               
                if(($username && $password) != null){
                    header("Location: ./admin.php");
                    session_start();
                $_SESSION['nombre'] = $username;
                exit();

                }else{
                    echo "No tiene permitido ingresar =(";

                }
                

           // echo "Login successful! Welcome, " . htmlspecialchars($username) . ".";
           
           ?>
          
                           <?php
            }else if($con == 0){

                if(($username && $password) != null){
                    header("Location: ./user.php");
                    session_start();
                $_SESSION['nombre'] = $username;
                exit();

                }else{
                    echo "No tiene permitido ingresar =(";

                }

            }
        } else {
            echo "Invalid username or password.";
        }
    } else {
        echo "Error opening the file.";
    }
}
?>
