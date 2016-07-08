package de.bht.mmi.iot.repository;

import de.bht.mmi.iot.model.Sensor;
import org.socialsignin.spring.data.dynamodb.repository.EnableScan;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;

@EnableScan
public interface SensorRepository extends CrudRepository<Sensor, String> {

    Iterable<Sensor> findByOwner(@Param("owner") String owner);

    Iterable<Sensor> findByAttachedGateway(@Param("attachedGateway") String gatewayId);

    Iterable<Sensor> findByAttachedCluster(@Param("attachedCluster") String clusterId);

}
