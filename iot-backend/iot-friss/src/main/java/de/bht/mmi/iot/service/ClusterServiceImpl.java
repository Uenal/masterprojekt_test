package de.bht.mmi.iot.service;

import de.bht.mmi.iot.exception.EntityNotFoundException;
import de.bht.mmi.iot.exception.NotAuthorizedException;
import de.bht.mmi.iot.model.Cluster;
import de.bht.mmi.iot.model.Sensor;
import de.bht.mmi.iot.model.User;
import de.bht.mmi.iot.repository.ClusterRepository;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

import static de.bht.mmi.iot.constants.RoleConstants.*;

@Service
public class ClusterServiceImpl implements ClusterService {

    @Autowired
    private ClusterRepository clusterRepository;

    @Autowired
    private UserService userService;

    @Autowired
    private SensorService sensorService;

    @Override
    public Iterable<Cluster> getAll() {
        return clusterRepository.findAll();
    }

    @Override
    public Iterable<Cluster> getAll(UserDetails authenticatedUser) throws EntityNotFoundException {
        final String username = authenticatedUser.getUsername();
        if (userService.isAnyRolePresent(authenticatedUser, ROLE_ADMIN, ROLE_GET_ALL_CLUSTER)) {
            return getAll();
        } else {
            final Set<Cluster> result = new HashSet<>();
            CollectionUtils.addAll(result, getAllByOwner(username));
            CollectionUtils.addAll(result, getAllReleasedForUser(username));
            return result;
        }
    }

    @Override
    public Iterable<Cluster> getAllReleasedForUser(String username) throws EntityNotFoundException {
        final User user = userService.loadUserByUsername(username);
        final Iterable<Cluster> userClusters = clusterRepository.findAll(user.getReleasedForClusters());
        return userClusters != null ? userClusters : Collections.emptyList();
    }

    @Override
    public Iterable<Cluster> getAllByOwner(String username) throws EntityNotFoundException {
        userService.loadUserByUsername(username);
        return clusterRepository.findAllByOwner(username);
    }

    @Override
    public Iterable<Cluster> getAllByOwner(String username, UserDetails authenticatedUser)
            throws EntityNotFoundException, NotAuthorizedException {
        userService.loadUserByUsername(username);
        if (userService.isAnyRolePresent(authenticatedUser, ROLE_ADMIN, ROLE_GET_ALL_CLUSTER)
                || username.equals(authenticatedUser.getUsername())) {
            return getAllByOwner(username);
        }
        throw new NotAuthorizedException(
                String.format("You are not authorized to get all clusters for owner '%s'", username));
    }

    @Override
    public Cluster getOne(String clusterId) throws EntityNotFoundException {
        final Cluster cluster = clusterRepository.findOne(clusterId);
        if (cluster != null) {
            return cluster;
        } else {
            throw new EntityNotFoundException(String.format("Cluster with id '%s' not found!", clusterId));
        }
    }

    @Override
    public Cluster save(Cluster cluster) throws EntityNotFoundException {
        userService.loadUserByUsername(cluster.getOwner());
        return clusterRepository.save(cluster);
    }

    @Override
    public Cluster save(Cluster cluster, UserDetails authenticatedUser)
            throws EntityNotFoundException, NotAuthorizedException {

        Cluster oldCluster = null;
        if (cluster.getId() != null) {
            oldCluster = clusterRepository.findOne(cluster.getId());
        }

        if (oldCluster == null) {
            if (userService.isAnyRolePresent(authenticatedUser, ROLE_ADMIN, ROLE_CREATE_CLUSTER)) {
                return save(cluster);
            }
        } else {
            if (userService.isAnyRolePresent(authenticatedUser, ROLE_ADMIN, ROLE_UPDATE_CLUSTER)
                    || oldCluster.getOwner().equals(authenticatedUser.getUsername())) {
                return save(cluster);
            }
        }
        throw new NotAuthorizedException("You are not authorized to save/update clusters");
    }

    @Override
    public void delete(String clusterId) throws EntityNotFoundException {
        getOne(clusterId);
        final Iterable<Sensor> sensorsAttachedToCluster = sensorService.getAllByClusterId(clusterId);
        for (Sensor sensor : sensorsAttachedToCluster) {
            sensor.setAttachedCluster(null);
            sensorService.save(sensor);
        }
        clusterRepository.delete(clusterId);
    }

    @Override
    public void delete(String clusterId, UserDetails authenticatedUser) throws EntityNotFoundException,
            NotAuthorizedException {
        final Cluster cluster = getOne(clusterId);
        if (userService.isAnyRolePresent(authenticatedUser, ROLE_ADMIN, ROLE_DELETE_CLUSTER)
                || cluster.getOwner().equals(authenticatedUser.getUsername())) {
            delete(clusterId);
            return;
        }
        throw new NotAuthorizedException(
                String.format("You are not authorized to delete cluster with id '%s'", clusterId));
    }

}
