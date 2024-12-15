package com.aurora.user_service.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.aurora.user_service.entities.UserDetails;

public interface UserRepositories extends JpaRepository<UserDetails,Long> {

    @Query("Select ud FROM UserDetails ud where ud.name=?1")
    List<UserDetails> findUserByName(String name);

}
