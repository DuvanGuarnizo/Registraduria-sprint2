package tutorial.misionTIC.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
<<<<<<< HEAD
import org.springframework.data.mongodb.repository.Query;
import tutorial.misionTIC.seguridad.Modelos.PermisosRoles;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles, String> {

    @Query("{'rol.$id': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    PermisosRoles getPermisoRol(String id_rol, String id_permiso);

=======
import tutorial.misionTIC.seguridad.Modelos.PermisosRoles;

public interface RepositorioPermisosRoles extends MongoRepository <PermisosRoles, String> {
>>>>>>> 73a45cb9761c065bb83f4a40b41910a26864325b
}
