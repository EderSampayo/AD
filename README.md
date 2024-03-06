# DirectorioActivo

1. **SELECT**
   - Especifica el nombre de usuario o el identificador único (DN)
     ```powershell
     $usuario = "NombreUsuario"
     ```

   - Recupera los atributos deseados del usuario
     ```powershell
     $atributos = Get-ADUser -Identity $usuario -Properties Attribute1, Attribute2, Attribute3
     ```

   - Muestra los valores de los atributos
     ```powershell
     $atributos.Attribute1
     $atributos.Attribute2
     $atributos.Attribute3
     ```

   - Especifica el timestamp obtenido
     ```powershell
     $timestamp = $atributos.Attribute1
     ```

   - Muestra la fecha y hora en un formato legible
     ```powershell
     $python .\Desktop\Prueba\nanoseg_a_fecha_AD_param.py $timestamp
     ```
