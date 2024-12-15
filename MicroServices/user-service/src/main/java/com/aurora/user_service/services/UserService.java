package com.aurora.user_service.services;

import java.util.List;
import java.util.stream.Collectors;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.CollectionUtils;

import com.aurora.user_service.dtos.UserDetailsDTO;
import com.aurora.user_service.entities.UserDetails;
import com.aurora.user_service.repositories.UserRepositories;

@Service
public class UserService {
    private final Logger Logger = LoggerFactory.getLogger(UserService.class);
    @Autowired
    private UserRepositories repository;

    @Transactional
    public UserDetailsDTO saveUpdate(UserDetailsDTO inputUser) {
        try {
            UserDetails userDetails = new UserDetails();
            userDetails.setName(inputUser.getName());
            userDetails.setAge(Integer.parseInt(inputUser.getAge()));
            return getUserDetailsDTO(repository.save(userDetails));

        } catch (Exception e) {
            Logger.warn("exception in userservice -> saveUpdate():" + e);
        }
        return null;

    }

    public UserDetailsDTO getUserDetailsDTO(UserDetails userDetails) {
        return new UserDetailsDTO(
                userDetails.getId().toString(),
                userDetails.getName(),
                userDetails.getAge().toString());
    }

    public UserDetailsDTO getById(Long id) {
        return getUserDetailsDTO(repository.getOne(id));

    }

    public List<UserDetailsDTO> getByName(String name) {
        List<UserDetails> list = repository.findUserByName(name);
        if(CollectionUtils.isEmpty(list)){
            return null;
        }
        return list.stream().map(this::getUserDetailsDTO).collect(Collectors.toList());

    }

}
