package tutorial.misionTIC.seguridad.Modelos;

<<<<<<< HEAD

=======
>>>>>>> 73a45cb9761c065bb83f4a40b41910a26864325b
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;
<<<<<<< HEAD

=======
//permisos
>>>>>>> 73a45cb9761c065bb83f4a40b41910a26864325b
@Data
@Document
public class PermisosRoles {
    @Id
    private String _id;
    @DBRef
    private Rol rol;
    @DBRef
    private Permiso permiso;

    public PermisosRoles() {
    }

    public String get_id() {
        return _id;
    }

    public Rol getRol() {
        return rol;
    }

    public void setRol(Rol rol) {
        this.rol = rol;
    }

    public Permiso getPermiso() {
        return permiso;
    }

    public void setPermiso(Permiso permiso) {
        this.permiso = permiso;
    }
<<<<<<< HEAD
}
=======
}
>>>>>>> 73a45cb9761c065bb83f4a40b41910a26864325b
