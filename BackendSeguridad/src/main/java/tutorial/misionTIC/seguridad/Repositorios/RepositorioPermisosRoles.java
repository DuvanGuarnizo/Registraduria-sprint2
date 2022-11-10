package tutorial.misionTIC.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import tutorial.misionTIC.seguridad.Modelos.PermisosRoles;

public interface RepositorioPermisosRoles extends MongoRepository <PermisosRoles, String> {
}
